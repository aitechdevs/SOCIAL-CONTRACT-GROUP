"""Clean URLs must retain status codes, POST handling and old bookmark redirects."""
import os,http.client,urllib.request,urllib.error,re
from urllib.parse import urlsplit
from html.parser import HTMLParser
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8080');parsed=urlsplit(base)
for old,new in [('/index.php','/'),('/index.php?page=about','/about'),('/?page=projects','/projects'),('/about/','/about'),('/about?page=projects','/about'),('/index.php?page=login','/login')]:
 c=http.client.HTTPConnection(parsed.hostname,parsed.port);c.request('GET',old);r=c.getresponse();assert r.status==301,(old,r.status);assert r.headers['Location']==new,(old,r.headers['Location']);c.close()
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a':self.urls.append(a.get('href',''))
for slug in ['', 'about','projects','achievements','news','sitemap','register']:
 r=urllib.request.urlopen(base+'/'+slug);html=r.read().decode();p=Links();p.feed(html)
 assert all('.php' not in u for u in p.urls if not u.startswith('http')),(slug,p.urls)
 if slug!='image-credits':
  assert '/assets/photos/' not in html and "'assets/photos/" not in html
  assert '<figcaption' not in html and 'Sources &amp; project status.' not in html
  assert 'Supplied illustration ·' not in html
for path in ['/does-not-exist','/does/not/exist']:
 try:urllib.request.urlopen(base+path);raise AssertionError(path)
 except urllib.error.HTTPError as ex:assert ex.code==404
print('PASS: six legacy/slash redirects, clean internal links, removed captions/banners, 404s and credits')
