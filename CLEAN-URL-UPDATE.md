# Clean URLs and full-screen slideshow

## Existing-site installation

1. Download `releases/scg-clean-urls-fullscreen-update.zip` from GitHub.
2. Back up your current website files and `.htaccess` outside the domain document root. In cPanel, enable **Settings → Show Hidden Files** so `.htaccess` is visible.
3. Upload and extract the update into the confirmed `socialcontractgroup.org` domain folder. The update includes the application source, frontend assets, regenerated sitemap/robots and the new `.htaccess` routing rules. Allow matching application files to be replaced.
4. Preserve any cPanel-generated PHP handler/version blocks from your previous `.htaccess`: append those hosting blocks beneath the new website rules. Keep `.user.ini`, `php.ini`, your `config` folder and existing database unchanged. Do not re-import SQL for this update.
5. Check `/`, `/about`, `/projects`, `/contact`, `/login` and `/image-credits`. Old `/index.php` and `/index.php?page=about` URLs should redirect to their clean equivalents. Log in and test member/admin access and an enquiry submission.
6. Confirm the browser loads CSS and images. ZIP files explicitly use 644 permissions for public files and 755 for directories.
7. Move the uploaded ZIP outside the public domain folder after extraction. Clear any hosting/CDN HTML cache and refresh the browser.

The domain must be served by Apache 2.4 (or compatible LiteSpeed) with URL rewriting and `.htaccess` overrides enabled. This is standard on most cPanel shared hosting. PHP remains the backend; `.php` is removed from public page URLs.

## Behaviour

- Public pages use `/about`, `/projects`, `/news`, etc.; the homepage uses `/`.
- GET/HEAD visits to legacy index.php URLs redirect permanently (301), preserving their page destination. Contact, registration and other POST flows remain functional.
- Navigation, form redirects, canonical/Open Graph URLs, structured data and sitemap use clean paths.
- Unknown paths retain HTTP 404; private setup/config paths remain blocked; account/admin pages remain noindex.
- The homepage has a full-width, image-only slideshow that fills the viewport below navigation, with previous/next/pause controls and reduced-motion support.
- Visible image captions and the source banners are removed. Accessibility alt descriptions remain. Image provenance is available on the separate Image credits page linked from the footer.
- Source/status labels on project records continue to describe the available evidence; project completion is not asserted without evidence.

## Embedded lettering

The update replaces all nine active pictures with text-free edited versions under `assets/photos-clean/`. Words on signs, book covers, posters, uniforms and equipment were removed in the image edits. The SCG identity/logo and functional interface labels remain. Previously uploaded `assets/photos/` files are unused by the new templates.
