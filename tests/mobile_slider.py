"""Complete image and separate captions must fit mobile widths on all four slides."""
import os
from playwright.sync_api import sync_playwright
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8080')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(320,740),(360,800),(390,844),(470,840),(768,1024),(844,390)]:
  page=b.new_page(viewport={'width':width,'height':height});page.goto(base,wait_until='networkidle');page.get_by_role('button',name='Pause slideshow').click()
  for i in range(4):
   im=page.locator('.slide-frame.is-active');box=im.bounding_box();assert abs(box['width']/box['height']-16/9)<.02
   assert im.evaluate('e=>getComputedStyle(e).objectFit')=='contain'
   assert im.evaluate('e=>getComputedStyle(e).transform')=='none'
   photo=page.locator('.hero-visual').bounding_box();caption=page.locator('.slide-caption').bounding_box();controls=page.locator('.slide-controls').bounding_box()
   assert caption['y']>=photo['y']+photo['height']-1
   assert controls['y']>=caption['y']+caption['height']-1
   assert controls['x']>=0 and controls['x']+controls['width']<=width
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
   if i<3:
    page.get_by_role('button',name='Next slide').click();page.wait_for_function("()=>document.querySelector('.homepage-hero').getAttribute('aria-busy')==='false'")
  page.close()
 b.close()
print('PASS: all four full-image slides, no zoom cropping, separate captions/controls and no overflow at six phone/tablet viewport sizes')
