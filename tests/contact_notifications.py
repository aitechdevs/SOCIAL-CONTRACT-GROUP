"""Contact integration check against a disposable runtime with captured mail only.
Run with SCG_MAIL_CAPTURE_CONTAINER and SCG_BASE_URL; never target production.
"""
import os,re,subprocess,json,uuid,urllib.request,urllib.parse,http.cookiejar
container=os.environ['SCG_MAIL_CAPTURE_CONTAINER']
base=os.environ['SCG_BASE_URL']
assert base.startswith('http://127.0.0.1:'),'Local test runtime required'
client=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
html=client.open(base+'/contact').read().decode()
for link in ['mailto:socialcontractgroup@gmail.com','mailto:info@socialcontractgroup.org','tel:+2348030920092','https://wa.me/2348030920092']:
 assert link in html,link
csrf=re.search(r'name="csrf" value="([a-f0-9]+)"',html).group(1)
message='Contact mail integration check '+uuid.uuid4().hex
payload={'action':'contact','csrf':csrf,'name':'Test Visitor\r\nBcc: attacker@example.test','email':'visitor@example.test','message':message,'consent':'yes'}
body=client.open(base+'/contact',urllib.parse.urlencode(payload).encode()).read().decode()
assert 'Thank you. Your submission has been received.' in body
failed=os.environ.get('SCG_EXPECT_MAIL_FAILURE')=='1'
assert ('email notification is temporarily unavailable' in body)==failed
php='echo json_encode(array_map("file_get_contents",glob("/tmp/scg-mail-*.eml")));'
mails=json.loads(subprocess.check_output(['docker','exec',container,'php','-r',php]))
mails=[m for m in mails if message in m];assert len(mails)==2,len(mails)
assert any('To: socialcontractgroup@gmail.com' in m for m in mails)
assert any('To: info@socialcontractgroup.org' in m for m in mails)
for mail in mails:
 headers=mail.replace('\r\n','\n').split('\n\n',1)[0]
 assert 'From: Social Contract Group <info@socialcontractgroup.org>' in headers
 assert 'Reply-To: visitor@example.test' in headers
 assert 'Bcc:' not in headers
 assert 'Name: Test Visitor' in mail
php='$_SERVER["REQUEST_METHOD"]="GET";require "/var/www/html/bootstrap.php";$q=db()->prepare("SELECT COUNT(*) FROM submissions WHERE message=?");$q->execute([$argv[1]]);echo $q->fetchColumn();$q=db()->prepare("DELETE FROM submissions WHERE message=?");$q->execute([$argv[1]]);'
assert subprocess.check_output(['docker','exec',container,'php','-r',php,message]).decode()=='1'
print('PASS: contact details, saved enquiry, both recipients, safe Reply-To, header injection resistance'+(' and honest failure feedback' if failed else '')+'; no external mail sent')
