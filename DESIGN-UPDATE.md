# Installing the editorial/image update

This historical guide describes the earlier layout package. For the current full-screen/text-free update with clean URLs, use `CLEAN-URL-UPDATE.md`, including its Apache routing instructions.

Download `releases/scg-editorial-image-update.zip` from GitHub. This is an update for an existing installation, not the full first-install archive.

1. Back up `index.php` and your existing `assets` directory outside the website document root.
2. Upload the update ZIP into the domain document root (`socialcontractgroup.org` in the confirmed cPanel setup).
3. Extract there, allowing replacement of `index.php`, `assets/app.js` and `assets/social-preview.png`. The package also adds `assets/editorial.css` and `assets/photos/`.
4. Existing `config/local.php`, database contents, `.htaccess` and hosting PHP settings are not part of the update and are preserved.
5. Refresh the page. CSS and JavaScript URLs have updated version parameters; clear any hosting/CDN HTML cache if the previous layout persists.
6. Check the four sliders, topic filters on Home and News, mobile navigation, public pages, registration/login and the administrator dashboard.
7. Move the uploaded ZIP out of the public domain folder after extraction.

Nine supplied images are used as illustrations. The image provenance and exclusions are documented in `IMAGE-MANIFEST.md`. No claims of actual project completion or official image provenance are made.
