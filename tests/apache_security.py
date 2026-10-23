"""Run against Apache with the project .htaccess enabled, not PHP's dev server."""
import urllib.request,urllib.error,os
base=os.environ.get('SCG_BASE_URL','http://127.0.0.1:8080')
for path in ['/config/local.php','/config/example.php','/database/schema.sql','/bootstrap.php','/data.php','/.git/HEAD','/assets/','/tests/smoke.py']:
 try:
  response=urllib.request.urlopen(base+path)
  raise AssertionError((path,'unexpectedly accessible',response.status))
 except urllib.error.HTTPError as error:assert error.code in [403,404],(path,error.code)
r=urllib.request.urlopen(base+'/');assert r.status==200
assert r.headers['X-Content-Type-Options']=='nosniff'
assert "frame-ancestors 'none'" in r.headers['Content-Security-Policy']
assert r.headers['Cache-Control']=='no-store'
print('PASS: 8 private paths/listings denied; public home and security headers correct')
