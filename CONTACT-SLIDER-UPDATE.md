# Office contacts and slider captions update

Upload `releases/scg-contact-slider-update.zip` into the existing domain root `socialcontractgroup.org` and extract, replacing matching files. Back up `index.php`, `bootstrap.php` and `assets` outside the public web root first. Extract the complete assets folder. Clear hosting/CDN caches and refresh the browser. This ZIP excludes config, database schema, .htaccess and unrelated source files; keep the existing database and configuration. Files are 0644 and directories 0755.

Office contacts are shown on /contact and in the footer:
- socialcontractgroup@gmail.com
- info@socialcontractgroup.org
- 08030920092

A floating WhatsApp button opens `https://wa.me/2348030920092` with a prefilled enquiry. This is WhatsApp click-to-chat; the visitor chooses whether to send. It does not send messages automatically or require an API token. WhatsApp Business Cloud API messaging would require a separately configured Meta account and credentials.

The contact form still saves each enquiry in the existing submissions table and now hands a plain-text notification to the hosting server for each office email. The fixed sender is `info@socialcontractgroup.org`; Reply-To is the validated visitor address. Replies therefore go to the visitor. Volunteer and member flows remain unchanged. If mail handoff fails, the saved enquiry remains available to administrators and the visitor receives an honest fallback message with office contacts. No schema import or password is required for PHP mail().

The host must allow PHP mail and outbound delivery. Ensure the info mailbox exists, then submit one real enquiry after deployment and check both inboxes and spam folders. cPanel Email Deliverability (SPF/DKIM) and Track Delivery help diagnose missing messages. Local testing captured messages to both recipients without sending external mail; it does not establish delivery from the live hosting server.

A dark green gradient overlay and four topic captions accompany the existing slideshow pictures. Captions cover community, education, energy and infrastructure without identifying illustrations as documentary photographs. Font, routing, imagery and the rest of the site are retained. Captions update with slides and respect reduced-motion preferences.
