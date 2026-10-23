# cPanel deployment

1. Select PHP 8.2 or newer in MultiPHP Manager. Enable PDO, pdo_mysql, sessions and mbstring if available. Serve only over HTTPS.
2. In MySQL Database Wizard create a database and dedicated user. cPanel usually prefixes names with the account username. Grant SELECT and INSERT for runtime use. Use a separate privileged account for schema import and role changes.
3. Import `database/schema.sql` in phpMyAdmin once. Do not rerun it on a populated database.
4. Upload the PHP files, `assets`, `config`, and `.htaccess` into the domain document root. Do not upload tests, documentation, database exports, Git metadata or the source DOCX into the public directory. Apache must honour `.htaccess`; its deny rules block private directories and internal files.
5. Create `config/local.php` from the example with your actual database details. Give it restrictive permissions supported by your host (typically 600/640). Prefer storing credentials outside public_html and adapting the configuration include if your host permits it.
6. Register the first member via the site. Using phpMyAdmin and a privileged account, promote only a verified operator: `UPDATE users SET role='admin' WHERE email='your-verified-operator-address';`. Sign out and back in to refresh the role. No default administrator or public admin promotion exists.
7. Verify home and all sitemap pages, register/login/logout, contact and volunteer submission, member dashboard, unauthorised admin denial, and admin enquiry visibility. Verify `/config/local.php`, `/database/schema.sql`, `/bootstrap.php`, `/.git/HEAD` and directory listings return 403/404. Test on mobile and with keyboard navigation.
8. Before public launch: complete the operator identity, real contact route, privacy/legal basis and retention policy; verify chapter contacts, source claims and any event announcements; add real social URLs. Use host-level rate limiting, backups, error logging, monitoring and database access restrictions. Email verification, password recovery and stronger distributed rate limiting are not implemented; assess and implement these before broad account enrolment.

## Donation and editorial controls

Donations remain disabled; there is no payment integration or bank instruction. Confirm legal status, funding rules, beneficiary account, oversight, payment processor, refund rules and disclosures before implementing collection in a separate development task.

The admin dashboard lists members count and the latest 100 enquiries. It is read-only and does not publish articles or edit projects. Source verification and content edits currently happen in `data.php` and `index.php`. The security model assumes a trusted administrator and server operator. Role changes require fresh login; revoke active sessions when removing administrator access.

## Third-party resources

Logos and icons are local SVGs; the editorial imagery uses owner-supplied WebP illustrations with visible captions. See IMAGE-MANIFEST.md for provenance and excluded files. Optional typography uses Google Fonts, with system fallbacks; remove font links for a fully self-hosted deployment or self-host licensed fonts. Reference links point to third-party sites; they are starting points, not endorsements or proof of a particular claim.

## Search visibility

See `SEO.md` for the exact deployment, Google ownership-verification and sitemap-submission steps. Upload `seo.php`, `config/seo.php`, `robots.txt`, `sitemap.xml`, `assets/social-preview.png` and the updated application/Apache files. `config/seo.php` is a public-identity configuration file; keep `config/local.php` private. The `tools` directory contains a CLI-only sitemap generator and is denied over HTTP. Google Search Console verification and submission require the property owner and have not been completed by generating these files.
