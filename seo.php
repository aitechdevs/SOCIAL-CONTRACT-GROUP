<?php
declare(strict_types=1);
$seoConfig = require __DIR__.'/config/seo.php';
$siteUrl = rtrim($seoConfig['site_url'], '/');
$seoPages = [
 'home' => ['Social Contract Group | Nigerian Civic & Policy Information', 'Explore Nigerian public policy, civic participation and national development with Social Contract Group. Find project references and community resources.'],
 'about' => ['About Social Contract Group | Purpose & Principles', 'Learn about Social Contract Group, its founding context, public accountability principles and approach to evidence-led civic information.'],
 'achievements' => ['PBAT Projects, Achievements & National Impact | SCG', 'Explore 12 policy and project research records associated with the Tinubu administration, with source links, verification status and questions for public scrutiny.'],
 'projects' => ['Nigeria Project & Policy Reference Library | SCG', 'Browse education, electricity, infrastructure, economy, institutional and agriculture references. Filter public policy themes and find official source starting points.'],
 'campaign' => ['2027 Nigeria Civic Information & INEC Resources | SCG', 'Find neutral civic information for Nigeria’s 2027 electoral process, including INEC references, information-checking guidance and peaceful participation.'],
 'chapters' => ['Nigeria State & FCT Chapter Directory | SCG', 'Search Social Contract Group’s proposed directory for Nigeria’s 36 states and FCT. Chapter contacts and operating status are awaiting verification.'],
 'news' => ['Nigeria Public Policy Resources & Insights | SCG', 'Explore source-led resources on Nigerian education, energy, infrastructure, the economy and institutions, plus Social Contract Group’s publication standards.'],
 'volunteer' => ['Civic Education Volunteer Enquiries | SCG', 'Enquire about volunteering for civic education, source checking, translation and community dialogue with Social Contract Group.'],
 'contact' => ['Contact Social Contract Group | Enquiries & Corrections', 'Contact Social Contract Group about policy sources, corrections, state chapter enquiries, civic education and community dialogue.'],
 'privacy' => ['Privacy Notice | Social Contract Group', 'Read how Social Contract Group uses account and enquiry information, session cookies and third-party font resources, including deployment disclosures.'],
 'sitemap' => ['Website Directory | Social Contract Group', 'Find Social Contract Group’s public information pages, project library, civic resources, state directory and member access pages.'],
];
function scgCanonical(string $page, string $siteUrl): string {
 return $siteUrl.($page === 'home' ? '/' : '/'.rawurlencode($page));
}
