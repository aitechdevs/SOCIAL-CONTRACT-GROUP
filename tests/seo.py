"""Validate rendered SEO and canonical redirects on the local Apache instance."""
import os,re,json,http.client,urllib.request,urllib.error,xml.etree.ElementTree as E
from html.parser import HTMLParser
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8080')
site='https://socialcontractgroup.org'
class Head(HTMLParser):
 def __init__(self):super().__init__();self.meta={};self.canonical=[];self.ld=[];self.in_ld=False;self.in_title=False;self.title=''
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='script' and a.get('type')=='application/ld+json':self.in_ld=True
  if tag=='title':self.in_title=True
 def handle_endtag(self,tag):
  if tag=='script':self.in_ld=False
  if tag=='title':self.in_title=False
 def handle_data(self,data):
  if self.in_ld:self.ld.append(json.loads(data))
  if self.in_title:self.title+=data
xml=urllib.request.urlopen(base+'/sitemap.xml');assert xml.headers.get_content_type() in ['application/xml','text/xml']
root=E.fromstring(xml.read());urls=[e.text for e in root.findall('{*}url/{*}loc')];assert len(urls)==11 and len(set(urls))==11
names=[];descriptions=[]
for url in urls:
 assert url.startswith(site+'/')
 r=urllib.request.urlopen(base+url[len(site):]);h=Head();h.feed(r.read().decode());assert h.canonical==[url]
 assert h.meta['robots'].startswith('index, follow') and r.headers['X-Robots-Tag'].startswith('index, follow')
 assert 40<len(h.meta['description'])<200
 assert h.meta['og:url']==url and h.meta['og:title']==h.title
 assert h.meta['twitter:card']=='summary_large_image'
 assert len(h.ld)==1 and len(h.ld[0]['@graph'])>=3
 assert '/#organization' in json.dumps(h.ld)
 assert 'google-site-verification' not in h.meta # No fake verification token.
 names.append(h.title);descriptions.append(h.meta['description'])
assert len(set(names))==11 and len(set(descriptions))==11
for page in ['login','register','dashboard','admin','events','donate','missing']:
 try:r=urllib.request.urlopen(base+'/index.php?page='+page)
 except urllib.error.HTTPError as ex:r=ex
 h=Head();h.feed(r.read().decode());assert 'noindex' in h.meta['robots'],page;assert 'noindex' in r.headers['X-Robots-Tag'],page
 assert not h.ld
head=urllib.request.urlopen(urllib.request.Request(base+'/',method='HEAD'));assert head.headers['X-Robots-Tag'].startswith('index, follow')
robots=urllib.request.urlopen(base+'/robots.txt').read().decode();assert 'Sitemap: '+site+'/sitemap.xml' in robots;assert 'Disallow: /\n' not in robots;assert 'Disallow: /index.php' not in robots
image=urllib.request.urlopen(base+'/assets/social-preview.png').read();assert image[:8]==b'\x89PNG\r\n\x1a\n'
for host in ['socialcontractgroup.org','www.socialcontractgroup.org']:
 from urllib.parse import urlsplit
 parsed=urlsplit(base);c=http.client.HTTPConnection(parsed.hostname,parsed.port);c.request('GET','/index.php?page=about',headers={'Host':host});r=c.getresponse();assert r.status==301;assert r.headers['Location']==site+'/index.php?page=about';c.close()
for private in ['/seo.php','/tools/generate-sitemap.php']:
 try:urllib.request.urlopen(base+private);raise AssertionError(private+' exposed')
 except urllib.error.HTTPError as ex:assert ex.code==403
print('PASS: 11 sitemap URLs, unique metadata, canonicals, structured data, social previews, noindex, robots and production redirects')
