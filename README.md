# Social Contract Group

A responsive, source-led Nigerian civic information website. PHP 8.2+, MySQL 8 / MariaDB 10.6+, HTML, CSS and plain JavaScript. No Node.js, framework or build step.

The supplied SCG document informs the policy taxonomy; unsupported figures, election dates, comparative accusations and electoral advocacy have not been reproduced as factual reporting. No donation transactions are enabled.

See [deployment instructions](DEPLOYMENT.md), [sitemap](SITEMAP.md) and [asset guide](ASSET-GUIDE.md).

## Download for cPanel

[Download the cPanel-ready ZIP](https://github.com/aitechdevs/SOCIAL-CONTRACT-GROUP/raw/refs/heads/main/releases/social-contract-group-cpanel.zip)

The archive contains `public_html/` for the website and `setup/` for the database schema and guides. Upload only the contents of `public_html/` into your domain’s document root. Import `setup/schema.sql` through phpMyAdmin, then create your private `config/local.php` as described in `setup/DEPLOYMENT.md`. The package contains no production database credentials or preset admin account.

GitHub’s **Code → Download ZIP** downloads the full development repository instead. Use the dedicated cPanel archive above for deployment. Do not upload the `releases` directory into your web root.

## Updating the existing live site

Use [the editorial/image update ZIP](https://github.com/aitechdevs/SOCIAL-CONTRACT-GROUP/raw/refs/heads/main/releases/scg-editorial-image-update.zip) and follow `DESIGN-UPDATE.md`. It preserves private database configuration and hosting settings. Image provenance and exclusions are in `IMAGE-MANIFEST.md`.

## Logo and publication artwork

The full-name logo is integrated into the header and footer. Download the transparent PNG master or logo kit from `releases/`; see `LOGO-GUIDE.md` for format, print sizing and the existing-site update instructions. The full cPanel source archive includes the new logo.

## Local development

With PHP and MySQL installed:
1. Create a database and limited database user. Import `database/schema.sql` once.
2. Copy `config/example.php` to `config/local.php`. Set the DSN, user and password privately. Never commit this file.
3. Run `php -S 127.0.0.1:8000 -t .` from this directory. PHP's built-in server is for local development only.
4. Visit the home page, register an account, sign in, and submit a contact or volunteer enquiry.

Use the existing checkout; a Git worktree is unnecessary. Public pages render without a configured database, while account/submission forms report that setup is unavailable. Session cookies and CSRF tokens protect forms. Prepared SQL and escaped output protect database and page boundaries. This is a working starter with member and read-only admin dashboards, not a full CMS.

## Validation

Run PHP lint over PHP files. `python tests/smoke.py` exercises public routes, security boundaries and forms against a server at `http://127.0.0.1:8000`. Set `SCG_TEST_DATABASE=1` only against a disposable configured database to exercise registration, login and stored enquiries; that test creates a member and enquiries. `python tests/browser.py` uses an installed Python Playwright and Chromium for mobile navigation, slider controls, filters and screenshots.

## Corrected asset-permission package

If a deployed page has no styling or has missing images, download `releases/scg-logo-update-fixed.zip`. It contains the current frontend with explicit 644 file and 755 directory permissions. Extract it into the domain document root and allow matching frontend files to be replaced. Private configuration and database files are excluded. See `LOGO-GUIDE.md`.
