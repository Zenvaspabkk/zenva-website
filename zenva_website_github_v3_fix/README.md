# Zenva Private Onsen & Spa — Website

Trilingual (EN / TH / ZH) static marketing site for Zenva Private Onsen & Spa (Thonglor, Bangkok).

- **Live (production preview):** https://ornate-profiterole-d93eb6.netlify.app
- **GitHub Pages mirror (backup):** https://zenvaspabkk.github.io/zenva-website/
- **This repo:** source-of-truth backup + version history for the site.

## Structure

- `/` — built static site (34 HTML pages: English root, `/th/`, `/zh/`), plus `assets/` (images, video, fonts), `robots.txt`, `sitemap.xml`.
- `/scripts/build_zenva_v4.py` — the Python generator script that produces every page in this repo. Edit this script, re-run it, and re-commit the output to update the site.

## Important: two slightly different builds live here vs. Netlify

Netlify serves this site from a domain root, so the build script's asset links (`/assets/...`) resolve correctly there unchanged.

GitHub Pages serves this repo from a sub-path (`/zenva-website/`), so in this repo's copy only, every root-relative `/assets/...` reference (in `href=`, `src=`, `content=`, and inline CSS `url(...)`) has been rewritten to `/zenva-website/assets/...` so images, video, and fonts resolve correctly on the GitHub Pages mirror. Absolute URLs pointing at `https://zenvaspabkk.com/...` (canonical tags, sitemap, hreflang) were left untouched.

**If you regenerate this repo's content from `scripts/build_zenva_v4.py`, re-apply that path rewrite before committing** — otherwise every image/video/font on the GitHub Pages mirror will 404 (Netlify is unaffected either way, since it uses the unmodified output).

## Notes

- Primary hosting is Netlify. This repo exists as an independent backup and change-history record, and also serves the same site via GitHub Pages as a secondary mirror.
- Do not point the production domain (zenvaspabkk.com) at either host until PDPA legal sign-off is complete (see project master brief).
