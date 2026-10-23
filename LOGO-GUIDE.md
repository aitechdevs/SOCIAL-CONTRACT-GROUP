# Social Contract Group logo

The new full-name identity combines an SCG monogram with the words **SOCIAL CONTRACT GROUP**, in forest green with a restrained gold linking element. The supplied design is an original generated raster artwork; no claim is made that it is an official government or party mark.

## Publication master

`assets/brand/social-contract-group-logo-master.png`

- Original resolution: 2172 × 724 pixels.
- Format: PNG, RGBA with transparent background.
- Suitable for website use, document headers, presentations, letterheads and publication layouts at an appropriate physical size.
- This is a raster master, not an editable SVG/AI/EPS vector. The favicon is a separate editable SVG text icon, not a vector reconstruction of the full logo.
- Keep the 3:1 canvas aspect ratio. Do not stretch, remove letters, or use a screenshot of the header as a publication source.
- Use a white or light background for best contrast. The website places the logo on a white panel in the dark footer.
- Retain clear space around the mark. At 300 pixels per inch, the complete canvas is about 7.24 × 2.41 inches; actual artwork includes transparent clear space. Larger placement reduces effective print resolution.

`releases/social-contract-group-logo-master.png` is an identical convenient download. `releases/social-contract-group-logo-kit.zip` contains the master and this guide.

## Existing-site update

For the latest clean-URL/full-screen revision, use `CLEAN-URL-UPDATE.md` and its new package. The instructions below refer to the earlier logo-only package.

1. Back up your existing `index.php` and `assets` directory outside the domain document root.
2. Upload and extract `releases/scg-logo-update-fixed.zip` into the domain document root (`socialcontractgroup.org` in the confirmed cPanel setup), replacing matching files.
3. The update includes the current frontend assets and `index.php`, so it also works if you have not yet installed the previous editorial image update. It adds `assets/brand/social-contract-group-logo-master.png` and `assets/favicon.svg`, and updates the header/footer, responsive logo sizing, favicon reference, structured-data logo URL and social-sharing image.
4. Your private `config/local.php`, database tables, `.htaccess` and hosting PHP settings are not included and are preserved.
5. Refresh the website; clear any hosting/CDN page cache if necessary. Check header and footer at mobile and desktop widths.
6. Move the uploaded ZIP outside the public domain folder after extraction.

## Full source package for cPanel

`releases/social-contract-group-cpanel.zip` contains all PHP, HTML templates, CSS, plain JavaScript and image assets under `public_html/`, plus the SQL schema and guides under `setup/`. It requires no Node.js or build step. Upload only `public_html/` contents to the domain document root. Keep existing private database configuration on an already deployed site. Import the SQL schema only for a new database; do not re-import it into your working database for a logo update.

## Asset permissions

The corrected archives explicitly store public files with mode 644 and directories with mode 755. If a page renders as plain text with oversized icons or missing images, check that `assets/`, `assets/brand/` and `assets/photos/` are 755 and that CSS, JavaScript and image files inside them are 644. Keep private `config/local.php` restrictive; do not change it as part of an asset repair.
