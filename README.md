# Zenva Private Onsen & Spa — Website

Trilingual (EN / TH / ZH) static marketing site for Zenva Private Onsen & Spa (Thonglor, Bangkok).

- **Live (production preview):** https://ornate-profiterole-d93eb6.netlify.app
- **This repo:** source-of-truth backup + version history for the site, and (optionally) a GitHub Pages mirror.

## Structure

- `/` — built static site (34 HTML pages: English root, `/th/`, `/zh/`), plus `assets/` (images, video, fonts), `robots.txt`, `sitemap.xml`.
- `/scripts/build_zenva_v4.py` — the Python generator script that produces every page in this repo. Edit this script, re-run it, and re-commit the output to update the site.

## Notes

- Primary hosting is Netlify. This repo exists as an independent backup and change-history record, and can optionally serve the same site via GitHub Pages.
- Do not point the production domain (zenvaspabkk.com) at this or any host until PDPA legal sign-off is complete (see project master brief).
