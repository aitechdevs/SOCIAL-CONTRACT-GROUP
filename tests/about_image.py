"""Replacement feature preserves proportions; removed route stays removed."""
import os,urllib.request,urllib.error
from playwright.sync_api import sync_playwright
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8080')
try:urllib.request.urlopen(base+'/image-credits');raise AssertionError('Removed page still exists')
except urllib.error.HTTPError as e:assert e.code==404
assert 'image-credits' not in urllib.request.urlopen(base+'/sitemap.xml').read().decode()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 for width,height in [(390,844),(1366,900)]:
  page=b.new_page(viewport={'width':width,'height':height});page.goto(base+'/about',wait_until='networkidle')
  photo=page.locator('.about-feature img');photo.scroll_into_view_if_needed()
  page.wait_for_function('()=>document.querySelector(".about-feature img").naturalWidth>0')
  assert photo.get_attribute('src').endswith('tinubu-community-feature.webp')
  assert photo.evaluate('el=>getComputedStyle(el).objectFit')=='contain'
  box=photo.bounding_box();assert abs(box['width']/box['height']-16/9)<.02
  assert page.locator('a[href="/image-credits"]').count()==0
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.screenshot(path=f'/tmp/scg-about-{width}.png');page.close()
 b.close()
print('PASS: responsive About image, natural proportions, removed credits route/link/sitemap entry')
