#!/usr/bin/env node
/* _tools/render-diff.js - prove a change moved nothing a reader can see.
 *
 *   node _tools/render-diff.js <dir-A> <dir-B> [page.html ...]
 *
 * Renders each page from both directories in headless Chromium at 1280 and
 * 390 CSS pixels and compares four channels: the rendered DOM with the
 * structured-data blocks stripped, the geometry and paint of every element,
 * the visible text, and the full-page screenshot. With no page list it diffs
 * every .html file present in both directories.
 *
 * Needs Chromium and Playwright, which live in the cloud container and not in
 * the desktop shell, so stage the two trees and run it there.
 *
 * WHY THE FREEZE LOOKS LIKE THIS, because the obvious version does not work
 * and cost the 2026-11-17 pass an hour. This site has TWO animation families:
 * the masthead marquee (`.ticker-track`) and the `.reveal` entrance
 * transition that every article paragraph and heading carries. A freeze
 * injected after `load` stops both at whatever phase they had reached, and
 * that phase is not reproducible: rendering ONE file twice that way reported
 * 4 of 8 page-widths different, 116 of 1185 elements off by a single pixel,
 * with identical DOM and identical visible text. The 2026-11-16 pass named
 * the marquee and missed `.reveal`.
 *
 * So the freeze is injected with addInitScript, before the first paint, and
 * names the final state of both families explicitly. ALWAYS RUN THE CONTROL
 * (--control, the same directory against itself) BEFORE BELIEVING A DIFF:
 * on this site a render harness that cannot report one tree identical to
 * itself cannot report two trees identical to each other.
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const FREEZE = `*,*::before,*::after{animation:none!important;transition:none!important;
scroll-behavior:auto!important}
.ticker-track{transform:none!important}
.reveal{opacity:1!important;transform:none!important;filter:none!important}`;

const WIDTHS = [1280, 390];

const probe = () => {
  const clone = document.documentElement.cloneNode(true);
  clone.querySelectorAll('script[type="application/ld+json"]').forEach((n) => n.remove());
  const geom = [];
  document.querySelectorAll('*').forEach((el) => {
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    geom.push([el.tagName, (el.className || '').toString(), el.id,
      Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height),
      s.color, s.backgroundColor, s.fontSize, s.fontWeight, s.display,
      s.textDecorationLine, s.outlineStyle].join('|'));
  });
  return { dom: clone.outerHTML, geom: geom.join('\n'), n: geom.length,
           text: document.body.innerText };
};

async function shoot(browser, dir, page, width, tag) {
  const ctx = await browser.newContext({
    viewport: { width, height: 900 }, deviceScaleFactor: 1,
  });
  await ctx.addInitScript((css) => {
    const put = () => {
      const s = document.createElement('style');
      s.textContent = css;
      document.documentElement.appendChild(s);
    };
    if (document.documentElement) put();
    else document.addEventListener('readystatechange', put, { once: true });
  }, FREEZE);
  const pg = await ctx.newPage();
  await pg.goto('file://' + path.join(dir, page), { waitUntil: 'load' });
  await pg.addStyleTag({ content: FREEZE });
  await pg.waitForTimeout(500);
  const result = await pg.evaluate(probe);
  const shot = path.join('/tmp', `render-diff-${tag}-${width}-${page}.png`);
  await pg.screenshot({ path: shot, fullPage: true });
  result.png = fs.readFileSync(shot);
  await ctx.close();
  return result;
}

(async () => {
  const args = process.argv.slice(2).filter((a) => a !== '--control');
  const control = process.argv.includes('--control');
  const [dirA, dirB] = args;
  if (!dirA || !dirB) {
    console.error('usage: node _tools/render-diff.js <dir-A> <dir-B> [page.html ...] [--control]');
    process.exit(2);
  }
  let pages = args.slice(2);
  if (!pages.length) {
    pages = fs.readdirSync(dirA)
      .filter((f) => f.endsWith('.html') && fs.existsSync(path.join(dirB, f)))
      .sort();
  }
  const browser = await chromium.launch();
  let ok = 0;
  let bad = 0;
  const right = control ? dirA : dirB;
  if (control) console.log('CONTROL: ' + dirA + ' against itself');
  for (const width of WIDTHS) {
    for (const page of pages) {
      const a = await shoot(browser, dirA, page, width, 'a');
      const c = await shoot(browser, right, page, width, 'c');
      const same = a.dom === c.dom && a.geom === c.geom && a.text === c.text
        && a.png.equals(c.png);
      console.log(`${same ? 'IDENTICAL' : 'DIFFERS  '}  ${width}px  ${page}  `
        + `dom ${a.dom === c.dom ? '=' : 'X'} geom ${a.geom === c.geom ? '=' : 'X'} `
        + `text ${a.text === c.text ? '=' : 'X'} pixels ${a.png.equals(c.png) ? '=' : 'X'}  `
        + `(${a.n} elements)`);
      same ? ok++ : bad++;
    }
  }
  console.log(`\nrender-diff: ${ok} identical, ${bad} different, of ${ok + bad}`);
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
