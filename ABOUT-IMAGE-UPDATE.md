# About-page image update

Upload `scg-about-image-update.zip` to the existing `socialcontractgroup.org` document root and extract all files, replacing matches. Back up index.php, data.php, seo.php, sitemap.xml and assets outside the web root first. Clear hosting/CDN caches and refresh.

The About-page banner uses a supplied-image-based illustration of Tinubu among people with Nigerian flags. It retains landscape proportions with natural image height rather than stretching faces or forcing the old shallow crop. It is artwork, not authenticated documentary evidence of a specific gathering. No duplicate placement is added.

The image-credits page and its navigation/metadata/sitemap entries are removed; /image-credits returns 404. Sitemap now lists 11 public URLs. The patch excludes private configuration, database schema, bootstrap.php and .htaccess; existing settings and form processing remain intact.
