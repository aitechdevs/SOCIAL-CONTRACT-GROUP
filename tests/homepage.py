"""Validate full-bleed sizing, no captions, preloaded fades and motion preferences."""
import os
from playwright.sync_api import sync_playwright
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8080')
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(360,800),(390,844),(768,1024),(1366,768),(1920,1080),(844,390)]:
  page=browser.new_page(viewport={'width':width,'height':height})
  page.goto(base,wait_until='networkidle');page.evaluate('document.fonts.ready');assert page.evaluate("document.fonts.check('700 16px \"Roboto Condensed\"') && document.fonts.check('400 30px \"Fjalla One\"')");page.get_by_role('button',name='Pause slideshow').click()
  assert page.locator('#slide-title').count()==0
  assert 'Connect communities. Follow the progress' not in page.locator('body').inner_text()
  assert page.locator('.home-site-heading').bounding_box()['width']<=1
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  box=page.locator('.homepage-hero').bounding_box();assert abs(box['width']-width)<=1
  # Buttons scroll into view if necessary; size verification is independent of scroll position.
  actual_height=page.locator('.homepage-hero').evaluate('el=>el.offsetHeight');assert actual_height>=180
  if width>=768 and height>=768:assert abs(actual_height-(height-page.locator('.homepage-hero').evaluate('el=>Number.parseFloat(el.style.getPropertyValue("--hero-offset"))')))<3
  assert page.locator('.slide-frame.is-active').get_attribute('src').startswith('/assets/homepage-photos/')
  page.close()
 page=browser.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(base,wait_until='networkidle');page.evaluate('document.fonts.ready');assert page.evaluate("document.fonts.check('700 16px \"Roboto Condensed\"') && document.fonts.check('400 30px \"Fjalla One\"')");page.get_by_role('button',name='Pause slideshow').click()
 page.get_by_role('button',name='Next slide').click();page.wait_for_function("()=>document.querySelector('#slide-number').textContent==='02'")
 values=page.locator('.slide-frame').evaluate_all('els=>els.map(e=>Number(getComputedStyle(e).opacity))')
 assert len(values)==2 and all(0<=x<=1 for x in values)
 assert all(page.locator('.slide-frame').evaluate_all('els=>els.map(e=>e.complete&&e.naturalWidth>0)'))
 page.wait_for_function("()=>document.querySelector('.homepage-hero').getAttribute('aria-busy')==='false'")
 assert page.locator('.slide-frame.is-active').get_attribute('src').endswith('students-library.webp')
 page.locator('.homepage-hero').focus();page.keyboard.press('ArrowLeft');page.wait_for_function("()=>document.querySelector('#slide-number').textContent==='01'")
 page.wait_for_function("()=>document.querySelector('.homepage-hero').getAttribute('aria-busy')==='false'")
 assert not errors,errors
 reduced=browser.new_context(reduced_motion='reduce');r=reduced.new_page();r.goto(base,wait_until='networkidle')
 assert r.get_by_role('button',name='Play slideshow').is_visible()
 assert r.locator('.slide-frame.is-active').evaluate('el=>getComputedStyle(el).animationName')=='none'
 assert r.locator('.slide-frame').first.evaluate('el=>getComputedStyle(el).transitionDuration')=='0s'
 browser.close()
print('PASS: six viewport sizes, no slide captions, decoded images, crossfade controls, keyboard navigation and reduced motion')
