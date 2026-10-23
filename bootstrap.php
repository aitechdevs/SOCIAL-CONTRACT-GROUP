<?php
declare(strict_types=1);
ini_set('session.use_strict_mode','1');
session_set_cookie_params(['httponly'=>true,'secure'=>!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off','samesite'=>'Lax']);
session_start();
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: strict-origin-when-cross-origin');
header("Content-Security-Policy: default-src 'self'; img-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; script-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'");
function e($s): string {return htmlspecialchars((string)$s, ENT_QUOTES,'UTF-8');}
function db(): PDO {static $db; if ($db) return $db; $path=__DIR__.'/config/local.php'; if(!is_file($path)) throw new RuntimeException('Database not configured.'); $c=require $path; return $db=new PDO($c['dsn'],$c['user'],$c['password'],[PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION,PDO::ATTR_DEFAULT_FETCH_MODE=>PDO::FETCH_ASSOC,PDO::ATTR_EMULATE_PREPARES=>false]);}
// Fixed office recipients; visitor input is used only in the validated Reply-To and body.
function notifyContactOffice(string $name, string $email, string $message, string $reference): bool {
 if (!filter_var($email,FILTER_VALIDATE_EMAIL) || preg_match('/[\r\n]/',$email)) return false;
 $headers=[
  'From'=>'Social Contract Group <info@socialcontractgroup.org>',
  'Reply-To'=>$email,
  'MIME-Version'=>'1.0',
  'Content-Type'=>'text/plain; charset=UTF-8',
  'Content-Transfer-Encoding'=>'8bit'
 ];
 $body="New website contact enquiry\nReference: ".$reference."\nName: ".$name."\nEmail: ".$email."\n\n".$message;
 $accepted=true;
 foreach (['socialcontractgroup@gmail.com','info@socialcontractgroup.org'] as $recipient) {
  try {$sent=mail($recipient,'SCG website contact enquiry',$body,$headers);}
  catch (Throwable $ex) {$sent=false;}
  if (!$sent) {error_log('SCG contact email handoff failed; submission reference '.$reference);$accepted=false;}
 }
 return $accepted;
}
$_SESSION['csrf'] ??= bin2hex(random_bytes(32));
header('Cache-Control: no-store');
$error=''; $success='';
if($_SERVER['REQUEST_METHOD']==='POST') {
 if(!hash_equals($_SESSION['csrf'],$_POST['csrf']??'')){http_response_code(403);exit('Invalid form token. Please reload.');}
 $action=$_POST['action']??'';
 if($action==='logout'){$_SESSION=[];session_destroy();header('Location: /');exit;}
 if(time()-($_SESSION['last_submit']??0)<3) {$error='Please wait a moment before trying again.';}
 else {$_SESSION['last_submit']=time();try {
 $name=trim($_POST['name']??'');$email=trim($_POST['email']??'');$password=$_POST['password']??'';
 if(($_POST['consent']??'')!=='yes') throw new InvalidArgumentException('Please read and accept the privacy notice.');
 if(strlen($password)>72) throw new InvalidArgumentException('Password must not exceed 72 bytes.');
 if(!filter_var($email,FILTER_VALIDATE_EMAIL)||strlen($email)>190) throw new InvalidArgumentException('Enter a valid email address.');
 if($action==='register'){
 if(strlen($name)<2||strlen($name)>120||strlen($password)<12||strlen($password)>72||!in_array($_POST['state']??'',$states??[])) throw new InvalidArgumentException('Enter your name, select a state, and use a password of 12–72 characters (maximum 72 bytes).');
 $q=db()->prepare('INSERT INTO users(name,email,password_hash,state) VALUES(?,?,?,?)');$q->execute([$name,$email,password_hash($password,PASSWORD_DEFAULT),$_POST['state']]);$success='Account created. You can now sign in.';
 }elseif($action==='login'){
 $q=db()->prepare('SELECT * FROM users WHERE email=?');$q->execute([$email]);$u=$q->fetch();
 if(!$u||!password_verify($password,$u['password_hash'])) throw new InvalidArgumentException('Email or password is incorrect.');
 session_regenerate_id(true);$_SESSION['user']=['id'=>$u['id'],'name'=>$u['name'],'role'=>$u['role']];header('Location: /dashboard');exit;
 }elseif(in_array($action,['contact','volunteer'],true)){
 $message=trim($_POST['message']??'');if(strlen($name)<2||strlen($name)>120||strlen($message)<10||strlen($message)>5000) throw new InvalidArgumentException('Enter your name and a message of 10–5,000 characters.');
 $q=db()->prepare('INSERT INTO submissions(kind,name,email,message) VALUES(?,?,?,?)');$q->execute([$action,$name,$email,$message]);$success='Thank you. Your submission has been received.';
 if($action==='contact'&&!notifyContactOffice($name,$email,$message,(string)db()->lastInsertId())) $success.=' Your message is saved, but email notification is temporarily unavailable. You can also reach our office at info@socialcontractgroup.org or 08030920092.';
 }else{throw new InvalidArgumentException('Unknown request.');}
 }catch(InvalidArgumentException $ex){$error=$ex->getMessage();}catch(PDOException $ex){$error=$ex->getCode()==='23000'?'An account with this email already exists.':'We could not save your request. Please try again later.';}catch(Throwable $ex){$error='Online submissions are not enabled yet. Please contact the site administrator.';}}}
