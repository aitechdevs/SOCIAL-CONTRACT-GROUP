# Sitemap

Public routes use clean paths with Apache/LiteSpeed URL rewriting. Old `index.php?page=...` links permanently redirect to their clean equivalent.

| Route | Purpose |
|---|---|
| `/` | Homepage, four slides, policy cards, project overview and participation links |
| `/about` | Identity, purpose, editorial principles |
| `/achievements` | PBAT Major Projects, Achievements & National Impact; six categories, source/status disclosure |
| `/projects` | Filterable project and policy reference library |
| `/campaign` | Neutral 2027 civic information and INEC reference |
| `/chapters` | Searchable 36-state and FCT directory; contacts pending |
| `/news` | Policy resource desk and editorial standard |
| `/events` | Honest empty state pending confirmed events |
| `/volunteer` | Civic volunteer enquiry form |
| `/donate` | Funding transparency; payment collection disabled |
| `/contact` | Stored enquiry form |
| `/register` | Member account creation |
| `/login` | Authentication |
| `/dashboard` | Authenticated member navigation and logout |
| `/admin` | Admin-only member count and recent submissions |
| `/privacy` | Data-use notice and deployment requirements |
| `/sitemap` | Navigable directory |
| `/image-credits` | Image provenance and attribution |

Unknown routes return HTTP 404. Unauthenticated dashboard access redirects to login. Non-admin users receive HTTP 403 for admin access.

## Search-engine sitemap

`sitemap.xml` contains 12 canonical public URLs. It excludes login, registration, dashboards, errors, and pending events/donation pages marked noindex. `robots.txt` declares its production URL. Update the route metadata in `seo.php` and run `php tools/generate-sitemap.php` to regenerate both files. Search Console setup is documented in `SEO.md`.
