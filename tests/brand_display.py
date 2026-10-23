"""Shared brand colours and bounded WhatsApp widget, including missing old CSS."""
from playwright.sync_api import sync_playwright
import os
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8080')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(360,800),(390,844),(1366,768)]:
  page=b.new_page(viewport={'width':width,'height':height})
  for slug in ['/','/about','/contact','/projects','/news','/login']:
   page.goto(base+slug,wait_until='networkidle')
   page.locator('.whatsapp-float').scroll_into_view_if_needed()
   assert page.locator('footer .whatsapp-float').count()==1
   assert page.locator('.whatsapp-float').evaluate('el=>getComputedStyle(el).position')=='absolute'
   for selector,expected in [('.whatsapp-float',52 if width<641 else 58),('.whatsapp-float svg',32)]:
    box=page.locator(selector).bounding_box();assert abs(box['width']-expected)<1 and abs(box['height']-expected)<1
    assert box['x']>=0 and box['y']>=0 and box['x']+box['width']<=width and box['y']+box['height']<=height
   colours=page.locator('main h1,main h2,main h3,main h4').evaluate_all('els=>els.filter(e=>e.getBoundingClientRect().width>1).map(e=>getComputedStyle(e).color)')
   assert all(c in ['rgb(3, 73, 55)','rgb(192, 146, 64)'] for c in colours),(slug,colours)
   if slug=='/contact':
    assert page.locator('.office-contacts dt').all_text_contents()==['Email','Phone','WhatsApp']
    rows=page.locator('.office-contacts dd').all()
    assert len(rows)==4
    boxes=[r.bounding_box() for r in rows]
    assert all(boxes[i+1]['y']>=boxes[i]['y']+boxes[i]['height'] for i in range(3))
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.close()
 page=b.new_page();page.route('**/assets/editorial.css*',lambda route:route.abort())
 page.goto(base,wait_until='networkidle');page.locator('.whatsapp-float').scroll_into_view_if_needed();assert page.locator('.whatsapp-float svg').bounding_box()['width']==32
 page.screenshot(path='/tmp/scg-brand-display.png');b.close()
print('PASS: logo heading colours, WhatsApp sizing/position, footer attachment, missing older stylesheet resilience across desktop/mobile and six pages')
