# Homepage refresh — 23 October 2026

Use `releases/scg-homepage-animation-update.zip` for the existing installation. Back up the current `index.php` and `assets` outside the web root, upload the ZIP to the domain document root `socialcontractgroup.org`, and extract it there. Accept replacement of matching files and extract the entire assets folder. Do not move the domain into another site's public_html. This update does not contain database configuration, schema, or .htaccess. Do not reimport the database. Purge hosting/CDN cache and hard refresh the browser after extraction. Files must be 0644 and directories 0755.

The homepage uses two image buffers, waits for image decoding before crossfading, gently zooms the active slide, and fills the viewport below the navigation. It supports pause, touch, keyboard controls, and reduced motion. Dedicated homepage styles and content-hashed stylesheet/script URLs reduce stale asset conflicts. Old dynamic caption strings have been removed from the script.

The owner supplied Roboto Condensed 700 at 16px/20px with #81d742 for menus, and Fjalla One at 30px/32px with #016701 for headings. These are bundled locally under their included SIL Open Font Licenses, with system fallbacks. Fjalla One is supplied in its available regular weight to avoid synthetic bold. Body copy retains Inter for readability. Direct inspection of power.gov.ng was blocked by the execution environment; the fade/zoom animation is our implementation rather than a verified copy.

Four homepage illustrations were revised for more natural daylight, textures, and ordinary surroundings. They remain generated illustrations, not documentary photographs of people, government projects, or SCG events. Native image dimensions are approximately 1672 × 941; WebP quality 92 preserves detail without pretending to add photographic information. The image credits page retains provenance. No descriptive text is overlaid on the slides.

The full `social-contract-group-cpanel.zip` remains available for a new installation or complete source backup. Existing installations should use the smaller update to preserve local settings.
