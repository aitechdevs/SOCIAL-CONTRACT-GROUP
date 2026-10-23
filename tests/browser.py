from playwright.sync_api import sync_playwright
import os
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8000')
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path=os.environ.get('SCG_CHROMIUM','/usr/bin/chromium'),args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
 page.goto(base,wait_until='networkidle');page.locator('img[loading=lazy]').evaluate_all("imgs=>imgs.forEach(i=>i.loading='eager')");page.wait_for_function("() => Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)");page.screenshot(path='/tmp/scg-desktop.png',full_page=True)
 page.get_by_role('button',name='Next slide').click();assert page.locator('#slide-number').inner_text()=='02'
 page.get_by_role('button',name='Pause slideshow').click()
 for expected in ['03','04','01']:
  page.get_by_role('button',name='Next slide').click();assert page.locator('#slide-number').inner_text()==expected
 page.goto(base+'/index.php?page=projects');page.locator('#project-filter').select_option('03');assert page.locator('.project-card:visible').count()==1
 page.goto(base+'/index.php?page=chapters');page.locator('#state-search').fill('Lagos');assert page.locator('[data-state]:visible').count()==1
 page.locator('#state-search').fill('zzzz');assert page.locator('#no-states').is_visible()
 page.set_viewport_size({'width':390,'height':844});page.goto(base,wait_until='networkidle')
 assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
 page.get_by_role('button',name='Open navigation').click();assert page.locator('#navigation').is_visible()
 page.keyboard.press('Escape');assert not page.locator('#navigation').is_visible()
 page.locator('img[loading=lazy]').evaluate_all("imgs=>imgs.forEach(i=>i.loading='eager')");page.wait_for_function("() => Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)");page.screenshot(path='/tmp/scg-mobile.png',full_page=True)
 for route in ['about','achievements','chapters','login','register','contact','sitemap']:
  page.goto(base+'/index.php?page='+route);assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),route
 assert not errors,errors
 browser.close();print('PASS: desktop/mobile layout, navigation, slider, filters, no JavaScript errors')
