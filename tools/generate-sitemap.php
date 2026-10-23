<?php
declare(strict_types=1);
if(PHP_SAPI !== 'cli'){http_response_code(404);exit;}
require __DIR__.'/../seo.php';
$xml = '<?xml version="1.0" encoding="UTF-8"?>'."\n".'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'."\n";
foreach(array_keys($seoPages) as $page){
 $url=htmlspecialchars(scgCanonical($page,$siteUrl),ENT_XML1|ENT_QUOTES,'UTF-8');
 $xml.='  <url><loc>'.$url.'</loc></url>'."\n";
}
$xml.="</urlset>\n";
if(file_put_contents(__DIR__.'/../sitemap.xml',$xml,LOCK_EX)===false)throw new RuntimeException('Could not write sitemap.');
$robots="User-agent: *\nAllow: /\n";
foreach(['/config/','/database/','/tests/','/tools/','/docs/','/.git/','/bootstrap.php','/data.php','/seo.php'] as $private){$robots.='Disallow: '.$private."\n";}
$robots.="\n# Account/admin pages use noindex headers and meta tags, not crawl blocks.\n# Crawlers must fetch these pages to observe noindex. Authentication protects data.\nSitemap: {$siteUrl}/sitemap.xml\n";
if(file_put_contents(__DIR__.'/../robots.txt',$robots,LOCK_EX)===false)throw new RuntimeException('Could not write robots file.');
echo 'Generated sitemap for '.count($seoPages)." public pages and robots.txt.\n";
