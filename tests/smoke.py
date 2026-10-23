"""HTTP integration checks; use a disposable database for optional write tests."""
import os,re,time,urllib.request,urllib.parse,http.cookiejar,uuid
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8000')
jar=http.cookiejar.CookieJar();client=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
def get(page=''):
 try:
  r=client.open(base+('/'+page if page else '/'));return r.status,r.read().decode(),r.url
 except urllib.error.HTTPError as ex:return ex.code,ex.read().decode(),ex.url
def post(page,data):
 status,body,_=get(page);csrf=re.search(r'name="csrf" value="([a-f0-9]+)"',body).group(1)
 data['csrf']=csrf;data['consent']='yes'
 r=client.open(base+'/'+page,urllib.parse.urlencode(data).encode());return r.status,r.read().decode(),r.url
pages=['','about','achievements','projects','campaign','chapters','news','events','volunteer','donate','contact','register','login','privacy','sitemap','image-credits']
for page in pages:
 status,body,_=get(page);assert status==200,(page,status);assert '<main id="main">' in body;assert 'Fatal error' not in body
assert get('missing')[0]==404
assert '/login' in get('dashboard')[2]
assert '/login' in get('admin')[2]
try:client.open(base+'/contact',urllib.parse.urlencode({'action':'contact','csrf':'wrong'}).encode());raise AssertionError('CSRF accepted')
except urllib.error.HTTPError as ex:assert ex.code==403
print('PASS: 16 public pages, 404, dashboard/admin redirects and CSRF rejection')
if os.environ.get('SCG_TEST_DATABASE')=='1':
 email='test-'+uuid.uuid4().hex[:12]+'@example.test';password='Example-only-password-123!'
 _,body,_=post('register',{'action':'register','name':'Smoke Test','email':email,'password':password,'state':'Lagos'});assert 'Account created' in body,body
 time.sleep(3.1)
 _,body,_=post('login',{'action':'login','email':email,'password':password});assert 'Hello, Smoke Test' in body
 assert get('admin')[0]==403
 time.sleep(3.1)
 _,body,_=post('contact',{'action':'contact','name':'Smoke Test','email':email,'message':'Integration check: civic information enquiry.'});assert 'submission has been received' in body
 time.sleep(3.1)
 _,body,_=post('volunteer',{'action':'volunteer','name':'Smoke Test','email':email,'message':'Integration check: available for source checking.'});assert 'submission has been received' in body
 _,body,_=post('dashboard',{'action':'logout'});assert '/login' in get('dashboard')[2]
 print('PASS: registration, login, member dashboard, admin denial, contact, volunteer, logout')
