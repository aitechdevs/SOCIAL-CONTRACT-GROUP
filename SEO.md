# SEO and Google Search Console

## Implemented

- Unique titles and descriptions for 12 indexable public pages.
- Absolute HTTPS canonical URLs on `socialcontractgroup.org`.
- Open Graph and Twitter large-image cards with a local 1200 × 630 PNG.
- Organization, WebSite, WebPage and public-page breadcrumb JSON-LD. No invented address, reviews, event dates, statistics or social profiles.
- `sitemap.xml` lists only indexable, canonical public URLs. No invented modification dates.
- `robots.txt` permits public crawling and declares the absolute sitemap URL. Private source/configuration directories are crawl-blocked and protected by Apache.
- Login, registration, member/admin pages, errors and POST responses use noindex. Events and donations are also noindex while their content is pending. These pages are not crawl-blocked: search engines must fetch them to see noindex.
- HTTP and www requests for the production domain redirect to HTTPS non-www. Local development hosts are unaffected. If TLS terminates at a proxy, adapt redirects using only the hosting provider’s trusted proxy configuration to prevent a loop.
- The detailed initiative register appears on National Impact; Projects remains a category browser to reduce duplicated content.

## Deploy and check

Upload the complete `public_html` contents of the updated release package. This includes `seo.php`, `config/seo.php`, `robots.txt`, `sitemap.xml`, `assets/social-preview.png` and updated `.htaccess` and `index.php`. Preserve your private `config/local.php` database settings.

Check the real domain over HTTPS:

1. Home returns HTTP 200, with a canonical URL of `https://socialcontractgroup.org/`.
2. `https://socialcontractgroup.org/robots.txt` returns plain text, permits public crawling, and declares the correct sitemap.
3. `https://socialcontractgroup.org/sitemap.xml` returns XML with the production URLs.
4. HTTP and www requests redirect once to the HTTPS non-www equivalent, preserving paths and query parameters. Proxy/host-level redirects may also be in place; avoid loops.
5. Google Search Console’s URL Inspection Live Test can fetch a public page and reports no accidental crawl or indexing restriction.
6. Private paths remain inaccessible and member pages retain noindex. Robots.txt is not an access-control mechanism.

This environment could not check the live domain because DNS resolution was unavailable and outbound requests were denied by the network proxy. This does not establish that the domain is offline. Local Apache checks passed; real-host deployment is not verified.

## Register with Google: ownership required

**Google registration and sitemap submission have not been performed.** No authenticated Search Console connection, verification record, DNS/hosting access or confirmed live deployment is available in this session. No verification token has been fabricated.

Recommended method:

1. Sign in at https://search.google.com/search-console with the account that should own the property.
2. Add a **Domain** property: `socialcontractgroup.org` (no scheme or path).
3. Copy the exact TXT verification record issued by Google into the authoritative DNS service. Use cPanel Zone Editor only if that service actually hosts the domain’s authoritative DNS. Preserve all existing TXT records and use Google’s exact host/name and value.
4. Allow DNS changes to propagate, then select **Verify** in Search Console.
5. Once the website is deployed, open **Sitemaps** and submit `https://socialcontractgroup.org/sitemap.xml` (or `sitemap.xml` when the interface supplies the site prefix).
6. Check sitemap processing results and inspect the homepage plus representative public pages. Request indexing for important public pages through URL Inspection if available.

Alternative if DNS is unavailable: create a **URL-prefix** property for `https://socialcontractgroup.org/`, select the HTML tag verification method, and put only Google’s issued `content` token into `google_site_verification` in `config/seo.php`. Deploy that configuration and use Google’s Verify action. The meta tag is emitted server-side on the homepage. Do not use a Google account password, OAuth token or API key here. Keep the verification record/tag after ownership is established.

The verification TXT record or HTML meta tag is a public identifier and may be shared for implementation. Google account passwords and private credentials must not be shared in chat.

Declaring a sitemap in robots.txt assists discovery; it does not create a Search Console property, verify ownership or submit a sitemap inside the account. Sitemap submission and indexing are separate: Google controls whether and when eligible content is indexed.

## Maintaining SEO

Edit public metadata and the list of indexable routes in `seo.php`. Keep entries factual and consistent with rendered content. Change the production identity only in `config/seo.php`, then regenerate:

```sh
php tools/generate-sitemap.php
```

This updates both `sitemap.xml` and `robots.txt` from the same configured domain and public-route map. Run locally if cPanel has no terminal, then upload the two generated files. Add verified, original content and per-article sources before indexing new publication/event pages. Do not index empty placeholders or expose private pages to grow sitemap counts.

Tests: `python tests/seo.py` against the local Apache development server (default port 8080). Override with `SCG_BASE_URL` only for a controlled test environment; this test checks HTTP redirect behaviours using production Host headers. It validates sitemap/canonical consistency, unique descriptions/titles, JSON-LD, social images, noindex coverage, robots and source-file protection.

## Clean URL update

All public canonicals and sitemap entries now use clean paths such as `/about`. Legacy `/index.php` and query-string page links permanently redirect. The sitemap includes the Image credits page. See `CLEAN-URL-UPDATE.md` for the required Apache rules and how to preserve cPanel PHP settings.
