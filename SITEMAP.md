# Sitemap

Routes use `index.php?page=...` so they work without URL rewriting.

| Route | Purpose |
|---|---|
| `index.php` | Homepage, four slides, policy cards, project overview and participation links |
| `?page=about` | Identity, purpose, editorial principles |
| `?page=achievements` | PBAT Major Projects, Achievements & National Impact; six categories, source/status disclosure |
| `?page=projects` | Filterable project and policy reference library |
| `?page=campaign` | Neutral 2027 civic information and INEC reference |
| `?page=chapters` | Searchable 36-state and FCT directory; contacts pending |
| `?page=news` | Policy resource desk and editorial standard |
| `?page=events` | Honest empty state pending confirmed events |
| `?page=volunteer` | Civic volunteer enquiry form |
| `?page=donate` | Funding transparency; payment collection disabled |
| `?page=contact` | Stored enquiry form |
| `?page=register` | Member account creation |
| `?page=login` | Authentication |
| `?page=dashboard` | Authenticated member navigation and logout |
| `?page=admin` | Admin-only member count and recent submissions |
| `?page=privacy` | Data-use notice and deployment requirements |
| `?page=sitemap` | Navigable directory |

Unknown routes return HTTP 404. Unauthenticated dashboard access redirects to login. Non-admin users receive HTTP 403 for admin access.

## Search-engine sitemap

`sitemap.xml` contains 11 canonical public URLs. It excludes login, registration, dashboards, errors, and pending events/donation pages marked noindex. `robots.txt` declares its production URL. Update the route metadata in `seo.php` and run `php tools/generate-sitemap.php` to regenerate both files. Search Console setup is documented in `SEO.md`.
