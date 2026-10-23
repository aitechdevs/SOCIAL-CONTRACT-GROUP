from playwright.sync_api import sync_playwright
import os
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8000')
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path=os.environ.get('SCG_CHROMIUM','/usr/bin/chromium'),args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
 page.goto(base,wait_until='networkidle');assert abs(page.locator('.fullscreen-hero').bounding_box()['width']-page.viewport_size['width'])<2;page.locator('img[loading=lazy]').evaluate_all("imgs=>imgs.forEach(i=>i.loading='eager')");page.wait_for_function("() => Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)");page.screenshot(path='/tmp/scg-desktop.png',full_page=True)
 page.get_by_role('button',name='Education',exact=True).click();assert page.locator('.resource-grid .topic-card:visible').count()==1
 page.get_by_role('button',name='Featured topics',exact=True).click();assert page.locator('.resource-grid .topic-card:visible').count()==3
 assert page.locator('.slide-frame.is-active').get_attribute('src').endswith('community-skyline.webp')
 page.get_by_role('button',name='Next slide').click();page.wait_for_function("()=>document.querySelector('#slide-number').textContent==='02'");page.wait_for_function("()=>document.querySelector('.homepage-hero').getAttribute('aria-busy')==='false'")
 assert page.locator('.slide-frame.is-active').get_attribute('src').endswith('students-library.webp')
 page.get_by_role('button',name='Pause slideshow').click()
 for expected in ['03','04','01']:
  page.get_by_role('button',name='Next slide').click();page.wait_for_function("expected=>document.querySelector('#slide-number').textContent===expected",arg=expected);page.wait_for_function("()=>document.querySelector('.homepage-hero').getAttribute('aria-busy')==='false'")
 page.goto(base+'/news');page.get_by_role('button',name='Energy',exact=True).focus();page.keyboard.press('Enter')
 assert page.locator('.resource-grid .topic-card:visible').count()==1
 assert page.get_by_role('button',name='Energy',exact=True).get_attribute('aria-pressed')=='true'
 page.get_by_role('button',name='All topics',exact=True).click();assert page.locator('.resource-grid .topic-card:visible').count()==6
 page.goto(base+'/projects');page.locator('#project-filter').select_option('03');assert page.locator('.project-card:visible').count()==1
 page.goto(base+'/chapters');page.locator('#state-search').fill('Lagos');assert page.locator('[data-state]:visible').count()==1
 page.locator('#state-search').fill('zzzz');assert page.locator('#no-states').is_visible()
 page.set_viewport_size({'width':390,'height':844});page.goto(base,wait_until='networkidle')
 assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
 assert page.locator('.fullscreen-hero .hero-copy').count()==0
 assert page.locator('figcaption').count()==0
 page.get_by_role('button',name='Open navigation').click();assert page.locator('#navigation').is_visible()
 page.keyboard.press('Escape');assert not page.locator('#navigation').is_visible()
 page.locator('img[loading=lazy]').evaluate_all("imgs=>imgs.forEach(i=>i.loading='eager')");page.wait_for_function("() => Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)");page.screenshot(path='/tmp/scg-mobile.png',full_page=True)
 for route in ['about','achievements','projects','news','chapters','login','register','contact','sitemap']:
  page.goto(base+'/'+route);assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),route
  page.locator('img[loading=lazy]').evaluate_all("imgs=>imgs.forEach(i=>i.loading='eager')");page.wait_for_function("() => Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)")
 assert not errors,errors
 browser.close();print('PASS: desktop/mobile layout, navigation, slider, filters, no JavaScript errors')
