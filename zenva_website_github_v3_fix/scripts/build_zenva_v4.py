import os, shutil

# ---------- SEO P0-1: externalized, real, cacheable static assets ----------
# Previously every photo/video/font was base64-encoded and embedded directly inside
# the HTML (see SEO audit, P0 #1). That produced ~19MB HTML documents with no
# independently cacheable or crawlable image/video/font files, hurt Core Web
# Vitals (LCP/INP), and removed Google Images as a discovery channel entirely.
# Fix: copy the real source files into /assets/{img,video,fonts}/ inside the
# build output and reference them by real, root-relative URL everywhere.
SITE_DIR = "/tmp/zenva_site"
IMG_ASSET_DIR = os.path.join(SITE_DIR, "assets", "img")
VIDEO_ASSET_DIR = os.path.join(SITE_DIR, "assets", "video")
FONT_ASSET_DIR = os.path.join(SITE_DIR, "assets", "fonts")
os.makedirs(IMG_ASSET_DIR, exist_ok=True)
os.makedirs(VIDEO_ASSET_DIR, exist_ok=True)
os.makedirs(FONT_ASSET_DIR, exist_ok=True)

photo_dir = "/tmp/zenva_review/selected"
def img_asset(name):
    shutil.copyfile(os.path.join(photo_dir, name), os.path.join(IMG_ASSET_DIR, name))
    return f"/assets/img/{name}"

IMG = {k: img_asset(v) for k, v in {
    "hero": "hero.jpg", "onsen": "onsen_room1_bonsai.jpg", "massage": "massage.jpg",
    "signature": "signature.jpg", "reception": "storefront_new.jpg", "water": "water.jpg",
    "g1": "gallery1_steamroom.jpg", "g2": "gallery2.jpg", "g3": "gallery3.jpg",
    "g4": "gallery4.jpg", "g5": "gallery5.jpg", "g6": "gallery6.jpg",
    "g7": "gallery7.jpg", "g8": "gallery8.jpg", "g9": "gallery9.jpg", "g10": "gallery10.jpg",
    "g11": "gallery11.jpg",
    "room_bonsai": "onsen_room1_bonsai.jpg", "room_sakura": "onsen_room2_sakura.jpg",
    "massage_card": "massage_card.jpg", "signature_card": "signature_card.jpg",
    "menu_card_onsen": "menu_card_onsen.jpg", "chair_card": "chair_card.jpg",
    "vietnamese_card": "vietnamese_card.jpg",
    # Real hero-carousel photography (client-supplied, added 2026-08-31), replacing
    # the gradient/SVG placeholder art on homepage hero slides 2-6 (English only).
    "hero_couple": "hero_couple_together.jpg", "hero_ritual": "hero_ritual_sauna.jpg",
    "hero_membership": "hero_membership_gold.jpg", "hero_firsttime": "hero_first_time.jpg",
    "hero_hotcold": "hero_hotcold.jpg",
}.items()}

video_dir = "/tmp/zenva_video"
def video_asset(name):
    shutil.copyfile(os.path.join(video_dir, name), os.path.join(VIDEO_ASSET_DIR, name))
    return f"/assets/video/{name}"

VID = {k: video_asset(v) for k, v in {
    "reel1_webm": "clip1.webm", "reel1_mp4": "clip1.mp4",
    "reel3_webm": "clip3.webm", "reel3_mp4": "clip3.mp4",
    "reel5_webm": "clip5.webm", "reel5_mp4": "clip5.mp4",
    "reel6_webm": "clip6.webm", "reel6_mp4": "clip6.mp4",
    "reel7_webm": "clip7.webm", "reel7_mp4": "clip7.mp4",
    "reel8_webm": "clip8.webm", "reel8_mp4": "clip8.mp4",
}.items()}

font_dir = "/tmp/zenva_fonts"
def font_asset(name):
    shutil.copyfile(os.path.join(font_dir, name), os.path.join(FONT_ASSET_DIR, name))
    return f"/assets/fonts/{name}"

FONTS = {k: font_asset(v) for k, v in {
    "cg400": "cg-400.woff2", "cg500": "cg-500.woff2", "cg600": "cg-600.woff2", "cg700": "cg-700.woff2",
    "jost300": "jost-300.woff2", "jost400": "jost-400.woff2", "jost500": "jost-500.woff2",
    "jost600": "jost-600.woff2", "jost700": "jost-700.woff2",
}.items()}

# Self-hosted, real, externally-cacheable @font-face files — no external Google Fonts
# request, no render-blocking third-party connection, no FOUC, and one less external
# data call for PDPA purposes. (Previously base64-inlined; see SEO audit P0 #1.)
FONT_FACE_CSS = f"""
<style>
@font-face{{font-family:'Cormorant Garamond'; font-style:normal; font-weight:400; font-display:swap; src:url('{FONTS['cg400']}') format('woff2');}}
@font-face{{font-family:'Cormorant Garamond'; font-style:normal; font-weight:500; font-display:swap; src:url('{FONTS['cg500']}') format('woff2');}}
@font-face{{font-family:'Cormorant Garamond'; font-style:normal; font-weight:600; font-display:swap; src:url('{FONTS['cg600']}') format('woff2');}}
@font-face{{font-family:'Cormorant Garamond'; font-style:normal; font-weight:700; font-display:swap; src:url('{FONTS['cg700']}') format('woff2');}}
@font-face{{font-family:'Jost'; font-style:normal; font-weight:300; font-display:swap; src:url('{FONTS['jost300']}') format('woff2');}}
@font-face{{font-family:'Jost'; font-style:normal; font-weight:400; font-display:swap; src:url('{FONTS['jost400']}') format('woff2');}}
@font-face{{font-family:'Jost'; font-style:normal; font-weight:500; font-display:swap; src:url('{FONTS['jost500']}') format('woff2');}}
@font-face{{font-family:'Jost'; font-style:normal; font-weight:600; font-display:swap; src:url('{FONTS['jost600']}') format('woff2');}}
@font-face{{font-family:'Jost'; font-style:normal; font-weight:700; font-display:swap; src:url('{FONTS['jost700']}') format('woff2');}}
</style>
"""

# Generic minimal chat-bubble icon, no brand marks, tinted via currentColor to match CI.
CHAT_ICON = """<svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M4 5.5C4 4.67 4.67 4 5.5 4h13c.83 0 1.5.67 1.5 1.5v9c0 .83-.67 1.5-1.5 1.5H9l-4 3.5v-3.5H5.5C4.67 16 4 15.33 4 14.5v-9z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
</svg>"""

ZOOM_ICON = """<svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="11" cy="11" r="7" stroke="#211C17" stroke-width="2"/><path d="M21 21l-4.3-4.3" stroke="#211C17" stroke-width="2" stroke-linecap="round"/>
</svg>"""

BOOK_LINKS = {
    "LINE": "https://lin.ee/Qcbmudy",
    "WhatsApp": "https://wa.me/66802629191?text=Hi%20Zenva%2C%20I%27d%20like%20to%20book%20a%20private%20onsen%20session.",
}

# Same real, already-live profile URLs already used in the footer's "Connect"
# column on every page (see footer()) — centralized here as the single source
# so the new header icon row below and the footer can't drift out of sync.
SOCIAL_LINKS = {
    "Instagram": "https://www.instagram.com/zenvaspabkk/",
    "Facebook": "https://www.facebook.com/zenvaspa/",
    "TikTok": "https://www.tiktok.com/@zenvaspabkk",
}

# Generic, hand-built (not copied from any icon library) monochrome glyphs,
# tinted via currentColor so they inherit .social-icon's color/hover state
# like every other icon on the site (see CHAT_ICON above for the same pattern).
SOCIAL_ICON_SVG = {
    "Instagram": """<svg width="17" height="17" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect x="3" y="3" width="18" height="18" rx="5.5" stroke="currentColor" stroke-width="1.7"/>
<circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/>
<circle cx="17.15" cy="6.85" r="1.05" fill="currentColor"/>
</svg>""",
    "Facebook": """<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<path d="M14.6 8.4H17V5.15c-.46-.06-1.62-.2-2.86-.2-2.83 0-4.77 1.77-4.77 5.02V13H6.7v3.6h2.67V23h3.63v-6.4h2.72l.5-3.6h-3.22v-2.4c0-1.04.28-1.75 1.6-1.75Z"/>
</svg>""",
    "TikTok": """<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<path d="M16.6 3c.38 2.28 1.83 3.75 4.1 3.95v3.02c-1.5-.02-2.9-.46-4.1-1.24v6.5c0 3.55-2.87 6.42-6.42 6.42S3.76 18.78 3.76 15.23s2.87-6.42 6.42-6.42c.4 0 .8.04 1.18.1v3.2a3.35 3.35 0 1 0 2.35 3.2V3h2.89Z"/>
</svg>""",
}

def social_icons_html():
    return "".join(
        f'<a class="social-icon" href="{SOCIAL_LINKS[name]}" target="_blank" rel="noopener" aria-label="Zenva on {name}">{svg}</a>'
        for name, svg in SOCIAL_ICON_SVG.items()
    )

def book_btn(channel, variant="solid"):
    cls = "btn-book-solid" if variant == "solid" else "btn-book-outline"
    href = BOOK_LINKS.get(channel, "#")
    return f'''<a class="btn-book {cls}" href="{href}" target="_blank" rel="noopener"><span class="bb-icon">{CHAT_ICON}</span><span class="bb-txt"><span class="bb-main">Book Now</span><span class="bb-sub">via {channel}</span></span></a>'''

def cta_buttons():
    return book_btn("LINE", "solid") + book_btn("WhatsApp", "outline")

# Chinese CTA variant — same buttons/links/brand rules (no literal LINE/WhatsApp
# brand colors), just localized copy: 立即预订 (Book Now) / LINE预约 & WhatsApp预约.
def book_btn_zh(channel, variant="solid"):
    cls = "btn-book-solid" if variant == "solid" else "btn-book-outline"
    href = BOOK_LINKS.get(channel, "#")
    sub = "LINE预约" if channel == "LINE" else "WhatsApp预约"
    return f'''<a class="btn-book {cls}" href="{href}" target="_blank" rel="noopener"><span class="bb-icon">{CHAT_ICON}</span><span class="bb-txt"><span class="bb-main">立即预订</span><span class="bb-sub">{sub}</span></span></a>'''

def cta_buttons_zh():
    return book_btn_zh("LINE", "solid") + book_btn_zh("WhatsApp", "outline")

# Thai CTA variant — same buttons/links/brand rules, localized copy:
# จองเลย (Book Now) / จองผ่าน LINE & จองผ่าน WhatsApp.
def book_btn_th(channel, variant="solid"):
    cls = "btn-book-solid" if variant == "solid" else "btn-book-outline"
    href = BOOK_LINKS.get(channel, "#")
    sub = "ผ่าน LINE" if channel == "LINE" else "ผ่าน WhatsApp"
    return f'''<a class="btn-book {cls}" href="{href}" target="_blank" rel="noopener"><span class="bb-icon">{CHAT_ICON}</span><span class="bb-txt"><span class="bb-main">จองเลย</span><span class="bb-sub">{sub}</span></span></a>'''

def cta_buttons_th():
    return book_btn_th("LINE", "solid") + book_btn_th("WhatsApp", "outline")

# Compact single-button "Book Now" used ONLY in header()'s desktop and mobile
# nav CTA slots (2026-08-30 client request: the header specifically felt
# crowded with 2 separate buttons — "save space and tidy up the header").
# Everywhere else on the site (in-page section CTAs, blog closing CTAs, the
# footer's sticky-mobile-cta bar) deliberately keeps showing both LINE and
# WhatsApp as separate, immediately-visible buttons — that scope boundary is
# intentional, not an oversight; those spots aren't the cramped header and
# showing both channels up front there is still the better call. Clicking
# this single trigger reveals both real channels in a small popover — same
# 2 real links, same brand-neutral CHAT_ICON as everywhere else, nothing new
# invented, just collapsed into one control. `uid` keeps element IDs unique
# since this renders twice per page (desktop header-right + mobile nav).
def book_picker(lang="en", uid=""):
    main_label = {"en": "Book Now", "zh": "立即预订", "th": "จองเลย"}[lang]
    line_label = {"en": "via LINE", "zh": "LINE预约", "th": "ผ่าน LINE"}[lang]
    wa_label = {"en": "via WhatsApp", "zh": "WhatsApp预约", "th": "ผ่าน WhatsApp"}[lang]
    menu_id = f"bookPickerMenu-{uid}"
    return f'''<div class="book-picker">
      <button type="button" class="btn-book btn-book-solid book-picker-trigger" aria-haspopup="true" aria-expanded="false" aria-controls="{menu_id}">
        <span class="bb-icon">{CHAT_ICON}</span>
        <span class="bb-txt"><span class="bb-main">{main_label}</span></span>
        <span class="book-caret" aria-hidden="true">&#9662;</span>
      </button>
      <div class="book-picker-menu" id="{menu_id}">
        <a href="{BOOK_LINKS['LINE']}" target="_blank" rel="noopener"><span class="bb-icon">{CHAT_ICON}</span>{line_label}</a>
        <a href="{BOOK_LINKS['WhatsApp']}" target="_blank" rel="noopener"><span class="bb-icon">{CHAT_ICON}</span>{wa_label}</a>
      </div>
    </div>'''

# ---------- PDPA-ALIGNED COOKIE / CONSENT BANNER ----------
# GA4 property and Meta Pixel created 2026-08-28 (logged into admin@zenvaspabkk.com
# and the Zenva Private Onsen and Spa Meta Business Suite, both already
# authenticated in the connected browser session — real IDs below, not invented).
# LINE Tag is still a placeholder: LINE Tag lives in LINE Ads Manager
# (ads.line.me), a separate product from LINE Official Account Manager
# (manager.line.biz) where the Zenva account itself was found — ads.line.me is
# blocked by this session's browser-tool safety allowlist, so it could not be
# reached. Needs a manual visit to ads.line.me (logged in as the Zenva LINE
# Official Account, @zenvaspa) to create the tag and fill this in.
ANALYTICS_IDS = {
    "ga4_id": "G-0RNSHPLBX5",
    "meta_pixel_id": "1046174144821584",
    "line_tag_id": "REPLACE_ME_LINE_TAG_ID",
}

COOKIE_CSS = """
  .ck-banner{{position:fixed; left:0; right:0; bottom:0; z-index:200; background:var(--ink); color:var(--cream); padding:18px 24px; box-shadow:0 -6px 24px rgba(0,0,0,.25); display:none; }}
  .ck-banner.show{{display:block;}}
  .ck-wrap{{max-width:1100px; margin:0 auto; display:flex; align-items:center; gap:24px; flex-wrap:wrap;}}
  .ck-text{{flex:1; min-width:240px; font-size:13px; line-height:1.6; color:#E9E1CC;}}
  .ck-text a{{color:var(--gold-text); text-decoration:underline;}}
  .ck-actions{{display:flex; gap:10px; flex-wrap:wrap;}}
  .ck-btn{{font-family:inherit; font-size:12.5px; font-weight:700; border-radius:5px; padding:10px 16px; cursor:pointer; border:1px solid var(--gold); background:transparent; color:var(--cream);}}
  .ck-btn.primary{{background:var(--gold); color:var(--ink); border-color:var(--gold);}}
  .ck-btn:hover{{opacity:.88;}}
  .ck-modal-overlay{{position:fixed; inset:0; background:rgba(33,28,23,.55); z-index:210; display:none; align-items:center; justify-content:center; padding:20px;}}
  .ck-modal-overlay.show{{display:flex;}}
  .ck-modal{{background:#fff; color:var(--ink); border-radius:8px; max-width:520px; width:100%; max-height:86vh; overflow-y:auto; padding:28px;}}
  .ck-modal h3{{font-size:19px; margin-bottom:6px;}}
  .ck-modal p.intro{{font-size:13px; color:var(--ink-soft); margin-bottom:20px; line-height:1.6;}}
  .ck-cat{{border-top:1px solid var(--line); padding:14px 0;}}
  .ck-cat-head{{display:flex; justify-content:space-between; align-items:center; gap:12px;}}
  .ck-cat-head strong{{font-size:14px;}}
  .ck-cat p{{font-size:12.5px; color:var(--ink-soft); margin-top:6px; line-height:1.55;}}
  .ck-switch{{position:relative; width:40px; height:22px; flex:none;}}
  .ck-switch input{{opacity:0; width:0; height:0;}}
  .ck-slider{{position:absolute; inset:0; background:#D9CFB3; border-radius:22px; cursor:pointer; transition:.2s;}}
  .ck-slider:before{{content:""; position:absolute; width:16px; height:16px; left:3px; top:3px; background:#fff; border-radius:50%; transition:.2s;}}
  .ck-switch input:checked + .ck-slider{{background:var(--gold);}}
  .ck-switch input:checked + .ck-slider:before{{transform:translateX(18px);}}
  .ck-switch input:disabled + .ck-slider{{opacity:.6; cursor:not-allowed;}}
  .ck-modal-actions{{display:flex; gap:10px; margin-top:22px; flex-wrap:wrap;}}
  .ck-modal-actions .ck-btn{{border-color:var(--gold); color:var(--ink);}}
  .ck-modal-actions .ck-btn.primary{{background:var(--gold); color:var(--ink);}}
  @media (max-width:640px){{.ck-wrap{{flex-direction:column; align-items:stretch;}} .ck-actions{{justify-content:stretch;}} .ck-actions .ck-btn{{flex:1;}}}}
""".format()

COOKIE_BANNER_HTML = f"""
<div class="ck-banner" id="ckBanner" role="dialog" aria-live="polite" aria-label="Cookie consent">
  <div class="ck-wrap">
    <div class="ck-text">We use a few cookies to help this site run smoothly, see how it's being used, and &mdash; only with your permission &mdash; to share offers you might like. See our <a href="privacy-policy.html">Privacy &amp; Cookie Policy</a> for details, or change your preferences anytime via "Cookie Settings" in the footer.</div>
    <div class="ck-actions">
      <button class="ck-btn" id="ckRejectBtn" type="button">Reject Non-Essential</button>
      <button class="ck-btn" id="ckCustomizeBtn" type="button">Customize</button>
      <button class="ck-btn primary" id="ckAcceptBtn" type="button">Accept All</button>
    </div>
  </div>
</div>

<div class="ck-modal-overlay" id="ckModalOverlay">
  <div class="ck-modal" role="dialog" aria-modal="true" aria-labelledby="ckModalTitle">
    <h3 id="ckModalTitle">Cookie Preferences</h3>
    <p class="intro">Choose which categories of cookies we may use. Necessary cookies keep the site working and can't be turned off. You can change these settings at any time from the "Cookie Settings" link in the site footer.</p>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>Necessary</strong>
        <label class="ck-switch"><input type="checkbox" checked disabled><span class="ck-slider"></span></label>
      </div>
      <p>Required for core site functionality (navigation, security, remembering your cookie choice). Always active.</p>
    </div>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>Analytics</strong>
        <label class="ck-switch"><input type="checkbox" id="ckAnalyticsToggle"><span class="ck-slider"></span></label>
      </div>
      <p>Helps us understand how visitors use the site (e.g. Google Analytics) so we can improve it. No data is sold.</p>
    </div>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>Marketing</strong>
        <label class="ck-switch"><input type="checkbox" id="ckMarketingToggle"><span class="ck-slider"></span></label>
      </div>
      <p>Used to measure and personalize ads (e.g. Meta Pixel, LINE Tag). Only loads with your consent.</p>
    </div>

    <div class="ck-modal-actions">
      <button class="ck-btn" id="ckModalRejectBtn" type="button">Reject Non-Essential</button>
      <button class="ck-btn primary" id="ckModalSaveBtn" type="button">Save Preferences</button>
    </div>
  </div>
</div>

<script>
(function(){{
  var COOKIE_NAME = "zenva_consent";
  var COOKIE_DAYS = 180; // re-ask roughly every 6 months, per PDPA good-practice guidance
  var GA4_ID = "{ANALYTICS_IDS['ga4_id']}";
  var META_PIXEL_ID = "{ANALYTICS_IDS['meta_pixel_id']}";
  var LINE_TAG_ID = "{ANALYTICS_IDS['line_tag_id']}";

  function getCookie(name){{
    var m = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }}
  function setCookie(name, value, days){{
    var d = new Date();
    d.setTime(d.getTime() + days*24*60*60*1000);
    document.cookie = name + "=" + encodeURIComponent(value) + ";expires=" + d.toUTCString() + ";path=/;SameSite=Lax";
  }}
  function readConsent(){{
    var raw = getCookie(COOKIE_NAME);
    if(!raw) return null;
    try {{ return JSON.parse(raw); }} catch(e) {{ return null; }}
  }}
  function saveConsent(consent){{
    consent.necessary = true;
    consent.timestamp = new Date().toISOString();
    consent.version = "1.0";
    setCookie(COOKIE_NAME, JSON.stringify(consent), COOKIE_DAYS);
    applyConsent(consent);
    hideBanner();
    hideModal();
  }}

  function loadGA4(){{
    if(!GA4_ID || GA4_ID.indexOf("REPLACE_ME") === 0) return;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA4_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){{ dataLayer.push(arguments); }}
    gtag('js', new Date());
    gtag('config', GA4_ID, {{ anonymize_ip: true }});
    window.gtag = gtag;
  }}
  function loadMetaPixel(){{
    if(!META_PIXEL_ID || META_PIXEL_ID.indexOf("REPLACE_ME") === 0) return;
    !function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', META_PIXEL_ID);
    fbq('track', 'PageView');
  }}
  function loadLineTag(){{
    if(!LINE_TAG_ID || LINE_TAG_ID.indexOf("REPLACE_ME") === 0) return;
    // Placeholder loader — replace with the real snippet LINE Tag Manager provides
    // once the LINE Tag is created (see analytics setup guide).
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://tr.line.me/tag.js?id=" + LINE_TAG_ID;
    document.head.appendChild(s);
  }}

  function applyConsent(consent){{
    if(consent.analytics) loadGA4();
    if(consent.marketing){{ loadMetaPixel(); loadLineTag(); }}
  }}

  function showBanner(){{ document.getElementById("ckBanner").classList.add("show"); }}
  function hideBanner(){{ document.getElementById("ckBanner").classList.remove("show"); }}
  function showModal(){{
    var existing = readConsent() || {{}};
    document.getElementById("ckAnalyticsToggle").checked = !!existing.analytics;
    document.getElementById("ckMarketingToggle").checked = !!existing.marketing;
    document.getElementById("ckModalOverlay").classList.add("show");
  }}
  function hideModal(){{ document.getElementById("ckModalOverlay").classList.remove("show"); }}

  document.addEventListener("DOMContentLoaded", function(){{
    var consent = readConsent();
    if(consent){{
      applyConsent(consent);
    }} else {{
      showBanner();
    }}

    document.getElementById("ckAcceptBtn").addEventListener("click", function(){{
      saveConsent({{analytics:true, marketing:true}});
    }});
    document.getElementById("ckRejectBtn").addEventListener("click", function(){{
      saveConsent({{analytics:false, marketing:false}});
    }});
    document.getElementById("ckCustomizeBtn").addEventListener("click", showModal);
    document.getElementById("ckModalRejectBtn").addEventListener("click", function(){{
      saveConsent({{analytics:false, marketing:false}});
    }});
    document.getElementById("ckModalSaveBtn").addEventListener("click", function(){{
      saveConsent({{
        analytics: document.getElementById("ckAnalyticsToggle").checked,
        marketing: document.getElementById("ckMarketingToggle").checked
      }});
    }});

    // Reopen from the footer "Cookie Settings" link, on any page.
    var reopenLink = document.getElementById("ckReopenLink");
    if(reopenLink){{
      reopenLink.addEventListener("click", function(e){{
        e.preventDefault();
        showModal();
      }});
    }}
  }});
}})();
</script>
"""

# Chinese cookie banner — identical structure/IDs/JS to COOKIE_BANNER_HTML above
# (the consent script binds to these same element IDs regardless of language),
# only the visible copy is translated, using the approved wording from the
# zh translation review doc.
COOKIE_BANNER_HTML_ZH = f"""
<div class="ck-banner" id="ckBanner" role="dialog" aria-live="polite" aria-label="Cookie 同意">
  <div class="ck-wrap">
    <div class="ck-text">我们使用一些Cookie，让网站运行更顺畅、了解您的浏览体验，并在您同意后为您推荐感兴趣的优惠。详情请参阅我们的《<a href="../privacy-policy.html">隐私与Cookie政策</a>》，您也可以随时通过页脚的"Cookie设置"调整您的偏好。</div>
    <div class="ck-actions">
      <button class="ck-btn" id="ckRejectBtn" type="button">仅接受必要项</button>
      <button class="ck-btn" id="ckCustomizeBtn" type="button">自定义设置</button>
      <button class="ck-btn primary" id="ckAcceptBtn" type="button">接受全部</button>
    </div>
  </div>
</div>

<div class="ck-modal-overlay" id="ckModalOverlay">
  <div class="ck-modal" role="dialog" aria-modal="true" aria-labelledby="ckModalTitle">
    <h3 id="ckModalTitle">Cookie偏好设置</h3>
    <p class="intro">请选择您允许我们使用的Cookie类别。必要性Cookie用于维持网站正常运行，无法关闭。您可以随时通过网站页脚的"Cookie设置"链接更改这些设置。</p>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>必要性</strong>
        <label class="ck-switch"><input type="checkbox" checked disabled><span class="ck-slider"></span></label>
      </div>
      <p>用于维持网站核心功能（导航、安全性、记住您的Cookie选择），始终启用。</p>
    </div>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>分析性</strong>
        <label class="ck-switch"><input type="checkbox" id="ckAnalyticsToggle"><span class="ck-slider"></span></label>
      </div>
      <p>帮助我们了解访客如何使用本网站（例如通过Google Analytics），以便持续改进。我们不会出售任何数据。</p>
    </div>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>营销性</strong>
        <label class="ck-switch"><input type="checkbox" id="ckMarketingToggle"><span class="ck-slider"></span></label>
      </div>
      <p>用于衡量广告效果并提供个性化内容（例如Meta Pixel、LINE Tag）。仅在您同意后才会启用。</p>
    </div>

    <div class="ck-modal-actions">
      <button class="ck-btn" id="ckModalRejectBtn" type="button">仅接受必要项</button>
      <button class="ck-btn primary" id="ckModalSaveBtn" type="button">保存设置</button>
    </div>
  </div>
</div>

<script>
(function(){{
  var COOKIE_NAME = "zenva_consent";
  var COOKIE_DAYS = 180; // re-ask roughly every 6 months, per PDPA good-practice guidance
  var GA4_ID = "{ANALYTICS_IDS['ga4_id']}";
  var META_PIXEL_ID = "{ANALYTICS_IDS['meta_pixel_id']}";
  var LINE_TAG_ID = "{ANALYTICS_IDS['line_tag_id']}";

  function getCookie(name){{
    var m = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }}
  function setCookie(name, value, days){{
    var d = new Date();
    d.setTime(d.getTime() + days*24*60*60*1000);
    document.cookie = name + "=" + encodeURIComponent(value) + ";expires=" + d.toUTCString() + ";path=/;SameSite=Lax";
  }}
  function readConsent(){{
    var raw = getCookie(COOKIE_NAME);
    if(!raw) return null;
    try {{ return JSON.parse(raw); }} catch(e) {{ return null; }}
  }}
  function saveConsent(consent){{
    consent.necessary = true;
    consent.timestamp = new Date().toISOString();
    consent.version = "1.0";
    setCookie(COOKIE_NAME, JSON.stringify(consent), COOKIE_DAYS);
    applyConsent(consent);
    hideBanner();
    hideModal();
  }}

  function loadGA4(){{
    if(!GA4_ID || GA4_ID.indexOf("REPLACE_ME") === 0) return;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA4_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){{ dataLayer.push(arguments); }}
    gtag('js', new Date());
    gtag('config', GA4_ID, {{ anonymize_ip: true }});
    window.gtag = gtag;
  }}
  function loadMetaPixel(){{
    if(!META_PIXEL_ID || META_PIXEL_ID.indexOf("REPLACE_ME") === 0) return;
    !function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', META_PIXEL_ID);
    fbq('track', 'PageView');
  }}
  function loadLineTag(){{
    if(!LINE_TAG_ID || LINE_TAG_ID.indexOf("REPLACE_ME") === 0) return;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://tr.line.me/tag.js?id=" + LINE_TAG_ID;
    document.head.appendChild(s);
  }}

  function applyConsent(consent){{
    if(consent.analytics) loadGA4();
    if(consent.marketing){{ loadMetaPixel(); loadLineTag(); }}
  }}

  function showBanner(){{ document.getElementById("ckBanner").classList.add("show"); }}
  function hideBanner(){{ document.getElementById("ckBanner").classList.remove("show"); }}
  function showModal(){{
    var existing = readConsent() || {{}};
    document.getElementById("ckAnalyticsToggle").checked = !!existing.analytics;
    document.getElementById("ckMarketingToggle").checked = !!existing.marketing;
    document.getElementById("ckModalOverlay").classList.add("show");
  }}
  function hideModal(){{ document.getElementById("ckModalOverlay").classList.remove("show"); }}

  document.addEventListener("DOMContentLoaded", function(){{
    var consent = readConsent();
    if(consent){{
      applyConsent(consent);
    }} else {{
      showBanner();
    }}

    document.getElementById("ckAcceptBtn").addEventListener("click", function(){{
      saveConsent({{analytics:true, marketing:true}});
    }});
    document.getElementById("ckRejectBtn").addEventListener("click", function(){{
      saveConsent({{analytics:false, marketing:false}});
    }});
    document.getElementById("ckCustomizeBtn").addEventListener("click", showModal);
    document.getElementById("ckModalRejectBtn").addEventListener("click", function(){{
      saveConsent({{analytics:false, marketing:false}});
    }});
    document.getElementById("ckModalSaveBtn").addEventListener("click", function(){{
      saveConsent({{
        analytics: document.getElementById("ckAnalyticsToggle").checked,
        marketing: document.getElementById("ckMarketingToggle").checked
      }});
    }});

    var reopenLink = document.getElementById("ckReopenLink");
    if(reopenLink){{
      reopenLink.addEventListener("click", function(e){{
        e.preventDefault();
        showModal();
      }});
    }}
  }});
}})();
</script>
"""

# Thai cookie banner — same structure/IDs/JS as the English and Chinese
# versions above (the consent script binds to these same element IDs
# regardless of language), only the visible copy is translated.
COOKIE_BANNER_HTML_TH = f"""
<div class="ck-banner" id="ckBanner" role="dialog" aria-live="polite" aria-label="ยินยอมการใช้คุกกี้">
  <div class="ck-wrap">
    <div class="ck-text">เราใช้คุกกี้เล็กน้อยเพื่อให้เว็บไซต์นี้ทำงานได้อย่างราบรื่น เข้าใจการใช้งานของท่าน และ &mdash; เมื่อได้รับอนุญาตจากท่านเท่านั้น &mdash; เพื่อนำเสนอสิทธิพิเศษที่ท่านอาจสนใจ ดูรายละเอียดเพิ่มเติมได้ที่<a href="../privacy-policy.html">นโยบายความเป็นส่วนตัวและคุกกี้</a>ของเรา หรือปรับเปลี่ยนการตั้งค่าได้ตลอดเวลาผ่าน "ตั้งค่าคุกกี้" ที่ส่วนท้ายของเว็บไซต์</div>
    <div class="ck-actions">
      <button class="ck-btn" id="ckRejectBtn" type="button">ปฏิเสธที่ไม่จำเป็น</button>
      <button class="ck-btn" id="ckCustomizeBtn" type="button">ตั้งค่า</button>
      <button class="ck-btn primary" id="ckAcceptBtn" type="button">ยอมรับทั้งหมด</button>
    </div>
  </div>
</div>

<div class="ck-modal-overlay" id="ckModalOverlay">
  <div class="ck-modal" role="dialog" aria-modal="true" aria-labelledby="ckModalTitle">
    <h3 id="ckModalTitle">การตั้งค่าคุกกี้</h3>
    <p class="intro">โปรดเลือกประเภทคุกกี้ที่ท่านอนุญาตให้เราใช้งาน คุกกี้ที่จำเป็นมีไว้เพื่อให้เว็บไซต์ทำงานได้ตามปกติและไม่สามารถปิดได้ ท่านสามารถเปลี่ยนการตั้งค่านี้ได้ตลอดเวลาผ่านลิงก์ "ตั้งค่าคุกกี้" ที่ส่วนท้ายของเว็บไซต์</p>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>จำเป็น</strong>
        <label class="ck-switch"><input type="checkbox" checked disabled><span class="ck-slider"></span></label>
      </div>
      <p>จำเป็นสำหรับการทำงานหลักของเว็บไซต์ (การนำทาง ความปลอดภัย การจดจำการตั้งค่าคุกกี้ของท่าน) เปิดใช้งานเสมอ</p>
    </div>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>การวิเคราะห์</strong>
        <label class="ck-switch"><input type="checkbox" id="ckAnalyticsToggle"><span class="ck-slider"></span></label>
      </div>
      <p>ช่วยให้เราเข้าใจว่าผู้เข้าชมใช้งานเว็บไซต์นี้อย่างไร (เช่น ผ่าน Google Analytics) เพื่อนำไปปรับปรุงเว็บไซต์ เราจะไม่ขายข้อมูลใด ๆ</p>
    </div>

    <div class="ck-cat">
      <div class="ck-cat-head">
        <strong>การตลาด</strong>
        <label class="ck-switch"><input type="checkbox" id="ckMarketingToggle"><span class="ck-slider"></span></label>
      </div>
      <p>ใช้เพื่อวัดผลโฆษณาและนำเสนอเนื้อหาที่ตรงกับความสนใจของท่าน (เช่น Meta Pixel, LINE Tag) จะเริ่มทำงานก็ต่อเมื่อท่านยินยอมเท่านั้น</p>
    </div>

    <div class="ck-modal-actions">
      <button class="ck-btn" id="ckModalRejectBtn" type="button">ปฏิเสธที่ไม่จำเป็น</button>
      <button class="ck-btn primary" id="ckModalSaveBtn" type="button">บันทึกการตั้งค่า</button>
    </div>
  </div>
</div>

<script>
(function(){{
  var COOKIE_NAME = "zenva_consent";
  var COOKIE_DAYS = 180; // re-ask roughly every 6 months, per PDPA good-practice guidance
  var GA4_ID = "{ANALYTICS_IDS['ga4_id']}";
  var META_PIXEL_ID = "{ANALYTICS_IDS['meta_pixel_id']}";
  var LINE_TAG_ID = "{ANALYTICS_IDS['line_tag_id']}";

  function getCookie(name){{
    var m = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }}
  function setCookie(name, value, days){{
    var d = new Date();
    d.setTime(d.getTime() + days*24*60*60*1000);
    document.cookie = name + "=" + encodeURIComponent(value) + ";expires=" + d.toUTCString() + ";path=/;SameSite=Lax";
  }}
  function readConsent(){{
    var raw = getCookie(COOKIE_NAME);
    if(!raw) return null;
    try {{ return JSON.parse(raw); }} catch(e) {{ return null; }}
  }}
  function saveConsent(consent){{
    consent.necessary = true;
    consent.timestamp = new Date().toISOString();
    consent.version = "1.0";
    setCookie(COOKIE_NAME, JSON.stringify(consent), COOKIE_DAYS);
    applyConsent(consent);
    hideBanner();
    hideModal();
  }}

  function loadGA4(){{
    if(!GA4_ID || GA4_ID.indexOf("REPLACE_ME") === 0) return;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA4_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){{ dataLayer.push(arguments); }}
    gtag('js', new Date());
    gtag('config', GA4_ID, {{ anonymize_ip: true }});
    window.gtag = gtag;
  }}
  function loadMetaPixel(){{
    if(!META_PIXEL_ID || META_PIXEL_ID.indexOf("REPLACE_ME") === 0) return;
    !function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', META_PIXEL_ID);
    fbq('track', 'PageView');
  }}
  function loadLineTag(){{
    if(!LINE_TAG_ID || LINE_TAG_ID.indexOf("REPLACE_ME") === 0) return;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://tr.line.me/tag.js?id=" + LINE_TAG_ID;
    document.head.appendChild(s);
  }}

  function applyConsent(consent){{
    if(consent.analytics) loadGA4();
    if(consent.marketing){{ loadMetaPixel(); loadLineTag(); }}
  }}

  function showBanner(){{ document.getElementById("ckBanner").classList.add("show"); }}
  function hideBanner(){{ document.getElementById("ckBanner").classList.remove("show"); }}
  function showModal(){{
    var existing = readConsent() || {{}};
    document.getElementById("ckAnalyticsToggle").checked = !!existing.analytics;
    document.getElementById("ckMarketingToggle").checked = !!existing.marketing;
    document.getElementById("ckModalOverlay").classList.add("show");
  }}
  function hideModal(){{ document.getElementById("ckModalOverlay").classList.remove("show"); }}

  document.addEventListener("DOMContentLoaded", function(){{
    var consent = readConsent();
    if(consent){{
      applyConsent(consent);
    }} else {{
      showBanner();
    }}

    document.getElementById("ckAcceptBtn").addEventListener("click", function(){{
      saveConsent({{analytics:true, marketing:true}});
    }});
    document.getElementById("ckRejectBtn").addEventListener("click", function(){{
      saveConsent({{analytics:false, marketing:false}});
    }});
    document.getElementById("ckCustomizeBtn").addEventListener("click", showModal);
    document.getElementById("ckModalRejectBtn").addEventListener("click", function(){{
      saveConsent({{analytics:false, marketing:false}});
    }});
    document.getElementById("ckModalSaveBtn").addEventListener("click", function(){{
      saveConsent({{
        analytics: document.getElementById("ckAnalyticsToggle").checked,
        marketing: document.getElementById("ckMarketingToggle").checked
      }});
    }});

    var reopenLink = document.getElementById("ckReopenLink");
    if(reopenLink){{
      reopenLink.addEventListener("click", function(e){{
        e.preventDefault();
        showModal();
      }});
    }}
  }});
}})();
</script>
"""

BASE_CSS = """
  :root{{
    --gold:#A68526; --mustard:#B59121; --cream:#F3E8CE; --cream-soft:#FAF5E7;
    --ink:#211C17; --ink-soft:#5C5346; --line:#E7DCBE; --white:#FFFFFF; --radius:4px;
    --bonsai:#5C6B3F; --sakura:#B96A56;
    --gold-text:#7E651D;
    --font-display:'Cormorant Garamond', 'Noto Serif SC', Georgia, serif;
    --font-body:'Jost', 'PingFang SC', 'Microsoft YaHei', 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
  }}
  *{{box-sizing:border-box; margin:0; padding:0;}}
  body{{font-family:var(--font-body); color:var(--ink); background:var(--white); -webkit-font-smoothing:antialiased; line-height:1.6;}}
  h1,h2,h3{{font-family:var(--font-display); font-weight:600; color:var(--ink); letter-spacing:-0.01em;}}
  .eyebrow{{font-family:var(--font-body); font-size:11px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--gold-text); margin-bottom:14px; display:block;}}
  .note-banner{{background:#1a1611; color:#e9dcb8; text-align:center; padding:9px 16px; font-size:12px; letter-spacing:.02em;}}
  .promo-banner{{background:var(--ink); color:var(--cream); text-align:center; padding:11px 20px; font-size:13px; font-weight:500; position:relative;}}
  .promo-banner b{{color:var(--cream); font-weight:800; text-decoration:underline; text-decoration-color:var(--mustard); text-underline-offset:3px;}}
  .promo-tag{{display:inline-block; font-size:9px; letter-spacing:.12em; font-weight:700; background:var(--mustard); color:var(--ink); padding:2px 8px; border-radius:3px; margin-right:10px; vertical-align:middle;}}
  header{{border-bottom:1px solid var(--line); position:sticky; top:0; background:rgba(255,255,255,.97); backdrop-filter:blur(6px); z-index:50;}}
  .header-inner{{display:flex; align-items:center; justify-content:space-between; padding:16px 24px; max-width:1200px; margin:0 auto; gap:20px;}}
  .logo{{display:flex; flex-direction:column; align-items:flex-start; line-height:1; text-decoration:none;}}
  .logo .mark{{font-family:var(--font-display); font-size:23px; letter-spacing:.1em; font-weight:600; color:var(--gold);}}
  .logo .sub{{font-size:9px; letter-spacing:.24em; color:var(--ink-soft); font-weight:600; margin-top:4px;}}
  nav.primary{{display:flex; gap:22px; font-size:14px; font-weight:500; white-space:nowrap;}}
  nav.primary a{{color:var(--ink); text-decoration:none; padding:6px 0; border-bottom:1px solid transparent; transition:.15s;}}
  nav.primary a:hover, nav.primary a.active{{border-bottom:1px solid var(--gold); color:var(--gold-text);}}
  /* "Onsen & Spa" nav dropdown — surfaces the 3 sibling service pages
     (Contrast Therapy, Couples Spa, Massage & Spa Treatments) that were
     previously only reachable via the homepage's 3rd menu card or a
     bottom-of-page crosslink. Hover/focus reveals the panel; the trigger
     link itself still navigates straight to onsen-spa.html on click, so no
     existing link behavior changes — this only adds discoverability. */
  .nav-dropdown{{position:relative;}}
  .nav-dropdown > a{{display:inline-flex; align-items:center; gap:4px;}}
  .nav-dropdown .nav-caret{{font-size:8px; opacity:.6; transition:transform .15s; margin-bottom:-1px;}}
  .nav-dropdown:hover .nav-caret, .nav-dropdown:focus-within .nav-caret{{transform:rotate(180deg);}}
  .nav-dropdown-menu{{position:absolute; top:100%; left:50%; transform:translateX(-50%); padding-top:12px; opacity:0; visibility:hidden; transition:opacity .15s, transform .15s; z-index:60;}}
  .nav-dropdown:hover .nav-dropdown-menu, .nav-dropdown:focus-within .nav-dropdown-menu{{opacity:1; visibility:visible;}}
  .nav-dropdown-menu-inner{{background:#fff; border:1px solid var(--line); border-radius:8px; box-shadow:0 14px 32px rgba(33,28,23,.14); padding:8px; min-width:230px;}}
  .nav-dropdown-menu a{{display:block; padding:9px 12px; border-radius:5px; font-size:13.5px; font-weight:500; color:var(--ink); text-decoration:none; white-space:nowrap; border-bottom:none;}}
  .nav-dropdown-menu a:hover{{background:var(--cream-soft); color:var(--gold-text);}}
  .header-right{{display:flex; align-items:center; gap:12px; flex-shrink:0;}}
  .lang-inline{{display:flex; align-items:center; gap:5px; font-size:11.5px; font-weight:700; color:var(--ink-soft); white-space:nowrap; flex-shrink:0;}}
  .lang-inline .lang-active{{color:var(--gold-text);}}
  .lang-inline .lang-sep{{opacity:.4;}}
  .lang-inline .lang-item{{color:var(--ink-soft); opacity:.65; display:inline-flex; align-items:center; gap:3px;}}
  .lang-inline .lang-item em{{font-style:normal; font-size:8px; letter-spacing:.03em; text-transform:uppercase; border:1px solid var(--line); border-radius:3px; padding:1px 4px;}}
  @media (max-width:900px){{.lang-inline{{display:none;}}}}
  .header-divider{{width:1px; height:16px; background:var(--line); flex-shrink:0;}}
  @media (max-width:900px){{.header-divider{{display:none;}}}}
  .cta-group{{display:flex; gap:10px;}}
  .social-icons{{display:flex; align-items:center; gap:12px; flex-shrink:0;}}
  .social-icon{{display:inline-flex; color:var(--ink-soft); opacity:.7; transition:color .15s, opacity .15s;}}
  .social-icon:hover{{color:var(--gold-text); opacity:1;}}
  @media (max-width:900px){{.header-right > .social-icons{{display:none;}}}}
  .mobile-nav .social-icons{{margin-top:18px; padding-top:16px; border-top:1px solid var(--line); justify-content:center; gap:22px;}}

  /* Book Now buttons — CI colors only, no green/brand-app colors */
  .btn-book{{display:inline-flex; align-items:center; gap:9px; padding:8px 16px; border-radius:var(--radius); text-decoration:none; border:1px solid transparent;}}
  .btn-book-solid{{background:var(--ink); color:var(--cream);}}
  .btn-book-solid .bb-icon{{color:var(--gold);}}
  .btn-book-outline{{background:var(--cream); border:1.5px solid var(--gold); color:var(--ink); box-shadow:0 1px 3px rgba(0,0,0,.12);}}
  .btn-book-outline .bb-icon{{color:var(--gold-text);}}
  .btn-book-outline .bb-sub{{opacity:.85;}}
  .bb-txt{{display:flex; flex-direction:column; line-height:1.15; text-align:left;}}
  .bb-main{{font-weight:800; font-size:12.5px; letter-spacing:.01em;}}
  .bb-sub{{font-weight:500; font-size:10px; opacity:.7;}}
  /* Compact header "Book Now" — single trigger, click-revealed channel
     picker. Click (not hover) so it behaves identically on touch and desktop,
     unlike the "Onsen & Spa" nav dropdown which can rely on hover. */
  .book-picker{{position:relative;}}
  .book-picker-trigger{{cursor:pointer; font:inherit; border:1px solid transparent;}}
  .book-caret{{font-size:8px; opacity:.7; margin-left:2px; transition:transform .15s;}}
  .book-picker.open .book-caret{{transform:rotate(180deg);}}
  .book-picker-menu{{position:absolute; top:calc(100% + 10px); right:0; min-width:190px; background:#fff; border:1px solid var(--line); border-radius:8px; box-shadow:0 14px 32px rgba(33,28,23,.16); padding:8px; opacity:0; visibility:hidden; transform:translateY(-4px); transition:opacity .15s, transform .15s, visibility .15s; z-index:70;}}
  .book-picker.open .book-picker-menu{{opacity:1; visibility:visible; transform:translateY(0);}}
  .book-picker-menu a{{display:flex; align-items:center; gap:9px; padding:9px 10px; border-radius:5px; font-size:13px; font-weight:600; color:var(--ink); text-decoration:none; white-space:nowrap; border-bottom:none;}}
  .book-picker-menu a:hover{{background:var(--cream-soft); color:var(--gold-text);}}
  .book-picker-menu a .bb-icon{{color:var(--gold-text); display:inline-flex;}}
  /* Inside the mobile menu the picker menu drops from a full-width trigger
     instead of a narrow header button, so anchor it to the left and let it
     span full width rather than floating off the right edge. Also restates
     padding/border-bottom the same way the fix above already had to for the
     plain LINE/WhatsApp buttons — same ".mobile-nav a" specificity trap. */
  .mobile-nav .book-picker-trigger{{width:100%; justify-content:center; padding:8px 16px; border-bottom:none;}}
  .mobile-nav .book-picker-menu{{left:0; right:0; top:calc(100% + 8px);}}
  .mobile-nav .book-picker-menu a{{padding:10px 12px; border-bottom:none;}}
  .btn-outline{{background:transparent; border:1px solid var(--gold); color:var(--gold-text); font-size:12.5px; font-weight:700; padding:10px 18px; border-radius:var(--radius); text-decoration:none; display:inline-block;}}
  .hamburger{{display:none; font-size:20px; background:none; border:none; cursor:pointer; color:var(--ink);}}
  .trust{{display:flex; justify-content:center; align-items:center; row-gap:10px; column-gap:40px; flex-wrap:wrap; padding:18px 20px; border-bottom:1px solid var(--line); background:var(--cream-soft); font-size:13px; color:var(--ink-soft); font-weight:600;}}
  .trust b{{color:var(--gold-text); font-weight:800;}}
  .trust a{{color:var(--ink-soft); text-decoration:none; font-weight:600;}}
  .trust a:hover{{color:var(--ink);}}
  .section{{padding:88px 24px;}}
  .section-head{{text-align:center; max-width:640px; margin:0 auto 48px;}}
  .section-head h2{{font-size:32px; margin-bottom:12px;}}
  .section-head p{{color:var(--ink-soft); font-size:15px;}}
  footer{{background:#161310; color:#B8AA84; padding:56px 24px 40px; font-size:13px;}}
  .footer-grid{{display:grid; grid-template-columns:1.4fr 1fr 1fr 1fr; gap:30px; max-width:1200px; margin:0 auto;}}
  .footer-grid h4{{color:#EDE2C4; font-size:12px; letter-spacing:.08em; text-transform:uppercase; margin-bottom:16px;}}
  .footer-grid a{{color:#B8AA84; text-decoration:none; display:block; margin-bottom:10px;}}
  .footer-bottom{{max-width:1200px; margin:32px auto 0; padding-top:20px; border-top:1px solid #2c2717; display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px; font-size:12px;}}
  .sticky-mobile-cta{{display:none; position:fixed; bottom:0; left:0; right:0; z-index:60; background:#fff; border-top:1px solid var(--line); padding:10px 14px; gap:10px; box-shadow:0 -4px 14px rgba(0,0,0,0.08); justify-content:center;}}
  .uxnote-wrap{{text-align:center; margin-top:18px;}}
  .uxnote{{font-size:11px; color:var(--gold-text); border:1px dashed var(--gold); background:#fffdf5; padding:6px 12px; border-radius:6px; display:inline-block;}}
  .mobile-nav{{display:none; flex-direction:column; background:var(--white); border-bottom:1px solid var(--line); padding:6px 24px 18px;}}
  .mobile-nav a{{color:var(--ink); text-decoration:none; padding:12px 0; border-bottom:1px solid var(--line); font-size:15px; font-weight:500;}}
  .mobile-nav a:last-of-type{{border-bottom:none;}}
  .mobile-nav a.active{{color:var(--gold-text); font-weight:700;}}
  .mobile-nav a.sub-link{{padding:10px 0 10px 18px; font-size:13.5px; font-weight:500; color:var(--ink-soft); position:relative;}}
  .mobile-nav a.sub-link::before{{content:"–"; position:absolute; left:0; color:var(--gold);}}
  .mobile-nav .cta-group{{margin-top:14px; gap:10px;}}
  /* Real pre-existing bug, found while verifying the new header social icons
     (2026-08-30): the blanket ".mobile-nav a" rule above (color:var(--ink),
     padding:12px 0, border-bottom) has higher CSS specificity than
     ".btn-book-solid"/".btn-book" and was silently winning inside the mobile
     menu — on the solid (LINE) button this made the text render var(--ink)
     on a var(--ink) background: completely invisible, icon-only, on every
     language. The outline (WhatsApp) button happened to look fine only
     because its own intended color (var(--ink)) is dark-on-light anyway, so
     the collision was invisible there. Scoped override below restores both
     buttons' own intended padding/color inside the mobile menu, matching
     how they already render correctly in the desktop header.
  */
  .mobile-nav .cta-group a{{padding:8px 16px; border-bottom:none;}}
  .mobile-nav .btn-book-solid{{color:var(--cream);}}
  .mobile-nav .btn-book-outline{{color:var(--ink);}}
  .mobile-nav .social-icons a{{padding:0; border-bottom:none;}}
  .mobile-nav .social-icon{{color:var(--ink-soft); opacity:.6;}}
  .mobile-nav.open{{display:flex;}}
  @media (max-width: 900px){{
    nav.primary{{display:none;}} .cta-group.desktop-only{{display:none;}} .hamburger{{display:block;}}
    .footer-grid{{grid-template-columns:1fr 1fr;}} .sticky-mobile-cta{{display:flex;}} body{{padding-bottom:70px;}}
  }}
  @media (min-width: 901px){{ .mobile-nav{{display:none !important;}} }}

  /* ---------- CJK readability pass (Chinese pages only) ----------
     Scoped with :lang(zh-CN), which matches only elements inheriting
     lang="zh-CN" from <html> — this rule set is always safe to ship in the
     shared stylesheet because it can never match on an English page (or a
     future Thai one), regardless of how CSS files get consolidated later.
     Why this exists: several UI sizes here were tuned for Latin letterforms
     (11px/9px small-caps-style labels with wide .1–.16em letter-spacing).
     Chinese characters are denser logographs, so the same pixel size reads
     noticeably smaller and wide tracking between characters looks like
     unintended gaps rather than stylistic spacing — this block raises the
     small end of the type scale and tightens letter-spacing for Chinese only,
     without touching the English sizes at all. */
  :lang(zh-CN){{ line-height:1.8; }}
  :lang(zh-CN) .eyebrow{{ font-size:13px; letter-spacing:.05em; }}
  :lang(zh-CN) nav.primary a{{ font-size:15.5px; }}
  :lang(zh-CN) .mobile-nav a{{ font-size:16px; }}
  :lang(zh-CN) .lang-inline{{ font-size:12.5px; }}
  :lang(zh-CN) .lang-inline .lang-item em{{ font-size:9.5px; }}
  :lang(zh-CN) .promo-banner{{ font-size:14px; }}
  :lang(zh-CN) .promo-tag{{ font-size:10.5px; letter-spacing:.04em; }}
  :lang(zh-CN) .bb-main{{ font-size:13.5px; }}
  :lang(zh-CN) .bb-sub{{ font-size:11px; }}
  :lang(zh-CN) .btn-outline{{ font-size:14px; }}
  :lang(zh-CN) .section-head p{{ font-size:16px; }}
  :lang(zh-CN) .card .kicker{{ font-size:12.5px; letter-spacing:.04em; }}
  :lang(zh-CN) .card p{{ font-size:15px; }}
  :lang(zh-CN) .why-item .why-num{{ font-size:13px; letter-spacing:.04em; }}
  :lang(zh-CN) .why-item p{{ font-size:15px; }}
  :lang(zh-CN) .t-card p{{ font-size:14.5px; }}
  :lang(zh-CN) .t-card .who span{{ font-size:12.5px; }}
  :lang(zh-CN) .t-card .t-rating{{ font-size:12px; }}
  :lang(zh-CN) .t-card .read-more{{ font-size:13px; }}
  :lang(zh-CN) footer{{ font-size:14px; }}
  :lang(zh-CN) .footer-grid h4{{ font-size:13px; }}
  :lang(zh-CN) .footer-bottom{{ font-size:13px; }}
  :lang(zh-CN) .page-hero p{{ font-size:16px; }}
  :lang(zh-CN) .menu-title-bar span{{ font-size:13px; }}
  :lang(zh-CN) table.menu-table{{ font-size:14.5px; }}
  :lang(zh-CN) table.menu-table th{{ font-size:12px; letter-spacing:.04em; }}
  :lang(zh-CN) .room-card .desc{{ font-size:13.5px; }}
  :lang(zh-CN) .room-card .price-line .dur{{ font-size:12.5px; }}
  :lang(zh-CN) .room-card .addon{{ font-size:12.5px; }}
  :lang(zh-CN) .spa-col-note{{ font-size:13.5px; }}
  :lang(zh-CN) .vat-note{{ font-size:14px; }}
  :lang(zh-CN) .tier .tier-badge{{ letter-spacing:.08em; }}
  :lang(zh-CN) .tier .tier-name{{ font-size:24px; }}
  :lang(zh-CN) .tier .pay-row{{ font-size:13.5px; }}
  :lang(zh-CN) .tier .regular-price, :lang(zh-CN) .tier .regular-line{{ font-size:14px; }}
  :lang(zh-CN) .tier ul{{ font-size:13.5px; }}
  :lang(zh-CN) .promo-flag{{ font-size:11px; letter-spacing:.04em; }}
  :lang(zh-CN) .promo-amount .unit{{ font-size:14.5px; }}
  :lang(zh-CN) .promo-bonus{{ font-size:12px; }}
  :lang(zh-CN) .best-value{{ font-size:10.5px; letter-spacing:.04em; }}
  :lang(zh-CN) .ck-text{{ font-size:14px; }}
  :lang(zh-CN) .ck-btn{{ font-size:13.5px; }}
  :lang(zh-CN) .ck-modal .intro{{ font-size:14px; }}
  :lang(zh-CN) .ck-cat p{{ font-size:13.5px; }}
  :lang(zh-CN) .ck-cat-head strong{{ font-size:15px; }}

  /* SEO P1-6: shared cross-link component used on the new commercial pages
     (Rooms & Packages, Contrast Therapy, Couples Spa, Massage & Spa, Visit
     Us) to satisfy the audit's "internal links OUT" spec for each page
     without duplicating this small block into every page-specific
     extra_css string. */
  .crosslink-grid{{display:grid; grid-template-columns:repeat(4,1fr); gap:18px; max-width:1100px; margin:40px auto 0;}}
  .crosslink-card{{border:1px solid var(--line); border-radius:6px; overflow:hidden; background:#fff; display:flex; flex-direction:column; transition:box-shadow .18s, transform .18s;}}
  .crosslink-card:hover{{box-shadow:0 8px 22px rgba(33,28,23,.1); transform:translateY(-2px);}}
  .crosslink-card .thumb{{height:120px; position:relative; overflow:hidden; background:var(--cream-soft);}}
  .crosslink-card .thumb img{{position:absolute; inset:0; width:100%; height:100%; object-fit:cover;}}
  .crosslink-card .body{{padding:16px 18px 18px; display:flex; flex-direction:column; gap:6px; flex:1;}}
  .crosslink-card.no-thumb .body{{padding-top:20px;}}
  .crosslink-card h4{{font-size:14.5px; margin:0;}}
  .crosslink-card p{{font-size:12px; color:var(--ink-soft); margin:0 0 2px; line-height:1.6; flex:1;}}
  .crosslink-card .price-tag{{font-size:12.5px; font-weight:800; color:var(--ink);}}
  .crosslink-card a{{font-size:11.5px; font-weight:700; color:var(--gold-text); text-decoration:none; margin-top:2px;}}
  @media (max-width:900px){{.crosslink-grid{{grid-template-columns:1fr 1fr;}}}}
  @media (max-width:560px){{.crosslink-grid{{grid-template-columns:1fr;}}}}
"""

def header(active, lang="en", zh_href=None, en_href=None, th_href=None):
    def navlink(label, href, key):
        cls = " active" if key == active else ""
        return f'<a class="{cls.strip()}" href="{href}">{label}</a>'

    def services_dropdown(main_label, main_href, sub_items):
        # main_href/label render exactly as the old plain navlink did (same
        # click target, same active-state styling) — the dropdown is a pure
        # hover/focus addition on top, so no existing link behavior changes.
        # sub_items: list of (label, href) for the 3 sibling service pages.
        cls = " active" if active == "services" else ""
        items_html = "\n      ".join(f'<a href="{href}">{label}</a>' for label, href in sub_items)
        desktop = f'''<div class="nav-dropdown">
      <a class="{cls.strip()}" href="{main_href}" aria-haspopup="true">{main_label} <span class="nav-caret">&#9662;</span></a>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-menu-inner">
          {items_html}
        </div>
      </div>
    </div>'''
        mobile = navlink(main_label, main_href, "services") + "\n    " + "\n    ".join(
            f'<a class="sub-link" href="{href}">{label}</a>' for label, href in sub_items
        )
        return desktop, mobile

    if lang == "zh":
        # zh/*.html pages sit one directory below the site root. index/onsen-spa/
        # membership/blog + all 7 articles are siblings inside zh/ (flat relative
        # links). The privacy policy isn't translated yet, so that one link still
        # steps back up to the English root with "../" (see footer()).
        home_href, services_href, membership_href, blog_href = "index.html", "onsen-spa.html", "membership.html", "blog.html"
        gallery_href, location_href, contact_href = "index.html#gallery", "index.html#location", "index.html#contact"
        logo_href = "index.html"
        promo_html = f'''<span class="promo-tag">限时优惠</span>
  60分钟私人温泉 + 60分钟芳香精油按摩（双人・共120分钟）— <b>3,888泰铢</b> <span style="opacity:.55; text-decoration:line-through;">6,313泰铢</span> &middot; <a href="{BOOK_LINKS['LINE']}" target="_blank" rel="noopener" style="color:var(--cream); font-weight:800; text-decoration:underline; text-underline-offset:2px;">立即预订</a>'''
        logo_sub = "PRIVATE ONSEN &amp; SPA"
        labels = {"home": "首页", "services": "温泉与SPA", "membership": "会员", "blog": "养生日志", "gallery": "图库", "location": "位置", "contact": "联系我们"}
        # No dropdown here: Chinese never split Contrast Therapy/Couples/Massage
        # into their own pages (still uses the original combined onsen-spa.html
        # with #couple/#spa anchors — a deliberate, long-standing scope
        # boundary, see project brief). Keep this nav item a plain flat link,
        # same as before, rather than listing pages that don't exist in
        # Chinese. Revisit only if/when zh gets its own page split.
        services_desktop_html = navlink(labels["services"], services_href, "services")
        services_mobile_html = navlink(labels["services"], services_href, "services")
        # Language switcher on a zh page: 中文 is the active/current language;
        # EN links back to the matching English page (en_href is always known
        # for a page we're generating in Chinese). Thai's page set doesn't map
        # 1:1 onto Chinese's older page structure (zh kept the old combined
        # onsen-spa.html; th split into separate Contrast/Couples/Massage/
        # Location pages) — but for the 3 pages that DO exist on both sides
        # (index, onsen-spa, membership), th_href is passed in and a real
        # direct zh<->th link is shown instead of routing through EN. Pages
        # with no Thai counterpart still correctly fall back to "Soon".
        th_switch_item = f'<a class="lang-item" href="{th_href}" style="text-decoration:none;">ไทย</a>' if th_href else '<span class="lang-item">ไทย <em>即将上线</em></span>'
        lang_switch = f'''<a class="lang-item" href="{en_href or 'index.html'}" style="text-decoration:none;">EN</a>
        <span class="lang-sep">&middot;</span>
        {th_switch_item}
        <span class="lang-sep">&middot;</span>
        <span class="lang-active">中文</span>'''
    elif lang == "th":
        # th/*.html pages sit one directory below the site root, same pattern
        # as zh/. Built against the CURRENT (post-P1) English architecture
        # from the start, so — unlike zh — Location routes to a real
        # translated Visit Us page, and Blog falls back to the English blog
        # ("../blog.html") since Thai blog translation isn't in scope yet.
        home_href, services_href, membership_href, blog_href = "index.html", "onsen-spa.html", "membership.html", "../blog.html"
        gallery_href, location_href, contact_href = "index.html#gallery", "location-thonglor-bangkok.html", "index.html#contact"
        logo_href = "index.html"
        promo_html = f'''<span class="promo-tag">โปรโมชั่นจำกัดเวลา</span>
  ออนเซ็นส่วนตัว 60 นาที + นวดอโรมาเธอราพี 60 นาที สำหรับ 2 ท่าน (รวม 120 นาที) — <b>3,888 บาท</b> <span style="opacity:.55; text-decoration:line-through;">6,313 บาท</span> &middot; <a href="{BOOK_LINKS['LINE']}" target="_blank" rel="noopener" style="color:var(--cream); font-weight:800; text-decoration:underline; text-underline-offset:2px;">จองเลย</a>'''
        logo_sub = "PRIVATE ONSEN &amp; SPA"
        # Blog nav label carries a plain "(EN)" note — the blog itself has no
        # Thai translation in scope, and clicking through lands on the English
        # blog.html (with its own English header/footer). Same "don't surprise
        # a reader with an unannounced language switch" rule already applied
        # to the in-body article links elsewhere on these pages.
        labels = {"home": "หน้าแรก", "services": "ออนเซ็นและสปา", "membership": "สมาชิก", "blog": '''บล็อก <em style="font-style:normal; font-size:9px; letter-spacing:.03em; opacity:.6;">(EN)</em>''', "gallery": "แกลเลอรี", "location": "ที่ตั้ง", "contact": "ติดต่อเรา"}
        # Thai has all 4 real service pages (built against the current
        # post-P1 architecture from day one — see project brief), so it gets
        # the full dropdown, same as English. Sub-labels reuse the exact
        # Thai terms already established on each page's own <h1>/crosslink
        # cards, not new translations.
        services_desktop_html, services_mobile_html = services_dropdown(
            labels["services"], services_href,
            [
                ("ห้องออนเซ็นส่วนตัว", "onsen-spa.html"),
                ("การบำบัดความร้อนสลับเย็น", "contrast-therapy-ice-bath-bangkok.html"),
                ("สปาคู่รัก", "couples-spa-bangkok.html"),
                ("นวดและทรีตเมนต์สปา", "massage-spa-bangkok.html"),
            ]
        )
        # Language switcher on a th page: ไทย is the active/current language;
        # EN links back to the matching English page. For the 3 pages that
        # exist on both zh and th (index, onsen-spa, membership), zh_href is
        # passed in and a real direct th<->zh link is shown; pages with no
        # Chinese counterpart (Contrast/Couples/Massage/Location — zh never
        # split these out of its combined onsen-spa.html) fall back to "Soon".
        zh_switch_item = f'<a class="lang-item" href="{zh_href}" style="text-decoration:none;">中文</a>' if zh_href else '<span class="lang-item">中文 <em>Soon</em></span>'
        lang_switch = f'''<a class="lang-item" href="{en_href or 'index.html'}" style="text-decoration:none;">EN</a>
        <span class="lang-sep">&middot;</span>
        <span class="lang-active">ไทย</span>
        <span class="lang-sep">&middot;</span>
        {zh_switch_item}'''
    else:
        home_href, services_href, membership_href, blog_href = "index.html", "onsen-spa.html", "membership.html", "blog.html"
        # SEO P1-6/25: "Location" now routes to the new dedicated Visit Us page
        # (full NAP, hours, map, directions) instead of the homepage's #location
        # anchor, which stays in place as valid on-page content but is no longer
        # the nav target. English only — no Chinese Visit Us page exists yet.
        gallery_href, location_href, contact_href = "index.html#gallery", "location-thonglor-bangkok.html", "index.html#contact"
        logo_href = "index.html"
        promo_html = f'''<span class="promo-tag">Limited-time</span>
  60-Min Private Onsen + 60-Min Aromatherapy for 2 Guests (120 min) — <b>3,888 THB</b> <span style="opacity:.55; text-decoration:line-through;">6,313 THB</span> &middot; <a href="{BOOK_LINKS['LINE']}" target="_blank" rel="noopener" style="color:var(--cream); font-weight:800; text-decoration:underline; text-underline-offset:2px;">Book Now</a>'''
        logo_sub = "PRIVATE ONSEN &amp; SPA"
        labels = {"home": "Home", "services": "Onsen &amp; Spa", "membership": "Membership", "blog": "Blog", "gallery": "Gallery", "location": "Location", "contact": "Contact"}
        # "Onsen & Spa" becomes a hover/focus dropdown covering all 4 real
        # service pages (client request, 2026-08-30 — standalone treatments
        # were previously reachable only via the homepage's 3rd menu card or
        # a bottom-of-page crosslink, with no route from the persistent nav
        # at all). The trigger link itself still goes straight to
        # onsen-spa.html on click, same as before.
        services_desktop_html, services_mobile_html = services_dropdown(
            labels["services"], services_href,
            [
                ("Private Onsen Rooms", "onsen-spa.html"),
                ("Contrast Therapy", "contrast-therapy-ice-bath-bangkok.html"),
                ("Couples Spa", "couples-spa-bangkok.html"),
                ("Massage &amp; Spa Treatments", "massage-spa-bangkok.html"),
            ]
        )
        # Language switcher on an English page: 中文/ไทย become real links the
        # moment a counterpart exists for this page (zh_href/th_href passed
        # in); otherwise each stays a "Soon" placeholder.
        zh_switch_item = f'<a class="lang-item" href="{zh_href}" style="text-decoration:none;">中文</a>' if zh_href else '<span class="lang-item">中文 <em>Soon</em></span>'
        th_switch_item = f'<a class="lang-item" href="{th_href}" style="text-decoration:none;">ไทย</a>' if th_href else '<span class="lang-item">ไทย <em>Soon</em></span>'
        lang_switch = f'''<span class="lang-active">EN</span>
        <span class="lang-sep">&middot;</span>
        {th_switch_item}
        <span class="lang-sep">&middot;</span>
        {zh_switch_item}'''

    return f"""
<div class="promo-banner">
  {promo_html}
</div>
<header>
  <div class="header-inner">
    <a class="logo" href="{logo_href}">
      <span class="mark">ZENVA</span>
      <span class="sub">{logo_sub}</span>
    </a>
    <nav class="primary">
      {navlink(labels["home"], home_href, "home")}
      {services_desktop_html}
      {navlink(labels["membership"], membership_href, "membership")}
      {navlink(labels["blog"], blog_href, "blog")}
      {navlink(labels["gallery"], gallery_href, "")}
      {navlink(labels["location"], location_href, "location")}
      {navlink(labels["contact"], contact_href, "")}
    </nav>
    <div class="header-right">
      <div class="lang-inline" role="group" aria-label="Choose language">
        {lang_switch}
      </div>
      <span class="header-divider" aria-hidden="true"></span>
      <div class="social-icons" role="group" aria-label="Follow Zenva">{social_icons_html()}</div>
      <div class="cta-group desktop-only">{book_picker(lang, "desktop")}</div>
      <button class="hamburger" id="hamburgerBtn" type="button" aria-expanded="false" aria-controls="mobileNavPanel" aria-label="Open menu">&#9776;</button>
    </div>
  </div>
  <nav class="mobile-nav" id="mobileNavPanel" aria-label="Mobile">
    {navlink(labels["home"], home_href, "home")}
    {services_mobile_html}
    {navlink(labels["membership"], membership_href, "membership")}
    {navlink(labels["blog"], blog_href, "blog")}
    {navlink(labels["gallery"], gallery_href, "")}
    {navlink(labels["location"], location_href, "location")}
    {navlink(labels["contact"], contact_href, "")}
    <div class="cta-group">{book_picker(lang, "mobile")}</div>
    <div class="social-icons" role="group" aria-label="Follow Zenva">{social_icons_html()}</div>
  </nav>
</header>
<script>
(function(){{
  var btn = document.getElementById('hamburgerBtn');
  var panel = document.getElementById('mobileNavPanel');
  if(!btn || !panel) return;
  function closeMenu(){{
    panel.classList.remove('open');
    btn.setAttribute('aria-expanded','false');
    btn.setAttribute('aria-label','Open menu');
  }}
  function openMenu(){{
    panel.classList.add('open');
    btn.setAttribute('aria-expanded','true');
    btn.setAttribute('aria-label','Close menu');
  }}
  btn.addEventListener('click', function(){{
    if(panel.classList.contains('open')){{ closeMenu(); }} else {{ openMenu(); }}
  }});
  panel.querySelectorAll('a').forEach(function(a){{
    a.addEventListener('click', closeMenu);
  }});
  document.addEventListener('keydown', function(e){{
    if(e.key === 'Escape') closeMenu();
  }});
}})();
(function(){{
  // Compact header "Book Now" trigger — click (not hover) toggles the
  // LINE/WhatsApp channel picker so it works identically on touch and
  // desktop. There are 2 instances per page (desktop header + mobile nav);
  // wire each up independently so opening one never affects the other.
  var pickers = document.querySelectorAll('.book-picker');
  pickers.forEach(function(picker){{
    var trigger = picker.querySelector('.book-picker-trigger');
    var menu = picker.querySelector('.book-picker-menu');
    if(!trigger || !menu) return;
    function close(){{
      picker.classList.remove('open');
      trigger.setAttribute('aria-expanded','false');
    }}
    function open(){{
      pickers.forEach(function(p){{ if(p !== picker){{ p.classList.remove('open'); var t=p.querySelector('.book-picker-trigger'); if(t) t.setAttribute('aria-expanded','false'); }} }});
      picker.classList.add('open');
      trigger.setAttribute('aria-expanded','true');
    }}
    trigger.addEventListener('click', function(e){{
      e.stopPropagation();
      if(picker.classList.contains('open')){{ close(); }} else {{ open(); }}
    }});
    menu.querySelectorAll('a').forEach(function(a){{
      a.addEventListener('click', close);
    }});
  }});
  document.addEventListener('click', function(e){{
    pickers.forEach(function(picker){{
      if(!picker.contains(e.target)){{
        picker.classList.remove('open');
        var t = picker.querySelector('.book-picker-trigger');
        if(t) t.setAttribute('aria-expanded','false');
      }}
    }});
  }});
  document.addEventListener('keydown', function(e){{
    if(e.key === 'Escape'){{
      pickers.forEach(function(picker){{
        picker.classList.remove('open');
        var t = picker.querySelector('.book-picker-trigger');
        if(t) t.setAttribute('aria-expanded','false');
      }});
    }}
  }});
}})();
</script>
"""

def footer(lang="en", zh_href=None, en_href=None, th_href=None):
    if lang == "zh":
        blog_href, privacy_href = "blog.html", "../privacy-policy.html"
        cta_html = cta_buttons_zh()
        # Same fix as header(): a real direct link to Thai when th_href is
        # passed in (the 3 pages that exist on both sides), "Soon" otherwise.
        th_col_item = f'<a href="{th_href}" style="color:inherit; text-decoration:underline;">ไทย (Thai)</a>' if th_href else 'ไทย (Thai) <em style="font-style:normal; font-size:10px; letter-spacing:.06em; text-transform:uppercase; opacity:.75;">— 即将上线</em>'
        lang_col = f'''<span style="display:block; color:#8a7c5c; font-size:13px;"><a href="{en_href or '../index.html'}" style="color:inherit; text-decoration:underline;">English</a></span><span style="display:block; color:#8a7c5c; font-size:13px; margin-top:8px;">{th_col_item}</span><span style="display:block; color:#cdbf98; font-size:13px; margin-top:8px;">中文 (Chinese)</span>'''
        return f"""
<footer>
  <div class="footer-grid">
    <div><h4>Zenva — Private Onsen &amp; Spa</h4><p style="color:#8a7c5c;">Seenspace Thonglor, FL 03-01<br>251/1 Thong Lo 13 Alley, Khlong Tan Nuea, Watthana<br>曼谷 10110，泰国</p><p style="color:#8a7c5c; margin-top:10px;">致电我们：<a href="tel:+66802629191" style="color:inherit; text-decoration:underline;">+66 80 262 9191</a></p><p style="color:#8a7c5c; margin-top:10px;">每日营业，12:00&ndash;00:00</p></div>
    <div><h4>探索</h4><a href="onsen-spa.html">温泉与SPA</a><a href="membership.html">会员</a><a href="{blog_href}">养生日志</a><a href="index.html#gallery">图库</a><a href="index.html#location">位置</a></div>
    <div><h4>关注我们</h4><a href="https://www.instagram.com/zenvaspabkk/" target="_blank" rel="noopener">Instagram</a><a href="https://www.tiktok.com/@zenvaspabkk" target="_blank" rel="noopener">TikTok</a><a href="https://www.facebook.com/zenvaspa/" target="_blank" rel="noopener">Facebook</a><a href="https://lin.ee/Qcbmudy" target="_blank" rel="noopener">LINE官方账号</a></div>
    <div><h4>语言</h4>{lang_col}</div>
  </div>
  <div class="footer-bottom"><span>&copy; Zenva Management 版权所有。</span><span><a href="{privacy_href}" style="color:inherit;">隐私与Cookie政策</a> &middot; <a href="#" id="ckReopenLink" style="color:inherit;">Cookie设置</a> &middot; 条款</span></div>
</footer>
<div class="sticky-mobile-cta">{cta_html}</div>
"""

    if lang == "th":
        # th/*.html pages sit one directory below the site root, same pattern
        # as zh/. Blog falls back to the English blog (not yet translated);
        # Location is a real translated page (unlike zh's current #anchor).
        blog_href, privacy_href = "../blog.html", "../privacy-policy.html"
        cta_html = cta_buttons_th()
        # Same fix as header(): a real direct link to Chinese when zh_href is
        # passed in (the 3 pages that exist on both sides), "Soon" otherwise.
        zh_col_item = f'<a href="{zh_href}" style="color:inherit; text-decoration:underline;">中文 (Chinese)</a>' if zh_href else '中文 (Chinese) <em style="font-style:normal; font-size:10px; letter-spacing:.06em; text-transform:uppercase; opacity:.75;">— Soon</em>'
        lang_col = f'''<span style="display:block; color:#8a7c5c; font-size:13px;"><a href="{en_href or '../index.html'}" style="color:inherit; text-decoration:underline;">English</a></span><span style="display:block; color:#cdbf98; font-size:13px; margin-top:8px;">ไทย (Thai)</span><span style="display:block; color:#8a7c5c; font-size:13px; margin-top:8px;">{zh_col_item}</span>'''
        return f"""
<footer>
  <div class="footer-grid">
    <div><h4>Zenva — Private Onsen &amp; Spa</h4><p style="color:#8a7c5c;">ซีนสเปซ ทองหล่อ ชั้น 3 (FL 03-01)<br>เลขที่ 251/1 ซอยทองหล่อ 13<br>แขวงคลองตันเหนือ เขตวัฒนา กรุงเทพฯ 10110</p><p style="color:#8a7c5c; margin-top:10px;">โทร: <a href="tel:+66802629191" style="color:inherit; text-decoration:underline;">+66 80 262 9191</a></p><p style="color:#8a7c5c; margin-top:10px;">เปิดทุกวัน 12:00&ndash;00:00 น.</p></div>
    <div><h4>สำรวจ</h4><a href="onsen-spa.html">ออนเซ็นและสปา</a><a href="membership.html">สมาชิก</a><a href="{blog_href}">บล็อก <em style="font-style:normal; font-size:9px; letter-spacing:.03em; opacity:.65;">(EN)</em></a><a href="index.html#gallery">แกลเลอรี</a><a href="location-thonglor-bangkok.html">ที่ตั้ง</a></div>
    <div><h4>ติดตามเรา</h4><a href="https://www.instagram.com/zenvaspabkk/" target="_blank" rel="noopener">Instagram</a><a href="https://www.tiktok.com/@zenvaspabkk" target="_blank" rel="noopener">TikTok</a><a href="https://www.facebook.com/zenvaspa/" target="_blank" rel="noopener">Facebook</a><a href="https://lin.ee/Qcbmudy" target="_blank" rel="noopener">LINE ทางการ</a></div>
    <div><h4>ภาษา</h4>{lang_col}</div>
  </div>
  <div class="footer-bottom"><span>&copy; สงวนลิขสิทธิ์ Zenva Management</span><span><a href="{privacy_href}" style="color:inherit;">นโยบายความเป็นส่วนตัวและคุกกี้</a> &middot; <a href="#" id="ckReopenLink" style="color:inherit;">ตั้งค่าคุกกี้</a> &middot; ข้อกำหนด</span></div>
</footer>
<div class="sticky-mobile-cta">{cta_html}</div>
"""

    zh_col_item = f'<a href="{zh_href}" style="color:inherit; text-decoration:underline;">中文 (Chinese)</a>' if zh_href else '中文 (Chinese) <em style="font-style:normal; font-size:10px; letter-spacing:.06em; text-transform:uppercase; opacity:.75;">— Soon</em>'
    th_col_item = f'<a href="{th_href}" style="color:inherit; text-decoration:underline;">ไทย (Thai)</a>' if th_href else 'ไทย (Thai) <em style="font-style:normal; font-size:10px; letter-spacing:.06em; text-transform:uppercase; opacity:.75;">— Soon</em>'
    return f"""
<footer>
  <div class="footer-grid">
    <div><h4>Zenva — Private Onsen &amp; Spa</h4><p style="color:#8a7c5c;">SEENSPACE Thonglor, FL 03-01<br>251/1 Thong Lo 13 Alley, Khlong Tan Nuea, Watthana<br>Bangkok 10110, Thailand</p><p style="color:#8a7c5c; margin-top:10px;">Call us: <a href="tel:+66802629191" style="color:inherit; text-decoration:underline;">+66 80 262 9191</a></p><p style="color:#8a7c5c; margin-top:10px;">Open daily, 12:00&ndash;00:00</p></div>
    <div><h4>Explore</h4><a href="onsen-spa.html">Onsen &amp; Spa</a><a href="membership.html">Membership</a><a href="blog.html">Blog</a><a href="index.html#gallery">Gallery</a><a href="location-thonglor-bangkok.html">Location</a></div>
    <div><h4>Connect</h4><a href="https://www.instagram.com/zenvaspabkk/" target="_blank" rel="noopener">Instagram</a><a href="https://www.tiktok.com/@zenvaspabkk" target="_blank" rel="noopener">TikTok</a><a href="https://www.facebook.com/zenvaspa/" target="_blank" rel="noopener">Facebook</a><a href="https://lin.ee/Qcbmudy" target="_blank" rel="noopener">LINE Official</a></div>
    <div><h4>Language</h4><span style="display:block; color:#cdbf98; font-size:13px;">English</span><span style="display:block; color:#8a7c5c; font-size:13px; margin-top:8px;">{th_col_item}</span><span style="display:block; color:#8a7c5c; font-size:13px; margin-top:8px;">{zh_col_item}</span></div>
  </div>
  <div class="footer-bottom"><span>&copy; Zenva Management. All rights reserved.</span><span><a href="privacy-policy.html" style="color:inherit;">Privacy &amp; Cookie Policy</a> &middot; <a href="#" id="ckReopenLink" style="color:inherit;">Cookie Settings</a> &middot; Terms</span></div>
</footer>
<div class="sticky-mobile-cta">{cta_buttons()}</div>
"""

# SEO P0-3: the "image" field now points at the real hosted hero image (depended on
# P0-1's asset externalization being done first) instead of a placeholder string.
# The "aggregateRating" block previously shipped a placeholder reviewCount and was
# removed entirely rather than filled with an invented number, per the project's
# standing rule against fabricating business facts. It has now been added back
# (2026-08-29) with a real figure: 4.8 / 261 reviews, confirmed by navigating
# directly to Zenva's own Google Business Profile panel (not typed from memory —
# read live off the rendered page) the same day the on-page reviews section was
# UPDATED 2026-08-31: re-checked live on Google Maps, count moved to 267 (rating
# unchanged at 4.8). Re-verify this figure periodically — it will keep climbing.
# rebuilt with 12 individually re-verified Google review links. Re-confirm and
# update this figure periodically as new reviews accrue; do not let it go stale
# indefinitely. "sameAs" has
# been expanded to the other real, already-live social profiles used elsewhere on
# this site (footer links). Full street address + postal code (client-supplied,
# 2026-08-27) is now in place below. Precise lat/long "geo" coordinates are still
# intentionally left out — Claude has not independently verified them and won't
# invent a coordinate pair; add once the client supplies (or confirms) them.
# SEO P0-4: openingHoursSpecification below reflects hours confirmed directly by
# the client (2026-08-23): open daily, 12:00-00:00 (noon to midnight).
# SEO P0-5: client confirmed (2026-08-23) that a Google Business Profile exists
# and is live/active — full profile-completeness details (category, photos,
# hours matching the site) are NOT independently verified from this session.
BASE_URL = "https://zenvaspabkk.com"

SCHEMA_JSONLD = f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "DaySpa",
  "name": "Zenva - Private Onsen & Spa",
  "image": "{BASE_URL}{IMG['hero']}",
  "telephone": "+66802629191",
  "priceRange": "THB 590 - THB 7900",
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "267"
  }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "SEENSPACE Thonglor, FL 03-01, 251/1 Thong Lo 13 Alley, Khlong Tan Nuea, Watthana",
    "addressLocality": "Bangkok",
    "postalCode": "10110",
    "addressCountry": "TH"
  }},
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ],
    "opens": "12:00",
    "closes": "00:00"
  }},
  "sameAs": [
    "https://www.instagram.com/zenvaspabkk/",
    "https://www.tiktok.com/@zenvaspabkk",
    "https://www.facebook.com/zenvaspa/",
    "https://lin.ee/Qcbmudy"
  ]
}}
</script>"""

# ---------- MULTILINGUAL SEO ARCHITECTURE ----------
# Decisions locked in (2026-08-15): subdirectories for future non-English
# languages (/zh/..., /th/...), not suffixed filenames — keeps hreflang, robots
# rules, and sitemap grouping simple as content scales, and costs nothing extra
# since pages are generated by this script either way.
#
# PAGE_ALTERNATES is the single source of truth for every page's translated
# counterparts. Right now only "en" is populated (Chinese/Thai aren't live yet —
# see master-brief.md). Canonical + hreflang tags are generated automatically
# from this dict, so turning on a new language sitewide is a ONE-LINE change
# per page here, not a manual per-page edit:
#   "membership.html": {"en": "membership.html", "zh": "zh/membership.html"}
# The moment "zh" is approved and its page exists on disk, add that one key/value
# pair below and every page's <head> updates with correct hreflang automatically.
# (moved above SCHEMA_JSONLD, which now needs BASE_URL to build a fully-qualified
# image URL for structured data — see SEO P0-3)

PAGE_ALTERNATES = {
    # NOTE: zh pages for these three now exist on disk (see ZH PREVIEW BUILD
    # section below) but are intentionally NOT yet added here as a "zh-CN" key.
    # They're an unapproved preview, not yet signed off by a native speaker —
    # exactly like privacy-policy.html's legal-review gate. Registering them
    # here would turn on sitemap + hreflang for content that hasn't been
    # approved to represent Zenva publicly yet. The moment the translation is
    # approved, add e.g. "zh-CN": "zh/index.html" to each of these three lines
    # — hreflang goes sitewide-correct automatically — and remove the matching
    # "Disallow: /zh/" line from robots.txt in the same change.
    "index.html":                                 {"en": "index.html"},
    "onsen-spa.html":                              {"en": "onsen-spa.html"},
    # SEO P1-6: the 3 new commercial pages split out of onsen-spa.html, plus
    # the new Visit Us page — see Section 3 of the SEO audit. onsen-spa.html
    # itself is KEPT as the URL for the trimmed "Private Onsen Rooms &
    # Packages" page rather than renamed to the audit's literal suggestion
    # of /private-onsen-rooms-bangkok.html, specifically to avoid breaking
    # the existing zh/onsen-spa.html mirror page and its hreflang entry
    # (Chinese restructuring was not requested/approved). Flagged here as a
    # deliberate deviation from the audit's literal wording, not an oversight.
    "contrast-therapy-ice-bath-bangkok.html":      {"en": "contrast-therapy-ice-bath-bangkok.html"},
    "couples-spa-bangkok.html":                    {"en": "couples-spa-bangkok.html"},
    "massage-spa-bangkok.html":                    {"en": "massage-spa-bangkok.html"},
    "location-thonglor-bangkok.html":              {"en": "location-thonglor-bangkok.html"},
    "membership.html":                             {"en": "membership.html"},
    "blog.html":                                   {"en": "blog.html"},
    "blog-contrast-therapy.html":                  {"en": "blog-contrast-therapy.html"},
    "blog-private-vs-public-onsen.html":           {"en": "blog-private-vs-public-onsen.html"},
    "blog-couples-spa-day-checklist.html":         {"en": "blog-couples-spa-day-checklist.html"},
    "blog-thai-vs-aromatherapy-massage.html":      {"en": "blog-thai-vs-aromatherapy-massage.html"},
    "blog-choosing-private-onsen-bangkok.html":    {"en": "blog-choosing-private-onsen-bangkok.html"},
    "blog-onsen-aftercare-guide.html":             {"en": "blog-onsen-aftercare-guide.html"},
    "blog-self-care-history.html":                {"en": "blog-self-care-history.html"},
    "privacy-policy.html":                        {"en": "privacy-policy.html"},
}

# Registered here so sitemap.xml (built at the end of this script) stays in sync
# with every page automatically — nothing to remember to update by hand.
SITEMAP_PATHS = list(PAGE_ALTERNATES.keys())

def seo_head_tags(path, group=None):
    """Canonical + hreflang <link> tags for one page, driven by PAGE_ALTERNATES.
    `path` is the actual output location of THIS page (used for the canonical
    tag); `group` is the PAGE_ALTERNATES key holding all of its language
    siblings (defaults to `path` itself, which is exactly right for English
    pages where the output path IS the group key). A translated page (e.g.
    zh/membership.html) passes its own `path` plus `group="membership.html"`
    so it still finds and lists its English/Thai siblings correctly.
    Safe to call even with only one language live — the x-default fallback and
    self-referencing canonical are valid on their own and require zero changes
    when zh/th are added later."""
    group = group or path
    if not path or group not in PAGE_ALTERNATES:
        return ""
    alts = PAGE_ALTERNATES[group]
    tags = [f'<link rel="canonical" href="{BASE_URL}/{path}">']
    for lang, lang_path in alts.items():
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="{BASE_URL}/{lang_path}">')
    if "en" in alts:
        tags.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}/{alts["en"]}">')
    return "\n".join(tags)

def page(title, active, body, extra_css, description="", path=None, group=None, lang="en", zh_href=None, en_href=None, th_href=None, hero_image=None, og_image=None):
    desc_tag = f'<meta name="description" content="{description}">' if description else ""
    # LCP element on pages with a full-bleed CSS hero background is discovered late by the
    # preload scanner (it's inside a <style> block, not a real <img>). A high-priority
    # preload hint closes most of that gap without restructuring the hero markup.
    hero_preload = f'<link rel="preload" as="image" href="{hero_image}" fetchpriority="high">' if hero_image else ""
    # SEO P1-9: og:image/og:url were previously impossible (no real hosted image
    # files existed pre-P0-1). Now that every photo is a real asset, every page
    # gets a real, absolute og:image — the page's own hero/lead photo where one
    # was passed in via hero_image, falling back to the site's main hero photo
    # otherwise (e.g. Membership, which has no photographic hero) — plus a
    # real og:url and og:locale, so links shared on LINE/Facebook/WhatsApp/
    # iMessage render a preview image instead of none at all.
    resolved_og_image = og_image or hero_image or IMG["hero"]
    og_url_tag = f'<meta property="og:url" content="{BASE_URL}/{path}">' if path else ""
    og_tags = f"""
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="{BASE_URL}{resolved_og_image}">
{og_url_tag}
<meta property="og:locale" content="{'zh_CN' if lang == 'zh' else 'th_TH' if lang == 'th' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">""" if description else ""
    seo_tags = seo_head_tags(path, group)
    html_lang = "zh-CN" if lang == "zh" else "th" if lang == "th" else "en"
    header_html = header(active, lang=lang, zh_href=zh_href, en_href=en_href, th_href=th_href)
    footer_html = footer(lang=lang, zh_href=zh_href, en_href=en_href, th_href=th_href)
    cookie_html = COOKIE_BANNER_HTML_ZH if lang == "zh" else COOKIE_BANNER_HTML_TH if lang == "th" else COOKIE_BANNER_HTML
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{hero_preload}
{desc_tag}{og_tags}
{seo_tags}
{FONT_FACE_CSS}
<style>{BASE_CSS}
{COOKIE_CSS}
{extra_css}
</style>
{SCHEMA_JSONLD}
</head>
<body>
{header_html}
{body}
{footer_html}
{cookie_html}
</body>
</html>"""

BASE_CSS = BASE_CSS.format()
print("v4 module ready")

# ---------- INDEX ----------
index_extra_css = """
  /* Hero is a horizontal scroll-snap carousel (2026-08-30 client correction:
     the scrollable promotions/education banner they asked for is the hero
     itself, not a separate strip below it — that earlier strip has been
     removed). Structure: .hero-carousel wraps a flex .hero-track of
     full-width .hero-slide panels, one per topic. The English homepage
     carries 6 slides — the real hero first, completely unchanged, then 5
     promo/education slides, each now using real client-supplied photography
     (added 2026-08-31, see per-slide comments below) rather than the earlier
     placeholder gradient art. Chinese/Thai homepages keep a single .hero-slide
     (same real hero, no new copy) —
     same markup shape, so this shared CSS applies with no visual change
     there and no untranslated content goes live. */
  .hero-carousel{{position:relative; height:640px;}}
  .hero-track{{display:flex; height:100%; overflow-x:auto; scroll-snap-type:x mandatory; scrollbar-width:none;}}
  .hero-track::-webkit-scrollbar{{display:none;}}
  .hero-slide{{position:relative; flex:0 0 100%; width:100%; height:100%; display:flex; align-items:flex-end; scroll-snap-align:start;}}
  .hero-bg{{position:absolute; inset:0; background-size:cover; background-position:center 30%;}}
  .hero-scrim{{position:absolute; inset:0; background:linear-gradient(180deg, rgba(33,28,23,.15) 0%, rgba(33,28,23,.8) 100%);}}
  .hero-content{{position:relative; z-index:2; padding:0 76px 62px; max-width:1200px; margin:0 auto; width:100%; color:#fff;}}
  .hero-content h1, .hero-content h2{{font-size:50px; color:#fff; line-height:1.12; max-width:680px; margin-bottom:16px;}}
  .hero-content p.sub{{font-size:16px; color:#E9E1CC; max-width:520px; margin-bottom:28px;}}
  .hero-content .eyebrow{{color:var(--cream);}}
  .hero-more-link{{display:inline-block; font-size:13px; font-weight:700; color:var(--cream); text-decoration:none; border-bottom:1px solid rgba(255,255,255,.5); margin-bottom:24px;}}
  .hero-more-link:hover{{border-color:#fff;}}
  .hero-nav-btn{{position:absolute; top:50%; transform:translateY(-50%); z-index:3; background:rgba(255,255,255,.14); backdrop-filter:blur(2px); border:1px solid rgba(255,255,255,.45); color:#fff; width:44px; height:44px; border-radius:50%; cursor:pointer; font-size:18px; font-family:inherit; display:flex; align-items:center; justify-content:center;}}
  .hero-nav-btn:hover:not(:disabled){{background:rgba(255,255,255,.3);}}
  .hero-nav-btn:disabled{{opacity:.35; cursor:default;}}
  .hero-nav-prev{{left:20px;}}
  .hero-nav-next{{right:20px;}}
  .hero-dots{{position:absolute; left:50%; transform:translateX(-50%); bottom:20px; z-index:3; display:flex; gap:8px;}}
  .hero-dots button{{width:9px; height:9px; padding:0; border-radius:50%; border:1px solid rgba(255,255,255,.75); background:rgba(255,255,255,.25); cursor:pointer;}}
  .hero-dots button.active{{background:#fff;}}
  .why-strip{{padding:52px 24px; background:var(--cream-soft); border-bottom:1px solid var(--line);}}
  .why-grid{{display:grid; grid-template-columns:repeat(3,1fr); gap:36px; max-width:1100px; margin:0 auto;}}
  .why-item{{text-align:center;}}
  .why-item .why-num{{font-size:11px; color:var(--gold-text); letter-spacing:.1em; text-transform:uppercase; font-weight:700; margin-bottom:10px; display:block;}}
  .why-item h3{{font-size:18px; margin-bottom:8px;}}
  .why-item p{{font-size:13px; color:var(--ink-soft); line-height:1.7;}}
  @media (max-width:900px){{.why-grid{{grid-template-columns:1fr; gap:28px;}}}}
  .cards{{display:grid; grid-template-columns:repeat(3,1fr); gap:26px; max-width:1200px; margin:0 auto;}}
  .card{{border:1px solid var(--line); border-radius:6px; overflow:hidden; display:flex; flex-direction:column;}}
  .card .thumb{{height:220px; position:relative; overflow:hidden;}}
  .card .thumb img{{position:absolute; inset:0; width:100%; height:100%; object-fit:cover;}}
  .card .body{{padding:24px 22px 26px; display:flex; flex-direction:column; gap:9px; flex:1;}}
  .card .kicker{{font-size:10.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--ink-soft); font-weight:700;}}
  .card h3{{font-size:19px;}}
  .card p{{font-size:13.5px; color:var(--ink-soft); flex:1;}}
  .card .price-row{{display:flex; justify-content:space-between; align-items:center; margin-top:6px; padding-top:14px; border-top:1px solid var(--line);}}
  .card .price{{font-weight:800; font-size:14px;}}
  .card a.link{{font-size:12.5px; font-weight:700; color:var(--gold-text); text-decoration:none;}}
  .split{{display:grid; grid-template-columns:1fr 1fr; gap:56px; max-width:1200px; margin:0 auto; align-items:center;}}
  .split .photo{{height:400px; border-radius:6px; position:relative; overflow:hidden;}}
  .split .photo img{{position:absolute; inset:0; width:100%; height:100%; object-fit:cover;}}
  .split h2{{font-size:28px; margin-bottom:16px;}}
  .split p{{color:var(--ink-soft); font-size:14.5px; margin-bottom:14px;}}
  .gallery-grid{{display:grid; grid-template-columns:repeat(4,1fr); grid-auto-rows:150px; grid-auto-flow:dense; gap:12px; max-width:1200px; margin:0 auto;}}
  .g-item{{position:relative; overflow:hidden; border-radius:8px; cursor:pointer; background:var(--ink);}}
  .g-item.g-tall{{grid-row:span 2;}}
  .g-item .g-bg{{position:absolute; inset:0; overflow:hidden; transition:transform .5s cubic-bezier(.2,.8,.2,1);}}
  .g-item .g-bg img{{width:100%; height:100%; object-fit:cover; display:block;}}
  .g-item:hover .g-bg{{transform:scale(1.08);}}
  .g-item .g-scrim{{position:absolute; inset:0; background:linear-gradient(180deg, rgba(33,28,23,0) 55%, rgba(33,28,23,.55) 100%); opacity:0; transition:opacity .3s;}}
  .g-item:hover .g-scrim{{opacity:1;}}
  .g-item .g-zoom{{position:absolute; right:12px; bottom:10px; width:26px; height:26px; border-radius:50%; background:rgba(255,255,255,.92); display:flex; align-items:center; justify-content:center; opacity:0; transform:translateY(6px); transition:.3s;}}
  .g-item:hover .g-zoom{{opacity:1; transform:translateY(0);}}
  @media (max-width:900px){{.gallery-grid{{grid-template-columns:repeat(2,1fr); grid-auto-rows:180px;}}}}
  .g-lightbox{{position:fixed; inset:0; background:rgba(20,16,12,.92); z-index:300; display:none; align-items:center; justify-content:center; padding:40px;}}
  .g-lightbox.show{{display:flex;}}
  .g-lightbox img{{max-width:100%; max-height:100%; border-radius:6px; box-shadow:0 20px 60px rgba(0,0,0,.5);}}
  .g-lightbox-close{{position:absolute; top:22px; right:28px; color:#fff; font-size:32px; line-height:1; cursor:pointer; opacity:.85;}}
  .g-lightbox-close:hover{{opacity:1;}}
  .g-lightbox-nav{{position:absolute; top:50%; transform:translateY(-50%); color:#fff; font-size:34px; cursor:pointer; opacity:.75; padding:10px 16px; user-select:none;}}
  .g-lightbox-nav:hover{{opacity:1;}}
  .g-lightbox-prev{{left:10px;}} .g-lightbox-next{{right:10px;}}
  .mem-teaser{{background:var(--ink); color:var(--cream); padding:60px 24px; text-align:center;}}
  .mem-teaser h2{{color:var(--cream); margin-bottom:10px;}}
  .mem-teaser p{{color:#cdbf98; max-width:520px; margin:0 auto 20px;}}
  .reels-grid{{display:grid; grid-template-columns:repeat(3,1fr); gap:20px; max-width:900px; margin:0 auto;}}
  @media (max-width:700px){{.reels-grid{{grid-template-columns:repeat(2,1fr); max-width:640px;}}}}
  .reels-grid video{{width:100%; aspect-ratio:9/16; object-fit:cover; border-radius:8px; background:var(--ink); display:block;}}
  .testimonials{{display:grid; grid-template-columns:repeat(4,1fr); gap:18px; max-width:1200px; margin:0 auto;}}
  .t-card{{background:var(--cream-soft); border:1px solid var(--line); border-radius:6px; padding:26px 22px 22px; display:flex; flex-direction:column;}}
  .t-card .t-mark{{font-family:var(--font-display); font-size:34px; line-height:1; color:var(--gold); opacity:.55; margin-bottom:6px;}}
  .t-card p{{font-size:13px; color:var(--ink-soft); margin-bottom:16px; font-style:italic; flex:1;}}
  .t-card .t-foot{{display:flex; justify-content:space-between; align-items:flex-end; gap:10px; border-top:1px solid var(--line); padding-top:12px;}}
  .t-card .who{{font-size:12px; font-weight:700; color:var(--ink); line-height:1.5;}}
  .t-card .who span{{display:block; font-weight:500; color:var(--ink-soft); font-style:normal; font-size:11.5px;}}
  .t-card .t-rating{{font-size:11px; font-weight:700; color:var(--gold-text); white-space:nowrap;}}
  .t-card .read-more{{font-size:11.5px; font-weight:700; color:var(--gold-text); text-decoration:none; margin-top:10px; display:inline-block;}}
  .t-card.pending{{border-style:dashed; color:var(--ink-soft);}}
  @media (max-width:1100px){{.testimonials{{grid-template-columns:repeat(2,1fr);}}}}
  @media (max-width:900px){{.cards{{grid-template-columns:1fr;}} .split{{grid-template-columns:1fr;}} .gallery-grid{{grid-template-columns:repeat(3,1fr);}} .hero-content{{padding:0 24px 62px;}} .hero-content h1, .hero-content h2{{font-size:30px;}} .hero-carousel{{height:560px;}} .hero-nav-btn{{display:none;}} .hero-dots{{bottom:12px;}} .testimonials{{grid-template-columns:1fr;}}}}
  .reviews-nav{{display:flex; align-items:center; justify-content:center; gap:18px; margin-top:30px;}}
  .reviews-nav button{{background:transparent; border:1px solid var(--gold); color:var(--gold-text); font-size:12.5px; font-weight:700; padding:10px 22px; border-radius:var(--radius); cursor:pointer; font-family:inherit;}}
  .reviews-nav button:hover:not(:disabled){{background:var(--gold); color:#fff;}}
  .reviews-nav button:disabled{{opacity:.35; cursor:default;}}
  .reviews-nav .reviews-page-count{{font-size:12px; color:var(--ink-soft); min-width:46px; text-align:center;}}
""".format(**IMG)

index_body = """
<section class="hero-carousel" aria-roledescription="carousel" aria-label="Featured offers and guides">
  <div class="hero-track" id="heroTrack">
    <div class="hero-slide" aria-roledescription="slide" aria-label="1 of 6">
      <div class="hero-bg" style="background-image:url('{hero}');" role="img" aria-label="Private onsen room with a guest seated at the edge of the hot bath"></div><div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">Contrast Therapy &middot; Full Recovery</span>
        <h1>Hot Onsen. Ice Bath. Complete Recovery, Entirely Private.</h1>
        <p class="sub">Alternate between mineral onsen heat and ice-bath cold — the contrast therapy ritual proven to ease muscle recovery and mental fatigue — then complete it with signature spa treatments for a fuller recovery experience. Fully private, up to three guests.</p>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
    <!-- Slide 2 — real limited-time offer, already live in the header promo strip.
         Real photo (client-supplied, added 2026-08-31): couple seated together at
         the edge of a private onsen bath, candlelight nearby. -->
    <div class="hero-slide" aria-roledescription="slide" aria-label="2 of 6">
      <div class="hero-bg" style="background-image:url('{hero_couple}');" role="img" aria-label="A couple seated together at the edge of a private onsen bath, candlelight nearby"></div>
      <div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">Limited-Time</span>
        <h2>Two, Together &mdash; 3,888 THB</h2>
        <p class="sub">60 minutes in a private onsen room, plus 60 minutes of aromatherapy massage for two. 120 minutes, one price &mdash; down from 6,313 THB.</p>
        <a class="hero-more-link" href="onsen-spa.html">Book This Offer &rarr;</a>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
    <!-- Slide 3 — real bundle passes (Signature Spa / Aromatherapy / Thai Authentic),
         already priced and live on onsen-spa.html#bundles. Real photo (client-supplied,
         added 2026-08-31): couple relaxing together in a private wood sauna, salt
         panel wall — evokes the repeat-visit/ritual theme. -->
    <div class="hero-slide" aria-roledescription="slide" aria-label="3 of 6">
      <div class="hero-bg" style="background-image:url('{hero_ritual}');" role="img" aria-label="A couple relaxing together in a private wood sauna with a glowing salt panel wall"></div>
      <div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">For Regulars</span>
        <h2>Make It a Ritual</h2>
        <p class="sub">Multi-visit passes for Signature Spa, Aromatherapy, and Thai Authentic treatments &mdash; from 10,800 THB for 3 visits.</p>
        <a class="hero-more-link" href="onsen-spa.html#bundles">See Bundle Passes &rarr;</a>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
    <!-- Slide 4 — real membership tiers (Silver 10,000&rarr;11,000 through Platinum
         100,000&rarr;150,000), already live on membership.html. Real photo
         (client-supplied, added 2026-08-31): abstract warm gold/bronze texture,
         used deliberately as brand-toned art rather than a literal room photo. -->
    <div class="hero-slide" aria-roledescription="slide" aria-label="4 of 6">
      <div class="hero-bg" style="background-image:url('{hero_membership}');" role="img" aria-label="Warm gold and bronze abstract texture"></div>
      <div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">Membership</span>
        <h2>Turn 10,000 THB Into 11,000</h2>
        <p class="sub">Silver through Platinum tiers add bonus credit to every top-up &mdash; redeemable across all onsen, spa, and massage services.</p>
        <a class="hero-more-link" href="membership.html">View Membership Tiers &rarr;</a>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
    <!-- Slide 5 — educational, links to the existing "Choosing a Private Onsen in
         Bangkok" article. Real photo (client-supplied, added 2026-08-31): a folded
         robe, towels, and slippers on a bench beside a private onsen bath — a calm,
         welcoming "what to expect" moment. -->
    <div class="hero-slide" aria-roledescription="slide" aria-label="5 of 6">
      <div class="hero-bg" style="background-image:url('{hero_firsttime}');" role="img" aria-label="A folded robe, towels, and slippers on a bench beside a private onsen bath"></div>
      <div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">New Here?</span>
        <h2>What to Expect Your First Time</h2>
        <p class="sub">No communal bathing, no crowds, no guesswork. Here's exactly how a private onsen visit works, from arrival to aftercare.</p>
        <a class="hero-more-link" href="blog-choosing-private-onsen-bangkok.html">Read the Guide &rarr;</a>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
    <!-- Slide 6 — educational, links to the existing "Contrast Therapy" Journal
         article. Real photo (client-supplied, added 2026-08-31): twin private
         onsen tubs, one steaming hot and one cool, side by side in one frame. -->
    <div class="hero-slide" aria-roledescription="slide" aria-label="6 of 6">
      <div class="hero-bg" style="background-image:url('{hero_hotcold}');" role="img" aria-label="Twin private onsen tubs, one steaming hot and one cool, side by side"></div>
      <div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">The Science</span>
        <h2>Why Hot + Cold Works</h2>
        <p class="sub">Contrast therapy pairs a hot onsen soak with an Ice Bath. Here's what it's commonly reported to do &mdash; and who should check with a doctor first.</p>
        <a class="hero-more-link" href="blog-contrast-therapy.html">Read the Full Guide &rarr;</a>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
  </div>
  <button type="button" class="hero-nav-btn hero-nav-prev" id="heroPrev" aria-label="Previous slide">&#8249;</button>
  <button type="button" class="hero-nav-btn hero-nav-next" id="heroNext" aria-label="Next slide">&#8250;</button>
  <div class="hero-dots" id="heroDots" role="tablist" aria-label="Choose slide"></div>
</section>
<script>
(function(){{
  var track = document.getElementById('heroTrack');
  var prev = document.getElementById('heroPrev');
  var next = document.getElementById('heroNext');
  var dotsWrap = document.getElementById('heroDots');
  if(!track || !prev || !next || !dotsWrap) return;
  var slides = Array.prototype.slice.call(track.children);
  slides.forEach(function(_, i){{
    var d = document.createElement('button');
    d.type = 'button';
    d.setAttribute('role', 'tab');
    d.setAttribute('aria-label', 'Go to slide ' + (i + 1));
    d.addEventListener('click', function(){{
      slides[i].scrollIntoView({{behavior:'smooth', block:'nearest', inline:'start'}});
    }});
    dotsWrap.appendChild(d);
  }});
  var dots = Array.prototype.slice.call(dotsWrap.children);
  function closestIndex(){{
    var best = 0, bestDist = Infinity;
    slides.forEach(function(s, i){{
      var dist = Math.abs(s.offsetLeft - track.scrollLeft);
      if(dist < bestDist){{ bestDist = dist; best = i; }}
    }});
    return best;
  }}
  function refresh(){{
    var i = closestIndex();
    dots.forEach(function(d, di){{ d.classList.toggle('active', di === i); d.setAttribute('aria-selected', di === i ? 'true' : 'false'); }});
    prev.disabled = track.scrollLeft <= 4;
    next.disabled = track.scrollLeft >= track.scrollWidth - track.clientWidth - 4;
  }}
  prev.addEventListener('click', function(){{
    var i = Math.max(0, closestIndex() - 1);
    slides[i].scrollIntoView({{behavior:'smooth', block:'nearest', inline:'start'}});
  }});
  next.addEventListener('click', function(){{
    var i = Math.min(slides.length - 1, closestIndex() + 1);
    slides[i].scrollIntoView({{behavior:'smooth', block:'nearest', inline:'start'}});
  }});
  track.addEventListener('scroll', function(){{
    window.requestAnimationFrame(refresh);
  }}, {{passive:true}});
  refresh();
}})();
</script>
<div class="why-strip">
  <div class="section-head" style="margin-bottom:34px;">
    <span class="eyebrow">A Quiet Philosophy</span>
  </div>
  <div class="why-grid">
    <div class="why-item"><span class="why-num">Hot &amp; Cold</span><h3>Contrast Therapy, Considered</h3><p>Mineral onsen heat and ice-bath cold, held within the same private room — a recovery ritual gaining renewed attention worldwide, practiced here as a discipline, not a gimmick.</p><a class="link" style="font-size:12px; font-weight:700; color:var(--gold-text); text-decoration:none; display:inline-block; margin-top:8px;" href="contrast-therapy-ice-bath-bangkok.html">Learn more &rarr;</a></div>
    <div class="why-item"><span class="why-num">Privacy</span><h3>Yours Alone</h3><p>No shared bathhouse, no communal schedule. Each room belongs to you alone — as a couple, or with close company of up to three.</p></div>
    <div class="why-item"><span class="why-num">Craft</span><h3>Quiet, Considered Detail</h3><p>Real mineral-salt water and thoughtful materials, chosen for genuine recovery rather than for how a room photographs.</p></div>
  </div>
</div>
<section class="section" id="menu">
  <div class="section-head"><span class="eyebrow">Explore</span><h2>Our Menu</h2><p>Three categories — see the full menu &amp; rates on each page below</p></div>
  <div class="cards">
    <div class="card">
      <div class="thumb"><img src="{menu_card_onsen}" alt="Guest relaxing against the glowing Himalayan salt wall inside the private sauna" loading="lazy"></div>
      <div class="body"><span class="kicker">Contrast Therapy</span><h3>Private Onsen Rooms</h3>
      <p>Bonsai (sauna room) &amp; Sakura (steam room) — ice bath, mineral onsen, Himalayan salt sauna. Up to 3 pax.</p>
      <div class="price-row"><span class="price">From 3,190+ THB</span><a class="link" href="onsen-spa.html">Full menu &rarr;</a></div></div>
    </div>
    <div class="card">
      <div class="thumb"><img src="{massage_card}" alt="Therapist giving an aromatherapy massage" loading="lazy"></div>
      <div class="body"><span class="kicker">For Two</span><h3>Couple Onsen Packages</h3>
      <p>Onsen + massage combinations for two guests, 120&ndash;150 minutes of shared ritual.</p>
      <div class="price-row"><span class="price">From 4,900+ THB</span><a class="link" href="couples-spa-bangkok.html">Full menu &rarr;</a></div></div>
    </div>
    <div class="card">
      <div class="thumb"><img src="{signature_card}" alt="Zenva signature spa treatment tray" loading="lazy"></div>
      <div class="body"><span class="kicker">Full Recovery</span><h3>Spa &amp; Massage Collection</h3>
      <p>Luxury Aromatherapy, Thai Authentic, and our 18-Steps Vietnamese Zenva Spa — hair, ear &amp; facial rituals.</p>
      <div class="price-row"><span class="price">From 590+ THB</span><a class="link" href="massage-spa-bangkok.html">Full menu &rarr;</a></div></div>
    </div>
  </div>
</section>
<section class="section" style="background:var(--cream-soft); padding-top:76px; padding-bottom:76px;" id="location">
  <div class="split">
    <div class="photo"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div>
    <div><span class="eyebrow">Our Space</span><h2>A Quiet Room of One's Own</h2>
    <p>Every visit begins the same way — a private room, a private ritual, no shared waiting areas. Seenspace Thonglor, 3rd Floor.</p>
    <p style="color:var(--ink-soft); font-size:14px; margin-bottom:18px;">Open daily, 12:00&ndash;00:00</p>
    <a class="btn-outline" href="location-thonglor-bangkok.html">Hours &amp; Directions &rarr;</a>
    <a href="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor" target="_blank" rel="noopener" style="margin-left:14px; font-size:12.5px; font-weight:700; color:var(--gold-text); text-decoration:none;">Get Directions &rarr;</a></div>
  </div>
  <div style="max-width:1100px; margin:40px auto 0; border-radius:8px; overflow:hidden; border:1px solid var(--line);">
    <iframe src="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor&output=embed" width="100%" height="320" style="border:0; display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Zenva location map"></iframe>
  </div>
</section>
<div class="mem-teaser">
  <span class="eyebrow" style="color:var(--cream);">Wellness Privilege</span>
  <h2>Four Membership Tiers</h2>
  <p>Silver, Gold, Diamond &amp; Platinum — redeemable across all onsen, spa, and massage services.</p>
  <a class="btn-outline" style="color:var(--cream); border-color:var(--cream);" href="membership.html">See Membership Details &rarr;</a>
</div>
<section class="section" id="gallery">
  <div class="section-head"><span class="eyebrow">Inside Zenva</span><h2>Gallery</h2></div>
  <div class="gallery-grid" id="galleryGrid">
    <div class="g-item g-tall" data-full="{g1}" data-caption="Sakura steam room, after dark">
      <div class="g-bg"><img src="{g1}" alt="Sakura steam room at night, lit by warm ambient light beneath cherry blossoms" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g7}" data-caption="An evening in the Bonsai room">
      <div class="g-bg"><img src="{g7}" alt="Guest seated at the edge of the Bonsai onsen bath among the greenery" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g2}" data-caption="A session in progress">
      <div class="g-bg"><img src="{g2}" alt="Therapist performing a treatment in a private room" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g3}" data-caption="Ear-candling treatment detail">
      <div class="g-bg"><img src="{g3}" alt="Ear-candling spa treatment detail" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g8}" data-caption="The Zenva welcome ritual">
      <div class="g-bg"><img src="{g8}" alt="Zenva welcome tray with branded linen and aromatherapy salts" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g4}" data-caption="The Zenva sign, framed by blossoms">
      <div class="g-bg"><img src="{g4}" alt="The Zenva sign framed by blossom branches at the entrance" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g5}" data-caption="Welcome tea &amp; mango sticky rice">
      <div class="g-bg"><img src="{g5}" alt="Welcome tea and mango sticky rice" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g6}" data-caption="Candlelight by the water">
      <div class="g-bg"><img src="{g6}" alt="Guest holding a candle beside the onsen water" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g9}" data-caption="Massage chairs with personal streaming">
      <div class="g-bg"><img src="{g9}" alt="Guest reclining in a premium massage chair, streaming entertainment on the personal screen" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g10}" data-caption="Into the salt-wall sauna">
      <div class="g-bg"><img src="{g10}" alt="Guest stepping into the Himalayan salt-wall sauna, silhouetted in the evening light" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g11}" data-caption="The rain shower, ready">
      <div class="g-bg"><img src="{g11}" alt="Overhead rain showerhead beside the private spa treatment bed" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
  </div>
</section>
<div class="g-lightbox" id="gLightbox">
  <span class="g-lightbox-close" id="gLightboxClose">&times;</span>
  <span class="g-lightbox-nav g-lightbox-prev" id="gLightboxPrev">&#8249;</span>
  <img id="gLightboxImg" src="" alt="">
  <span class="g-lightbox-nav g-lightbox-next" id="gLightboxNext">&#8250;</span>
</div>
<script>
(function(){{
  var items = Array.prototype.slice.call(document.querySelectorAll("#galleryGrid .g-item"));
  if(!items.length) return;
  var lb = document.getElementById("gLightbox");
  var lbImg = document.getElementById("gLightboxImg");
  var idx = 0;
  function open(i){{
    idx = i;
    lbImg.src = items[idx].getAttribute("data-full");
    lbImg.alt = items[idx].getAttribute("data-caption") || "";
    lb.classList.add("show");
  }}
  function close(){{ lb.classList.remove("show"); lbImg.src = ""; }}
  function step(d){{ idx = (idx + d + items.length) % items.length; lbImg.src = items[idx].getAttribute("data-full"); lbImg.alt = items[idx].getAttribute("data-caption") || ""; }}
  items.forEach(function(el, i){{ el.addEventListener("click", function(){{ open(i); }}); }});
  document.getElementById("gLightboxClose").addEventListener("click", close);
  document.getElementById("gLightboxPrev").addEventListener("click", function(){{ step(-1); }});
  document.getElementById("gLightboxNext").addEventListener("click", function(){{ step(1); }});
  lb.addEventListener("click", function(e){{ if(e.target === lb) close(); }});
  document.addEventListener("keydown", function(e){{
    if(!lb.classList.contains("show")) return;
    if(e.key === "Escape") close();
    if(e.key === "ArrowLeft") step(-1);
    if(e.key === "ArrowRight") step(1);
  }});
}})();
</script>
<section class="section" id="reels" style="background:var(--cream-soft);">
  <div class="section-head"><span class="eyebrow">In Motion</span><h2>Zenva Reels</h2><p>A closer look, straight from our own social feed.</p></div>
  <div class="reels-grid" id="reelsGrid">
    <video muted loop playsinline preload="metadata">
      <source src="{reel1_webm}" type="video/webm">
      <source src="{reel1_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel3_webm}" type="video/webm">
      <source src="{reel3_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel5_webm}" type="video/webm">
      <source src="{reel5_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel6_webm}" type="video/webm">
      <source src="{reel6_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel7_webm}" type="video/webm">
      <source src="{reel7_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel8_webm}" type="video/webm">
      <source src="{reel8_mp4}" type="video/mp4">
    </video>
  </div>
</section>
<script>
(function(){{
  var vids = Array.prototype.slice.call(document.querySelectorAll("#reelsGrid video"));
  if(!vids.length) {{ return; }}
  if(!('IntersectionObserver' in window)){{
    vids.forEach(function(v){{ v.play().catch(function(){{}}); }});
  }} else {{
    var io = new IntersectionObserver(function(entries){{
      entries.forEach(function(entry){{
        if(entry.isIntersecting){{ entry.target.play().catch(function(){{}}); }}
        else {{ entry.target.pause(); }}
      }});
    }}, {{threshold: 0.25}});
    vids.forEach(function(v){{ io.observe(v); }});
  }}
}})();
</script>
<section class="section" id="reviews">
  <div class="section-head"><span class="eyebrow">In Their Words &middot; 4.8&#9733; on Google &middot; 267 reviews</span><h2>Loved on Google</h2></div>
  <div class="testimonials" id="reviewsGrid">
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>We had booked the couple's private Bonsai Sauna experience&mdash;Himalayan pink salt sauna, one of a kind place... Although it looked very aesthetic with the beautiful decor and ambient lighting&hellip;</p>
      <div class="t-foot">
        <div class="who">The Traveler<span>41 reviews in Bangkok</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/31Vv077s7GpMqaAt1" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>I booked the private Sakura onsen room, which includes a hot onsen bath, a cold plunge, and a steam room. The facilities felt quite new and the room was very private, making the whole experience feel calm and exclusive&hellip;</p>
      <div class="t-foot">
        <div class="who">Ami Narissara<span>Local Guide &middot; 38 reviews</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/iXiLC4lhTXhcnjVvc" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>My wife and I had such a great private onsen experience here today&hellip; Genuinely great, and such a good location! Highly, highly recommend.</p>
      <div class="t-foot">
        <div class="who">Jonathan O'Callaghan<span>Local Guide &middot; 32 reviews</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/eoyRkCzlwQwFBk5jO" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Great service and place is clean. The therapy person is very great.</p>
      <div class="t-foot">
        <div class="who">P. Panyasakorn<span>4 weeks ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/FagUAf6goHtcNnEit" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Amazing spa in Thonglor with a great variety of treatments. Really enjoy both the steam &amp; sauna rooms. Will definitely be coming back.</p>
      <div class="t-foot">
        <div class="who">Zach Cohen<span>a month ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/rH4tOAehC1tibdiBU" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>A really nice relaxing and experience for the weekend. The overall atmosphere is made for peace in body and mind. Definitely gonna come back to this place.</p>
      <div class="t-foot">
        <div class="who">Nichalee T.<span>a month ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/gADn1tD0YCyQUoYmo" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Nice and clean onsen. You can have a private room and relax fully. Massage is good, they have lemongrass oil&mdash;very nice smell.</p>
      <div class="t-foot">
        <div class="who">&#1070;&#1083;&#1080;&#1103; &#1040;&#1079;&#1072;&#1088;&#1080;&#1085;&#1072;<span>a month ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/IpmrWLS77bBxlBe29" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>I had Jaae as my masseuse, and she was absolutely wonderful&hellip; Her hands have a magic touch, and the massage was one of the best I've ever experienced.</p>
      <div class="t-foot">
        <div class="who">omar ben sellam<span>2 months ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/G6e7orSjqXAH3x2C1" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Private onsen and spa in the middle of Thong lo. I spent 2 hrs here. The Mineral salt Japanese onsen and Ice bath are awesome. Highly recommend this place!</p>
      <div class="t-foot">
        <div class="who">natthawat ru<span>4 months ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/n2oqeuPcMZWwguBGk" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>What a great experience. I was looking for a relaxation spa with wellness, a cold plunge, and a sauna, and this place had it all&hellip; Apple was incredibly kind and welcoming. Highly recommended!</p>
      <div class="t-foot">
        <div class="who">&#1491;&#1504;&#1497;&#1488;&#1500; &#1488;&#1500;&#1506;&#1494;&#1512;<span>7 months ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/4vderGJuuPJYkh8Fm" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>We tried this new place as it just opened and took the 2 hour private onsen + Vietnamese Spa session. It was very refreshing and the place looks gorgeous! Highly recommend!</p>
      <div class="t-foot">
        <div class="who">Robert<span>8 months ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/iZrE5f6zwqdjUs49D" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>A newly opened spa on Thonglor Soi 13 offers an elevated relaxation experience with private onsens, Vietnamese spa rituals, and dedicated neck&ndash;shoulder massages&hellip; The therapists are exceptional&mdash;strong, precise hands with truly professional technique.</p>
      <div class="t-foot">
        <div class="who">Ek-kapop<span>8 months ago</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/Pr0SYhJPXkMRlpKEY" target="_blank" rel="noopener">Read on Google &rarr;</a>
    </div>
  </div>
  <div class="reviews-nav">
    <button type="button" id="reviewsPrev">&#8249; Previous</button>
    <span class="reviews-page-count" id="reviewsPageCount"></span>
    <button type="button" id="reviewsNext">Next &#8250;</button>
  </div>
</section>
<script>
(function(){{
  var grid = document.getElementById("reviewsGrid");
  if(!grid) return;
  var cards = Array.prototype.slice.call(grid.children);
  var perPage = 4;
  var pages = Math.ceil(cards.length / perPage) || 1;
  var page = 0;
  var prevBtn = document.getElementById("reviewsPrev");
  var nextBtn = document.getElementById("reviewsNext");
  var countEl = document.getElementById("reviewsPageCount");
  function render(){{
    cards.forEach(function(card, i){{
      card.style.display = (Math.floor(i / perPage) === page) ? "" : "none";
    }});
    if(prevBtn) prevBtn.disabled = (page === 0);
    if(nextBtn) nextBtn.disabled = (page === pages - 1);
    if(countEl) countEl.textContent = (page + 1) + " / " + pages;
  }}
  if(prevBtn) prevBtn.addEventListener("click", function(){{ if(page > 0){{ page--; render(); }} }});
  if(nextBtn) nextBtn.addEventListener("click", function(){{ if(page < pages - 1){{ page++; render(); }} }});
  render();
}})();
</script>
<section class="section" id="contact" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">Contact</span><h2 style="margin-bottom:14px;">Reserve Your Ritual</h2>
  <p style="color:var(--ink-soft); margin-bottom:24px;">Chat with our front desk directly — real-time replies during opening hours.</p>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons(), ZOOM_ICON=ZOOM_ICON, **IMG, **VID)

with open("/tmp/zenva_site/index.html", "w") as f:
    f.write(page("Private Onsen Bangkok | Zenva — Private Onsen & Spa, Thonglor", "home", index_body, index_extra_css,
                 description="Private hot onsen and ice bath contrast therapy rooms in Bangkok, paired with signature spa treatments. Fully private, up to 3 guests, at Seenspace Thonglor.", path="index.html", zh_href="zh/index.html", th_href="th/index.html", hero_image=IMG["hero"]))
print("index.html v4 written")

# ---------- ONSEN & SPA — MENU/TABLE FORMAT ----------
# SEO P1-6: this single page previously covered 6+ distinct commercial search
# intents (rooms, couple packages, massage/spa treatments) under one thin H2
# each — see audit Section 3/4. It's now split into 4 focused pages:
#   - THIS page (URL kept as onsen-spa.html — see PAGE_ALTERNATES note above
#     for why the URL wasn't renamed) becomes "Private Onsen Rooms & Packages"
#   - couples-spa-bangkok.html: the former "Onsen Package (Couple)" block
#   - massage-spa-bangkok.html: the former "Spa & Massage Collection" block
#   - location-thonglor-bangkok.html: new, not split from this page
# Shared helper functions/data (couple_table, spa_col, bonsai_packages, etc.)
# stay defined once here and are reused by the new pages below.
services_extra_css = """
  .page-hero{{padding:52px 24px 36px; text-align:center; background:var(--cream-soft); border-bottom:1px solid var(--line);}}
  .page-hero h1{{font-size:36px; margin-bottom:8px;}}
  .page-hero p{{color:var(--ink-soft); max-width:520px; margin:0 auto;}}
  .menu-block{{max-width:1040px; margin:0 auto 70px;}}
  .menu-title-bar{{background:var(--ink); color:var(--cream); text-align:center; padding:12px 20px; border-radius:4px; margin-bottom:24px;}}
  .menu-title-bar h2{{color:var(--cream); font-size:20px; letter-spacing:.04em;}}
  .menu-title-bar span{{font-size:11.5px; color:#cdbf98; letter-spacing:.06em; text-transform:uppercase;}}

  .room-pair{{display:grid; grid-template-columns:1fr 1fr; gap:22px; margin-bottom:8px;}}
  .room-card{{border:1px solid var(--line); border-radius:8px; overflow:hidden;}}
  .room-card .photo{{height:230px; position:relative; overflow:hidden;}}
  .room-card .photo img{{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center 62%;}}
  .room-card .tag{{position:absolute; bottom:0; left:0; color:#fff; padding:7px 16px; font-family:var(--font-display); font-size:16px; letter-spacing:.03em;}}
  .room-card.bonsai .tag{{background:var(--bonsai);}}
  .room-card.sakura .tag{{background:var(--sakura);}}
  .room-card .info{{padding:14px 16px 16px;}}
  .room-card .desc{{font-size:12.5px; color:var(--ink-soft); margin-bottom:10px;}}
  .room-card .price-line{{display:flex; justify-content:space-between; align-items:baseline; border-top:1px dashed var(--line); padding-top:10px;}}
  .room-card .price-line .amt{{font-weight:800; font-size:16px;}}
  .room-card .price-line .dur{{font-size:11.5px; color:var(--ink-soft);}}
  .room-card .addon{{font-size:11px; color:var(--ink-soft); margin-top:6px;}}
  .room-intro{{max-width:760px; margin:0 auto 40px; font-size:14px; color:var(--ink-soft); line-height:1.85;}}
  .room-intro a{{color:var(--gold-text); font-weight:700; text-decoration:none;}}
  .vat-note{{text-align:center; font-size:12.5px; color:var(--ink-soft); margin-top:-40px; margin-bottom:60px;}}
  @media (max-width:900px){{.room-pair{{grid-template-columns:1fr;}}}}
"""

def couple_table(room_class, room_label, price_list, headers=("Package", "Duration", "Price")):
    rows = "".join(f'<tr><td class="pkg">{name}</td><td class="dur">{dur}</td><td class="pr">{price}</td></tr>' for name, dur, price in price_list)
    return f"""<div>
      <h3><span class="swatch {room_class}"></span>{room_label}</h3>
      <table class="menu-table">
        <tr><th>{headers[0]}</th><th>{headers[1]}</th><th>{headers[2]}</th></tr>
        {rows}
      </table>
    </div>"""

bonsai_packages = [
    ("+ Aromatherapy", "120 min", "5,900+ THB"),
    ("+ Aromatherapy (ext.)", "150 min", "7,900+ THB"),
    ("+ Any 2 Vietnamese Spa", "120 min", "4,900+ THB"),
    ("+ Vietnamese Full Course", "150 min", "5,900+ THB"),
]
sakura_packages = [
    ("+ Aromatherapy", "120 min", "5,900+ THB"),
    ("+ Aromatherapy (ext.)", "150 min", "7,900+ THB"),
    ("+ Any 2 Vietnamese Spa", "120 min", "4,900+ THB"),
    ("+ Vietnamese Full Course", "150 min", "5,900+ THB"),
]

def spa_col(title, rows, note=""):
    body = "".join(f'<tr><td class="pkg">{n}</td><td class="pr">{p}</td></tr>' for n, p in rows)
    note_html = f'<p class="spa-col-note">{note}</p>' if note else ""
    return f"""<div class="spa-col"><h3>{title}</h3><table class="menu-table">{body}</table>{note_html}</div>"""

luxury_rows = [("Aromatherapy Massage — 60 min", "1,590+ THB"), ("Aromatherapy Massage — 90 min", "2,390+ THB")]
thai_rows = [("Foot / Head / Neck / Shoulder — 30 min", "590+ THB"), ("— 60 min", "790+ THB"), ("— 90 min", "1,090+ THB"), ("— 120 min", "1,390+ THB")]
signature_rows = [("Any 1: Hair / Ear / Facial — 30 min", "690+ THB"), ("Any 2 — 60 min", "1,290+ THB"), ("18-Steps Vietnamese Zenva Spa (Hair, Ear &amp; Facial), All 3 — 90 min", "1,590+ THB")]

# ---------- BUNDLE / MULTI-VISIT RITUAL PASSES (client-supplied pricing, 2026-08-24) ----------
# Placed on onsen-spa.html (not massage-spa-bangkok.html) because every bundle
# pairs the Private Onsen room with a treatment ("Private Onsen + ..."), and
# massage-spa-bangkok.html's own hero copy says "no onsen room required" —
# putting onsen-inclusive bundles there would contradict that page. Mirrors
# Yunomori's pattern of keeping multi-visit passes on the same page as the
# base item's own pricing, rather than a separate isolated page (client asked
# for this research before deciding placement; see master-brief.md).
BUNDLE_CSS = """
  .bundle-intro{{max-width:760px; margin:0 auto 34px; font-size:14px; color:var(--ink-soft); line-height:1.85; text-align:center;}}
  .bundle-grid{{display:grid; grid-template-columns:repeat(3,1fr); gap:26px;}}
  .bundle-col{{border:1px solid var(--line); border-radius:8px; padding:20px 20px 22px; background:#fff;}}
  .bundle-col h3{{font-size:15px; margin-bottom:14px; border-bottom:2px solid var(--gold); padding-bottom:8px;}}
  .bundle-block + .bundle-block{{margin-top:18px;}}
  .bundle-block-head{{font-size:11px; text-transform:uppercase; letter-spacing:.08em; color:var(--ink-soft); font-weight:700; margin-bottom:6px;}}
  table.bundle-table{{width:100%; border-collapse:collapse; font-size:13px;}}
  table.bundle-table td{{padding:7px 4px; border-bottom:1px solid var(--line);}}
  table.bundle-table td.pr{{font-weight:800; text-align:right; white-space:nowrap;}}
  table.bundle-table tr.preferred{{background:var(--cream-soft);}}
  .pref-badge{{display:inline-block; font-size:9px; font-weight:800; letter-spacing:.04em; text-transform:uppercase; color:var(--gold-text); background:var(--cream-soft); border:1px solid var(--gold); border-radius:20px; padding:1px 7px; margin-left:6px; vertical-align:middle;}}
  tr.preferred .pref-badge{{background:#fff;}}
  @media (max-width:900px){{.bundle-grid{{grid-template-columns:1fr;}}}}
"""

def bundle_row(visits, price, pref, badge_label):
    badge = f' <span class="pref-badge">{badge_label}</span>' if pref else ""
    row_cls = "preferred" if pref else ""
    return f'<tr class="{row_cls}"><td class="pkg">{visits}{badge}</td><td class="pr">{price}</td></tr>'

def bundle_col(title, blocks, badge_label="Most Preferred"):
    block_html = ""
    for dur_label, rows in blocks:
        rows_html = "".join(bundle_row(visits, price, pref, badge_label) for visits, price, pref in rows)
        block_html += f'<div class="bundle-block"><div class="bundle-block-head">{dur_label}</div><table class="bundle-table">{rows_html}</table></div>'
    return f'<div class="bundle-col"><h3>{title}</h3>{block_html}</div>'

pref_label = "Most Preferred"
pref_label_th = "ยอดนิยมที่สุด"

BUNDLE_SIGNATURE = [
    ("60 min · Choose 2 of 3: Hair / Ear / Facial", [("3 Visits", "13,200 THB", False), ("5 Visits", "21,500 THB", True), ("10 Visits", "41,000 THB", False)]),
    ("90 min · Full Course: Hair + Ear + Facial", [("3 Visits", "15,900 THB", False), ("5 Visits", "25,000 THB", True), ("10 Visits", "50,000 THB", False)]),
]
BUNDLE_AROMATHERAPY = [
    ("60 min", [("3 Visits", "15,900 THB", False), ("5 Visits", "25,000 THB", True), ("10 Visits", "50,000 THB", False)]),
    ("90 min", [("3 Visits", "21,300 THB", False), ("5 Visits", "35,000 THB", True), ("10 Visits", "65,000 THB", False)]),
]
BUNDLE_THAI = [
    ("60 min", [("3 Visits", "10,800 THB", False), ("5 Visits", "17,500 THB", True), ("10 Visits", "33,000 THB", False)]),
    ("90 min", [("3 Visits", "11,800 THB", False), ("5 Visits", "19,500 THB", True), ("10 Visits", "36,000 THB", False)]),
]

BUNDLE_SIGNATURE_TH = [
    ("60 นาที · เลือก 2 ใน 3: ผม / หู / ใบหน้า", [("3 ครั้ง", "13,200 บาท", False), ("5 ครั้ง", "21,500 บาท", True), ("10 ครั้ง", "41,000 บาท", False)]),
    ("90 นาที · คอร์สเต็ม: ผม + หู + ใบหน้า", [("3 ครั้ง", "15,900 บาท", False), ("5 ครั้ง", "25,000 บาท", True), ("10 ครั้ง", "50,000 บาท", False)]),
]
BUNDLE_AROMATHERAPY_TH = [
    ("60 นาที", [("3 ครั้ง", "15,900 บาท", False), ("5 ครั้ง", "25,000 บาท", True), ("10 ครั้ง", "50,000 บาท", False)]),
    ("90 นาที", [("3 ครั้ง", "21,300 บาท", False), ("5 ครั้ง", "35,000 บาท", True), ("10 ครั้ง", "65,000 บาท", False)]),
]
BUNDLE_THAI_TH = [
    ("60 นาที", [("3 ครั้ง", "10,800 บาท", False), ("5 ครั้ง", "17,500 บาท", True), ("10 ครั้ง", "33,000 บาท", False)]),
    ("90 นาที", [("3 ครั้ง", "11,800 บาท", False), ("5 ครั้ง", "19,500 บาท", True), ("10 ครั้ง", "36,000 บาท", False)]),
]

def bundle_section_en():
    grid = (bundle_col("Zenva Signature Spa", BUNDLE_SIGNATURE)
            + bundle_col("Aromatherapy Massage", BUNDLE_AROMATHERAPY)
            + bundle_col("Thai Authentic Spa", BUNDLE_THAI))
    return f"""<section class="section" id="bundles" style="background:var(--cream-soft);">
  <div class="menu-block" style="margin-bottom:0;">
    <div class="section-head"><span class="eyebrow">Save With a Pass</span><h2>Multi-Visit Bundle Passes</h2></div>
    <p class="bundle-intro">Prefer to make it a habit? Each bundle pairs a Private Onsen room with the treatment below, at a lower per-visit rate the more you book. Passes are valid for 1 year from the date of purchase.</p>
    <div class="bundle-grid">{grid}</div>
  </div>
</section>"""

def bundle_section_th():
    grid = (bundle_col("Zenva Signature Spa", BUNDLE_SIGNATURE_TH, pref_label_th)
            + bundle_col("นวดอโรมาเธอราพี", BUNDLE_AROMATHERAPY_TH, pref_label_th)
            + bundle_col("Thai Authentic Spa", BUNDLE_THAI_TH, pref_label_th))
    return f"""<section class="section" id="bundles" style="background:var(--cream-soft);">
  <div class="menu-block" style="margin-bottom:0;">
    <div class="section-head"><span class="eyebrow">ประหยัดกว่าด้วยแพ็กเกจ</span><h2>แพ็กเกจหลายครั้ง</h2></div>
    <p class="bundle-intro">อยากกลับมาอีกหรือ? แพ็กเกจแต่ละชุดรวมห้องออนเซ็นส่วนตัวกับทรีตเมนต์ด้านล่าง ยิ่งจองมากครั้ง ยิ่งคุ้มกว่าต่อครั้ง แพ็กเกจมีอายุการใช้งาน 1 ปีนับจากวันที่ซื้อ</p>
    <div class="bundle-grid">{grid}</div>
  </div>
</section>"""

# Reusable table/couple-pair/spa-grid CSS, shared by couples-spa-bangkok.html
# and massage-spa-bangkok.html below (both render couple_table()/spa_col()
# markup, which this page no longer does).
TABLE_GRID_CSS = """
  table.menu-table{{width:100%; border-collapse:collapse; font-size:13.5px;}}
  table.menu-table th{{text-align:left; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--ink-soft); font-weight:700; padding:0 10px 10px; border-bottom:2px solid var(--gold);}}
  table.menu-table td{{padding:11px 10px; border-bottom:1px solid var(--line); vertical-align:top;}}
  table.menu-table td.pkg{{font-weight:700;}}
  table.menu-table td.dur{{color:var(--ink-soft); white-space:nowrap;}}
  table.menu-table td.pr{{font-weight:800; text-align:right; white-space:nowrap;}}
  .couple-pair{{display:grid; grid-template-columns:1fr 1fr; gap:36px;}}
  .couple-pair h3{{font-size:14px; margin-bottom:12px; display:flex; align-items:center; gap:8px;}}
  .swatch{{width:11px; height:11px; border-radius:50%; display:inline-block;}}
  .swatch.bonsai{{background:var(--bonsai);}}
  .swatch.sakura{{background:var(--sakura);}}
  .spa-grid{{display:grid; grid-template-columns:repeat(3,1fr); gap:26px;}}
  .spa-col h3{{font-size:14px; margin-bottom:12px; border-bottom:2px solid var(--gold); padding-bottom:8px;}}
  .spa-col table.menu-table td{{padding:9px 4px;}}
  .spa-col-note{{font-size:12px; color:var(--ink-soft); margin-top:10px; padding-top:10px; border-top:1px dashed var(--line); line-height:1.6;}}
  .vat-note{{text-align:center; font-size:12.5px; color:var(--ink-soft); margin-top:-40px; margin-bottom:60px;}}
  .spa-photo-row{{grid-template-columns:repeat(3,1fr);}}
  @media (max-width:900px){{.couple-pair, .spa-grid{{grid-template-columns:1fr;}} .spa-photo-row{{grid-template-columns:1fr 1fr; gap:10px;}} .spa-photo-row > div{{height:150px !important;}}}}
  @media (max-width:520px){{.spa-photo-row{{grid-template-columns:1fr;}}}}
"""

services_body = ("""
<div class="page-hero">
  <span class="eyebrow">Private Onsen Rooms</span>
  <h1>Private Onsen Rooms in Bangkok — Bonsai &amp; Sakura</h1>
  <p>Bonsai and Sakura — each a fully private room with a hot mineral-salt onsen, ice bath, and a sauna or steam room, for up to three guests.</p>
</div>
<section class="section" id="rooms">
  <div class="menu-block">
    <div class="menu-title-bar"><h2>Private Onsen</h2><span>Up to 3 Pax &middot; 60 min base</span></div>
    <div class="room-pair">
      <div class="room-card bonsai">
        <div class="photo"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"><span class="tag">Bonsai &middot; Sauna Room</span></div>
        <div class="info"><div class="desc">Ice bath, mineral salt Japanese hot onsen, Himalayan salt-wall sauna room.</div>
        <div class="price-line"><span class="amt">3,190+ THB</span><span class="dur">per room / 60 min</span></div>
        <div class="addon">Add-on: 1,000+ THB / 15 min</div></div>
      </div>
      <div class="room-card sakura">
        <div class="photo"><img src="{room_sakura}" alt="Sakura private onsen room with steam room" loading="lazy"><span class="tag">Sakura &middot; Steam Room</span></div>
        <div class="info"><div class="desc">Ice bath, mineral salt Japanese hot onsen, and steam room.</div>
        <div class="price-line"><span class="amt">3,190+ THB</span><span class="dur">per room / 60 min</span></div>
        <div class="addon">Add-on: 1,000+ THB / 15 min</div></div>
      </div>
    </div>
    <p class="room-intro">Each room is entirely private for the length of your booking &mdash; no shared bathhouse, no communal schedule. A hot mineral-salt onsen bath is paired with a separate ice bath for contrast bathing (alternating hot and cold), plus either a Himalayan salt-wall sauna (Bonsai) or a steam room (Sakura). Sessions run from 60 minutes and extend in 15-minute increments; both rooms comfortably hold up to three guests. New to hot-cold contrast bathing, or wondering whether it's right for you? Our <a href="contrast-therapy-ice-bath-bangkok.html">Contrast Therapy, Ice Bath &amp; Sauna</a> page covers how a session is structured, and our <a href="blog-contrast-therapy.html">Journal guide to contrast therapy</a> goes deeper on the reported benefits and who should check with a doctor first.</p>
  </div>
</section>
""" + bundle_section_en() + """
<p class="vat-note">All prices are subject to 7% VAT.</p>
<section class="section">
  <div class="section-head"><span class="eyebrow">Continue Exploring</span><h2>Plan Your Visit</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{menu_card_onsen}" alt="Guest relaxing against the glowing Himalayan salt wall inside the private sauna" loading="lazy"></div><div class="body"><h4>Contrast Therapy, Ice Bath &amp; Sauna</h4><p>The full hot-cold contrast ritual, explained in depth.</p><div class="price-tag">From 3,190+ THB</div><a href="contrast-therapy-ice-bath-bangkok.html">Learn more &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="Therapist giving a massage in a private treatment room" loading="lazy"></div><div class="body"><h4>Couples Spa Experience</h4><p>Onsen + massage packages built for two.</p><div class="price-tag">From 4,900+ THB</div><a href="couples-spa-bangkok.html">See packages &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{hero}" alt="Private onsen room at Zenva" loading="lazy"></div><div class="body"><h4>Membership</h4><p>Silver, Gold, Diamond &amp; Platinum credit tiers.</p><div class="price-tag">From 10,000 THB credit</div><a href="membership.html">View tiers &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>Visit Us</h4><p>Address, opening hours, and directions.</p><a href="location-thonglor-bangkok.html">Get directions &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">Ready to Book?</span><h2 style="margin-bottom:14px;">Reserve Your Ritual</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""").format(ctas=cta_buttons(), **IMG)

services_extra_css = (services_extra_css + TABLE_GRID_CSS + BUNDLE_CSS).format()
with open("/tmp/zenva_site/onsen-spa.html", "w") as f:
    f.write(page("Private Onsen Rooms & Packages Bangkok | Zenva Thonglor", "services", services_body, services_extra_css,
                 description="Private onsen rooms in Thonglor, Bangkok — Bonsai and Sakura, each with a hot mineral-salt onsen, ice bath, and sauna or steam room. From 3,190+ THB, up to 3 guests.", path="onsen-spa.html", zh_href="zh/onsen-spa.html", th_href="th/onsen-spa.html", hero_image=IMG["room_bonsai"]))
print("onsen-spa.html v4 written (trimmed to Rooms & Packages — SEO P1-6)")

# ---------- CONTRAST THERAPY, ICE BATH & SAUNA (new — SEO P1-6) ----------
contrast_extra_css = """
  .page-hero{{padding:52px 24px 36px; text-align:center; background:var(--ink); color:var(--cream);}}
  .page-hero h1{{font-size:36px; margin-bottom:10px; color:var(--cream);}}
  .page-hero p{{color:#B8AA84; max-width:600px; margin:0 auto;}}
  .ct-body{{max-width:760px; margin:0 auto; font-size:14.5px; color:var(--ink-soft); line-height:1.9;}}
  .ct-body h2{{color:var(--ink); font-size:22px; margin:36px 0 12px;}}
  .ct-body ul{{margin:0 0 18px 20px;}}
  .ct-body li{{margin-bottom:8px;}}
  .ct-body a{{color:var(--gold-text); font-weight:700; text-decoration:none;}}
  .ct-price-card{{max-width:520px; margin:32px auto; border:1px solid var(--gold); border-radius:8px; padding:24px 26px; background:var(--cream-soft); text-align:center;}}
  .ct-price-card .amt{{font-size:30px; font-weight:800; color:var(--ink);}}
  .ct-price-card .unit{{font-size:13px; color:var(--ink-soft);}}
  .ct-callout{{background:var(--cream-soft); border-left:3px solid var(--gold); padding:16px 20px; font-size:13.5px; color:var(--ink-soft); margin:24px 0; border-radius:0 4px 4px 0;}}
  .disclaimer{{font-size:11.5px; color:var(--ink-soft); opacity:.85; margin-top:24px;}}
"""
contrast_body = """
<div class="page-hero">
  <span class="eyebrow" style="color:var(--cream);">Hot &amp; Cold</span>
  <h1>Contrast Therapy, Ice Bath &amp; Sauna in Bangkok</h1>
  <p>Hot mineral onsen, an ice bath, and a Himalayan salt-wall sauna or steam room — fully private, in one room, at your own pace.</p>
</div>
<section class="section">
  <div class="ct-body">
    <p>Contrast therapy means alternating between hot water immersion and cold exposure in the same session. At Zenva, that's built into both of our private rooms: a hot mineral-salt onsen bath paired with a separate ice bath, plus a Himalayan salt-wall sauna in the Bonsai room or a steam room in the Sakura room.</p>

    <h2>How a Session Works</h2>
    <p>There's no fixed protocol, but a simple, beginner-friendly rhythm is to warm up in the hot onsen for 8&ndash;12 minutes, move to the ice bath for 30&ndash;90 seconds, return to the hot onsen for another 8&ndash;10 minutes, and repeat 2&ndash;3 times &mdash; finishing on warm to relax, or on cold for the alerting effect. Because the room is entirely private for your booking, there's no shared schedule to work around and no one waiting on the plunge pool.</p>

    <h2>Commonly Reported Benefits</h2>
    <ul>
      <li><strong>Muscle recovery</strong> after exercise, travel, or long periods of standing or sitting.</li>
      <li><strong>A mental reset</strong> — the temperature shift is often described as clarifying and energizing.</li>
      <li><strong>Circulation</strong> — heat widens blood vessels, cold narrows them, and alternating the two is the basis of most contrast-therapy protocols.</li>
    </ul>
    <p>We keep this section deliberately measured: contrast therapy is a well-established wellness practice, not a medical treatment, and individual results vary. For the fuller explanation — including a step-by-step first-timer's guide — see our <a href="blog-contrast-therapy.html">Journal article on contrast therapy</a>.</p>

    <div class="ct-price-card">
      <div class="amt">3,190+ THB</div>
      <div class="unit">per room &middot; 60 min &middot; up to 3 guests &middot; add-on 1,000+ THB / 15 min</div>
    </div>

    <div class="ct-callout">Contrast therapy is not recommended for everyone. If you have a cardiovascular condition, are pregnant, or have a history of severe migraines, speak with a doctor before trying hot-cold immersion, and mention it to our front desk when you book so we can advise on room and duration.</div>

    <h2>Pairing It With Spa Treatments</h2>
    <p>A hot-cold cycle leaves muscles warm and receptive to bodywork, which is why our couple and solo packages finish an onsen session with an aromatherapy or Thai massage rather than treating the two as separate visits. See the full <a href="onsen-spa.html">Private Onsen Rooms &amp; Packages</a>, or the standalone <a href="massage-spa-bangkok.html">Massage &amp; Spa Treatments</a> menu.</p>

    <p class="disclaimer">This page is educational and general in nature and is not medical advice. If you have a pre-existing health condition, consult a physician before beginning any hot-cold contrast practice.</p>
  </div>
</section>
<section class="section">
  <div class="section-head"><span class="eyebrow">Continue Exploring</span><h2>Plan Your Visit</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"></div><div class="body"><h4>Private Onsen Rooms</h4><p>Bonsai &amp; Sakura room details and full pricing.</p><div class="price-tag">From 3,190+ THB</div><a href="onsen-spa.html">Book a room &rarr;</a></div></div>
    <div class="crosslink-card no-thumb"><div class="body"><h4>Contrast Therapy Guide</h4><p>The educational deep-dive on our Journal.</p><a href="blog-contrast-therapy.html">Read the guide &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="Therapist giving a massage in a private treatment room" loading="lazy"></div><div class="body"><h4>Couples Spa Experience</h4><p>Share the ritual — onsen + massage for two.</p><div class="price-tag">From 4,900+ THB</div><a href="couples-spa-bangkok.html">See packages &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>Visit Us</h4><p>Address, opening hours, and directions.</p><a href="location-thonglor-bangkok.html">Get directions &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">Ready to Book?</span><h2 style="margin-bottom:14px;">Reserve Your Ritual</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons(), **IMG)

contrast_extra_css = contrast_extra_css.format()
with open("/tmp/zenva_site/contrast-therapy-ice-bath-bangkok.html", "w") as f:
    f.write(page("Ice Bath & Contrast Therapy Bangkok | Zenva Private Onsen", "services", contrast_body, contrast_extra_css,
                 description="Hot onsen, ice bath, and sauna or steam room, fully private, in Thonglor, Bangkok. Book a contrast-therapy session at Zenva — from 3,190 THB.", path="contrast-therapy-ice-bath-bangkok.html", th_href="th/contrast-therapy-ice-bath-bangkok.html", og_image=IMG["water"]))
print("contrast-therapy-ice-bath-bangkok.html v4 written (new — SEO P1-6)")

# ---------- COUPLES SPA EXPERIENCE (new — SEO P1-6) ----------
couples_extra_css = """
  .page-hero{{padding:52px 24px 36px; text-align:center; background:var(--cream-soft); border-bottom:1px solid var(--line);}}
  .page-hero h1{{font-size:36px; margin-bottom:8px;}}
  .page-hero p{{color:var(--ink-soft); max-width:560px; margin:0 auto;}}
  .menu-block{{max-width:1040px; margin:0 auto 50px;}}
""" + TABLE_GRID_CSS
couples_body = ("""
<div class="page-hero">
  <span class="eyebrow">For Two</span>
  <h1>A Private Onsen &amp; Spa Experience for Two — Bangkok</h1>
  <p>Share a private hot onsen and ice bath, then unwind together with massage — in the Bonsai or Sakura room, entirely your own for the visit.</p>
</div>
<section class="section" id="couple">
  <p style="max-width:700px; margin:0 auto 34px; text-align:center; font-size:14px; color:var(--ink-soft); line-height:1.8;">Each Couple Onsen Package combines a private room's hot mineral-salt onsen and ice bath with a massage treatment for two, in either the Bonsai (sauna) or Sakura (steam) room. Add-on massage options and durations are the same across both rooms.</p>
  <div class="menu-block">
    <div class="couple-pair">
      """ + couple_table("bonsai", "Bonsai Sauna", bonsai_packages) + couple_table("sakura", "Sakura Steam", sakura_packages) + """
    </div>
  </div>
</section>
<p class="vat-note">All prices are subject to 7% VAT.</p>
<section class="section">
  <div class="section-head"><span class="eyebrow">Continue Exploring</span><h2>Plan Your Visit</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"></div><div class="body"><h4>Private Onsen Rooms</h4><p>Full room details, capacity &amp; base pricing.</p><div class="price-tag">From 3,190+ THB</div><a href="onsen-spa.html">See rooms &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{hero}" alt="Private onsen room at Zenva" loading="lazy"></div><div class="body"><h4>Membership</h4><p>Silver, Gold, Diamond &amp; Platinum credit tiers.</p><div class="price-tag">From 10,000 THB credit</div><a href="membership.html">View tiers &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{signature_card}" alt="Zenva signature spa treatment tray" loading="lazy"></div><div class="body"><h4>Massage &amp; Spa Treatments</h4><p>Standalone treatments, priced separately.</p><div class="price-tag">From 590+ THB</div><a href="massage-spa-bangkok.html">See menu &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>Visit Us</h4><p>Address, opening hours, and directions.</p><a href="location-thonglor-bangkok.html">Get directions &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">Ready to Book?</span><h2 style="margin-bottom:14px;">Reserve Your Ritual</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""").format(ctas=cta_buttons(), **IMG)

couples_extra_css = couples_extra_css.format()
with open("/tmp/zenva_site/couples-spa-bangkok.html", "w") as f:
    f.write(page("Couples Spa Bangkok | Private Onsen for Two — Zenva Thonglor", "services", couples_body, couples_extra_css,
                 description="Share a private hot onsen and ice bath, then unwind together with massage — Zenva's Couple Onsen Package in Thonglor, Bangkok.", path="couples-spa-bangkok.html", th_href="th/couples-spa-bangkok.html", og_image=IMG["massage"]))
print("couples-spa-bangkok.html v4 written (new — SEO P1-6)")

# ---------- MASSAGE & SPA TREATMENTS (new — SEO P1-6) ----------
massage_page_extra_css = """
  .page-hero{{padding:52px 24px 36px; text-align:center; background:var(--cream-soft); border-bottom:1px solid var(--line);}}
  .page-hero h1{{font-size:36px; margin-bottom:8px;}}
  .page-hero p{{color:var(--ink-soft); max-width:560px; margin:0 auto;}}
  .menu-block{{max-width:1040px; margin:0 auto 50px;}}
  .room-pair{{display:grid; grid-template-columns:1fr 1fr; gap:22px;}}
""" + TABLE_GRID_CSS
massage_page_body = ("""
<div class="page-hero">
  <span class="eyebrow">Standalone Treatments</span>
  <h1>Massage &amp; Spa Treatments in Thonglor, Bangkok</h1>
  <p>Luxury aromatherapy, traditional Thai massage, and Zenva's Signature Vietnamese-inspired spa rituals &mdash; no onsen room required.</p>
</div>
<section class="section" id="spa">
  <div class="menu-block">
    <div class="room-pair spa-photo-row" style="margin-bottom:26px;">
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{massage_card}" alt="Therapist performing an aromatherapy massage" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;"></div>
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{chair_card}" alt="Guest reclining in a premium massage chair, streaming entertainment on a personal screen" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center 25%;"></div>
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{vietnamese_card}" alt="Traditional Vietnamese ear-cleaning treatment, part of the 18-Steps Zenva Spa" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;"></div>
    </div>
    <div class="spa-grid">
      """ + spa_col("Luxury Spa", luxury_rows) + spa_col("Thai Authentic Spa", thai_rows,
          note="Settle into one of our premium massage chairs with a personal screen, so you can stream your own entertainment while you relax.") \
        + spa_col("Zenva Signature Spa", signature_rows) + """
    </div>
    <p style="max-width:700px; margin:26px auto 0; font-size:13px; color:var(--ink-soft); line-height:1.8; text-align:center;">Not sure whether Thai or aromatherapy massage suits you? Our Journal compares them side by side in <a href="blog-thai-vs-aromatherapy-massage.html" style="color:var(--gold-text); font-weight:700; text-decoration:none;">Thai Massage vs. Aromatherapy Massage</a>.</p>
  </div>
</section>
<p class="vat-note">All prices are subject to 7% VAT.</p>
<section class="section">
  <div class="section-head"><span class="eyebrow">Continue Exploring</span><h2>Plan Your Visit</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"></div><div class="body"><h4>Private Onsen Rooms</h4><p>Pair any treatment with a hot onsen &amp; ice bath.</p><div class="price-tag">From 3,190+ THB</div><a href="onsen-spa.html">See rooms &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{hero}" alt="Private onsen room at Zenva" loading="lazy"></div><div class="body"><h4>Membership</h4><p>Silver, Gold, Diamond &amp; Platinum credit tiers.</p><div class="price-tag">From 10,000 THB credit</div><a href="membership.html">View tiers &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="Therapist giving a massage in a private treatment room" loading="lazy"></div><div class="body"><h4>Couples Spa Experience</h4><p>Onsen + massage packages built for two.</p><div class="price-tag">From 4,900+ THB</div><a href="couples-spa-bangkok.html">See packages &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>Visit Us</h4><p>Address, opening hours, and directions.</p><a href="location-thonglor-bangkok.html">Get directions &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">Ready to Book?</span><h2 style="margin-bottom:14px;">Reserve Your Ritual</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""").format(ctas=cta_buttons(), **IMG)

massage_page_extra_css = massage_page_extra_css.format()
with open("/tmp/zenva_site/massage-spa-bangkok.html", "w") as f:
    f.write(page("Aromatherapy & Thai Massage Bangkok | Zenva Spa, Thonglor", "services", massage_page_body, massage_page_extra_css,
                 description="Aromatherapy massage, traditional Thai massage, and Zenva's Signature Vietnamese-inspired spa treatments — Thonglor, Bangkok. From 590 THB.", path="massage-spa-bangkok.html", th_href="th/massage-spa-bangkok.html", og_image=IMG["signature"]))
print("massage-spa-bangkok.html v4 written (new — SEO P1-6)")

# ---------- VISIT US — LOCATION & HOURS (new — SEO P1-6) ----------
# NAP note: street/soi number and postal code are NOT included below because
# they haven't been supplied — the client was asked (2026-08-24) and chose to
# were previously not on file; client supplied the full street address on
# 2026-08-27 ("FL 03-01 251/1 Thong Lo 13 Alley, Khlong Tan Nuea, Watthana,
# Bangkok 10110"), now used sitewide (footer, schema, this page, privacy
# policy, Thai equivalents). Precise lat/long "geo" is still not on file.
location_extra_css = """
  .page-hero{{padding:52px 24px 36px; text-align:center; background:var(--cream-soft); border-bottom:1px solid var(--line);}}
  .page-hero h1{{font-size:36px; margin-bottom:8px;}}
  .page-hero p{{color:var(--ink-soft); max-width:560px; margin:0 auto;}}
  .nap-grid{{display:grid; grid-template-columns:1fr 1fr; gap:48px; max-width:1000px; margin:0 auto 40px; align-items:start;}}
  .nap-block h3{{font-size:13px; text-transform:uppercase; letter-spacing:.08em; color:var(--ink-soft); margin-bottom:8px;}}
  .nap-block p{{font-size:15px; color:var(--ink); margin-bottom:18px; line-height:1.7;}}
  .nap-block a{{color:var(--gold-text); font-weight:700; text-decoration:none;}}
  @media (max-width:800px){{.nap-grid{{grid-template-columns:1fr;}}}}
"""
location_body = """
<div class="page-hero">
  <span class="eyebrow">Thonglor, Bangkok</span>
  <h1>Visit Zenva &mdash; Thonglor, Bangkok</h1>
  <p>Full address, opening hours, and directions for Zenva Private Onsen &amp; Spa.</p>
</div>
<section class="section">
  <div class="nap-grid">
    <div class="nap-block">
      <h3>Address</h3>
      <p>Zenva &mdash; Private Onsen &amp; Spa<br>SEENSPACE Thonglor, FL 03-01<br>251/1 Thong Lo 13 Alley, Khlong Tan Nuea, Watthana<br>Bangkok 10110, Thailand</p>
      <h3>Opening Hours</h3>
      <p>Open daily, 12:00&ndash;00:00</p>
      <h3>Contact &amp; Booking</h3>
      <p>Call: <a href="tel:+66802629191">+66 80 262 9191</a><br>Or book directly via LINE or WhatsApp below.</p>
      <a class="btn-outline" href="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor" target="_blank" rel="noopener">Get Directions &rarr;</a>
    </div>
    <div class="nap-block">
      <h3>Getting Here</h3>
      <p>Seenspace Thonglor is walkable from BTS Thong Lo, with the Skytrain generally a reliable way to reach the area if road traffic looks heavy &mdash; Bangkok traffic on nearby roads like Sukhumvit runs heaviest roughly 7:30&ndash;9:30am and 5:00&ndash;7:30pm. Booking outside those windows, or building in extra travel time, makes it easier to arrive unrushed.</p>
    </div>
  </div>
  <div style="max-width:1100px; margin:0 auto; border-radius:8px; overflow:hidden; border:1px solid var(--line);">
    <iframe src="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor&output=embed" width="100%" height="360" style="border:0; display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Zenva location map"></iframe>
  </div>
</section>
<section class="section">
  <div class="section-head"><span class="eyebrow">Continue Exploring</span><h2>Explore Zenva</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"></div><div class="body"><h4>Private Onsen Rooms</h4><p>Bonsai &amp; Sakura room details and pricing.</p><div class="price-tag">From 3,190+ THB</div><a href="onsen-spa.html">See rooms &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{menu_card_onsen}" alt="Guest relaxing against the glowing Himalayan salt wall inside the private sauna" loading="lazy"></div><div class="body"><h4>Contrast Therapy, Ice Bath &amp; Sauna</h4><p>How a hot-cold session works.</p><div class="price-tag">From 3,190+ THB</div><a href="contrast-therapy-ice-bath-bangkok.html">Learn more &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="Therapist giving a massage in a private treatment room" loading="lazy"></div><div class="body"><h4>Couples Spa Experience</h4><p>Onsen + massage packages for two.</p><div class="price-tag">From 4,900+ THB</div><a href="couples-spa-bangkok.html">See packages &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{signature_card}" alt="Zenva signature spa treatment tray" loading="lazy"></div><div class="body"><h4>Massage &amp; Spa Treatments</h4><p>Standalone treatments, from 590+ THB.</p><div class="price-tag">From 590+ THB</div><a href="massage-spa-bangkok.html">See menu &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">Ready to Book?</span><h2 style="margin-bottom:14px;">Reserve Your Ritual</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons(), **IMG)

location_extra_css = location_extra_css.format()
with open("/tmp/zenva_site/location-thonglor-bangkok.html", "w") as f:
    f.write(page("Visit Us — Zenva Private Onsen & Spa, Thonglor Bangkok", "location", location_body, location_extra_css,
                 description="Zenva Private Onsen & Spa, 251/1 Thong Lo 13 Alley, Khlong Tan Nuea, Watthana, Bangkok 10110. Opening hours, directions from BTS Thong Lo, and how to book.", path="location-thonglor-bangkok.html", th_href="th/location-thonglor-bangkok.html", og_image=IMG["reception"]))
print("location-thonglor-bangkok.html v4 written (new — SEO P1-6)")

# ---------- MEMBERSHIP ----------
membership_extra_css = """
  .page-hero{{padding:56px 24px 40px; text-align:center; background:var(--ink); color:var(--cream);}}
  .page-hero h1{{font-size:38px; margin-bottom:10px; color:var(--cream);}}
  .page-hero p{{color:#B8AA84; max-width:520px; margin:0 auto;}}
  .tier-cards{{display:grid; grid-template-columns:repeat(4,1fr); gap:20px; max-width:1200px; margin:0 auto;}}
  .tier{{border:1px solid var(--line); border-radius:6px; padding:28px 22px; display:flex; flex-direction:column; gap:12px; background:#fff; position:relative;}}
  .tier.tier-platinum{{border-color:var(--gold); background:var(--cream-soft);}}
  .tier .tier-name{{font-family:var(--font-display); font-size:21px;}}
  .tier .tier-badge{{font-size:9.5px; letter-spacing:.12em; text-transform:uppercase; font-weight:700; color:var(--ink-soft);}}
  .tier .pay-row{{font-size:12.5px; color:var(--ink-soft); font-weight:600; margin-top:2px;}}
  .tier .regular-price{{font-size:15px; color:var(--ink-soft); font-weight:600;}}
  .tier .regular-price .amount{{font-size:26px; color:var(--ink); font-weight:800;}}
  .tier .regular-line{{font-size:12.5px; color:var(--ink-soft);}}
  .tier .regular-line s{{opacity:.7;}}
  .promo-box{{background:linear-gradient(160deg, var(--cream-soft) 0%, #fff 100%); border:1px solid var(--gold); border-radius:8px; padding:16px 16px 14px; margin-top:2px;}}
  .promo-flag{{background:var(--gold); color:#fff; font-size:10px; font-weight:800; letter-spacing:.07em; text-transform:uppercase; padding:4px 9px; border-radius:3px; display:inline-block; width:fit-content; margin-bottom:10px;}}
  .promo-amount{{font-size:30px; font-weight:800; color:var(--gold-text); line-height:1.1;}}
  .promo-amount .unit{{font-size:14px; font-weight:600; color:var(--ink-soft);}}
  .promo-bonus{{display:inline-block; margin-top:8px; background:var(--ink); color:var(--cream); font-size:11px; font-weight:700; padding:4px 10px; border-radius:20px;}}
  .best-value{{position:absolute; top:-11px; right:18px; background:var(--ink); color:var(--cream); font-size:9.5px; letter-spacing:.08em; font-weight:700; padding:4px 10px; border-radius:3px;}}
  .tier ul{{list-style:none; font-size:12.5px; color:var(--ink-soft); display:flex; flex-direction:column; gap:6px; margin-top:8px; border-top:1px solid var(--line); padding-top:14px;}}
  .tier ul li:before{{content:"— "; color:var(--gold-text);}}
  @media (max-width:900px){{.tier-cards{{grid-template-columns:1fr 1fr;}}}}
"""

def tier(name, pay, regular_amt, regular_bonus, promo_amt=None, promo_bonus=None, best=False, platinum=False):
    cls = "tier tier-platinum" if platinum else "tier"
    best_html = '<span class="best-value">Best Value</span>' if best else ""
    if promo_amt:
        price_block = f"""
        <div class="regular-line">Regular value: <s>{regular_amt} credits ({regular_bonus})</s></div>
        <div class="promo-box">
          <span class="promo-flag">Limited-Time Upgrade</span>
          <div class="promo-amount">{promo_amt} <span class="unit">credits</span></div>
          <span class="promo-bonus">{promo_bonus}</span>
        </div>
        """
    else:
        price_block = f"""<div class="regular-price"><span class="amount">{regular_amt}</span> credits <span style="font-weight:400;">({regular_bonus})</span></div>"""
    return f"""<div class="{cls}">{best_html}
      <span class="tier-badge">{name} Tier</span>
      <span class="tier-name">{name}</span>
      <div class="pay-row">Pay {pay} THB</div>
      {price_block}
      <ul><li>Redeemable across all onsen, spa &amp; massage services</li><li>Valid 12 months</li><li>Non-transferable</li></ul>
    </div>"""

membership_body = """
<div class="page-hero">
  <span class="eyebrow" style="color:var(--cream);">Wellness Privilege</span>
  <h1>Membership</h1>
  <p>Regular credit value on every tier, with the current limited-time promotional upgrade shown separately.</p>
</div>
<section class="section">
  <div class="tier-cards">
    """ + tier("Silver", "10,000", "11,000", "+1,000 bonus", promo_amt="13,000", promo_bonus="+3,000 bonus") + \
        tier("Gold", "30,000", "36,000", "+6,000 bonus", promo_amt="45,000", promo_bonus="+15,000 bonus") + \
        tier("Diamond", "50,000", "65,000", "+15,000 bonus") + \
        tier("Platinum", "100,000", "150,000", "+50,000 bonus", best=True, platinum=True) + """
  </div>
</section>
<section class="section" style="background:var(--cream-soft);">
  <div class="section-head"><span class="eyebrow">Terms</span><h2>Membership Terms</h2></div>
  <div style="max-width:700px; margin:0 auto; font-size:13.5px; color:var(--ink-soft); line-height:1.9;">
    Credits can be used for all Zenva services. Credits are non-transferable and non-refundable. Membership is valid for 12 months from the date of purchase and must be used before the expiration date. Credits cannot be exchanged for cash. Zenva reserves the right to amend these terms without prior notice.
  </div>
</section>
<section class="section">
  <div class="section-head"><span class="eyebrow">Continue Exploring</span><h2>Use Your Credits</h2></div>
  <div class="crosslink-grid" style="grid-template-columns:repeat(2,1fr); max-width:640px;">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"></div><div class="body"><h4>Private Onsen Rooms</h4><p>Redeem credits on Bonsai or Sakura.</p><div class="price-tag">From 3,190+ THB</div><a href="onsen-spa.html">See rooms &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>Visit Us</h4><p>Address, opening hours, and directions.</p><a href="location-thonglor-bangkok.html">Get directions &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center;">
  <span class="eyebrow">Begin Your Membership</span><h2 style="margin-bottom:14px;">Ask Our Front Desk</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons(), **IMG)

membership_extra_css = membership_extra_css.format()
with open("/tmp/zenva_site/membership.html", "w") as f:
    f.write(page("Membership | Zenva Private Onsen & Spa, Bangkok", "membership", membership_body, membership_extra_css,
                 description="Zenva membership credit tiers — Silver, Gold, Diamond, and Platinum — redeemable across all private onsen, spa, and massage services in Bangkok.", path="membership.html", zh_href="zh/membership.html", th_href="th/membership.html"))
print("membership.html v4 written")

# ---------- ZH (SIMPLIFIED CHINESE) PREVIEW BUILD ----------
# PREVIEW ONLY — not yet client/native-speaker approved. Built now at the
# client's request so the translation can be reviewed in context (the actual
# page layout) rather than only as a side-by-side docx table. Content is the
# same wording delivered in zenva_zh_translation_review.docx, including the
# finalized 静荟 club identity / 银·初见·金·随心·钻·臻境·铂·忘尘 tier names.
# See master-brief.md — native-speaker review is still recommended before
# this goes live on the real domain.
os.makedirs("/tmp/zenva_site/zh", exist_ok=True)

def tier_zh(badge_en, name_zh, pay, regular_amt, regular_bonus_zh, promo_amt=None, promo_bonus_zh=None, best=False, platinum=False):
    cls = "tier tier-platinum" if platinum else "tier"
    best_html = '<span class="best-value">超值之选</span>' if best else ""
    if promo_amt:
        price_block = f"""
        <div class="regular-line">常规价值：<s>{regular_amt}泰铢储值额度（{regular_bonus_zh}）</s></div>
        <div class="promo-box">
          <span class="promo-flag">限时升级优惠</span>
          <div class="promo-amount">{promo_amt} <span class="unit">泰铢储值额度</span></div>
          <span class="promo-bonus">{promo_bonus_zh}</span>
        </div>
        """
    else:
        price_block = f"""<div class="regular-price"><span class="amount">{regular_amt}</span> 泰铢储值额度 <span style="font-weight:400;">（{regular_bonus_zh}）</span></div>"""
    return f"""<div class="{cls}">{best_html}
      <span class="tier-badge">{badge_en}</span>
      <span class="tier-name">{name_zh}</span>
      <div class="pay-row">支付 {pay} 泰铢</div>
      {price_block}
      <ul><li>可于所有温泉、SPA与按摩服务中使用</li><li>有效期12个月</li><li>不可转让</li></ul>
    </div>"""

zh_index_body = """
<section class="hero-carousel">
  <div class="hero-track">
    <div class="hero-slide">
      <div class="hero-bg" style="background-image:url('{hero}');" role="img" aria-label="Private onsen room with a guest seated at the edge of the hot bath"></div><div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">冷热交替疗法 &middot; 身心焕活</span>
        <h1>热汤温泉，冰浴冷疗——专属私享，焕活身心的极致体验。</h1>
        <p class="sub">在矿物温泉的暖热与冰浴的冷冽之间交替——这项冷热交替疗法有助于缓解肌肉疲劳与精神疲惫，再搭配招牌SPA护理，带来更深层的身心焕活体验。全程私密独立，最多可供三位宾客共享。</p>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
  </div>
</section>
<div class="why-strip">
  <div class="section-head" style="margin-bottom:34px;">
    <span class="eyebrow">静谧哲学</span>
  </div>
  <div class="why-grid">
    <div class="why-item"><span class="why-num">冷与热</span><h3>冷热交替疗法，用心以待</h3><p>矿物温泉的暖热与冰浴的冷冽，同处一间私密房间之中——这项焕活仪式正重新受到全球关注，在这里，我们视其为一种专注的修行，而非噱头。</p></div>
    <div class="why-item"><span class="why-num">私密</span><h3>只属于您</h3><p>没有共用浴场，没有排队等候。每间房都完全属于您——无论是两人时光，还是最多三位亲友共享。</p></div>
    <div class="why-item"><span class="why-num">工艺</span><h3>静谧而讲究的细节</h3><p>真正的矿物盐水与臻选材质，一切选择只为真实的焕活效果，而非为了迎合镜头。</p></div>
  </div>
</div>
<section class="section" id="menu">
  <div class="section-head"><span class="eyebrow">探索</span><h2>服务项目</h2><p>三大服务类别——完整菜单与价目请见「温泉与SPA」页面</p></div>
  <div class="cards">
    <div class="card">
      <div class="thumb"><img src="{menu_card_onsen}" alt="Guest relaxing against the glowing Himalayan salt wall inside the private sauna" loading="lazy"></div>
      <div class="body"><span class="kicker">冷热交替疗法</span><h3>私人温泉房</h3>
      <p>盆景房（桑拿房）与樱花房（蒸汽房）——冰浴、矿物温泉、喜马拉雅盐晶桑拿。最多可供3位宾客使用。</p>
      <div class="price-row"><span class="price">3,190泰铢起</span><a class="link" href="onsen-spa.html">完整菜单 &rarr;</a></div></div>
    </div>
    <div class="card">
      <div class="thumb"><img src="{massage_card}" alt="Therapist giving an aromatherapy massage" loading="lazy"></div>
      <div class="body"><span class="kicker">双人专属</span><h3>双人温泉套餐</h3>
      <p>为双人打造的温泉加按摩组合，120至150分钟的共享时光。</p>
      <div class="price-row"><span class="price">4,900泰铢起</span><a class="link" href="onsen-spa.html#couple">完整菜单 &rarr;</a></div></div>
    </div>
    <div class="card">
      <div class="thumb"><img src="{signature_card}" alt="Zenva signature spa treatment tray" loading="lazy"></div>
      <div class="body"><span class="kicker">深度焕活</span><h3>SPA与按摩系列</h3>
      <p>尊享芳香精油按摩、正宗泰式按摩，以及Zenva招牌18步越南SPA护理——涵盖头部、采耳与面部护理。</p>
      <div class="price-row"><span class="price">590泰铢起</span><a class="link" href="onsen-spa.html#spa">完整菜单 &rarr;</a></div></div>
    </div>
  </div>
</section>
<section class="section" style="background:var(--cream-soft); padding-top:76px; padding-bottom:76px;" id="location">
  <div class="split">
    <div class="photo"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div>
    <div><span class="eyebrow">我们的空间</span><h2>静谧雅境，只属于您</h2>
    <p>每一次到访都从同样的仪式开始——私密的房间、私密的疗程，没有共用等候区。坐落于Seenspace Thonglor 3楼。</p>
    <p style="color:var(--ink-soft); font-size:14px; margin-bottom:18px;">每日营业，12:00&ndash;00:00</p>
    <a class="btn-outline" href="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor" target="_blank" rel="noopener">获取路线 &rarr;</a></div>
  </div>
  <div style="max-width:1100px; margin:40px auto 0; border-radius:8px; overflow:hidden; border:1px solid var(--line);">
    <iframe src="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor&output=embed" width="100%" height="320" style="border:0; display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Zenva location map"></iframe>
  </div>
</section>
<div class="mem-teaser">
  <span class="eyebrow" style="color:var(--cream);">尊享礼遇</span>
  <h2>四大会员等级</h2>
  <p>银·初见、金·随心、钻·臻境与铂·忘尘——可于所有温泉、SPA与按摩服务中使用。</p>
  <a class="btn-outline" style="color:var(--cream); border-color:var(--cream);" href="membership.html">查看会员详情 &rarr;</a>
</div>
<section class="section" id="gallery">
  <div class="section-head"><span class="eyebrow">走进Zenva</span><h2>图库</h2></div>
  <div class="gallery-grid" id="galleryGrid">
    <div class="g-item g-tall" data-full="{g1}" data-caption="Sakura steam room, after dark">
      <div class="g-bg"><img src="{g1}" alt="Sakura steam room at night, lit by warm ambient light beneath cherry blossoms" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g7}" data-caption="An evening in the Bonsai room">
      <div class="g-bg"><img src="{g7}" alt="Guest seated at the edge of the Bonsai onsen bath among the greenery" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g2}" data-caption="A session in progress">
      <div class="g-bg"><img src="{g2}" alt="Therapist performing a treatment in a private room" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g3}" data-caption="Ear-candling treatment detail">
      <div class="g-bg"><img src="{g3}" alt="Ear-candling spa treatment detail" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g8}" data-caption="The Zenva welcome ritual">
      <div class="g-bg"><img src="{g8}" alt="Zenva welcome tray with branded linen and aromatherapy salts" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g4}" data-caption="The Zenva sign, framed by blossoms">
      <div class="g-bg"><img src="{g4}" alt="The Zenva sign framed by blossom branches at the entrance" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g5}" data-caption="Welcome tea &amp; mango sticky rice">
      <div class="g-bg"><img src="{g5}" alt="Welcome tea and mango sticky rice" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g6}" data-caption="Candlelight by the water">
      <div class="g-bg"><img src="{g6}" alt="Guest holding a candle beside the onsen water" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g9}" data-caption="Massage chairs with personal streaming">
      <div class="g-bg"><img src="{g9}" alt="Guest reclining in a premium massage chair, streaming entertainment on the personal screen" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g10}" data-caption="Into the salt-wall sauna">
      <div class="g-bg"><img src="{g10}" alt="Guest stepping into the Himalayan salt-wall sauna, silhouetted in the evening light" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g11}" data-caption="The rain shower, ready">
      <div class="g-bg"><img src="{g11}" alt="Overhead rain showerhead beside the private spa treatment bed" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
  </div>
</section>
<div class="g-lightbox" id="gLightbox">
  <span class="g-lightbox-close" id="gLightboxClose">&times;</span>
  <span class="g-lightbox-nav g-lightbox-prev" id="gLightboxPrev">&#8249;</span>
  <img id="gLightboxImg" src="" alt="">
  <span class="g-lightbox-nav g-lightbox-next" id="gLightboxNext">&#8250;</span>
</div>
<script>
(function(){{
  var items = Array.prototype.slice.call(document.querySelectorAll("#galleryGrid .g-item"));
  if(!items.length) return;
  var lb = document.getElementById("gLightbox");
  var lbImg = document.getElementById("gLightboxImg");
  var idx = 0;
  function open(i){{
    idx = i;
    lbImg.src = items[idx].getAttribute("data-full");
    lbImg.alt = items[idx].getAttribute("data-caption") || "";
    lb.classList.add("show");
  }}
  function close(){{ lb.classList.remove("show"); lbImg.src = ""; }}
  function step(d){{ idx = (idx + d + items.length) % items.length; lbImg.src = items[idx].getAttribute("data-full"); lbImg.alt = items[idx].getAttribute("data-caption") || ""; }}
  items.forEach(function(el, i){{ el.addEventListener("click", function(){{ open(i); }}); }});
  document.getElementById("gLightboxClose").addEventListener("click", close);
  document.getElementById("gLightboxPrev").addEventListener("click", function(){{ step(-1); }});
  document.getElementById("gLightboxNext").addEventListener("click", function(){{ step(1); }});
  lb.addEventListener("click", function(e){{ if(e.target === lb) close(); }});
  document.addEventListener("keydown", function(e){{
    if(!lb.classList.contains("show")) return;
    if(e.key === "Escape") close();
    if(e.key === "ArrowLeft") step(-1);
    if(e.key === "ArrowRight") step(1);
  }});
}})();
</script>
<section class="section" id="reels" style="background:var(--cream-soft);">
  <div class="section-head"><span class="eyebrow">动态影像</span><h2>Zenva短片</h2><p>近距离感受Zenva，精选自我们的社交平台。</p></div>
  <div class="reels-grid" id="reelsGrid">
    <video muted loop playsinline preload="metadata">
      <source src="{reel1_webm}" type="video/webm">
      <source src="{reel1_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel3_webm}" type="video/webm">
      <source src="{reel3_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel5_webm}" type="video/webm">
      <source src="{reel5_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel6_webm}" type="video/webm">
      <source src="{reel6_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel7_webm}" type="video/webm">
      <source src="{reel7_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel8_webm}" type="video/webm">
      <source src="{reel8_mp4}" type="video/mp4">
    </video>
  </div>
</section>
<script>
(function(){{
  var vids = Array.prototype.slice.call(document.querySelectorAll("#reelsGrid video"));
  if(!vids.length) {{ return; }}
  if(!('IntersectionObserver' in window)){{
    vids.forEach(function(v){{ v.play().catch(function(){{}}); }});
  }} else {{
    var io = new IntersectionObserver(function(entries){{
      entries.forEach(function(entry){{
        if(entry.isIntersecting){{ entry.target.play().catch(function(){{}}); }}
        else {{ entry.target.pause(); }}
      }});
    }}, {{threshold: 0.25}});
    vids.forEach(function(v){{ io.observe(v); }});
  }}
}})();
</script>
<section class="section" id="reviews">
  <div class="section-head"><span class="eyebrow">宾客评价 &middot; Google评分4.8&#9733; &middot; 267条评价</span><h2>备受Google好评</h2></div>
  <div class="testimonials" id="reviewsGrid">
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>We had booked the couple's private Bonsai Sauna experience&mdash;Himalayan pink salt sauna, one of a kind place... Although it looked very aesthetic with the beautiful decor and ambient lighting&hellip;</p>
      <div class="t-foot">
        <div class="who">The Traveler<span>41条曼谷评价</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/31Vv077s7GpMqaAt1" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>I booked the private Sakura onsen room, which includes a hot onsen bath, a cold plunge, and a steam room. The facilities felt quite new and the room was very private, making the whole experience feel calm and exclusive&hellip;</p>
      <div class="t-foot">
        <div class="who">Ami Narissara<span>本地向导 &middot; 38条评价</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/iXiLC4lhTXhcnjVvc" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>My wife and I had such a great private onsen experience here today&hellip; Genuinely great, and such a good location! Highly, highly recommend.</p>
      <div class="t-foot">
        <div class="who">Jonathan O'Callaghan<span>本地向导 &middot; 32条评价</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/eoyRkCzlwQwFBk5jO" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Great service and place is clean. The therapy person is very great.</p>
      <div class="t-foot">
        <div class="who">P. Panyasakorn<span>4周前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/FagUAf6goHtcNnEit" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Amazing spa in Thonglor with a great variety of treatments. Really enjoy both the steam &amp; sauna rooms. Will definitely be coming back.</p>
      <div class="t-foot">
        <div class="who">Zach Cohen<span>1个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/rH4tOAehC1tibdiBU" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>A really nice relaxing and experience for the weekend. The overall atmosphere is made for peace in body and mind. Definitely gonna come back to this place.</p>
      <div class="t-foot">
        <div class="who">Nichalee T.<span>1个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/gADn1tD0YCyQUoYmo" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Nice and clean onsen. You can have a private room and relax fully. Massage is good, they have lemongrass oil&mdash;very nice smell.</p>
      <div class="t-foot">
        <div class="who">&#1070;&#1083;&#1080;&#1103; &#1040;&#1079;&#1072;&#1088;&#1080;&#1085;&#1072;<span>1个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/IpmrWLS77bBxlBe29" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>I had Jaae as my masseuse, and she was absolutely wonderful&hellip; Her hands have a magic touch, and the massage was one of the best I've ever experienced.</p>
      <div class="t-foot">
        <div class="who">omar ben sellam<span>2个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/G6e7orSjqXAH3x2C1" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Private onsen and spa in the middle of Thong lo. I spent 2 hrs here. The Mineral salt Japanese onsen and Ice bath are awesome. Highly recommend this place!</p>
      <div class="t-foot">
        <div class="who">natthawat ru<span>4个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/n2oqeuPcMZWwguBGk" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>What a great experience. I was looking for a relaxation spa with wellness, a cold plunge, and a sauna, and this place had it all&hellip; Apple was incredibly kind and welcoming. Highly recommended!</p>
      <div class="t-foot">
        <div class="who">&#1491;&#1504;&#1497;&#1488;&#1500; &#1488;&#1500;&#1506;&#1494;&#1512;<span>7个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/4vderGJuuPJYkh8Fm" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>We tried this new place as it just opened and took the 2 hour private onsen + Vietnamese Spa session. It was very refreshing and the place looks gorgeous! Highly recommend!</p>
      <div class="t-foot">
        <div class="who">Robert<span>8个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/iZrE5f6zwqdjUs49D" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>A newly opened spa on Thonglor Soi 13 offers an elevated relaxation experience with private onsens, Vietnamese spa rituals, and dedicated neck&ndash;shoulder massages&hellip; The therapists are exceptional&mdash;strong, precise hands with truly professional technique.</p>
      <div class="t-foot">
        <div class="who">Ek-kapop<span>8个月前</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/Pr0SYhJPXkMRlpKEY" target="_blank" rel="noopener">在Google上阅读 &rarr;</a>
    </div>
  </div>
  <div class="reviews-nav">
    <button type="button" id="reviewsPrev">&#8249; 上一页</button>
    <span class="reviews-page-count" id="reviewsPageCount"></span>
    <button type="button" id="reviewsNext">下一页 &#8250;</button>
  </div>
</section>
<script>
(function(){{
  var grid = document.getElementById("reviewsGrid");
  if(!grid) return;
  var cards = Array.prototype.slice.call(grid.children);
  var perPage = 4;
  var pages = Math.ceil(cards.length / perPage) || 1;
  var page = 0;
  var prevBtn = document.getElementById("reviewsPrev");
  var nextBtn = document.getElementById("reviewsNext");
  var countEl = document.getElementById("reviewsPageCount");
  function render(){{
    cards.forEach(function(card, i){{
      card.style.display = (Math.floor(i / perPage) === page) ? "" : "none";
    }});
    if(prevBtn) prevBtn.disabled = (page === 0);
    if(nextBtn) nextBtn.disabled = (page === pages - 1);
    if(countEl) countEl.textContent = (page + 1) + " / " + pages;
  }}
  if(prevBtn) prevBtn.addEventListener("click", function(){{ if(page > 0){{ page--; render(); }} }});
  if(nextBtn) nextBtn.addEventListener("click", function(){{ if(page < pages - 1){{ page++; render(); }} }});
  render();
}})();
</script>
<section class="section" id="contact" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">联系方式</span><h2 style="margin-bottom:14px;">预约您的疗愈时刻</h2>
  <p style="color:var(--ink-soft); margin-bottom:24px;">透过LINE直接联系前台，营业时间内即时回复。</p>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons_zh(), ZOOM_ICON=ZOOM_ICON, **IMG, **VID)

with open("/tmp/zenva_site/zh/index.html", "w") as f:
    f.write(page("Zenva — Private Onsen & Spa", "home", zh_index_body, index_extra_css,
                 description="曼谷私人温泉与冰浴冷热交替疗法，搭配招牌SPA护理。全程私密独立，最多可供三位宾客共享，位于Seenspace Thonglor。",
                 path="zh/index.html", group="index.html", lang="zh", en_href="../index.html", th_href="../th/index.html", hero_image=IMG["hero"]))
print("zh/index.html v4 written (PREVIEW — pending native-speaker review)")

zh_bonsai_packages = [
    ("+ 芳香精油按摩", "120分钟", "5,900泰铢起"),
    ("+ 芳香精油按摩（加长版）", "150分钟", "7,900泰铢起"),
    ("+ 任选2项越南SPA护理", "120分钟", "4,900泰铢起"),
    ("+ 越南SPA全套护理", "150分钟", "5,900泰铢起"),
]
zh_sakura_packages = list(zh_bonsai_packages)
zh_luxury_rows = [("芳香精油按摩 — 60分钟", "1,590泰铢起"), ("芳香精油按摩 — 90分钟", "2,390泰铢起")]
zh_thai_rows = [("足部 / 头部 / 颈部 / 肩部按摩 — 30分钟", "590泰铢起"), ("— 60分钟", "790泰铢起"), ("— 90分钟", "1,090泰铢起"), ("— 120分钟", "1,390泰铢起")]
zh_signature_rows = [("任选1项：头部 / 采耳 / 面部护理 — 30分钟", "690泰铢起"), ("任选2项 — 60分钟", "1,290泰铢起"), ("Zenva招牌18步越南SPA护理（头部、采耳与面部护理全套）— 90分钟", "1,590泰铢起")]

zh_services_body = ("""
<div class="page-hero">
  <span class="eyebrow">完整菜单</span>
  <h1>温泉与SPA菜单</h1>
  <p>Zenva现有的所有房型、套餐与疗程一览。</p>
</div>
<section class="section" id="rooms">
  <div class="menu-block">
    <div class="menu-title-bar"><h2>私人温泉</h2><span>最多3位宾客 &middot; 基础60分钟</span></div>
    <div class="room-pair">
      <div class="room-card bonsai">
        <div class="photo"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"><span class="tag">盆景房 &middot; 桑拿房</span></div>
        <div class="info"><div class="desc">冰浴、日式矿物盐温泉、喜马拉雅盐晶桑拿房。</div>
        <div class="price-line"><span class="amt">3,190泰铢起</span><span class="dur">每间房 &middot; 60分钟</span></div>
        <div class="addon">加时：1,000泰铢起 / 15分钟</div></div>
      </div>
      <div class="room-card sakura">
        <div class="photo"><img src="{room_sakura}" alt="Sakura private onsen room with steam room" loading="lazy"><span class="tag">樱花房 &middot; 蒸汽房</span></div>
        <div class="info"><div class="desc">冰浴、日式矿物盐温泉，以及蒸汽房。</div>
        <div class="price-line"><span class="amt">3,190泰铢起</span><span class="dur">每间房 &middot; 60分钟</span></div>
        <div class="addon">加时：1,000泰铢起 / 15分钟</div></div>
      </div>
    </div>
  </div>

  <div class="menu-block" id="couple">
    <div class="menu-title-bar"><h2>双人温泉套餐</h2><span>温泉加按摩，专为双人打造</span></div>
    <div class="couple-pair">
      """ + couple_table("bonsai", "盆景桑拿房", zh_bonsai_packages, headers=("套餐", "时长", "价格")) + couple_table("sakura", "樱花蒸汽房", zh_sakura_packages, headers=("套餐", "时长", "价格")) + """
    </div>
  </div>

  <div class="menu-block" id="spa">
    <div class="menu-title-bar"><h2>SPA与按摩系列</h2><span>单项疗程</span></div>
    <div class="room-pair spa-photo-row" style="margin-bottom:26px;">
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{massage_card}" alt="Therapist performing an aromatherapy massage" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;"></div>
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{chair_card}" alt="Guest reclining in a premium massage chair, streaming entertainment on a personal screen" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center 25%;"></div>
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{vietnamese_card}" alt="Traditional Vietnamese ear-cleaning treatment, part of the 18-Steps Zenva Spa" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;"></div>
    </div>
    <div class="spa-grid">
      """ + spa_col("尊享SPA", zh_luxury_rows) + spa_col("正宗泰式SPA", zh_thai_rows,
          note="舒适地坐入尊享按摩椅，配备个人屏幕，让您在放松身心的同时观赏自己喜爱的影音内容。") \
        + spa_col("Zenva招牌SPA", zh_signature_rows) + """
    </div>
  </div>
</section>
<p class="vat-note">以上价格均需另加7%增值税。</p>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">准备好预约了吗？</span><h2 style="margin-bottom:14px;">预约您的疗愈时刻</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""").format(ctas=cta_buttons_zh(), **IMG)

with open("/tmp/zenva_site/zh/onsen-spa.html", "w") as f:
    f.write(page("温泉与SPA菜单 — Zenva", "services", zh_services_body, services_extra_css,
                 description="Zenva私人温泉房、双人套餐与SPA按摩疗程的完整菜单与价目——盆景房与樱花房，3,190泰铢起，曼谷。",
                 path="zh/onsen-spa.html", group="onsen-spa.html", lang="zh", en_href="../onsen-spa.html", th_href="../th/onsen-spa.html"))
print("zh/onsen-spa.html v4 written (PREVIEW — pending native-speaker review)")

zh_membership_body = """
<div class="page-hero">
  <span class="eyebrow" style="color:var(--cream);">尊享礼遇</span>
  <h1>会员计划</h1>
  <p>各等级均享有对应储值额度，现正推出限时升级优惠。</p>
</div>
<section class="section">
  <div class="tier-cards">
    """ + tier_zh("SILVER", "银&middot;初见", "10,000", "11,000", "+1,000赠送", promo_amt="13,000", promo_bonus_zh="+3,000赠送") + \
        tier_zh("GOLD", "金&middot;随心", "30,000", "36,000", "+6,000赠送", promo_amt="45,000", promo_bonus_zh="+15,000赠送") + \
        tier_zh("DIAMOND", "钻&middot;臻境", "50,000", "65,000", "+15,000赠送") + \
        tier_zh("PLATINUM", "铂&middot;忘尘", "100,000", "150,000", "+50,000赠送", best=True, platinum=True) + """
  </div>
</section>
<section class="section" style="background:var(--cream-soft);">
  <div class="section-head"><span class="eyebrow">条款</span><h2>会员条款</h2></div>
  <div style="max-width:700px; margin:0 auto; font-size:13.5px; color:var(--ink-soft); line-height:1.9;">
    储值额度可用于Zenva所有服务项目。储值额度不可转让、不可退款。会员资格自购买之日起有效期为12个月，须在到期日前使用完毕。储值额度不可兑换现金。Zenva保留随时修改本条款的权利，恕不另行通知。
  </div>
</section>
<section class="section" style="text-align:center;">
  <span class="eyebrow">开启您的会员之旅</span><h2 style="margin-bottom:14px;">即刻开启您的会员礼遇</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/membership.html", "w") as f:
    f.write(page("会员计划 — Zenva", "membership", zh_membership_body, membership_extra_css,
                 description="Zenva静荟会员计划——银·初见、金·随心、钻·臻境、铂·忘尘四大等级，可于所有温泉、SPA与按摩服务中使用，曼谷。",
                 path="zh/membership.html", group="membership.html", lang="zh", en_href="../membership.html", th_href="../th/membership.html"))
print("zh/membership.html v4 written (PREVIEW — pending native-speaker review)")

# ---------- BLOG — INDEX + ONE FULL SAMPLE ARTICLE ----------
blog_extra_css = """
  .blog-hero{{padding:52px 24px 36px; text-align:center; background:var(--cream-soft); border-bottom:1px solid var(--line);}}
  .blog-hero h1{{font-size:36px; margin-bottom:8px;}}
  .blog-hero p{{color:var(--ink-soft); max-width:560px; margin:0 auto;}}
  .blog-grid{{display:grid; grid-template-columns:repeat(3,1fr); gap:26px; max-width:1100px; margin:0 auto;}}
  .b-card{{border:1px solid var(--line); border-radius:8px; overflow:hidden; background:var(--white); display:flex; flex-direction:column;}}
  .b-card .photo{{height:170px; position:relative; overflow:hidden;}}
  .b-card .photo img{{position:absolute; inset:0; width:100%; height:100%; object-fit:cover;}}
  .b-card .photo.placeholder{{background:var(--cream-soft); display:flex; align-items:center; justify-content:center; color:var(--ink-soft); font-size:11px; letter-spacing:.08em; text-transform:uppercase;}}
  .b-card .body{{padding:18px 18px 20px; display:flex; flex-direction:column; flex:1;}}
  .b-card .cat{{font-size:10.5px; font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--gold-text); margin-bottom:8px;}}
  .b-card h3{{font-size:16.5px; margin-bottom:8px; line-height:1.35;}}
  .b-card p{{font-size:13px; color:var(--ink-soft); flex:1; margin-bottom:12px;}}
  .b-card .read{{font-size:12.5px; font-weight:700; color:var(--ink);}}
  .b-card.soon{{opacity:.6;}}
  .b-card .soon-tag{{font-size:10px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-soft); border:1px dashed var(--line); border-radius:3px; padding:3px 8px; display:inline-block; margin-bottom:8px; width:fit-content;}}
  @media (max-width:900px){{.blog-grid{{grid-template-columns:1fr;}}}}

  .article-hero{{padding:48px 24px 30px; text-align:center; background:var(--cream-soft); border-bottom:1px solid var(--line);}}
  .article-hero .cat{{font-size:11px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-text); display:block; margin-bottom:12px;}}
  .article-hero h1{{font-size:34px; max-width:760px; margin:0 auto 14px;}}
  .article-hero .meta{{font-size:12.5px; color:var(--ink-soft);}}
  .article-body{{max-width:720px; margin:0 auto; padding:50px 24px; font-size:15.5px; line-height:1.85; color:var(--ink);}}
  .article-body h2{{font-size:22px; margin:36px 0 14px;}}
  .article-body h3{{font-size:17px; margin:28px 0 10px;}}
  .article-body p{{margin-bottom:16px; color:var(--ink-soft);}}
  .article-body ul{{margin:0 0 16px 20px; color:var(--ink-soft);}}
  .article-body li{{margin-bottom:8px;}}
  .article-body .lead{{font-size:17px; color:var(--ink); font-family:var(--font-display);}}
  .article-body .callout{{background:var(--cream-soft); border-left:3px solid var(--gold); padding:16px 20px; font-size:13.5px; color:var(--ink-soft); margin:24px 0;}}
  .article-body .cta-block{{background:var(--ink); color:var(--cream); border-radius:8px; padding:30px; text-align:center; margin:40px 0 10px;}}
  .article-body .cta-block h3{{color:var(--cream); margin-bottom:8px;}}
  .article-body .cta-block p{{color:#cdbf98; margin-bottom:18px;}}
  .article-body .disclaimer{{font-size:11.5px; color:var(--ink-soft); border-top:1px solid var(--line); margin-top:40px; padding-top:16px;}}
""".format()

def blog_card(cat, title, teaser, photo_key=None, href=None, soon=False):
    if soon:
        return f'''<div class="b-card soon"><div class="photo placeholder">Coming Soon</div>
        <div class="body"><span class="soon-tag">In Planning</span><h3>{title}</h3><p>{teaser}</p></div></div>'''
    return f'''<div class="b-card"><a href="{href}"><div class="photo"><img src="{{{photo_key}}}" alt="{title}" loading="lazy"></div></a>
    <div class="body"><span class="cat">{cat}</span><h3><a href="{href}" style="color:inherit; text-decoration:none;">{title}</a></h3>
    <p>{teaser}</p><a class="read" href="{href}">Read the Guide &rarr;</a></div></div>'''

blog_body = ("""
<div class="blog-hero">
  <span class="eyebrow">Zenva Journal</span>
  <h1>Notes on Rest, Recovery &amp; Quiet Rituals</h1>
  <p>Shared reflections and practical notes on onsen bathing, contrast therapy, and the small rituals of recovery — for anyone curious about this world, whether or not Zenva is part of their routine yet.</p>
</div>
<section class="section">
  <div class="blog-grid">
    """ + blog_card("Contrast Therapy", "What Is Contrast Therapy? Hot Onsen + Ice Bath Benefits Explained",
                     "The hot-cold science behind Zenva's signature ritual, and how to do it safely.",
                     "water", "blog-contrast-therapy.html") + """
    """ + blog_card("Wellness Guides", "Private Onsen vs. Public Onsen: What's the Difference?",
                     "Private room or shared bathhouse? Here's how Japan's onsen tradition compares to Bangkok's private-onsen experiences.",
                     "room_sakura", "blog-private-vs-public-onsen.html") + """
    """ + blog_card("Guides &amp; Tips", "Planning a Couples Spa Day in Bangkok: A Simple Checklist",
                     "A practical, no-fuss checklist for planning a relaxed onsen-and-massage day in Bangkok as a couple.",
                     "signature", "blog-couples-spa-day-checklist.html") + """
    """ + blog_card("Wellness Guide", "Thai Massage vs. Aromatherapy Massage: Which Should You Choose?",
                     "Thai massage or aromatherapy massage — first-timers, here's how to pick the right one for your body and your mood.",
                     "massage", "blog-thai-vs-aromatherapy-massage.html") + """
    """ + blog_card("Wellness Guides", "Choosing a Private Onsen in Bangkok: What Actually Matters",
                     "Not all private onsens are equal — here's the real checklist for water hygiene, room design, and booking flexibility before you pay.",
                     "room_bonsai", "blog-choosing-private-onsen-bangkok.html") + """
    """ + blog_card("Wellness &amp; Recovery", "Before and After Your Onsen Session: A Short Aftercare Guide",
                     "Simple hydration, timing, and safety habits to help you get the most from every hot-cold onsen session.",
                     "reception", "blog-onsen-aftercare-guide.html") + """
    """ + blog_card("Self-Care", "Self-Care Isn't New: The Surprisingly Long History Behind a Very 2026 Word",
                     "Where the phrase actually came from, why it's having a moment again, and what it looks like beyond candles and bath salts.",
                     "menu_card_onsen", "blog-self-care-history.html") + """
  </div>
</section>
""").format(**IMG)

with open("/tmp/zenva_site/blog.html", "w") as f:
    f.write(page("Zenva Journal — Wellness & Recovery Guides", "blog", blog_body, blog_extra_css,
                 description="Practical guides on contrast therapy, private onsen bathing, and spa treatments from Zenva — Bangkok's private onsen and spa.", path="blog.html", zh_href="zh/blog.html"))
print("blog.html v4 written")

# ---- Sample full article: pillar piece on contrast therapy ----
article_body = """
<div class="article-hero">
  <span class="cat">Contrast Therapy</span>
  <h1>What Is Contrast Therapy? Hot Onsen + Ice Bath Benefits Explained</h1>
  <div class="meta">Zenva Journal &middot; Wellness &amp; Recovery</div>
</div>
<div class="article-body">
  <p class="lead">Contrast therapy — alternating between hot water immersion and cold exposure — has become one of the most talked-about recovery practices in wellness circles. At Zenva, it's the idea behind our private onsen rooms: a hot mineral-salt bath paired with an ice bath, done privately and at your own pace.</p>

  <h2>The Basic Idea</h2>
  <p>Contrast therapy works by moving your body between two temperature extremes. Heat — from a hot onsen, sauna, or steam room — encourages blood vessels to widen (vasodilation), increasing circulation and helping muscles relax. Cold exposure does the opposite: it narrows blood vessels (vasoconstriction), which many people find reduces the sensation of swelling and soreness after physical activity.</p>
  <p>Alternating between the two is thought to "pump" blood flow more actively than either temperature alone — heat draws blood to the surface and muscles, cold pushes it back toward the core, and the repeated cycle is the basis of most contrast-therapy protocols used in sports recovery and spa settings alike.</p>

  <h2>Why People Do It</h2>
  <ul>
    <li><strong>Muscle recovery:</strong> a common use case after exercise, travel, or long periods of standing or sitting.</li>
    <li><strong>Mental reset:</strong> the sharp temperature shift is frequently described as clarifying and energizing, distinct from a purely relaxing warm soak.</li>
    <li><strong>Circulation:</strong> the alternating vasodilation/vasoconstriction cycle is the mechanism most commonly cited for improved perceived circulation.</li>
    <li><strong>Sleep and stress:</strong> many guests use an evening hot-cold session as a wind-down ritual before rest.</li>
  </ul>
  <p>We keep this section deliberately measured: contrast therapy is a well-established wellness practice, but it is not a medical treatment, and individual results vary. Treat the above as commonly reported benefits, not guarantees.</p>

  <h2>How a Typical Session Works</h2>
  <p>There's no single "correct" protocol, but a simple, beginner-friendly structure looks like this:</p>
  <ul>
    <li>Warm up in the hot onsen for 8–12 minutes.</li>
    <li>Move to the ice bath for 30–90 seconds — start shorter, and only extend once you're comfortable.</li>
    <li>Return to the hot onsen for another 8–10 minutes.</li>
    <li>Repeat the cycle 2–3 times, always finishing on warm if you plan to relax afterward, or on cold if you want the alerting effect.</li>
  </ul>
  <p>At Zenva, this entire sequence happens inside a single private room — no shared schedule, no waiting for a plunge pool to free up, and no clock running while you find your own pace.</p>

  <h3>Pairing It With Spa Treatments</h3>
  <p>A hot-cold cycle leaves muscles warm, loose, and receptive to bodywork — which is why we built our couple and solo packages around finishing an onsen session with an aromatherapy or Thai massage rather than treating the two as separate visits. It's the idea behind our "full recovery experience" positioning: the contrast ritual handles circulation and reset, the massage handles the muscular follow-through.</p>

  <div class="callout">Contrast therapy is not recommended for everyone. If you have a cardiovascular condition, are pregnant, or have a history of severe migraines, speak with a doctor before trying hot-cold immersion, and mention it to our front desk when you book so we can advise on which room and duration suit you.</div>

  <h2>What to Bring / Know Before You Go</h2>
  <ul>
    <li>Arrive slightly early — jumping straight from Bangkok heat into a hot onsen without a few minutes to acclimatize isn't as effective.</li>
    <li>Hydrate before and after; temperature cycling is more taxing on the body than a standard warm bath.</li>
    <li>If it's your first time, tell our team — we'll walk you through timing so the ice bath doesn't feel like a shock.</li>
  </ul>

  <div class="cta-block">
    <h3>If You'd Like to Try It Yourself</h3>
    <p>Our Bonsai and Sakura rooms are each fitted with a hot onsen and ice bath, private for up to three guests — for whenever you're ready. See current pricing and what's included on our <a href="contrast-therapy-ice-bath-bangkok.html" style="color:inherit; text-decoration:underline;">Contrast Therapy, Ice Bath &amp; Sauna</a> page.</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">This article is educational and general in nature. It is not medical advice. If you have a pre-existing health condition, consult a physician before beginning any hot-cold contrast practice.</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">More From the Journal</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; Back to all guides</a>
  </div>
</div>
""".format(ctas=cta_buttons())

with open("/tmp/zenva_site/blog-contrast-therapy.html", "w") as f:
    f.write(page("Contrast Therapy: Hot Onsen + Ice Bath Benefits — Zenva Journal", "blog", article_body, blog_extra_css,
                 description="The hot-cold science behind Zenva's signature onsen ritual, how contrast therapy works, and how to do it safely — from Bangkok's private onsen and spa.", path="blog-contrast-therapy.html", zh_href="zh/blog-contrast-therapy.html"))
print("blog-contrast-therapy.html v4 written")

# ---- Article 2: Private Onsen vs. Public Onsen ----
article_body_2 = """
<div class="article-hero">
  <span class="cat">Wellness Guides</span>
  <h1>Private Onsen vs. Public Onsen: What's the Difference?</h1>
  <div class="meta">Zenva Journal &middot; Wellness &amp; Recovery</div>
</div>
<div class="article-body">
  <p class="lead">The word "onsen" carries centuries of Japanese bathing culture with it, but the experience itself now comes in very different formats. If you're in Bangkok trying to decide between a private onsen room and a shared, public-style bathhouse experience, here's what actually differs &mdash; and why it matters for comfort, privacy, and how you spend your time.</p>

  <h2>Where the Onsen Tradition Comes From</h2>
  <p>Onsen originated in Japan as naturally heated mineral springs, and communal bathing developed around them as a social and cultural ritual, not just a way to get clean. Traditional etiquette is specific and, for newcomers, sometimes surprising. Bathers are expected to wash and rinse thoroughly at individual shower stations before ever entering the shared water, since the communal bath is for soaking, not cleaning. Bathing is done nude, without swimwear, and small towels are kept out of the water entirely &mdash; usually rested on the head or set aside. Facilities are typically separated by gender.</p>
  <p>Tattoo policy is one of the more complex parts of onsen culture. Because tattoos have historically been associated with organized crime in Japan, many traditional public onsen have restricted or banned visibly tattooed guests. That stance has been gradually softening over the past decade, with more facilities allowing cover patches, calling ahead for approval, or pointing guests toward tattoo-friendly locations. Private-room bathing (called <em>kashikiri-buro</em> in Japan) has also become one of the standard workarounds, since a private room removes the issue entirely.</p>

  <h2>Public Onsen: Tradition, Community, and Trade-Offs</h2>
  <p>A public or shared onsen keeps the bathing tradition intact: communal soaking pools, a set of house rules, and often a genuinely social, unhurried atmosphere that's part of the appeal for many long-time onsen-goers. The trade-offs are real, though. You're bathing on the facility's schedule and etiquette terms, sharing water and space with strangers, and, depending on the venue and country, navigating rules around nudity, gender separation, and tattoos that may not fit every visitor's comfort level. For some people, that communal ritual is the whole point. For others &mdash; couples, guests with tattoos, people who simply prefer privacy, or anyone short on time &mdash; it's a barrier.</p>

  <h2>Why Private Onsen Rooms Have Grown in Popularity</h2>
  <p>Private-room and private-pool bathing formats aren't a new invention; Japanese ryokan have offered kashikiri-buro for a long time specifically to serve couples, families, and tattooed guests who want the mineral-bath experience without the communal setting. What has changed is how widely the format has spread. The global thermal and mineral springs sector has grown substantially in recent years, according to the Global Wellness Institute, and a meaningful share of that growth is concentrated in higher-end, amenity-added facilities aimed at travelers who want a more personalized soak rather than a purely communal one. Outside Japan, that same appetite for privacy has shown up in cities like Bangkok, where private onsen-style rooms have become a recognizable category of their own within the wellness and spa scene &mdash; not a replacement for the public tradition, but a distinct option built around control over time, company, and setting.</p>
  <p>A private room typically means:</p>
  <ul>
    <li>Booking a specific time slot rather than working around a public bathhouse's operating hours or crowd patterns</li>
    <li>Bathing only with the people you choose to bring &mdash; a partner, friends, or family</li>
    <li>No tattoo policy to navigate, since the space isn't shared with other bathers</li>
    <li>More flexibility to combine bathing with other treatments, like massage, in the same visit</li>
  </ul>
  <p>The trade-off runs the other way: private rooms generally cost more per person than a communal public onsen, and they don't offer the same social, tradition-steeped atmosphere that draws some visitors to public bathhouses in the first place.</p>

  <h2>Contrast Bathing: Hot Onsen Water Plus a Cold Plunge</h2>
  <p>One format increasingly available in private-room setups is contrast therapy &mdash; alternating between a hot mineral bath and a cold plunge or ice bath in the same session. This isn't unique to any one facility; cold plunging and contrast bathing have become a broader wellness trend over the past few years. It's worth being realistic about what the evidence actually supports: medical commentary, including guidance summarized by the American Medical Association, describes contrast therapy as offering mainly short-term effects &mdash; commonly reported temporary reductions in soreness, temporary mood lift, and improved short-term mobility &mdash; rather than proven long-term or curative benefits. It's reasonably viewed as a supportive recovery habit, not a guaranteed treatment, and people with cardiovascular conditions are generally advised to check with a doctor before trying cold immersion.</p>

  <h2>So Which One Should You Choose in Bangkok?</h2>
  <p>Neither format is objectively "better" &mdash; they serve different priorities. A public or shared onsen-style bathhouse suits people who value the communal tradition and don't mind sharing space and schedule with other bathers. A private onsen room suits people who want privacy, flexibility around who they bathe with, no tattoo restrictions, and the option to pair the soak with treatments like massage in one booking. If privacy, contrast bathing, and a couple-friendly or small-group setup matter to you, a private room is generally the more comfortable fit for a Bangkok visit.</p>

  <div class="callout">Zenva's private rooms are built around this exact idea: your own space, your own hot mineral-salt onsen tub with a separate ice bath for contrast bathing, and no communal schedule to work around.</div>

  <div class="cta-block">
    <h3>Where Zenva Fits In</h3>
    <p>If a fully private room sounds like your preference, we keep two &mdash; Bonsai and Sakura &mdash; each with its own hot mineral-salt onsen and a separate ice bath, for solo visits, couples, or small groups. See room details, capacity, and pricing on our <a href="onsen-spa.html" style="color:inherit; text-decoration:underline;">Private Onsen Rooms &amp; Packages</a> page.</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">Wellness information in this article is general and educational, not medical advice. Contrast bathing and hot-water immersion may not be suitable for everyone, including people with cardiovascular conditions; consult a doctor if you have health concerns before booking.</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">More From the Journal</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; Back to all guides</a>
  </div>
</div>
""".format(ctas=cta_buttons())

with open("/tmp/zenva_site/blog-private-vs-public-onsen.html", "w") as f:
    f.write(page("Private Onsen vs. Public Onsen — Zenva Journal", "blog", article_body_2, blog_extra_css,
                 description="Private room or shared bathhouse? How Japan's onsen tradition compares to Bangkok's private-onsen experiences, from Zenva — Bangkok's private onsen and spa.", path="blog-private-vs-public-onsen.html", zh_href="zh/blog-private-vs-public-onsen.html"))
print("blog-private-vs-public-onsen.html v4 written")

# ---- Article 3: Planning a Couples Spa Day in Bangkok ----
article_body_3 = """
<div class="article-hero">
  <span class="cat">Guides &amp; Tips</span>
  <h1>Planning a Couples Spa Day in Bangkok: A Simple Checklist</h1>
  <div class="meta">Zenva Journal &middot; Wellness &amp; Recovery</div>
</div>
<div class="article-body">
  <p class="lead">A good couples spa day doesn't happen by accident &mdash; it's the result of a few small decisions made in advance. This checklist walks through what to sort out before you go, what to bring, and how to time your visit around Bangkok's rhythms, so the only thing left to do on the day itself is relax.</p>

  <h2>1. Book Ahead and Tell the Spa What You Want</h2>
  <p>Spa and wellness publications consistently point to the same first step: reserve early and communicate your preferences before you arrive, rather than figuring it out at check-in. If you and your partner want to be treated in the same room, or you have a preference between a Thai massage and an aromatherapy massage, mention it when you book rather than hoping it works out.</p>
  <ul>
    <li>Confirm your date and time slot in advance, especially on weekends or holidays.</li>
    <li>Let the spa know it's a couple or group visit so they can plan the room accordingly.</li>
    <li>Ask any questions about the treatments or facilities ahead of time rather than during your session.</li>
  </ul>

  <h2>2. Pick a Time Slot With Bangkok Traffic in Mind</h2>
  <p>Bangkok's traffic is one of the more predictable parts of the city &mdash; heaviest roughly from 7:30&ndash;9:30 in the morning and again from 5:00&ndash;7:30 in the evening, with routes like Sukhumvit and Petchaburi Roads especially prone to slow crawls. Booking outside those windows, or building in extra travel time if you can't avoid them, makes it far easier to arrive unrushed. The BTS Skytrain is generally a reliable way to reach the Thonglor area during peak hours if road traffic looks heavy.</p>
  <ul>
    <li>Avoid booking right at the start of morning or evening rush hour if possible.</li>
    <li>Check the route in a maps app the night before, not the morning of.</li>
    <li>Consider the BTS or MRT as a backup if a taxi or ride-hail car looks stuck in traffic.</li>
    <li>Build in a buffer of 15&ndash;30 minutes so a delayed ride doesn't eat into your treatment time.</li>
  </ul>

  <h2>3. Pack Light, but Pack Smart</h2>
  <p>You don't need much for a couples spa visit, but a few small items make a real difference in comfort.</p>
  <ul>
    <li>Loose, comfortable clothing to wear before and after your session.</li>
    <li>Swimwear if you plan to use a hot tub or bath, plus a change for afterward so you're not sitting in something damp.</li>
    <li>A hair tie, if needed, and any basic toiletries you personally rely on.</li>
    <li>Your phone charged &mdash; then consider leaving it in a bag or locker once you arrive, so you're both actually present.</li>
  </ul>

  <h2>4. Hydrate Before, During, and After</h2>
  <p>Drinking water before and after a massage or a hot soak is a near-universal recommendation across spa and wellness guides, and it's easy to forget in the middle of a busy day. If your visit includes contrast-style bathing &mdash; moving between hot water and a cold plunge &mdash; staying hydrated and listening to your own body's signals matters even more. Go at your own pace, and skip the cold plunge (or keep it brief) if you have any health condition that makes rapid temperature changes inadvisable; when in doubt, check with a doctor first.</p>
  <ul>
    <li>Have a glass of water before you leave home.</li>
    <li>Sip water again once you arrive, and after your treatments.</li>
    <li>Ease into hot and cold water gradually rather than jumping straight in, especially if it's a first try.</li>
  </ul>

  <h2>5. On the Day: Arrive Early, Speak Up, Slow Down</h2>
  <p>Arriving a little early rather than right on time gives you both a chance to check in, change, and settle in without feeling rushed &mdash; a habit recommended across multiple spa-etiquette guides. Once your treatment starts, say something if pressure is too firm or too light, or if a room is too warm or too cool. A private couples setting makes this easier, since it's just the two of you and the therapist rather than a shared public space.</p>
  <ul>
    <li>Arrive 10&ndash;15 minutes before your booked time.</li>
    <li>Mention any allergies, sensitivities, or areas to avoid before your massage begins.</li>
    <li>Keep conversation low and phones away to actually unwind together.</li>
  </ul>

  <h2>6. After: Don't Rush Straight Back Into the Day</h2>
  <p>Give yourselves a few quiet minutes after your session before heading back into Bangkok traffic or a packed schedule. A slower transition &mdash; another glass of water, a short sit-down, an unhurried walk to the BTS &mdash; tends to make the relaxation last longer than diving straight into the next thing.</p>

  <div class="callout">This guide offers general planning tips, not medical advice. If you're pregnant, managing a heart or circulatory condition, or unsure whether contrast bathing is right for you, check with a doctor before booking hot-and-cold treatments.</div>

  <div class="cta-block">
    <h3>One Place That Covers the List</h3>
    <p>This is more or less the thinking behind our own <a href="couples-spa-bangkok.html" style="color:inherit; text-decoration:underline;">Couples Spa Experience</a> &mdash; private onsen and ice bath for two, paired with massage, in the Bonsai or Sakura room &mdash; built so a couple can work through most of this checklist in one visit, if it's useful.</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">General spa-planning guidance in this article is adapted from third-party wellness publications and is provided for informational purposes only; it is not medical advice. Zenva-specific details (rooms, treatments, pricing range, and booking channels) reflect current offerings and are subject to change &mdash; please confirm details when booking.</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">More From the Journal</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; Back to all guides</a>
  </div>
</div>
""".format(ctas=cta_buttons())

with open("/tmp/zenva_site/blog-couples-spa-day-checklist.html", "w") as f:
    f.write(page("Planning a Couples Spa Day in Bangkok — Zenva Journal", "blog", article_body_3, blog_extra_css,
                 description="A practical, no-fuss checklist for planning a relaxed onsen-and-massage day in Bangkok as a couple — from Zenva, Bangkok's private onsen and spa.", path="blog-couples-spa-day-checklist.html", zh_href="zh/blog-couples-spa-day-checklist.html"))
print("blog-couples-spa-day-checklist.html v4 written")

# ---- Article 4: Thai Massage vs. Aromatherapy Massage ----
article_body_4 = """
<div class="article-hero">
  <span class="cat">Wellness Guide</span>
  <h1>Thai Massage vs. Aromatherapy Massage: Which Should You Choose?</h1>
  <div class="meta">Zenva Journal &middot; Wellness &amp; Recovery</div>
</div>
<div class="article-body">
  <p class="lead">Booking your first massage and not sure whether to go with traditional Thai massage or an aromatherapy massage? The two treatments feel almost nothing alike &mdash; one is active and stretch-based, the other is slow and oil-based &mdash; so the right choice really comes down to what your body and your nervous system are asking for.</p>

  <h2>The Short Answer</h2>
  <p>If you want deep, active work on tight muscles, stiff joints, or restricted mobility, traditional Thai massage (nuad thai) is generally the better fit. If you want a calmer, more sensory experience focused on unwinding stress and quieting the mind, an aromatherapy massage is usually the more comfortable choice. Many guests alternate between the two depending on how their week has gone &mdash; and if you're booking a couple or group session, you don't have to agree on the same one.</p>

  <h2>What Is Traditional Thai Massage?</h2>
  <p>Thai massage (nuad thai) is one of Thailand's oldest healing traditions, with roots often traced back over two thousand years and documented influence from Indian and Southeast Asian bodywork practices. Stone inscriptions from Thailand's Sukhothai period already describe massage used to treat illness, and by the Ayutthaya era a dedicated massage department with specialist practitioners had been established. The tradition is significant enough that UNESCO added it to its Intangible Cultural Heritage list in 2019.</p>
  <p>Unlike most Western massage styles, Thai massage is done fully clothed, with no oil, on a padded mat rather than a table. The practitioner uses palms, thumbs, elbows, and even feet to apply rhythmic compression and acupressure along the body's energy pathways, known as "sen" lines, while also guiding you through assisted stretches that resemble yoga postures &mdash; which is why it's sometimes nicknamed "lazy person's yoga." You stay passive; the therapist moves your limbs, torso, and spine through a sequence of stretches and pressure points.</p>
  <p>On reported benefits, health publications commonly note that Thai massage may help with tension headaches, back pain, joint stiffness, and general flexibility, alongside improved circulation and stress relief. A systematic review of the evidence on traditional Thai massage for chronic pain found some supportive results across the trials examined, but &mdash; as is common in bodywork research &mdash; the review also pointed to a limited number of studies and inconsistent methodology, meaning the evidence is encouraging rather than conclusive. In short: research suggests real potential benefits, but Thai massage is a wellness practice, not a substitute for medical diagnosis or treatment.</p>

  <h2>What Is Aromatherapy Massage?</h2>
  <p>Aromatherapy massage pairs the technique of a classic Swedish-style massage &mdash; long, gliding strokes, kneading, and lighter overall pressure &mdash; with essential oils chosen for their scent and reputed calming or mood-lifting properties. It's performed on a table, typically with oil and a slower, more meditative pace than Thai massage, and it's designed primarily around relaxation rather than deep muscular release.</p>
  <p>The research picture here is genuinely mixed, and it's worth being upfront about that. Some randomized trials and reviews &mdash; including a meta-analysis of randomized controlled trials on aromatherapy and anxiety, and a systematic review looking at aromatherapy massage for anxiety in palliative care settings &mdash; have reported reductions in self-reported anxiety and stress after treatment. Some clinical sources also cite research linking lavender aromatherapy to improved sleep and reduced stress markers in certain settings. At the same time, reviewers consistently flag that many of these studies are small, short-term, or hard to compare directly against each other, and bodies such as the U.S. National Center for Complementary and Integrative Health note that evidence for complementary approaches to anxiety, aromatherapy included, remains preliminary overall. The honest summary: aromatherapy massage is commonly reported to support relaxation and a calmer mood, but it should be understood as a pleasant, low-risk wellness ritual rather than a clinically proven anxiety treatment.</p>

  <h2>Side-by-Side Comparison</h2>
  <ul>
    <li><strong>Pressure and pace:</strong> Thai massage is firmer and more active; aromatherapy massage is lighter and slower.</li>
    <li><strong>Clothing and setup:</strong> Thai massage is done clothed on a mat with no oil; aromatherapy massage is done on a table with oil, typically with minimal clothing under a sheet or towel.</li>
    <li><strong>What it targets:</strong> Thai massage focuses on stretching, joint mobility, and pressure-point work along the body's energy lines; aromatherapy massage focuses on sensory relaxation, scent, and gentle muscle soothing.</li>
    <li><strong>Best for:</strong> Thai massage suits guests who want to address stiffness, tightness, or restricted movement. Aromatherapy massage suits guests who mainly want to slow down, de-stress, and disconnect.</li>
    <li><strong>Energy after your session:</strong> Thai massage often leaves people feeling loosened up and "opened out"; aromatherapy massage tends to leave people drowsy and deeply relaxed.</li>
  </ul>

  <h2>Which One Should You Choose First?</h2>
  <p>If you're not sure, ask yourself one question: are you sore, or are you stressed? Sore, stiff, or tight from desk work, travel, or exercise &mdash; start with Thai massage. Wound up, overstimulated, or simply craving stillness &mdash; start with aromatherapy massage. There's no wrong choice, and plenty of regular guests eventually try both to see which their body responds to better.</p>

  <div class="callout">Not sure which to pick? Our team can help you choose based on how you're feeling that day when you call or message ahead of your visit.</div>

  <div class="cta-block">
    <h3>Both, If You Can't Decide</h3>
    <p>Both treatments are on our menu, and either pairs naturally with a soak in a private room's hot mineral-salt onsen or a plunge in the adjoining ice bath. Solo, couple, and group bookings are all welcome. Full pricing for both is on our <a href="massage-spa-bangkok.html" style="color:inherit; text-decoration:underline;">Massage &amp; Spa Treatments</a> page.</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">This article is for general wellness information only and is not medical advice. Thai massage and aromatherapy massage are not substitutes for diagnosis or treatment by a qualified healthcare provider &mdash; please consult one if you have a medical condition, are pregnant, or are recovering from injury or surgery before booking a massage.</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">More From the Journal</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; Back to all guides</a>
  </div>
</div>
""".format(ctas=cta_buttons())

with open("/tmp/zenva_site/blog-thai-vs-aromatherapy-massage.html", "w") as f:
    f.write(page("Thai Massage vs. Aromatherapy Massage — Zenva Journal", "blog", article_body_4, blog_extra_css,
                 description="Thai massage or aromatherapy massage? A side-by-side comparison to help first-time guests choose, from Zenva — Bangkok's private onsen and spa.", path="blog-thai-vs-aromatherapy-massage.html", zh_href="zh/blog-thai-vs-aromatherapy-massage.html"))
print("blog-thai-vs-aromatherapy-massage.html v4 written")

# ---- Article 5: Choosing a Private Onsen in Bangkok ----
article_body_5 = """
<div class="article-hero">
  <span class="cat">Wellness Guides</span>
  <h1>Choosing a Private Onsen in Bangkok: What Actually Matters</h1>
  <div class="meta">Zenva Journal &middot; Wellness &amp; Recovery</div>
</div>
<div class="article-body">
  <p class="lead">Bangkok's private onsen scene has grown fast, and on the surface most venues look similar: a hot tub, soft lighting, a closed door. The differences that actually affect your experience &mdash; and your health &mdash; are less visible. Here's what to check before you book.</p>

  <h2>"Private" Should Mean More Than a Locked Door</h2>
  <p>Privacy in a good onsen isn't just about not sharing the tub with strangers. It's about room layout, soundproofing, and whether the space is genuinely designed for one party at a time &mdash; versus a shared pool area with curtained-off sections. Ask how many guests a room is built for, whether the room is used by one party per booking, and whether change and shower facilities are private to that room or shared down a hallway.</p>

  <h2>Water Hygiene: The Question Most Guests Never Ask</h2>
  <p>Hot tub water is a genuinely different hygiene challenge than a swimming pool. Public health guidance from the U.S. CDC notes that warm water, high bather load, and lower water volume make hot tubs more prone to bacterial growth than cooler pools, and recommends that operators test disinfectant levels and pH multiple times a day, follow a documented water-management routine, and have trained staff handling the chemistry rather than leaving it to chance. None of this is visible to a guest walking in &mdash; which is exactly why it's worth asking directly.</p>
  <ul>
    <li>Is the water filtered and treated between every booking, or only at set times of day?</li>
    <li>Who tests the water, how often, and against what standard?</li>
    <li>Is the tub drained and refreshed for each new party, or topped up and reused?</li>
  </ul>
  <p>A venue that answers these questions confidently and specifically &mdash; rather than vaguely &mdash; is telling you something real about how it's run.</p>

  <h2>Contrast Therapy: Why the Ice Bath Matters as Much as the Onsen</h2>
  <p>Hot-to-cold contrast bathing (an onsen tub paired with a cold or ice plunge) has become a signature of newer private spa concepts, but a cold plunge has its own hygiene profile &mdash; cooler water slows down the disinfection process, so official cold-plunge guidance in other jurisdictions calls for more frequent water checks and, for smaller single-use units, regular full refills between uses. If a venue offers contrast therapy, it's reasonable to ask whether the cold plunge is treated with the same seriousness as the hot tub, not just presented as a novelty add-on.</p>

  <h2>Treatment Menu Depth and Staff Training</h2>
  <p>Spa-industry guidance points to two markers of a well-run spa: qualified, appropriately trained therapists, and a menu that goes beyond the tub itself. If massage or bodywork is part of the visit, ask what modalities are offered (Thai massage and aromatherapy massage are common benchmarks), how therapists are trained, and whether a short consultation happens before treatment to flag any health considerations.</p>

  <h2>Booking Flexibility for Couples and Groups</h2>
  <p>Because private rooms are typically capped at a small number of guests, how a venue handles couple or small-group bookings matters. Look for clarity upfront on maximum room capacity, whether multiple people can be booked into one room together, and how easy it is to actually reach someone to book &mdash; a phone line, LINE, or WhatsApp contact that responds is a practical sign of an operation that's easy to deal with, not just easy to find online.</p>

  <h2>Membership and Repeat-Visit Value</h2>
  <p>If you're likely to return, check whether the venue offers any kind of membership, package, or credit system, and how transparent the pricing structure is across its full menu. A wide published price range usually signals a menu that spans quick soaks through longer treatment combinations &mdash; worth comparing against what you actually plan to use.</p>

  <h2>Questions to Ask Before You Book</h2>
  <ul>
    <li>Is this room private to my party for the full booking, hot tub and cold plunge included?</li>
    <li>How and how often is the water tested and treated?</li>
    <li>What's the maximum number of guests the room is designed for?</li>
    <li>What treatments (massage, aromatherapy, etc.) can be added, and who performs them?</li>
    <li>Is there a membership or credit option if I plan to return?</li>
    <li>How do I actually reach the venue to book &mdash; phone, LINE, or WhatsApp?</li>
  </ul>

  <div class="callout">A hot-cold contrast setup is only as good as the hygiene routine behind it. Ask specifics, not just for a photo of the tub.</div>

  <div class="cta-block">
    <h3>For What It's Worth</h3>
    <p>Our two private rooms, Bonsai and Sakura, each pair a hot mineral-salt onsen tub with a separate ice bath, built for up to three guests per room &mdash; should it be useful to compare against. Room details and pricing are on our <a href="onsen-spa.html" style="color:inherit; text-decoration:underline;">Private Onsen Rooms &amp; Packages</a> page.</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">This article provides general guidance for evaluating private onsen and spa venues in Bangkok and is not medical advice. Contrast bathing (hot and cold immersion) is not suitable for everyone; consult a doctor if you have a heart condition, are pregnant, or have other health concerns before use.</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">More From the Journal</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; Back to all guides</a>
  </div>
</div>
""".format(ctas=cta_buttons())

with open("/tmp/zenva_site/blog-choosing-private-onsen-bangkok.html", "w") as f:
    f.write(page("Choosing a Private Onsen in Bangkok — Zenva Journal", "blog", article_body_5, blog_extra_css,
                 description="Not all private onsens are equal. A practical checklist for water hygiene, room privacy, and booking flexibility before you book in Bangkok — from Zenva.", path="blog-choosing-private-onsen-bangkok.html", zh_href="zh/blog-choosing-private-onsen-bangkok.html"))
print("blog-choosing-private-onsen-bangkok.html v4 written")

# ---- Article 6: Before and After Your Onsen Session (Aftercare) ----
article_body_6 = """
<div class="article-hero">
  <span class="cat">Wellness &amp; Recovery</span>
  <h1>Before and After Your Onsen Session: A Short Aftercare Guide</h1>
  <div class="meta">Zenva Journal &middot; Wellness &amp; Recovery</div>
</div>
<div class="article-body">
  <p class="lead">A hot mineral-salt soak followed by a plunge into an ice bath is a satisfying way to unwind &mdash; but like any warm-cold contrast experience, it asks a little of your body. A few simple habits before and after your session can help you feel steady, refreshed, and ready to enjoy the rest of your day.</p>

  <h2>Why Aftercare Is Worth a Few Minutes</h2>
  <p>Time in a hot tub increases sweating, which means your body is losing fluid, and moving between hot and cold water asks your circulation to adjust quickly. None of this is cause for concern for most healthy adults, but general guidance from sports-science and health sources commonly recommends paying attention to hydration and pacing around heat exposure and cold-water immersion, so your body can adjust comfortably rather than being caught off guard.</p>

  <h2>Before Your Session</h2>
  <ul>
    <li><strong>Hydrate in the hours beforehand.</strong> Sports-science guidance on fluid replacement around exercise and heat exposure generally suggests arriving well-hydrated rather than trying to "catch up" once you're already sweating.</li>
    <li><strong>Eat something light.</strong> A heavy, rich meal right before alternating hot and cold water can feel uncomfortable; a lighter snack an hour or so beforehand is a more comfortable option for many people.</li>
    <li><strong>Skip alcohol beforehand.</strong> Health guidance commonly advises against combining alcohol with heat exposure, since it can affect how your body regulates temperature and fluid balance.</li>
    <li><strong>Arrive a little early.</strong> Giving yourself a few unhurried minutes to settle in &mdash; rather than rushing straight from traffic into a hot tub &mdash; makes the transition feel calmer.</li>
    <li><strong>Bring a bottle of water.</strong> Having water on hand during your visit makes it easy to sip as you go.</li>
  </ul>

  <h2>During the Transition: What to Expect</h2>
  <p>Moving from the warmth of a mineral-salt onsen into an ice bath is a deliberate contrast, and it's normal for it to feel intense for the first moments. Many people describe an initial sharp, bracing sensation in the cold water that eases within a short time, followed by a warm, relaxed feeling once they're back to room temperature. Some describe the combination as mentally clarifying as well as physically relaxing, though individual reactions vary and general wellness guidance treats these as commonly reported subjective effects rather than guaranteed outcomes.</p>

  <h2>After Your Session</h2>
  <ul>
    <li><strong>Rehydrate steadily.</strong> Because heat exposure increases fluid loss through sweat, general guidance suggests replacing fluids gradually afterward rather than all at once &mdash; plain water is usually sufficient for a single session.</li>
    <li><strong>Warm up and dry off.</strong> After the cold plunge, drying off and allowing your body to return to a comfortable temperature at its own pace is commonly recommended before you head back out into the day.</li>
    <li><strong>Move gently.</strong> A slow walk or some easy stretching can feel better than sitting still immediately afterward, though there's no need to push into anything strenuous.</li>
    <li><strong>Give yourself a little downtime.</strong> Many people notice a wave of calm or mild tiredness after contrast bathing; treating the rest of your day with a bit less rush lets you enjoy that feeling.</li>
    <li><strong>Notice how you feel.</strong> Mild relaxation and a light head are common; anything that feels like dizziness, faintness, or persistent discomfort is a signal to sit down, rehydrate, and let a member of staff know.</li>
  </ul>

  <div class="callout">A note on caution: general health guidance suggests that people with cardiovascular conditions (such as heart disease or irregular heart rhythms), those who are pregnant, or anyone with a condition affected by rapid temperature change should check with a doctor before hot-cold contrast bathing. If this applies to you, please speak with your physician first and let our team know when booking.</div>

  <div class="cta-block">
    <h3>A Room to Practice This In</h3>
    <p>The Bonsai and Sakura rooms are set up for exactly this kind of session &mdash; a private hot mineral-salt onsen and ice bath, paired with Thai or aromatherapy massage, whenever you'd like to put it into practice. See how a session is structured and what's included on our <a href="contrast-therapy-ice-bath-bangkok.html" style="color:inherit; text-decoration:underline;">Contrast Therapy, Ice Bath &amp; Sauna</a> page.</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">This article is intended for general educational and self-care purposes only and is not medical advice. It does not replace guidance from a qualified healthcare provider. If you have a medical condition or any concerns about hot-cold contrast bathing, please consult your doctor before booking.</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">More From the Journal</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; Back to all guides</a>
  </div>
</div>
""".format(ctas=cta_buttons())

with open("/tmp/zenva_site/blog-onsen-aftercare-guide.html", "w") as f:
    f.write(page("Onsen Aftercare: Before and After Your Session — Zenva Journal", "blog", article_body_6, blog_extra_css,
                 description="Simple hydration, timing, and safety habits to help you get the most from every hot-cold onsen session — from Zenva, Bangkok's private onsen and spa.", path="blog-onsen-aftercare-guide.html", zh_href="zh/blog-onsen-aftercare-guide.html"))
print("blog-onsen-aftercare-guide.html v4 written")

article_body_7 = """
<div class="article-hero">
  <span class="cat">Self-Care</span>
  <h1>Self-Care Isn't New: The Surprisingly Long History Behind a Very 2026 Word</h1>
  <div class="meta">Zenva Journal &middot; Wellness &amp; Recovery</div>
</div>
<div class="article-body">
  <p class="lead">"Self-care" gets used so often now &mdash; on packaging, in captions, in ordinary conversation &mdash; that it can start to sound like marketing language invented for the wellness industry. It isn't. The idea is decades older than the hashtag, and its actual history is more interesting, and more useful, than a bubble bath.</p>

  <h2>Where the Phrase Actually Comes From</h2>
  <p>In medical and public-health literature, "self-care" originally described something fairly unglamorous: the everyday tasks a person does to manage their own health, from taking medication on schedule to managing a chronic condition, often without a health worker directly involved. The World Health Organization still defines it in those practical terms &mdash; as the ability of individuals, families, and communities to promote health, prevent disease, and cope with illness, with or without the support of a health worker.</p>
  <p>The phrase took on a different weight in the 1960s and 1970s, when civil rights and community-health movements in the United States began framing rest and health maintenance as something closer to a political act. Organizations including the Black Panther Party ran community health programs on the understanding that sustaining your own wellbeing was part of sustaining the work. The writer and activist Audre Lorde put it most directly in her 1988 essay collection <em>A Burst of Light</em>: "Caring for myself is not self-indulgence, it is self-preservation, and that is an act of political warfare." For Lorde and others writing in that era, self-care meant something closer to refusing burnout than to a spa afternoon.</p>

  <h2>Why It's Having Another Moment</h2>
  <p>The word re-entered everyday language gradually through the 2010s, as social media gave it a more visual, purchasable form &mdash; candles, face masks, "treat yourself" captions &mdash; and it has stayed prominent since, for reasons that are less about trends and more about circumstance. Rates of reported stress and burnout have remained a persistent topic in public-health conversation since the pandemic years, and the broader wellness industry has grown alongside that concern: the Global Wellness Institute's most recent Global Wellness Economy Monitor put the wellness economy at a record $6.8 trillion, forecast to reach $9.8 trillion by 2029. That figure spans everything from nutrition to fitness to spa and wellness tourism &mdash; a rough proxy for how many people, across how many countries, are now spending time and money on maintaining their own wellbeing rather than treating it as an afterthought.</p>

  <h2>What It Actually Looks Like, Day to Day</h2>
  <p>Strip away the marketing and most self-care research and clinical guidance points to fairly ordinary territory: consistent sleep, movement, nutrition, social connection, and boundaries around work and rest. None of it requires a purchase. But occasional, more deliberate rituals &mdash; the kind that ask you to slow down and pay attention to your body for an hour &mdash; have a place too, not as a replacement for the daily basics, but as a periodic reset that makes the daily basics easier to keep up with. A private onsen session, a massage, or simply an hour with a screen off and a book on is, in that sense, no more or less "self-care" than a good night's sleep &mdash; it's just a less frequent, more deliberate version of the same idea.</p>

  <div class="callout">The World Health Organization defines self-care as "the ability of individuals, families, and communities to promote health, prevent disease, maintain health, and to cope with illness and disability, with or without the support of a health worker." It is a broad, everyday idea &mdash; not a specific product or ritual.</div>

  <h2>Where a Ritual Like Ours Fits</h2>
  <p>We don't think a couple of hours in a private onsen room is the whole answer to burnout, and we'd rather say that plainly than oversell it. But if the occasional deliberate reset is part of how you think about looking after yourself, a quiet hour with hot water, cold water, and no phone is one reasonably well-evidenced way to spend it.</p>

  <div class="cta-block">
    <h3>An Hour, If You Have One to Spare</h3>
    <p>No agenda beyond hot onsen, ice bath, and whichever massage suits your mood &mdash; private, unhurried, and yours alone for the session. See our <a href="onsen-spa.html" style="color:inherit; text-decoration:underline;">Private Onsen Rooms &amp; Packages</a> for room details and pricing.</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">This article is provided for general educational and informational purposes and reflects publicly available historical and industry sources, cited above; it is not medical or psychological advice. If you are experiencing persistent stress, burnout, or a mental health concern, please speak with a qualified healthcare professional.</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">More From the Journal</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; Back to all guides</a>
  </div>
</div>
""".format(ctas=cta_buttons())

with open("/tmp/zenva_site/blog-self-care-history.html", "w") as f:
    f.write(page("Self-Care Isn't New: The History Behind the Word — Zenva Journal", "blog", article_body_7, blog_extra_css,
                 description="Where the phrase 'self-care' actually came from, why it's having a moment again, and what it looks like beyond candles and bath salts.", path="blog-self-care-history.html", zh_href="zh/blog-self-care-history.html"))
print("blog-self-care-history.html v4 written")


# ---------- ZH BLOG PREVIEW BUILD ----------
# Same preview-only gating as the 3 core zh pages above (index/onsen-spa/
# membership): fully built, fully linked, viewable for review — but
# intentionally NOT added to PAGE_ALTERNATES / sitemap.xml / hreflang until a
# native speaker signs off on the translation. robots.txt's blanket
# "Disallow: /zh/" already covers these new pages too, no separate change
# needed there. header()/footer() now point their zh "blog" nav link at the
# flat "blog.html" sibling inside zh/ (updated above) instead of "../blog.html".

def blog_card_zh(cat, title, teaser, photo_key, href):
    return f'''<div class="b-card"><a href="{href}"><div class="photo"><img src="{{{photo_key}}}" alt="{title}" loading="lazy"></div></a>
    <div class="body"><span class="cat">{cat}</span><h3><a href="{href}" style="color:inherit; text-decoration:none;">{title}</a></h3>
    <p>{teaser}</p><a class="read" href="{href}">阅读全文 &rarr;</a></div></div>'''

zh_blog_body = ("""
<div class="blog-hero">
  <span class="eyebrow">Zenva养生日志</span>
  <h1>关于休息、焕活与静谧仪式的札记</h1>
  <p>关于温泉沐浴、冷热交替疗法与日常焕活仪式的分享与实用心得——无论您是否已是Zenva的常客，这里都欢迎每一位对这个世界心怀好奇的人。</p>
</div>
<section class="section">
  <div class="blog-grid">
    """ + blog_card_zh("冷热交替疗法", "什么是冷热交替疗法？温泉与冰浴的功效解析",
                     "Zenva招牌仪式背后的冷热科学原理，以及如何安全地进行体验。",
                     "water", "blog-contrast-therapy.html") + """
    """ + blog_card_zh("养生指南", "私人温泉 vs. 公共温泉：两者有何不同？",
                     "私人房间还是公共浴场？了解日本温泉传统与曼谷私人温泉体验的差异。",
                     "room_sakura", "blog-private-vs-public-onsen.html") + """
    """ + blog_card_zh("实用贴士", "曼谷双人SPA日全攻略：一份简单清单",
                     "一份实用、省心的清单，助您轻松规划一场双人温泉与按摩的曼谷放松之旅。",
                     "signature", "blog-couples-spa-day-checklist.html") + """
    """ + blog_card_zh("养生指南", "泰式按摩 vs. 芳香精油按摩：该如何选择？",
                     "泰式按摩还是芳香精油按摩——初次体验者该如何根据身体状态与心情做出选择。",
                     "massage", "blog-thai-vs-aromatherapy-massage.html") + """
    """ + blog_card_zh("养生指南", "在曼谷挑选私人温泉：真正重要的事",
                     "并非所有私人温泉都一样——在付费之前，这份清单能帮您检视水质卫生、房间设计与预订灵活度。",
                     "room_bonsai", "blog-choosing-private-onsen-bangkok.html") + """
    """ + blog_card_zh("养生与焕活", "温泉体验前后：简明的护理指南",
                     "简单的补水、时间安排与安全习惯，助您从每一次冷热温泉体验中获益更多。",
                     "reception", "blog-onsen-aftercare-guide.html") + """
    """ + blog_card_zh("自我关怀", "自我关怀并不新鲜：这个「2026年热词」背后悠久的历史",
                     "这个词汇究竟从何而来，为何再度流行，以及它在蜡烛与浴盐之外真正的样子。",
                     "menu_card_onsen", "blog-self-care-history.html") + """
  </div>
</section>
""").format(**IMG)

with open("/tmp/zenva_site/zh/blog.html", "w") as f:
    f.write(page("Zenva养生日志——养生与焕活指南", "blog", zh_blog_body, blog_extra_css,
                 description="来自Zenva的实用指南——涵盖冷热交替疗法、私人温泉沐浴与SPA护理，专为曼谷私人温泉与SPA的宾客撰写。",
                 path="zh/blog.html", group="blog.html", lang="zh", en_href="../blog.html"))
print("zh/blog.html v4 written (PREVIEW — pending native-speaker review)")

# ---- ZH Article 1: Contrast Therapy ----
zh_article_body = """
<div class="article-hero">
  <span class="cat">冷热交替疗法</span>
  <h1>什么是冷热交替疗法？温泉与冰浴的功效解析</h1>
  <div class="meta">Zenva养生日志 &middot; 养生与焕活</div>
</div>
<div class="article-body">
  <p class="lead">冷热交替疗法——在热水浸浴与低温刺激之间交替进行——已成为养生圈中备受讨论的焕活方式之一。在Zenva，这正是我们私人温泉房的核心理念：一池富含矿物盐的暖汤温泉，搭配一池冰浴，私密进行，全凭您自己的节奏。</p>

  <h2>基本原理</h2>
  <p>冷热交替疗法的原理，是让身体在两种极端温度之间切换。热——无论来自热温泉、桑拿房或蒸汽房——会促使血管扩张（血管舒张），提升血液循环，帮助肌肉放松。而冷刺激则相反：它使血管收缩（血管收缩），许多人认为这有助于减轻运动后的肿胀与酸痛感。</p>
  <p>在两者之间交替，被认为能比单一温度更有效地"泵送"血液循环——热让血液流向体表与肌肉，冷则将其推回核心部位，这一反复循环正是运动恢复与SPA场景中大多数冷热交替疗法方案的基础。</p>

  <h2>人们为何选择尝试</h2>
  <ul>
    <li><strong>肌肉恢复：</strong>常见于运动、旅行或长时间站立、久坐之后。</li>
    <li><strong>精神焕新：</strong>这种剧烈的温度转换常被形容为清醒而充满能量，与单纯放松的温水浸浴截然不同。</li>
    <li><strong>血液循环：</strong>血管舒张与收缩交替的循环机制，是人们普遍认为循环改善的主要原理。</li>
    <li><strong>睡眠与压力：</strong>许多宾客将傍晚的冷热体验作为睡前的放松仪式。</li>
  </ul>
  <p>我们在这部分内容上刻意保持审慎的表述：冷热交替疗法是一项已被广泛认可的养生方式，但并非医疗手段，个体效果也因人而异。以上内容应被视为普遍反馈的益处，而非保证的结果。</p>

  <h2>典型体验流程</h2>
  <p>并没有唯一"正确"的方案，但一套简单、适合新手的流程大致如下：</p>
  <ul>
    <li>在热温泉中暖身8至12分钟。</li>
    <li>转入冰浴30至90秒——建议从较短时间开始，待适应后再逐步延长。</li>
    <li>再回到热温泉中，持续8至10分钟。</li>
    <li>重复此循环2至3次，若之后打算放松休息，建议以热结束；若想要提神效果，则以冷结束。</li>
  </ul>
  <p>在Zenva，整个流程都在同一间私人房间内完成——无需共用排期，无需等待冰池空出，也无需在寻找自己的节奏时被时间追赶。</p>

  <h3>与SPA护理的搭配</h3>
  <p>冷热循环之后，肌肉会处于温热、放松且更易被按摩深入舒缓的状态——这也是为什么我们将双人与单人套餐设计为在温泉体验后紧接芳香精油按摩或泰式按摩，而非将两者视为独立的两次到访。这正是我们"身心焕活体验"定位背后的理念：冷热仪式负责循环与焕新，按摩则负责后续的肌肉舒缓。</p>

  <div class="callout">冷热交替疗法并非适合所有人。若您患有心血管疾病、正在孕期，或有严重偏头痛病史，请在尝试冷热浸浴前咨询医生，并在预订时告知我们的前台，以便为您推荐合适的房型与时长。</div>

  <h2>前往体验前应了解与准备的事项</h2>
  <ul>
    <li>建议提前一些抵达——从曼谷的炎热天气直接跳入热温泉，若没有几分钟适应时间，效果会打折扣。</li>
    <li>体验前后请及时补水；温度循环对身体的负担大于一般的温水浴。</li>
    <li>若是第一次体验，请告知我们的团队——我们会为您讲解节奏安排，让冰浴不至于成为一种冲击。</li>
  </ul>

  <div class="cta-block">
    <h3>若您也想亲自体验</h3>
    <p>我们的盆景房与樱花房均配备热温泉与冰浴，最多可供三位宾客私密使用——随时欢迎您的到来。</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">本文内容仅供教育与一般参考之用，不构成医疗建议。若您有既往健康状况，请在开始任何冷热交替疗法体验前咨询医生。</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">更多养生日志文章</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; 返回所有文章</a>
  </div>
</div>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/blog-contrast-therapy.html", "w") as f:
    f.write(page("什么是冷热交替疗法？温泉与冰浴的功效解析 — Zenva养生日志", "blog", zh_article_body, blog_extra_css,
                 description="Zenva招牌温泉仪式背后的冷热科学原理，冷热交替疗法的运作方式，以及如何安全体验——来自曼谷私人温泉与SPA。",
                 path="zh/blog-contrast-therapy.html", group="blog-contrast-therapy.html", lang="zh", en_href="../blog-contrast-therapy.html"))
print("zh/blog-contrast-therapy.html v4 written (PREVIEW — pending native-speaker review)")

# ---- ZH Article 2: Private Onsen vs. Public Onsen ----
zh_article_body_2 = """
<div class="article-hero">
  <span class="cat">养生指南</span>
  <h1>私人温泉 vs. 公共温泉：两者有何不同？</h1>
  <div class="meta">Zenva养生日志 &middot; 养生与焕活</div>
</div>
<div class="article-body">
  <p class="lead">"温泉"这个词承载着数百年的日本沐浴文化，但如今这种体验已发展出截然不同的形式。如果您人在曼谷，正在私人温泉房与公共浴场式的共享体验之间犹豫不决，以下是两者真正的差异——以及它们为何会影响您的舒适度、隐私与时间安排。</p>

  <h2>温泉传统的起源</h2>
  <p>温泉起源于日本天然形成的矿物温泉，围绕它发展出的共浴文化，不仅是一种清洁方式，更是一种社会与文化仪式。传统礼仪相当讲究，对初次体验者而言有时颇为意外。入浴前，宾客需在独立的淋浴区彻底清洗干净，才能进入共用浴池，因为共浴池是用来浸泡放松的，而非用来清洁身体的。沐浴时不穿泳装，赤裸入浴，小毛巾完全不可带入水中——通常放在头顶或搁置一旁。设施通常按性别分开。</p>
  <p>纹身政策是温泉文化中较为复杂的一部分。由于纹身在日本历史上曾与黑帮组织产生关联，许多传统公共温泉曾限制甚至禁止有明显纹身的宾客入内。过去十年间，这一立场逐渐软化，越来越多的场所允许使用遮盖贴、提前致电获得许可，或为宾客推荐对纹身友好的场所。私人房间沐浴（在日本称为"贷切风吕"）也逐渐成为一种常见的变通方式，因为私人空间从根本上就避开了这个问题。</p>

  <h2>公共温泉：传统、社群与取舍</h2>
  <p>公共或共享式温泉保留了完整的沐浴传统：共用浸泡池、一套场所礼仪，以及往往真正社交、不慌不忙的氛围——这正是许多温泉常客钟爱之处。但取舍也是实实在在的：您需要配合场所的时间安排与礼仪规范，与陌生人共享水域与空间，并且根据场地与所在国家的不同，可能需要面对裸浴、性别分隔与纹身相关的规定，这些未必适合每一位到访者的舒适度。对某些人来说，这种共浴仪式正是意义所在。而对另一些人——情侣、有纹身的宾客、单纯偏好隐私的人，或时间有限的人——这则成为了一道门槛。</p>

  <h2>私人温泉房为何日益受欢迎</h2>
  <p>私人房间与私人池的沐浴形式并非新发明；日本的日式旅馆（Ryokan）长期以来一直提供"贷切风吕"，专门服务于情侣、家庭以及希望在不进入公共场合的情况下体验矿物温泉的纹身宾客。真正改变的，是这种形式如今传播的广度。根据全球健康研究院（Global Wellness Institute）的数据，全球温泉与矿物泉行业近年来增长显著，其中相当一部分增长集中在面向旅行者、设施更完善的高端场所——这些旅客更偏好个性化的浸浴体验，而非单纯的共浴形式。在日本以外，同样对隐私的需求也出现在曼谷这样的城市，私人温泉式房间已在养生与SPA领域中，发展成一个独立且可被清晰识别的品类——它并非取代公共传统，而是围绕时间、同伴与环境的自主权，形成的一种截然不同的选择。</p>
  <p>私人房间通常意味着：</p>
  <ul>
    <li>预订特定时间段，而非配合公共浴场的营业时间或人流高峰</li>
    <li>只与您选择的人一同沐浴——伴侣、朋友或家人</li>
    <li>无需面对纹身相关规定，因为空间不与其他沐浴者共享</li>
    <li>更灵活地在同一次到访中，将沐浴与按摩等其他护理结合</li>
  </ul>
  <p>而取舍则反映在另一面：私人房间的人均费用通常高于公共温泉，且无法提供公共浴场那种最初吸引部分访客的、充满传统气息的社交氛围。</p>

  <h2>冷热浸浴：热温泉水搭配冰浴</h2>
  <p>私人房间设置中日益普及的一种形式，是冷热交替疗法——在同一次体验中，于热矿物浴与冰浴或冷水浸浴之间交替进行。这并非某一家场所所独有；冷水浸浴与冷热交替浸浴近年来已成为更广泛的养生潮流。值得实事求是地看待其真正的科学依据：包括美国医学会（American Medical Association）汇总的相关指导在内的医学评论指出，冷热交替疗法主要提供短期效果——常见的反馈包括暂时缓解酸痛、暂时提振情绪，以及短期活动能力的改善——而非被证实的长期或治愈性益处。将其视为一种辅助性的恢复习惯，而非有保证的治疗手段，是更合理的看法；患有心血管疾病的人士通常建议在尝试冷水浸浴前先咨询医生。</p>

  <h2>那么在曼谷该如何选择？</h2>
  <p>两种形式并无绝对的"更好"——它们服务于不同的偏好。公共或共享式温泉浴场适合重视共浴传统、不介意与他人共享空间与时间安排的人。私人温泉房则适合看重隐私、希望自主选择同伴、不受纹身限制，并希望在一次预订中将泡浴与按摩等护理结合的人。如果隐私、冷热交替浸浴，以及适合情侣或小团体的空间对您而言很重要，私人房间通常是曼谷之行更为舒适的选择。</p>

  <div class="callout">Zenva的私人房间正是围绕这一理念打造：专属于您的空间、专属的热矿物盐温泉浴池，以及用于冷热交替浸浴的独立冰浴池，无需配合任何共用时间安排。</div>

  <div class="cta-block">
    <h3>Zenva能为您提供的</h3>
    <p>如果完全私密的房间正是您所偏好的，我们设有两间——盆景房与樱花房——每间都配备各自专属的热矿物盐温泉与独立冰浴池，适合单人到访、情侣或小型团体。</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">本文中的养生资讯为一般性教育内容，不构成医疗建议。冷热交替浸浴与热水浸泡并非适合所有人，包括患有心血管疾病的人士；如有健康疑虑，请在预订前咨询医生。</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">更多养生日志文章</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; 返回所有文章</a>
  </div>
</div>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/blog-private-vs-public-onsen.html", "w") as f:
    f.write(page("私人温泉 vs. 公共温泉：两者有何不同？ — Zenva养生日志", "blog", zh_article_body_2, blog_extra_css,
                 description="私人房间还是公共浴场？日本温泉传统与曼谷私人温泉体验的差异比较——来自Zenva，曼谷私人温泉与SPA。",
                 path="zh/blog-private-vs-public-onsen.html", group="blog-private-vs-public-onsen.html", lang="zh", en_href="../blog-private-vs-public-onsen.html"))
print("zh/blog-private-vs-public-onsen.html v4 written (PREVIEW — pending native-speaker review)")

# ---- ZH Article 3: Planning a Couples Spa Day in Bangkok ----
zh_article_body_3 = """
<div class="article-hero">
  <span class="cat">实用贴士</span>
  <h1>曼谷双人SPA日全攻略：一份简单清单</h1>
  <div class="meta">Zenva养生日志 &middot; 养生与焕活</div>
</div>
<div class="article-body">
  <p class="lead">一场理想的双人SPA之旅，从来不是偶然发生的——它源于事先做好的几个小决定。这份清单将带您了解出发前需要安排好的事项、该携带的物品，以及如何根据曼谷的城市节奏安排行程，让您在当天真正需要做的，只剩下放松。</p>

  <h2>1. 提前预订，并告知SPA您的需求</h2>
  <p>SPA与养生类刊物一致指出同一个首要步骤：提前预订并在抵达前就沟通好您的偏好，而不是到了现场才临时决定。如果您与伴侣希望在同一间房内接受护理，或对泰式按摩与芳香精油按摩有所偏好，请在预订时就说明，而不是抱着"到时候应该没问题"的心态。</p>
  <ul>
    <li>提前确认日期与时间段，尤其是在周末或假期。</li>
    <li>告知SPA这是一次双人或多人到访，以便他们妥善安排房间。</li>
    <li>提前询问有关护理项目或设施的任何问题，而非在护理过程中才提出。</li>
  </ul>

  <h2>2. 挑选时间时，留意曼谷的交通状况</h2>
  <p>曼谷的交通是这座城市中较容易预测的一部分——早上大约7:30至9:30，以及傍晚5:00至7:30为高峰时段，素坤逸路（Sukhumvit）与佩差布里路（Petchaburi）等路段尤其容易陷入缓慢拥堵。若能避开这些时段预订，或在无法避开时预留额外的交通时间，都能让您更从容地抵达。若道路交通看起来拥挤，BTS空铁通常是在高峰时段前往通罗（Thonglor）区域较为可靠的方式。</p>
  <ul>
    <li>尽量避免将预订时间安排在早晚高峰刚开始之时。</li>
    <li>前一晚就在地图应用中查看路线，而不是等到当天早上。</li>
    <li>若出租车或叫车软件显示交通拥堵，可考虑将BTS或MRT作为备选方案。</li>
    <li>预留15至30分钟的缓冲时间，以免行程延误挤占您的护理时间。</li>
  </ul>

  <h2>3. 轻装出行，但要带对物品</h2>
  <p>双人SPA之旅其实无需携带太多物品，但几件小东西能显著提升您的舒适度。</p>
  <ul>
    <li>护理前后穿着的宽松舒适衣物。</li>
    <li>若计划使用热水浴池，请携带泳装，并另备一套换洗衣物，以免结束后长时间穿着潮湿的衣物。</li>
    <li>若有需要，可带上发圈，以及您个人惯用的基础洗漱用品。</li>
    <li>手机请提前充满电——抵达后不妨考虑将其放入包中或寄存柜内，让彼此真正地全心投入当下。</li>
  </ul>

  <h2>4. 护理前、中、后都要及时补水</h2>
  <p>在按摩或热水浸浴前后饮水，是SPA与养生指南中几乎一致的建议，但在忙碌的一天中很容易被忽略。如果您的行程包含冷热交替式浸浴——在热水与冰浴之间切换——保持水分充足并倾听身体的反应就更为重要。请以自己的节奏进行，若有任何不宜快速温度变化的健康状况，建议跳过冰浴（或缩短时间）；如有疑虑，请先咨询医生。</p>
  <ul>
    <li>出门前先喝一杯水。</li>
    <li>抵达后以及护理结束后，再补充一些水分。</li>
    <li>逐步适应冷热水温，而非直接跳入，尤其是初次尝试时。</li>
  </ul>

  <h2>5. 当天：提前抵达、及时表达、放慢节奏</h2>
  <p>提前一点抵达，而非卡点到达，能让您和伴侣从容地办理登记、更衣与安顿——这是多份SPA礼仪指南共同建议的习惯。护理开始后，如果力度过重或过轻，或房间温度过热或过冷，请及时告知。私密的双人环境让这一切更容易开口，因为在场的只有你们二人与理疗师，而非共用的公共空间。</p>
  <ul>
    <li>建议在预订时间前10至15分钟抵达。</li>
    <li>在按摩开始前，告知任何过敏、敏感部位或需要避开的区域。</li>
    <li>交谈声音放低，手机放在一旁，让彼此真正一同放松下来。</li>
  </ul>

  <h2>6. 结束后：不要急着投入下一件事</h2>
  <p>护理结束后，给彼此留出几分钟安静的时间，再重新投入曼谷的交通或紧凑的行程。更从容的过渡方式——再喝一杯水、静坐片刻、悠然走向BTS——往往能让放松的感觉延续得更久，而不是立刻投入下一件事。</p>

  <div class="callout">本指南提供的是一般性的规划建议，并非医疗建议。若您正在孕期、患有心脏或循环系统相关疾病，或不确定冷热交替浸浴是否适合自己，请在预订冷热护理前咨询医生。</div>

  <div class="cta-block">
    <h3>一站式满足以上所有需求</h3>
    <p>这大致正是我们<a href="onsen-spa.html#couple" style="color:inherit; text-decoration:underline;">双人温泉套餐</a>背后的设计理念——两人共享的私人温泉与冰浴体验，搭配按摩护理，在盆景房或樱花房中进行——旨在让一对情侣仅需一次到访，便能完成这份清单中的大部分内容。</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">本文中的一般性SPA规划建议改编自第三方养生类刊物，仅供参考，不构成医疗建议。文中涉及Zenva的具体信息（房型、护理项目、价格区间与预订渠道）反映当前的服务内容，如有变动请以预订时的实际信息为准。</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">更多养生日志文章</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; 返回所有文章</a>
  </div>
</div>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/blog-couples-spa-day-checklist.html", "w") as f:
    f.write(page("曼谷双人SPA日全攻略：一份简单清单 — Zenva养生日志", "blog", zh_article_body_3, blog_extra_css,
                 description="一份实用、省心的清单，助您轻松规划一场双人温泉与按摩的曼谷放松之旅——来自Zenva，曼谷私人温泉与SPA。",
                 path="zh/blog-couples-spa-day-checklist.html", group="blog-couples-spa-day-checklist.html", lang="zh", en_href="../blog-couples-spa-day-checklist.html"))
print("zh/blog-couples-spa-day-checklist.html v4 written (PREVIEW — pending native-speaker review)")

# ---- ZH Article 4: Thai Massage vs. Aromatherapy Massage ----
zh_article_body_4 = """
<div class="article-hero">
  <span class="cat">养生指南</span>
  <h1>泰式按摩 vs. 芳香精油按摩：该如何选择？</h1>
  <div class="meta">Zenva养生日志 &middot; 养生与焕活</div>
</div>
<div class="article-body">
  <p class="lead">第一次预订按摩，却不确定该选择传统泰式按摩还是芳香精油按摩？这两种护理体验几乎完全不同——一种偏重主动式的伸展按压，另一种则以精油为基础、节奏舒缓——因此真正的答案，取决于您的身体与神经系统此刻真正需要的是什么。</p>

  <h2>简短的答案</h2>
  <p>如果您想针对僵硬的肌肉、紧绷的关节或受限的活动度进行深层、主动的处理，传统泰式按摩（Nuad Thai）通常是更合适的选择。如果您想要的是一种更平静、更注重感官体验，专注于舒缓压力与安抚心绪的护理，那么芳香精油按摩通常会是更舒适的选择。许多宾客会根据一周的状态在两者之间交替——若是预订双人或多人护理，也无需彼此选择相同的项目。</p>

  <h2>什么是传统泰式按摩？</h2>
  <p>泰式按摩（Nuad Thai）是泰国最古老的疗愈传统之一，其渊源常可追溯至两千多年前，并有明确记录显示曾受到印度与东南亚身体疗法的影响。泰国素可泰时期的石刻碑文中，已有关于以按摩治疗疾病的记载；到了大城王朝时期，更已设立专门的按摩机构，由专业理疗师负责。这一传统的重要性获得联合国教科文组织认可，于2019年将其列入非物质文化遗产名录。</p>
  <p>与大多数西式按摩不同，泰式按摩全程着衣进行，不使用精油，且在软垫地面而非按摩床上进行。理疗师运用掌心、拇指、手肘乃至双脚，沿着身体的能量通道（称为"Sen"经络线）施以有节奏的按压与指压，同时引导您完成一系列类似瑜伽体式的辅助伸展——因此有时也被戏称为"懒人瑜伽"。您全程保持被动；理疗师会引导您的四肢、躯干与脊柱，完成一连串伸展与按压动作。</p>
  <p>关于其功效，健康类刊物普遍指出，泰式按摩可能有助于缓解紧张性头痛、背痛、关节僵硬，并改善整体柔韧性，同时提升循环并缓解压力。一项针对传统泰式按摩用于慢性疼痛的系统性证据回顾，在所审视的试验中发现了一些支持性结果，但——正如身体疗法研究中常见的情况——该回顾也指出研究数量有限、方法不够一致，意味着现有证据令人鼓舞，但尚不足以下定论。简而言之：研究显示其可能带来实质益处，但泰式按摩终究是一种养生方式，而非医学诊断或治疗的替代品。</p>

  <h2>什么是芳香精油按摩？</h2>
  <p>芳香精油按摩将经典瑞典式按摩的手法——长而流畅的推抚、揉捏，以及整体较轻的力度——与依据香气及其舒缓或提振情绪特性所挑选的精油相结合。护理在按摩床上进行，通常使用精油，节奏比泰式按摩更缓慢、更具冥想感，其设计初衷主要是放松身心，而非深层肌肉的释放。</p>
  <p>这方面的研究结果确实较为参差，值得坦诚说明。部分随机对照试验与综述——包括一项针对芳香疗法与焦虑的随机对照试验荟萃分析，以及一项探讨姑息治疗环境中芳香精油按摩对焦虑影响的系统性回顾——报告了护理后自我评估焦虑与压力水平有所降低。一些临床资料也引用了将薰衣草芳香疗法与特定情境下睡眠改善及压力指标下降相关联的研究。与此同时，评论者也一致指出，其中许多研究样本量小、周期短，或彼此之间难以直接比较，美国国家补充与整合健康中心（NCCIH）也指出，包括芳香疗法在内的补充疗法对焦虑的证据总体仍处于初步阶段。诚实的总结是：芳香精油按摩常被反馈有助于放松与舒缓情绪，但应将其理解为一种令人愉悦、低风险的养生仪式，而非经临床证实的焦虑治疗手段。</p>

  <h2>两者对比</h2>
  <ul>
    <li><strong>力度与节奏：</strong>泰式按摩力度更强、节奏更主动；芳香精油按摩力度更轻、节奏更舒缓。</li>
    <li><strong>着装与形式：</strong>泰式按摩全程着衣，在软垫上进行，不使用精油；芳香精油按摩在按摩床上进行，使用精油，通常仅着极简衣物并覆盖床单或毛巾。</li>
    <li><strong>侧重点：</strong>泰式按摩专注于伸展、关节活动度，以及沿身体能量线的指压手法；芳香精油按摩专注于感官放松、香气体验与温和的肌肉舒缓。</li>
    <li><strong>适合人群：</strong>泰式按摩适合希望改善僵硬、紧绷或活动受限的宾客。芳香精油按摩适合主要希望放慢节奏、舒压并暂时抽离的宾客。</li>
    <li><strong>护理后的感受：</strong>泰式按摩后常让人感到舒展、"打开"；芳香精油按摩后则往往让人昏昏欲睡、深度放松。</li>
  </ul>

  <h2>该先选哪一种？</h2>
  <p>若不确定，不妨问自己一个问题：您是"酸痛"，还是"压力大"？如果因久坐办公、旅途劳顿或运动而感到酸痛、僵硬或紧绷——从泰式按摩开始。如果感到紧张、过度刺激，或单纯渴望静下心来——从芳香精油按摩开始。两者都没有错，许多常客最终会两者都尝试，看身体对哪一种反应更好。</p>

  <div class="callout">不确定该如何选择？在您到访前致电或留言告知我们当天的状态，我们的团队可以协助您做出选择。</div>

  <div class="cta-block">
    <h3>无法抉择？那就两者都体验</h3>
    <p>两项护理都在我们的菜单之中，且都能自然地与私人房间内的热矿物盐温泉浸浴，或相邻冰浴池的浸泡相搭配。单人、双人与多人预订均欢迎。</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">本文仅供一般养生资讯参考，不构成医疗建议。泰式按摩与芳香精油按摩皆不能替代合格医疗人员的诊断或治疗——若您有健康状况、正在孕期，或正在从伤病或手术中恢复，请在预订按摩前咨询医生。</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">更多养生日志文章</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; 返回所有文章</a>
  </div>
</div>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/blog-thai-vs-aromatherapy-massage.html", "w") as f:
    f.write(page("泰式按摩 vs. 芳香精油按摩：该如何选择？ — Zenva养生日志", "blog", zh_article_body_4, blog_extra_css,
                 description="泰式按摩还是芳香精油按摩？帮助初次到访的宾客选择的对比指南——来自Zenva，曼谷私人温泉与SPA。",
                 path="zh/blog-thai-vs-aromatherapy-massage.html", group="blog-thai-vs-aromatherapy-massage.html", lang="zh", en_href="../blog-thai-vs-aromatherapy-massage.html"))
print("zh/blog-thai-vs-aromatherapy-massage.html v4 written (PREVIEW — pending native-speaker review)")

# ---- ZH Article 5: Choosing a Private Onsen in Bangkok ----
zh_article_body_5 = """
<div class="article-hero">
  <span class="cat">养生指南</span>
  <h1>在曼谷挑选私人温泉：真正重要的事</h1>
  <div class="meta">Zenva养生日志 &middot; 养生与焕活</div>
</div>
<div class="article-body">
  <p class="lead">曼谷的私人温泉行业发展迅速，表面上看，大多数场所似乎相差无几：一池热水浴缸、柔和的灯光、一扇紧闭的门。而真正影响您体验——以及健康——的差异，往往并不那么显而易见。以下是预订前应当留意的重点。</p>

  <h2>"私人"不该只是一扇上锁的门</h2>
  <p>一间好的温泉，其私密性并不只体现在不与陌生人共用浴池上，更在于房间布局、隔音效果，以及空间是否真正为单一团体设计——而非只是用帘子隔开的共用池区。不妨询问一间房设计供多少宾客使用、是否每次预订仅供一组宾客使用，以及更衣与淋浴设施是否为该房间专属，还是与走廊另一端共用。</p>

  <h2>水质卫生：大多数宾客从未问过的问题</h2>
  <p>热水浴池的卫生挑战，与游泳池截然不同。美国疾病控制与预防中心（CDC）的公共卫生指南指出，温热的水温、较高的使用人次以及较小的水体容量，使热水浴池比温度较低的泳池更容易滋生细菌，并建议运营方每天多次检测消毒剂浓度与酸碱值，遵循有据可查的水质管理流程，并由受过培训的员工负责水质化学管理，而非随意处理。这些环节对入内的宾客而言完全不可见——这正是为什么值得直接开口询问。</p>
  <ul>
    <li>水是否在每次预订之间都经过过滤与处理，还是仅在固定时段进行？</li>
    <li>由谁负责检测水质、多久检测一次、依据何种标准？</li>
    <li>每接待一组新宾客，浴池是否会排空并重新注水，还是仅补充后重复使用？</li>
  </ul>
  <p>一间能够自信而具体地回答这些问题的场所——而非含糊其辞——其实正在向您传达一些关于其运营方式的真实信息。</p>

  <h2>冷热交替疗法：冰浴与温泉同样重要</h2>
  <p>冷热交替浸浴（温泉浴池搭配冷水或冰浴）已成为许多新兴私人SPA理念的标志性体验，但冰浴本身也有其独特的卫生特性——较低的水温会减缓消毒进程，因此其他地区针对冷水浸浴池的官方指南要求更频繁的水质检测，对于较小型的单次使用装置，则要求在每次使用之间进行彻底换水。如果一间场所提供冷热交替疗法，合理的做法是询问其冰浴池是否受到与热水浴池同等程度的重视，而非仅作为一项噱头式的附加体验。</p>

  <h2>护理项目的深度与员工培训</h2>
  <p>行业指南普遍指出，一间运营良好的SPA有两个关键标志：具备资质且训练有素的理疗师，以及超越浴池本身的丰富护理菜单。如果按摩或身体护理是行程的一部分，不妨询问提供哪些手法（泰式按摩与芳香精油按摩是常见的参考基准）、理疗师如何接受培训，以及护理开始前是否有简短的咨询环节，以便提前了解任何健康方面的注意事项。</p>

  <h2>双人与多人预订的灵活度</h2>
  <p>由于私人房间通常仅限接待少量宾客，一间场所如何处理双人或小团体预订就显得尤为重要。留意其是否清楚说明房间的最大容纳人数、是否可将多人安排在同一房间内，以及联系预订的便利程度——一条能得到及时回应的电话、LINE或WhatsApp联系方式，是一个运营顺畅、易于沟通的实际信号，而不仅仅是在网上容易被找到。</p>

  <h2>会员计划与复购价值</h2>
  <p>如果您可能会再次到访，不妨了解该场所是否提供会员、套餐或储值额度制度，以及其完整菜单的价格结构是否透明。价格区间跨度较大，通常意味着菜单涵盖从简单泡浴到更长护理组合的多种选择——值得与您实际计划使用的项目进行比较。</p>

  <h2>预订前应提出的问题</h2>
  <ul>
    <li>这间房在整个预订时段内，是否仅供我这一组宾客使用，包括热水浴池与冰浴在内？</li>
    <li>水质多久检测与处理一次，采用什么方式？</li>
    <li>房间设计的最大容纳人数是多少？</li>
    <li>可额外添加哪些护理项目（按摩、芳香疗法等），由谁执行？</li>
    <li>若我计划再次到访，是否有会员或储值方案？</li>
    <li>该如何实际联系场所进行预订——电话、LINE，还是WhatsApp？</li>
  </ul>

  <div class="callout">一套冷热交替体验的品质，取决于其背后的卫生管理流程。请询问具体细节，而不只是浴池的一张照片。</div>

  <div class="cta-block">
    <h3>仅供参考</h3>
    <p>我们的两间私人房间——盆景房与樱花房——各自配备一池热矿物盐温泉与独立冰浴，每间最多可供三位宾客使用——欢迎作为比较参考。</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">本文为评估曼谷私人温泉与SPA场所提供一般性指引，不构成医疗建议。冷热交替浸浴（热水与冷水浸泡）并非适合所有人；若您有心脏疾病、正在孕期，或有其他健康疑虑，请在使用前咨询医生。</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">更多养生日志文章</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; 返回所有文章</a>
  </div>
</div>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/blog-choosing-private-onsen-bangkok.html", "w") as f:
    f.write(page("在曼谷挑选私人温泉：真正重要的事 — Zenva养生日志", "blog", zh_article_body_5, blog_extra_css,
                 description="并非所有私人温泉都一样。曼谷预订前的水质卫生、房间隐私与预订灵活度实用检查清单——来自Zenva，曼谷私人温泉与SPA。",
                 path="zh/blog-choosing-private-onsen-bangkok.html", group="blog-choosing-private-onsen-bangkok.html", lang="zh", en_href="../blog-choosing-private-onsen-bangkok.html"))
print("zh/blog-choosing-private-onsen-bangkok.html v4 written (PREVIEW — pending native-speaker review)")

# ---- ZH Article 6: Before and After Your Onsen Session (Aftercare) ----
zh_article_body_6 = """
<div class="article-hero">
  <span class="cat">养生与焕活</span>
  <h1>温泉体验前后：简明的护理指南</h1>
  <div class="meta">Zenva养生日志 &middot; 养生与焕活</div>
</div>
<div class="article-body">
  <p class="lead">一场热矿物盐浸浴，接续一次冰浴的畅快体验，是一种令人满足的放松方式——但如同任何冷热交替体验一样，它也对身体提出了一些要求。体验前后的几个简单习惯，能帮助您感到平稳、焕然一新，并以最佳状态享受接下来的一天。</p>

  <h2>为何值得花几分钟做好护理</h2>
  <p>热水浴池中的时间会增加排汗，这意味着身体正在流失水分，而在冷热水之间切换，也需要循环系统快速调节。对大多数健康成年人而言，这并非需要担忧的事，但来自运动科学与健康领域的一般性指南通常建议，在热暴露与冷水浸浴前后留意补水与节奏安排，让身体能够从容适应，而不是措手不及。</p>

  <h2>体验前</h2>
  <ul>
    <li><strong>提前几小时补水。</strong>运动科学关于运动与热暴露前后补水的指南普遍建议，抵达时身体已处于良好水分状态，而非等到已经开始出汗才"临时补救"。</li>
    <li><strong>吃一些清淡的食物。</strong>在冷热交替浸浴前吃过于丰盛油腻的一餐，可能会让人感到不适；提前一小时左右吃一些清淡的点心，对许多人而言更为舒适。</li>
    <li><strong>体验前避免饮酒。</strong>健康指南普遍建议不要将饮酒与热暴露同时进行，因为酒精可能影响身体调节体温与水分平衡的能力。</li>
    <li><strong>提前一些抵达。</strong>给自己留出几分钟从容安顿的时间——而非从交通中匆忙赶来直接跳入热水浴池——能让整个过渡过程感觉更为平稳。</li>
    <li><strong>随身携带一瓶水。</strong>体验过程中手边有水，方便随时补充。</li>
  </ul>

  <h2>转换过程中：您可能会有的感受</h2>
  <p>从温暖的矿物盐温泉转入冰浴，是一种刻意设计的强烈对比，最初几秒感觉强烈是正常的。许多人形容冷水带来的初始感受是尖锐而令人清醒的，这种感觉会在短时间内缓和下来，随后回到常温环境时会感到一种温暖而放松的感觉。有些人形容这种组合既能让思绪清明，也能让身体放松，不过个体反应各有不同，一般养生指南将这些视为普遍反馈的主观感受，而非保证的结果。</p>

  <h2>体验后</h2>
  <ul>
    <li><strong>循序渐进地补水。</strong>由于热暴露会通过排汗增加水分流失，一般指南建议之后逐步补充水分，而非一次性大量饮用——对于单次体验而言，普通饮用水通常已经足够。</li>
    <li><strong>保暖并擦干身体。</strong>冰浴结束后，擦干身体并让体温以自己的节奏回到舒适状态，通常建议在此之后再重新投入接下来的行程。</li>
    <li><strong>温和活动身体。</strong>缓慢散步或轻柔伸展，可能比结束后立即静坐感觉更舒适，但无需勉强进行任何剧烈活动。</li>
    <li><strong>给自己留一点缓冲时间。</strong>许多人在冷热交替体验后会感到一阵平静或轻微的疲倦；以稍微放慢的节奏度过接下来的时间，能让这种感受延续得更久。</li>
    <li><strong>留意自身感受。</strong>轻微的放松感与头部轻盈感是常见的；若出现头晕、乏力或持续不适，应及时坐下休息、补充水分，并告知工作人员。</li>
  </ul>

  <div class="callout">提醒事项：一般健康指南建议，患有心血管疾病（如心脏病或心律不齐）、正在孕期，或有任何因快速温度变化而受影响的健康状况的人士，应在进行冷热交替浸浴前咨询医生。若您符合以上情况，请先与您的医生沟通，并在预订时告知我们的团队。</div>

  <div class="cta-block">
    <h3>一个适合实践的空间</h3>
    <p>盆景房与樱花房正是为这类体验而设计——私人的热矿物盐温泉与冰浴，搭配泰式按摩或芳香精油按摩，随时欢迎您前来实践。</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">本文仅供一般教育与自我护理参考之用，不构成医疗建议，亦不能替代合格医疗人员的指导。如您有健康状况，或对冷热交替浸浴有任何疑虑，请在预订前咨询医生。</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">更多养生日志文章</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; 返回所有文章</a>
  </div>
</div>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/blog-onsen-aftercare-guide.html", "w") as f:
    f.write(page("温泉体验前后：简明的护理指南 — Zenva养生日志", "blog", zh_article_body_6, blog_extra_css,
                 description="简单的补水、时间安排与安全习惯，助您从每一次冷热温泉体验中获益更多——来自Zenva，曼谷私人温泉与SPA。",
                 path="zh/blog-onsen-aftercare-guide.html", group="blog-onsen-aftercare-guide.html", lang="zh", en_href="../blog-onsen-aftercare-guide.html"))
print("zh/blog-onsen-aftercare-guide.html v4 written (PREVIEW — pending native-speaker review)")

# ---- ZH Article 7: Self-Care History ----
zh_article_body_7 = """
<div class="article-hero">
  <span class="cat">自我关怀</span>
  <h1>自我关怀并不新鲜：这个「2026年热词」背后悠久的历史</h1>
  <div class="meta">Zenva养生日志 &middot; 养生与焕活</div>
</div>
<div class="article-body">
  <p class="lead">"自我关怀"这个词如今被使用得如此频繁——出现在包装上、社交媒体配文里、日常对话中——以至于它开始听起来像是养生行业为营销而创造出来的说法。但事实并非如此。这个理念的历史，远比这个热词标签古老得多，其真正的来龙去脉，也比一场泡泡浴更耐人寻味、更有实际意义。</p>

  <h2>这个词汇究竟从何而来</h2>
  <p>在医学与公共卫生文献中，"自我关怀"最初描述的其实是一件颇为朴实的事：个人为管理自身健康而做的日常事务，从按时服药到应对慢性病，往往并不直接需要医护人员的介入。世界卫生组织至今仍以这种务实的方式对其进行定义——即个人、家庭与社区在有或没有医护人员支持的情况下，促进健康、预防疾病并应对疾病的能力。</p>
  <p>这个词汇在1960至1970年代承载了另一层不同的分量，当时美国的民权运动与社区健康运动，开始将休息与健康维护视为更接近政治行动的事情。包括黑豹党在内的一些组织，秉持"维系自身的健康，正是维系这份事业的一部分"这一理念，开展了社区健康项目。作家兼活动家奥德丽·洛德（Audre Lorde）在其1988年的散文集《A Burst of Light》中最为直接地表达了这一点："照顾好自己，不是放纵，而是自我保存，这本身就是一种政治抗争的行为。"对洛德以及那个时代其他持相同观点的作者而言，"自我关怀"更接近于拒绝被耗尽，而非一个SPA午后。</p>

  <h2>为何它再度成为热议话题</h2>
  <p>进入2010年代，这个词逐渐重新进入日常语言，社交媒体赋予了它更具视觉化、更"可购买"的形式——蜡烛、面膜、"犒赏自己"的配文——此后它的存在感一直居高不下，原因与其说是潮流，不如说是现实处境使然。自疫情时期以来，压力与职业倦怠的报告数据，一直是公共卫生讨论中的持续话题，而更广泛的养生行业也随之增长：全球健康研究院（Global Wellness Institute）最新的《全球健康经济监测报告》显示，全球健康经济规模已达到创纪录的6.8万亿美元，预计到2029年将增长至9.8万亿美元。这一数字涵盖了从营养、健身到SPA与养生旅游的方方面面——大致反映出，在多少个国家中，有多少人正将时间与金钱投入到维护自身健康之中，而不再将其视为可有可无的附属品。</p>

  <h2>它在日常生活中真正的样子</h2>
  <p>剥去营销的外衣，大多数关于自我关怀的研究与临床指导，指向的其实是相当平常的领域：规律的睡眠、运动、饮食、社交联系，以及在工作与休息之间设立界限。这些都无需任何消费。但偶尔更为刻意的仪式——那种要求您放慢脚步、花上一小时专注于自己身体感受的时刻——同样有其价值，它并非要取代日常的基本习惯，而是作为一种周期性的重启，让日常的坚持变得更容易维系。从这个意义上说，一次私人温泉体验、一次按摩，或仅仅是关掉屏幕、捧起一本书的一小时，与一夜好眠相比，并没有更多或更少的"自我关怀"成分——它只是同一个理念更不频繁、更为刻意的版本。</p>

  <div class="callout">世界卫生组织将自我关怀定义为"个人、家庭与社区在有或没有医护人员支持的情况下，促进健康、预防疾病、维持健康并应对疾病与残障的能力。"这是一个宽泛的日常理念——而非某种特定的产品或仪式。</div>

  <h2>像我们这样的仪式，适合放在哪里</h2>
  <p>我们并不认为在私人温泉房中度过几个小时，就是解决职业倦怠的全部答案，我们也更愿意坦率地这样说，而不是过度承诺。但如果偶尔刻意的重启，是您照顾自己方式的一部分，那么一段安静的时光——热水、冷水，没有手机——是一种有一定依据支持的、值得尝试的方式。</p>

  <div class="cta-block">
    <h3>若您愿意抽出一小时</h3>
    <p>没有额外的安排，只有热温泉、冰浴，以及最契合您心情的按摩——私密、从容，这段时光完全属于您自己。</p>
    <div class="cta-group" style="justify-content:center;">{ctas}</div>
  </div>

  <p class="disclaimer">本文仅供一般教育与资讯参考之用，内容基于上文引用的公开历史与行业资料来源，不构成医疗或心理建议。若您正经历持续的压力、职业倦怠或心理健康方面的困扰，请咨询合格的医疗专业人士。</p>

  <div style="margin-top:36px; padding-top:24px; border-top:1px solid var(--line);">
    <span class="eyebrow" style="display:block; margin-bottom:10px;">更多养生日志文章</span>
    <a href="blog.html" style="color:var(--ink); font-weight:700; text-decoration:none; font-size:14px;">&larr; 返回所有文章</a>
  </div>
</div>
""".format(ctas=cta_buttons_zh())

with open("/tmp/zenva_site/zh/blog-self-care-history.html", "w") as f:
    f.write(page("自我关怀并不新鲜：这个词的历史 — Zenva养生日志", "blog", zh_article_body_7, blog_extra_css,
                 description="「自我关怀」这个词究竟从何而来，为何再度流行，以及它在蜡烛与浴盐之外真正的样子——来自Zenva，曼谷私人温泉与SPA。",
                 path="zh/blog-self-care-history.html", group="blog-self-care-history.html", lang="zh", en_href="../blog-self-care-history.html"))
print("zh/blog-self-care-history.html v4 written (PREVIEW — pending native-speaker review)")

# ---------- TH (THAI) PREVIEW BUILD ----------
# Client approved (2026-08-24): "Full commercial site" scope — all 7 English
# commercial pages (Home, Rooms & Packages, Contrast Therapy, Couples Spa,
# Massage & Spa, Membership, Visit Us), no blog translation yet. Unlike zh
# (translated against the OLD pre-P1 architecture and never re-synced —
# flagged separately for correction), th is built from scratch against the
# CURRENT (post-P1) English page structure, so its internal links are correct
# from day one (couples-spa-bangkok.html / massage-spa-bangkok.html /
# location-thonglor-bangkok.html as real destinations, not #anchors).
# Same PDPA/legal-review + native-speaker-review gates apply as zh: this is a
# PREVIEW build only — kept out of PAGE_ALTERNATES/sitemap.xml and blocked via
# robots.txt (Disallow: /th/) until approved. See master-brief.md.
os.makedirs("/tmp/zenva_site/th", exist_ok=True)

th_index_body = """
<section class="hero-carousel">
  <div class="hero-track">
    <div class="hero-slide">
      <div class="hero-bg" style="background-image:url('{hero}');" role="img" aria-label="Private onsen room with a guest seated at the edge of the hot bath"></div><div class="hero-scrim"></div>
      <div class="hero-content">
        <span class="eyebrow">การบำบัดความร้อนสลับเย็น &middot; ฟื้นฟูครบวงจร</span>
        <h1>ออนเซ็นร้อน น้ำแข็งเย็น ฟื้นฟูร่างกายอย่างสมบูรณ์ แบบส่วนตัวทั้งหมด</h1>
        <p class="sub">สลับความร้อนจากออนเซ็นแร่ธาตุกับความเย็นจากน้ำแข็ง &mdash; พิธีกรรมบำบัดความร้อนสลับเย็นที่ช่วยฟื้นฟูกล้ามเนื้อและคลายความเหนื่อยล้าทางจิตใจ &mdash; จากนั้นเติมเต็มด้วยทรีตเมนต์สปาซิกเนเจอร์เพื่อประสบการณ์ฟื้นฟูที่ครบถ้วนยิ่งขึ้น เป็นส่วนตัวทั้งหมด รองรับสูงสุด 3 ท่าน</p>
        <div class="cta-group">{ctas}</div>
      </div>
    </div>
  </div>
</section>
<div class="why-strip">
  <div class="section-head" style="margin-bottom:34px;">
    <span class="eyebrow">ปรัชญาแห่งความสงบ</span>
  </div>
  <div class="why-grid">
    <div class="why-item"><span class="why-num">ร้อนและเย็น</span><h3>การบำบัดความร้อนสลับเย็น อย่างพิถีพิถัน</h3><p>ความร้อนจากออนเซ็นแร่ธาตุและความเย็นจากน้ำแข็ง อยู่ในห้องส่วนตัวเดียวกัน &mdash; พิธีกรรมฟื้นฟูที่กำลังได้รับความสนใจไปทั่วโลก ที่นี่เราปฏิบัติด้วยความตั้งใจจริง ไม่ใช่เพียงกระแสความนิยม</p><a class="link" style="font-size:12px; font-weight:700; color:var(--gold-text); text-decoration:none; display:inline-block; margin-top:8px;" href="contrast-therapy-ice-bath-bangkok.html">เรียนรู้เพิ่มเติม &rarr;</a></div>
    <div class="why-item"><span class="why-num">ความเป็นส่วนตัว</span><h3>เป็นของคุณเพียงผู้เดียว</h3><p>ไม่มีการใช้พื้นที่อาบน้ำร่วมกัน ไม่มีตารางเวลาส่วนกลาง แต่ละห้องเป็นของคุณโดยเฉพาะ &mdash; ไม่ว่าจะเป็นคู่รัก หรือกลุ่มเพื่อนสนิทสูงสุด 3 ท่าน</p></div>
    <div class="why-item"><span class="why-num">งานฝีมือ</span><h3>รายละเอียดที่พิถีพิถันและเงียบสงบ</h3><p>น้ำแร่เกลือแท้และวัสดุที่คัดสรรอย่างพิถีพิถัน เลือกใช้เพื่อการฟื้นฟูที่แท้จริง มากกว่าเพื่อความสวยงามในภาพถ่าย</p></div>
  </div>
</div>
<section class="section" id="menu">
  <div class="section-head"><span class="eyebrow">สำรวจ</span><h2>เมนูของเรา</h2><p>สามหมวดหมู่หลัก &mdash; ดูเมนูและราคาเต็มได้ในแต่ละหน้าด้านล่าง</p></div>
  <div class="cards">
    <div class="card">
      <div class="thumb"><img src="{menu_card_onsen}" alt="Guest relaxing against the glowing Himalayan salt wall inside the private sauna" loading="lazy"></div>
      <div class="body"><span class="kicker">การบำบัดความร้อนสลับเย็น</span><h3>ห้องออนเซ็นส่วนตัว</h3>
      <p>ห้อง Bonsai (ห้องซาวน่า) และห้อง Sakura (ห้องอบไอน้ำ) &mdash; น้ำแข็ง ออนเซ็นแร่ธาตุ ซาวน่าเกลือหิมาลัย รองรับสูงสุด 3 ท่าน</p>
      <div class="price-row"><span class="price">เริ่มต้น 3,190+ บาท</span><a class="link" href="onsen-spa.html">ดูเมนูเต็ม &rarr;</a></div></div>
    </div>
    <div class="card">
      <div class="thumb"><img src="{massage_card}" alt="Therapist giving an aromatherapy massage" loading="lazy"></div>
      <div class="body"><span class="kicker">สำหรับคู่รัก</span><h3>แพ็กเกจออนเซ็นคู่รัก</h3>
      <p>ชุดผสมออนเซ็นและนวดสำหรับ 2 ท่าน ระยะเวลา 120&ndash;150 นาทีแห่งพิธีกรรมร่วมกัน</p>
      <div class="price-row"><span class="price">เริ่มต้น 4,900+ บาท</span><a class="link" href="couples-spa-bangkok.html">ดูเมนูเต็ม &rarr;</a></div></div>
    </div>
    <div class="card">
      <div class="thumb"><img src="{signature_card}" alt="Zenva signature spa treatment tray" loading="lazy"></div>
      <div class="body"><span class="kicker">ฟื้นฟูครบวงจร</span><h3>คอลเลกชันสปาและนวด</h3>
      <p>นวดอโรมาเธอราพีสุดหรู นวดไทยแท้ และ Zenva Spa เวียดนาม 18 ขั้นตอน &mdash; พิธีกรรมดูแลผม หู และใบหน้า</p>
      <div class="price-row"><span class="price">เริ่มต้น 590+ บาท</span><a class="link" href="massage-spa-bangkok.html">ดูเมนูเต็ม &rarr;</a></div></div>
    </div>
  </div>
</section>
<section class="section" style="background:var(--cream-soft); padding-top:76px; padding-bottom:76px;" id="location">
  <div class="split">
    <div class="photo"><img src="{reception}" alt="Zenva storefront and reception at Seenspace Thonglor" loading="lazy"></div>
    <div><span class="eyebrow">พื้นที่ของเรา</span><h2>ห้องส่วนตัวอันเงียบสงบ</h2>
    <p>ทุกการมาเยือนเริ่มต้นแบบเดียวกัน &mdash; ห้องส่วนตัว พิธีกรรมส่วนตัว ไม่มีพื้นที่รอร่วมกัน ที่ Seenspace Thonglor ชั้น 3</p>
    <p style="color:var(--ink-soft); font-size:14px; margin-bottom:18px;">เปิดทุกวัน 12:00&ndash;00:00 น.</p>
    <a class="btn-outline" href="location-thonglor-bangkok.html">เวลาทำการและเส้นทาง &rarr;</a>
    <a href="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor" target="_blank" rel="noopener" style="margin-left:14px; font-size:12.5px; font-weight:700; color:var(--gold-text); text-decoration:none;">นำทาง &rarr;</a></div>
  </div>
  <div style="max-width:1100px; margin:40px auto 0; border-radius:8px; overflow:hidden; border:1px solid var(--line);">
    <iframe src="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor&output=embed" width="100%" height="320" style="border:0; display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Zenva location map"></iframe>
  </div>
</section>
<div class="mem-teaser">
  <span class="eyebrow" style="color:var(--cream);">สิทธิพิเศษเพื่อสุขภาพ</span>
  <h2>สมาชิก 4 ระดับ</h2>
  <p>Silver, Gold, Diamond และ Platinum &mdash; ใช้ได้กับบริการออนเซ็น สปา และนวดทั้งหมด</p>
  <a class="btn-outline" style="color:var(--cream); border-color:var(--cream);" href="membership.html">ดูรายละเอียดสมาชิก &rarr;</a>
</div>
<section class="section" id="gallery">
  <div class="section-head"><span class="eyebrow">ภายใน Zenva</span><h2>แกลเลอรี</h2></div>
  <div class="gallery-grid" id="galleryGrid">
    <div class="g-item g-tall" data-full="{g1}" data-caption="Sakura steam room, after dark">
      <div class="g-bg"><img src="{g1}" alt="Sakura steam room at night, lit by warm ambient light beneath cherry blossoms" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g7}" data-caption="An evening in the Bonsai room">
      <div class="g-bg"><img src="{g7}" alt="Guest seated at the edge of the Bonsai onsen bath among the greenery" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g2}" data-caption="A session in progress">
      <div class="g-bg"><img src="{g2}" alt="Therapist performing a treatment in a private room" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g3}" data-caption="Ear-candling treatment detail">
      <div class="g-bg"><img src="{g3}" alt="Ear-candling spa treatment detail" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g8}" data-caption="The Zenva welcome ritual">
      <div class="g-bg"><img src="{g8}" alt="Zenva welcome tray with branded linen and aromatherapy salts" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g4}" data-caption="The Zenva sign, framed by blossoms">
      <div class="g-bg"><img src="{g4}" alt="The Zenva sign framed by blossom branches at the entrance" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item" data-full="{g5}" data-caption="Welcome tea &amp; mango sticky rice">
      <div class="g-bg"><img src="{g5}" alt="Welcome tea and mango sticky rice" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g6}" data-caption="Candlelight by the water">
      <div class="g-bg"><img src="{g6}" alt="Guest holding a candle beside the onsen water" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g9}" data-caption="Massage chairs with personal streaming">
      <div class="g-bg"><img src="{g9}" alt="Guest reclining in a premium massage chair, streaming entertainment on the personal screen" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g10}" data-caption="Into the salt-wall sauna">
      <div class="g-bg"><img src="{g10}" alt="Guest stepping into the Himalayan salt-wall sauna, silhouetted in the evening light" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
    <div class="g-item g-tall" data-full="{g11}" data-caption="The rain shower, ready">
      <div class="g-bg"><img src="{g11}" alt="Overhead rain showerhead beside the private spa treatment bed" loading="lazy"></div><div class="g-scrim"></div><div class="g-zoom">{ZOOM_ICON}</div></div>
  </div>
</section>
<div class="g-lightbox" id="gLightbox">
  <span class="g-lightbox-close" id="gLightboxClose">&times;</span>
  <span class="g-lightbox-nav g-lightbox-prev" id="gLightboxPrev">&#8249;</span>
  <img id="gLightboxImg" src="" alt="">
  <span class="g-lightbox-nav g-lightbox-next" id="gLightboxNext">&#8250;</span>
</div>
<script>
(function(){{
  var items = Array.prototype.slice.call(document.querySelectorAll("#galleryGrid .g-item"));
  if(!items.length) return;
  var lb = document.getElementById("gLightbox");
  var lbImg = document.getElementById("gLightboxImg");
  var idx = 0;
  function open(i){{
    idx = i;
    lbImg.src = items[idx].getAttribute("data-full");
    lbImg.alt = items[idx].getAttribute("data-caption") || "";
    lb.classList.add("show");
  }}
  function close(){{ lb.classList.remove("show"); lbImg.src = ""; }}
  function step(d){{ idx = (idx + d + items.length) % items.length; lbImg.src = items[idx].getAttribute("data-full"); lbImg.alt = items[idx].getAttribute("data-caption") || ""; }}
  items.forEach(function(el, i){{ el.addEventListener("click", function(){{ open(i); }}); }});
  document.getElementById("gLightboxClose").addEventListener("click", close);
  document.getElementById("gLightboxPrev").addEventListener("click", function(){{ step(-1); }});
  document.getElementById("gLightboxNext").addEventListener("click", function(){{ step(1); }});
  lb.addEventListener("click", function(e){{ if(e.target === lb) close(); }});
  document.addEventListener("keydown", function(e){{
    if(!lb.classList.contains("show")) return;
    if(e.key === "Escape") close();
    if(e.key === "ArrowLeft") step(-1);
    if(e.key === "ArrowRight") step(1);
  }});
}})();
</script>
<section class="section" id="reels" style="background:var(--cream-soft);">
  <div class="section-head"><span class="eyebrow">ภาพเคลื่อนไหว</span><h2>Zenva Reels</h2><p>ภาพใกล้ชิดยิ่งขึ้น จากโซเชียลมีเดียของเราโดยตรง</p></div>
  <div class="reels-grid" id="reelsGrid">
    <video muted loop playsinline preload="metadata">
      <source src="{reel1_webm}" type="video/webm">
      <source src="{reel1_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel3_webm}" type="video/webm">
      <source src="{reel3_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel5_webm}" type="video/webm">
      <source src="{reel5_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel6_webm}" type="video/webm">
      <source src="{reel6_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel7_webm}" type="video/webm">
      <source src="{reel7_mp4}" type="video/mp4">
    </video>
    <video muted loop playsinline preload="metadata">
      <source src="{reel8_webm}" type="video/webm">
      <source src="{reel8_mp4}" type="video/mp4">
    </video>
  </div>
</section>
<script>
(function(){{
  var vids = Array.prototype.slice.call(document.querySelectorAll("#reelsGrid video"));
  if(!vids.length) {{ return; }}
  if(!('IntersectionObserver' in window)){{
    vids.forEach(function(v){{ v.play().catch(function(){{}}); }});
  }} else {{
    var io = new IntersectionObserver(function(entries){{
      entries.forEach(function(entry){{
        if(entry.isIntersecting){{ entry.target.play().catch(function(){{}}); }}
        else {{ entry.target.pause(); }}
      }});
    }}, {{threshold: 0.25}});
    vids.forEach(function(v){{ io.observe(v); }});
  }}
}})();
</script>
<section class="section" id="reviews">
  <div class="section-head"><span class="eyebrow">เสียงจากผู้ใช้บริการ &middot; 4.8&#9733; บน Google &middot; 267 รีวิว</span><h2>รีวิวดีเยี่ยมบน Google</h2></div>
  <div class="testimonials" id="reviewsGrid">
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>We had booked the couple's private Bonsai Sauna experience&mdash;Himalayan pink salt sauna, one of a kind place... Although it looked very aesthetic with the beautiful decor and ambient lighting&hellip;</p>
      <div class="t-foot">
        <div class="who">The Traveler<span>รีวิว 41 รายการในกรุงเทพฯ</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/31Vv077s7GpMqaAt1" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>I booked the private Sakura onsen room, which includes a hot onsen bath, a cold plunge, and a steam room. The facilities felt quite new and the room was very private, making the whole experience feel calm and exclusive&hellip;</p>
      <div class="t-foot">
        <div class="who">Ami Narissara<span>ไกด์ท้องถิ่น &middot; 38 รีวิว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/iXiLC4lhTXhcnjVvc" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>My wife and I had such a great private onsen experience here today&hellip; Genuinely great, and such a good location! Highly, highly recommend.</p>
      <div class="t-foot">
        <div class="who">Jonathan O'Callaghan<span>ไกด์ท้องถิ่น &middot; 32 รีวิว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/eoyRkCzlwQwFBk5jO" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Great service and place is clean. The therapy person is very great.</p>
      <div class="t-foot">
        <div class="who">P. Panyasakorn<span>4 สัปดาห์ที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/FagUAf6goHtcNnEit" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Amazing spa in Thonglor with a great variety of treatments. Really enjoy both the steam &amp; sauna rooms. Will definitely be coming back.</p>
      <div class="t-foot">
        <div class="who">Zach Cohen<span>1 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/rH4tOAehC1tibdiBU" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>A really nice relaxing and experience for the weekend. The overall atmosphere is made for peace in body and mind. Definitely gonna come back to this place.</p>
      <div class="t-foot">
        <div class="who">Nichalee T.<span>1 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/gADn1tD0YCyQUoYmo" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Nice and clean onsen. You can have a private room and relax fully. Massage is good, they have lemongrass oil&mdash;very nice smell.</p>
      <div class="t-foot">
        <div class="who">&#1070;&#1083;&#1080;&#1103; &#1040;&#1079;&#1072;&#1088;&#1080;&#1085;&#1072;<span>1 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/IpmrWLS77bBxlBe29" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>I had Jaae as my masseuse, and she was absolutely wonderful&hellip; Her hands have a magic touch, and the massage was one of the best I've ever experienced.</p>
      <div class="t-foot">
        <div class="who">omar ben sellam<span>2 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/G6e7orSjqXAH3x2C1" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>Private onsen and spa in the middle of Thong lo. I spent 2 hrs here. The Mineral salt Japanese onsen and Ice bath are awesome. Highly recommend this place!</p>
      <div class="t-foot">
        <div class="who">natthawat ru<span>4 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/n2oqeuPcMZWwguBGk" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>What a great experience. I was looking for a relaxation spa with wellness, a cold plunge, and a sauna, and this place had it all&hellip; Apple was incredibly kind and welcoming. Highly recommended!</p>
      <div class="t-foot">
        <div class="who">&#1491;&#1504;&#1497;&#1488;&#1500; &#1488;&#1500;&#1506;&#1494;&#1512;<span>7 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/4vderGJuuPJYkh8Fm" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>We tried this new place as it just opened and took the 2 hour private onsen + Vietnamese Spa session. It was very refreshing and the place looks gorgeous! Highly recommend!</p>
      <div class="t-foot">
        <div class="who">Robert<span>8 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/iZrE5f6zwqdjUs49D" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
    <div class="t-card">
      <div class="t-mark">&ldquo;</div>
      <p>A newly opened spa on Thonglor Soi 13 offers an elevated relaxation experience with private onsens, Vietnamese spa rituals, and dedicated neck&ndash;shoulder massages&hellip; The therapists are exceptional&mdash;strong, precise hands with truly professional technique.</p>
      <div class="t-foot">
        <div class="who">Ek-kapop<span>8 เดือนที่แล้ว</span></div>
        <div class="t-rating">5.0 &#9733;</div>
      </div>
      <a class="read-more" href="https://share.google/Pr0SYhJPXkMRlpKEY" target="_blank" rel="noopener">อ่านบน Google &rarr;</a>
    </div>
  </div>
  <div class="reviews-nav">
    <button type="button" id="reviewsPrev">&#8249; ก่อนหน้า</button>
    <span class="reviews-page-count" id="reviewsPageCount"></span>
    <button type="button" id="reviewsNext">ถัดไป &#8250;</button>
  </div>
</section>
<script>
(function(){{
  var grid = document.getElementById("reviewsGrid");
  if(!grid) return;
  var cards = Array.prototype.slice.call(grid.children);
  var perPage = 4;
  var pages = Math.ceil(cards.length / perPage) || 1;
  var page = 0;
  var prevBtn = document.getElementById("reviewsPrev");
  var nextBtn = document.getElementById("reviewsNext");
  var countEl = document.getElementById("reviewsPageCount");
  function render(){{
    cards.forEach(function(card, i){{
      card.style.display = (Math.floor(i / perPage) === page) ? "" : "none";
    }});
    if(prevBtn) prevBtn.disabled = (page === 0);
    if(nextBtn) nextBtn.disabled = (page === pages - 1);
    if(countEl) countEl.textContent = (page + 1) + " / " + pages;
  }}
  if(prevBtn) prevBtn.addEventListener("click", function(){{ if(page > 0){{ page--; render(); }} }});
  if(nextBtn) nextBtn.addEventListener("click", function(){{ if(page < pages - 1){{ page++; render(); }} }});
  render();
}})();
</script>
<section class="section" id="contact" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">ติดต่อ</span><h2 style="margin-bottom:14px;">จองพิธีกรรมของคุณ</h2>
  <p style="color:var(--ink-soft); margin-bottom:24px;">แชทกับพนักงานต้อนรับของเราโดยตรง &mdash; ตอบกลับทันทีในช่วงเวลาทำการ</p>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons_th(), ZOOM_ICON=ZOOM_ICON, **IMG, **VID)

with open("/tmp/zenva_site/th/index.html", "w") as f:
    f.write(page("Zenva — Private Onsen & Spa | Private Onsen Bangkok", "home", th_index_body, index_extra_css,
                 description="ออนเซ็นร้อนส่วนตัวและห้องบำบัดความร้อนสลับเย็นด้วยน้ำแข็งในกรุงเทพฯ พร้อมทรีตเมนต์สปาซิกเนเจอร์ เป็นส่วนตัวทั้งหมด รองรับสูงสุด 3 ท่าน ที่ Seenspace Thonglor",
                 path="th/index.html", group="index.html", lang="th", en_href="../index.html", zh_href="../zh/index.html", hero_image=IMG["hero"]))
print("th/index.html v4 written (PREVIEW — pending native-speaker review)")

# th/onsen-spa.html — "Private Onsen Rooms & Packages". Built against the
# CURRENT trimmed English page (Bonsai/Sakura rooms only — the old combined
# menu was already split out in P1), not the old structure. The room-intro
# paragraph links to blog-contrast-therapy.html, which has NO Thai translation
# in scope — that one link deliberately points to the English article
# ("../blog-contrast-therapy.html") with a plain-language "(EN)" note so a
# Thai reader isn't surprised to land on an English page.
th_services_body = ("""
<div class="page-hero">
  <span class="eyebrow">ห้องออนเซ็นส่วนตัว</span>
  <h1>ห้องออนเซ็นส่วนตัวในกรุงเทพฯ — Bonsai และ Sakura</h1>
  <p>Bonsai และ Sakura — ห้องส่วนตัวเต็มรูปแบบ พร้อมออนเซ็นน้ำแร่ร้อน อ่างน้ำแข็ง และห้องซาวน่าหรือห้องอบไอน้ำ รองรับสูงสุด 3 ท่าน</p>
</div>
<section class="section" id="rooms">
  <div class="menu-block">
    <div class="menu-title-bar"><h2>ออนเซ็นส่วนตัว</h2><span>สูงสุด 3 ท่าน &middot; เริ่มต้น 60 นาที</span></div>
    <div class="room-pair">
      <div class="room-card bonsai">
        <div class="photo"><img src="{room_bonsai}" alt="Bonsai private onsen room with sauna" loading="lazy"><span class="tag">Bonsai &middot; ห้องซาวน่า</span></div>
        <div class="info"><div class="desc">อ่างน้ำแข็ง ออนเซ็นน้ำแร่ร้อนสไตล์ญี่ปุ่น ห้องซาวน่าผนังเกลือหิมาลัย</div>
        <div class="price-line"><span class="amt">3,190+ บาท</span><span class="dur">ต่อห้อง / 60 นาที</span></div>
        <div class="addon">เพิ่มเวลา: 1,000+ บาท / 15 นาที</div></div>
      </div>
      <div class="room-card sakura">
        <div class="photo"><img src="{room_sakura}" alt="Sakura private onsen room with steam room" loading="lazy"><span class="tag">Sakura &middot; ห้องอบไอน้ำ</span></div>
        <div class="info"><div class="desc">อ่างน้ำแข็ง ออนเซ็นน้ำแร่ร้อนสไตล์ญี่ปุ่น และห้องอบไอน้ำ</div>
        <div class="price-line"><span class="amt">3,190+ บาท</span><span class="dur">ต่อห้อง / 60 นาที</span></div>
        <div class="addon">เพิ่มเวลา: 1,000+ บาท / 15 นาที</div></div>
      </div>
    </div>
    <p class="room-intro">ห้องแต่ละห้องเป็นส่วนตัวอย่างสมบูรณ์ตลอดระยะเวลาที่คุณจอง &mdash; ไม่มีการใช้พื้นที่อาบน้ำร่วมกัน ไม่มีตารางเวลาส่วนกลาง อ่างออนเซ็นน้ำแร่ร้อนจับคู่กับอ่างน้ำแข็งแยกต่างหากสำหรับการแช่สลับร้อนเย็น พร้อมด้วยห้องซาวน่าผนังเกลือหิมาลัย (Bonsai) หรือห้องอบไอน้ำ (Sakura) เซสชันเริ่มต้นที่ 60 นาทีและขยายเวลาได้ครั้งละ 15 นาที ทั้งสองห้องรองรับได้สบายสูงสุด 3 ท่าน หากคุณยังใหม่กับการแช่น้ำสลับร้อนเย็น หรือสงสัยว่าเหมาะกับคุณหรือไม่ หน้า <a href="contrast-therapy-ice-bath-bangkok.html">การบำบัดความร้อนสลับเย็น อ่างน้ำแข็ง และซาวน่า</a> ของเราอธิบายโครงสร้างของเซสชันไว้ และ <a href="../blog-contrast-therapy.html">คู่มือการบำบัดความร้อนสลับเย็นจากบล็อกของเรา (EN)</a> เจาะลึกประโยชน์ที่มีการรายงานไว้ และใครควรปรึกษาแพทย์ก่อน</p>
  </div>
</section>
""" + bundle_section_th() + """
<p class="vat-note">ราคาทั้งหมดยังไม่รวมภาษีมูลค่าเพิ่ม 7%</p>
<section class="section">
  <div class="section-head"><span class="eyebrow">สำรวจเพิ่มเติม</span><h2>วางแผนการมาเยือน</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{menu_card_onsen}" alt="แขกกำลังผ่อนคลายในห้องซาวน่าเกลือหิมาลัยส่วนตัว" loading="lazy"></div><div class="body"><h4>การบำบัดความร้อนสลับเย็น อ่างน้ำแข็ง และซาวน่า</h4><p>พิธีกรรมบำบัดความร้อนสลับเย็นแบบเต็มรูปแบบ อธิบายอย่างละเอียด</p><div class="price-tag">เริ่มต้น 3,190+ บาท</div><a href="contrast-therapy-ice-bath-bangkok.html">เรียนรู้เพิ่มเติม &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="นักบำบัดกำลังนวดในห้องทรีตเมนต์ส่วนตัว" loading="lazy"></div><div class="body"><h4>ประสบการณ์สปาคู่รัก</h4><p>แพ็กเกจออนเซ็นและนวดที่ออกแบบมาสำหรับสองท่าน</p><div class="price-tag">เริ่มต้น 4,900+ บาท</div><a href="couples-spa-bangkok.html">ดูแพ็กเกจ &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{hero}" alt="ห้องออนเซ็นส่วนตัวที่ Zenva" loading="lazy"></div><div class="body"><h4>สมาชิก</h4><p>ระดับเครดิตสมาชิก Silver, Gold, Diamond และ Platinum</p><div class="price-tag">เริ่มต้น 10,000 บาทเครดิต</div><a href="membership.html">ดูระดับสมาชิก &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="หน้าร้านและเคาน์เตอร์ต้อนรับ Zenva ที่ Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>มาเยือนเรา</h4><p>ที่อยู่ เวลาทำการ และเส้นทาง</p><a href="location-thonglor-bangkok.html">ดูเส้นทาง &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">พร้อมจองแล้วหรือยัง?</span><h2 style="margin-bottom:14px;">จองพิธีกรรมของคุณ</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""").format(ctas=cta_buttons_th(), **IMG)

with open("/tmp/zenva_site/th/onsen-spa.html", "w") as f:
    f.write(page("ห้องออนเซ็นส่วนตัวและแพ็กเกจ กรุงเทพฯ | Zenva Thonglor", "services", th_services_body, services_extra_css,
                 description="ห้องออนเซ็นส่วนตัวย่านทองหล่อ กรุงเทพฯ — Bonsai และ Sakura พร้อมออนเซ็นน้ำแร่ร้อน อ่างน้ำแข็ง และห้องซาวน่าหรือห้องอบไอน้ำ เริ่มต้น 3,190+ บาท รองรับสูงสุด 3 ท่าน",
                 path="th/onsen-spa.html", group="onsen-spa.html", lang="th", en_href="../onsen-spa.html", zh_href="../zh/onsen-spa.html", hero_image=IMG["room_bonsai"]))
print("th/onsen-spa.html v4 written (PREVIEW — pending native-speaker review)")

# th/contrast-therapy-ice-bath-bangkok.html. The medical-caution callout and
# disclaimer are translated as precisely as possible — nothing softened or
# dropped — since this is the one page on the site making health-adjacent
# claims. Links to blog-contrast-therapy.html (no Thai translation in scope)
# point to the English article with an "(EN)" note, same pattern as onsen-spa.html.
th_contrast_body = """
<div class="page-hero">
  <span class="eyebrow" style="color:var(--cream);">ร้อนและเย็น</span>
  <h1>การบำบัดความร้อนสลับเย็น อ่างน้ำแข็ง และซาวน่าในกรุงเทพฯ</h1>
  <p>ออนเซ็นแร่ธาตุร้อน อ่างน้ำแข็ง และห้องซาวน่าผนังเกลือหิมาลัยหรือห้องอบไอน้ำ &mdash; เป็นส่วนตัวทั้งหมด อยู่ในห้องเดียวกัน ตามจังหวะของคุณเอง</p>
</div>
<section class="section">
  <div class="ct-body">
    <p>การบำบัดความร้อนสลับเย็นหมายถึงการสลับระหว่างการแช่น้ำร้อนและการสัมผัสความเย็นในเซสชันเดียวกัน ที่ Zenva สิ่งนี้ถูกออกแบบไว้ในห้องส่วนตัวทั้งสองห้องของเรา ได้แก่ อ่างออนเซ็นน้ำแร่เกลือร้อนคู่กับอ่างน้ำแข็งแยกต่างหาก พร้อมด้วยห้องซาวน่าผนังเกลือหิมาลัยในห้อง Bonsai หรือห้องอบไอน้ำในห้อง Sakura</p>

    <h2>เซสชันดำเนินการอย่างไร</h2>
    <p>ไม่มีขั้นตอนตายตัว แต่จังหวะง่ายๆ ที่เหมาะสำหรับผู้เริ่มต้นคือ วอร์มร่างกายในออนเซ็นร้อนประมาณ 8&ndash;12 นาที จากนั้นย้ายไปแช่ในอ่างน้ำแข็ง 30&ndash;90 วินาที กลับมาที่ออนเซ็นร้อนอีก 8&ndash;10 นาที และทำซ้ำ 2&ndash;3 รอบ &mdash; จบด้วยความอุ่นเพื่อผ่อนคลาย หรือจบด้วยความเย็นเพื่อความรู้สึกกระปรี้กระเปร่า เนื่องจากห้องเป็นส่วนตัวทั้งหมดตลอดการจองของคุณ จึงไม่มีตารางเวลาที่ต้องแบ่งปันกับผู้อื่น และไม่มีใครต้องรอใช้อ่างน้ำเย็น</p>

    <h2>ประโยชน์ที่มีการรายงานโดยทั่วไป</h2>
    <ul>
      <li><strong>การฟื้นฟูกล้ามเนื้อ</strong> หลังการออกกำลังกาย การเดินทาง หรือการยืนหรือนั่งเป็นเวลานาน</li>
      <li><strong>การรีเซ็ตทางจิตใจ</strong> &mdash; การเปลี่ยนแปลงอุณหภูมิมักถูกอธิบายว่าช่วยให้รู้สึกปลอดโปร่งและมีพลัง</li>
      <li><strong>การไหลเวียนโลหิต</strong> &mdash; ความร้อนขยายหลอดเลือด ความเย็นทำให้หลอดเลือดหดตัว และการสลับทั้งสองอย่างเป็นพื้นฐานของแนวทางการบำบัดความร้อนสลับเย็นส่วนใหญ่</li>
    </ul>
    <p>เราตั้งใจนำเสนอส่วนนี้อย่างระมัดระวัง: การบำบัดความร้อนสลับเย็นเป็นแนวทางปฏิบัติด้านสุขภาพที่ได้รับการยอมรับอย่างกว้างขวาง ไม่ใช่การรักษาทางการแพทย์ และผลลัพธ์อาจแตกต่างกันไปในแต่ละบุคคล สำหรับคำอธิบายที่ละเอียดยิ่งขึ้น &mdash; รวมถึงคำแนะนำทีละขั้นตอนสำหรับผู้เริ่มต้น &mdash; โปรดดู<a href="../blog-contrast-therapy.html">บทความจากบล็อกของเราเกี่ยวกับการบำบัดความร้อนสลับเย็น (EN)</a></p>

    <div class="ct-price-card">
      <div class="amt">3,190+ บาท</div>
      <div class="unit">ต่อห้อง &middot; 60 นาที &middot; สูงสุด 3 ท่าน &middot; เพิ่มเวลา 1,000+ บาท / 15 นาที</div>
    </div>

    <div class="ct-callout">การบำบัดความร้อนสลับเย็นไม่เหมาะสำหรับทุกคน หากคุณมีโรคหัวใจและหลอดเลือด กำลังตั้งครรภ์ หรือมีประวัติไมเกรนรุนแรง โปรดปรึกษาแพทย์ก่อนลองการแช่น้ำสลับร้อนเย็น และแจ้งให้พนักงานต้อนรับของเราทราบเมื่อคุณจอง เพื่อให้เราสามารถให้คำแนะนำเรื่องห้องและระยะเวลาที่เหมาะสม</div>

    <h2>จับคู่กับทรีตเมนต์สปา</h2>
    <p>วงจรร้อนเย็นทำให้กล้ามเนื้ออบอุ่นและพร้อมรับการนวด นี่คือเหตุผลที่แพ็กเกจสำหรับคู่รักและเดี่ยวของเราจบเซสชันออนเซ็นด้วยนวดอโรมาเธอราพีหรือนวดไทย แทนที่จะแยกเป็นสองการมาเยือน ดู<a href="onsen-spa.html">ห้องออนเซ็นส่วนตัวและแพ็กเกจ</a>ฉบับเต็ม หรือเมนู<a href="massage-spa-bangkok.html">นวดและทรีตเมนต์สปา</a>แบบเดี่ยว</p>

    <p class="disclaimer">หน้านี้มีจุดประสงค์เพื่อให้ความรู้ทั่วไปเท่านั้น ไม่ใช่คำแนะนำทางการแพทย์ หากคุณมีภาวะสุขภาพที่เป็นอยู่ก่อน โปรดปรึกษาแพทย์ก่อนเริ่มการปฏิบัติการแช่น้ำสลับร้อนเย็นใดๆ</p>
  </div>
</section>
<section class="section">
  <div class="section-head"><span class="eyebrow">สำรวจเพิ่มเติม</span><h2>วางแผนการมาเยือน</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="ห้องออนเซ็นส่วนตัว Bonsai พร้อมซาวน่า" loading="lazy"></div><div class="body"><h4>ห้องออนเซ็นส่วนตัว</h4><p>รายละเอียดห้อง Bonsai และ Sakura พร้อมราคาเต็ม</p><div class="price-tag">เริ่มต้น 3,190+ บาท</div><a href="onsen-spa.html">จองห้อง &rarr;</a></div></div>
    <div class="crosslink-card no-thumb"><div class="body"><h4>คู่มือการบำบัดความร้อนสลับเย็น</h4><p>บทความเชิงลึกจากบล็อกของเรา (EN)</p><a href="../blog-contrast-therapy.html">อ่านคู่มือ &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="นักบำบัดกำลังนวดในห้องทรีตเมนต์ส่วนตัว" loading="lazy"></div><div class="body"><h4>ประสบการณ์สปาคู่รัก</h4><p>แบ่งปันพิธีกรรมร่วมกัน &mdash; ออนเซ็นและนวดสำหรับสองท่าน</p><div class="price-tag">เริ่มต้น 4,900+ บาท</div><a href="couples-spa-bangkok.html">ดูแพ็กเกจ &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="หน้าร้านและเคาน์เตอร์ต้อนรับ Zenva ที่ Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>มาเยือนเรา</h4><p>ที่อยู่ เวลาทำการ และเส้นทาง</p><a href="location-thonglor-bangkok.html">ดูเส้นทาง &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">พร้อมจองแล้วหรือยัง?</span><h2 style="margin-bottom:14px;">จองพิธีกรรมของคุณ</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons_th(), **IMG)

with open("/tmp/zenva_site/th/contrast-therapy-ice-bath-bangkok.html", "w") as f:
    f.write(page("อ่างน้ำแข็งและการบำบัดความร้อนสลับเย็น | Zenva Thonglor", "services", th_contrast_body, contrast_extra_css,
                 description="ออนเซ็นร้อน อ่างน้ำแข็ง และห้องซาวน่าหรือห้องอบไอน้ำ เป็นส่วนตัวทั้งหมด ย่านทองหล่อ กรุงเทพฯ จองเซสชันบำบัดความร้อนสลับเย็นที่ Zenva ได้แล้ววันนี้ เริ่มต้น 3,190 บาท",
                 path="th/contrast-therapy-ice-bath-bangkok.html", group="contrast-therapy-ice-bath-bangkok.html", lang="th", en_href="../contrast-therapy-ice-bath-bangkok.html", og_image=IMG["water"]))
print("th/contrast-therapy-ice-bath-bangkok.html v4 written (PREVIEW — pending native-speaker review)")

# th/couples-spa-bangkok.html — reuses the generic couple_table() helper
# (labels/rows are just parameters, no hardcoded English inside it) with
# Thai package data and headers.
th_bonsai_packages = [
    ("+ นวดอโรมาเธอราพี", "120 นาที", "5,900+ บาท"),
    ("+ นวดอโรมาเธอราพี (เพิ่มเวลา)", "150 นาที", "7,900+ บาท"),
    ("+ เลือก 2 รายการสปาเวียดนาม", "120 นาที", "4,900+ บาท"),
    ("+ คอร์สสปาเวียดนามเต็มรูปแบบ", "150 นาที", "5,900+ บาท"),
]
th_sakura_packages = list(th_bonsai_packages)

th_couples_body = ("""
<div class="page-hero">
  <span class="eyebrow">สำหรับคู่รัก</span>
  <h1>ประสบการณ์ออนเซ็นและสปาส่วนตัวสำหรับคู่รัก — กรุงเทพฯ</h1>
  <p>แช่ออนเซ็นร้อนและอ่างน้ำแข็งส่วนตัวร่วมกัน จากนั้นผ่อนคลายไปด้วยกันด้วยการนวด &mdash; ในห้อง Bonsai หรือ Sakura ที่เป็นของคุณเพียงผู้เดียวตลอดการมาเยือน</p>
</div>
<section class="section" id="couple">
  <p style="max-width:700px; margin:0 auto 34px; text-align:center; font-size:14px; color:var(--ink-soft); line-height:1.8;">แต่ละแพ็กเกจออนเซ็นคู่รักผสมผสานออนเซ็นน้ำแร่ร้อนและอ่างน้ำแข็งในห้องส่วนตัว เข้ากับทรีตเมนต์นวดสำหรับสองท่าน ไม่ว่าจะเป็นห้อง Bonsai (ซาวน่า) หรือห้อง Sakura (ไอน้ำ) ตัวเลือกนวดเสริมและระยะเวลาเหมือนกันทั้งสองห้อง</p>
  <div class="menu-block">
    <div class="couple-pair">
      """ + couple_table("bonsai", "Bonsai ซาวน่า", th_bonsai_packages, headers=("แพ็กเกจ", "ระยะเวลา", "ราคา")) + couple_table("sakura", "Sakura ไอน้ำ", th_sakura_packages, headers=("แพ็กเกจ", "ระยะเวลา", "ราคา")) + """
    </div>
  </div>
</section>
<p class="vat-note">ราคาทั้งหมดยังไม่รวมภาษีมูลค่าเพิ่ม 7%</p>
<section class="section">
  <div class="section-head"><span class="eyebrow">สำรวจเพิ่มเติม</span><h2>วางแผนการมาเยือน</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="ห้องออนเซ็นส่วนตัว Bonsai พร้อมซาวน่า" loading="lazy"></div><div class="body"><h4>ห้องออนเซ็นส่วนตัว</h4><p>รายละเอียดห้องเต็มรูปแบบ ความจุ และราคาเริ่มต้น</p><div class="price-tag">เริ่มต้น 3,190+ บาท</div><a href="onsen-spa.html">ดูห้องพัก &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{hero}" alt="ห้องออนเซ็นส่วนตัวที่ Zenva" loading="lazy"></div><div class="body"><h4>สมาชิก</h4><p>ระดับเครดิตสมาชิก Silver, Gold, Diamond และ Platinum</p><div class="price-tag">เริ่มต้น 10,000 บาทเครดิต</div><a href="membership.html">ดูระดับสมาชิก &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{signature_card}" alt="ถาดทรีตเมนต์สปาซิกเนเจอร์ของ Zenva" loading="lazy"></div><div class="body"><h4>นวดและทรีตเมนต์สปา</h4><p>ทรีตเมนต์แบบเดี่ยว คิดราคาแยกต่างหาก</p><div class="price-tag">เริ่มต้น 590+ บาท</div><a href="massage-spa-bangkok.html">ดูเมนู &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="หน้าร้านและเคาน์เตอร์ต้อนรับ Zenva ที่ Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>มาเยือนเรา</h4><p>ที่อยู่ เวลาทำการ และเส้นทาง</p><a href="location-thonglor-bangkok.html">ดูเส้นทาง &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">พร้อมจองแล้วหรือยัง?</span><h2 style="margin-bottom:14px;">จองพิธีกรรมของคุณ</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""").format(ctas=cta_buttons_th(), **IMG)

with open("/tmp/zenva_site/th/couples-spa-bangkok.html", "w") as f:
    f.write(page("สปาคู่รัก กรุงเทพฯ | ออนเซ็นส่วนตัวสำหรับสองท่าน — Zenva Thonglor", "services", th_couples_body, couples_extra_css,
                 description="แช่ออนเซ็นร้อนและอ่างน้ำแข็งส่วนตัวร่วมกัน จากนั้นผ่อนคลายไปด้วยกันด้วยการนวด — แพ็กเกจออนเซ็นคู่รักของ Zenva ย่านทองหล่อ กรุงเทพฯ",
                 path="th/couples-spa-bangkok.html", group="couples-spa-bangkok.html", lang="th", en_href="../couples-spa-bangkok.html", og_image=IMG["massage"]))
print("th/couples-spa-bangkok.html v4 written (PREVIEW — pending native-speaker review)")

# th/massage-spa-bangkok.html — reuses the generic spa_col() helper with Thai
# titles/rows. The "Thai vs. Aromatherapy Massage" comparison link points to
# the English blog article (no Thai translation in scope), same "(EN)" pattern
# as the other two pages above.
th_luxury_rows = [("นวดอโรมาเธอราพี — 60 นาที", "1,590+ บาท"), ("นวดอโรมาเธอราพี — 90 นาที", "2,390+ บาท")]
th_thai_rows = [("นวดเท้า / ศีรษะ / คอ / บ่า — 30 นาที", "590+ บาท"), ("— 60 นาที", "790+ บาท"), ("— 90 นาที", "1,090+ บาท"), ("— 120 นาที", "1,390+ บาท")]
th_signature_rows = [("เลือก 1 รายการ: ผม / หู / ใบหน้า — 30 นาที", "690+ บาท"), ("เลือก 2 รายการ — 60 นาที", "1,290+ บาท"), ("Zenva Spa เวียดนาม 18 ขั้นตอน (ผม หู และใบหน้า) ครบทั้ง 3 รายการ — 90 นาที", "1,590+ บาท")]

th_massage_page_body = ("""
<div class="page-hero">
  <span class="eyebrow">ทรีตเมนต์แบบเดี่ยว</span>
  <h1>นวดและทรีตเมนต์สปาในย่านทองหล่อ กรุงเทพฯ</h1>
  <p>นวดอโรมาเธอราพีสุดหรู นวดไทยแบบดั้งเดิม และพิธีกรรมสปาซิกเนเจอร์แรงบันดาลใจจากเวียดนามของ Zenva &mdash; ไม่จำเป็นต้องใช้ห้องออนเซ็น</p>
</div>
<section class="section" id="spa">
  <div class="menu-block">
    <div class="room-pair spa-photo-row" style="margin-bottom:26px;">
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{massage_card}" alt="Therapist performing an aromatherapy massage" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;"></div>
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{chair_card}" alt="Guest reclining in a premium massage chair, streaming entertainment on a personal screen" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center 25%;"></div>
      <div style="border-radius:8px; overflow:hidden; height:230px; position:relative;"><img src="{vietnamese_card}" alt="Traditional Vietnamese ear-cleaning treatment, part of the 18-Steps Zenva Spa" loading="lazy" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover;"></div>
    </div>
    <div class="spa-grid">
      """ + spa_col("สปาสุดหรู", th_luxury_rows) + spa_col("สปาไทยแท้", th_thai_rows,
          note="นั่งพักผ่อนในเก้าอี้นวดพรีเมียมพร้อมหน้าจอส่วนตัว เพื่อให้คุณสามารถรับชมความบันเทิงของตัวเองได้ระหว่างผ่อนคลาย") \
        + spa_col("Zenva Signature Spa", th_signature_rows) + """
    </div>
    <p style="max-width:700px; margin:26px auto 0; font-size:13px; color:var(--ink-soft); line-height:1.8; text-align:center;">ไม่แน่ใจว่านวดไทยหรือนวดอโรมาเธอราพีเหมาะกับคุณมากกว่ากัน? บล็อกของเราเปรียบเทียบทั้งสองแบบไว้ใน <a href="../blog-thai-vs-aromatherapy-massage.html" style="color:var(--gold-text); font-weight:700; text-decoration:none;">นวดไทย เทียบกับ นวดอโรมาเธอราพี (EN)</a></p>
  </div>
</section>
<p class="vat-note">ราคาทั้งหมดยังไม่รวมภาษีมูลค่าเพิ่ม 7%</p>
<section class="section">
  <div class="section-head"><span class="eyebrow">สำรวจเพิ่มเติม</span><h2>วางแผนการมาเยือน</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="ห้องออนเซ็นส่วนตัว Bonsai พร้อมซาวน่า" loading="lazy"></div><div class="body"><h4>ห้องออนเซ็นส่วนตัว</h4><p>จับคู่ทรีตเมนต์ใดก็ได้กับออนเซ็นร้อนและอ่างน้ำแข็ง</p><div class="price-tag">เริ่มต้น 3,190+ บาท</div><a href="onsen-spa.html">ดูห้องพัก &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{hero}" alt="ห้องออนเซ็นส่วนตัวที่ Zenva" loading="lazy"></div><div class="body"><h4>สมาชิก</h4><p>ระดับเครดิตสมาชิก Silver, Gold, Diamond และ Platinum</p><div class="price-tag">เริ่มต้น 10,000 บาทเครดิต</div><a href="membership.html">ดูระดับสมาชิก &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="นักบำบัดกำลังนวดในห้องทรีตเมนต์ส่วนตัว" loading="lazy"></div><div class="body"><h4>ประสบการณ์สปาคู่รัก</h4><p>แพ็กเกจออนเซ็นและนวดที่ออกแบบมาสำหรับสองท่าน</p><div class="price-tag">เริ่มต้น 4,900+ บาท</div><a href="couples-spa-bangkok.html">ดูแพ็กเกจ &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="หน้าร้านและเคาน์เตอร์ต้อนรับ Zenva ที่ Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>มาเยือนเรา</h4><p>ที่อยู่ เวลาทำการ และเส้นทาง</p><a href="location-thonglor-bangkok.html">ดูเส้นทาง &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">พร้อมจองแล้วหรือยัง?</span><h2 style="margin-bottom:14px;">จองพิธีกรรมของคุณ</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""").format(ctas=cta_buttons_th(), **IMG)

with open("/tmp/zenva_site/th/massage-spa-bangkok.html", "w") as f:
    f.write(page("นวดอโรมาเธอราพีและนวดไทย กรุงเทพฯ | Zenva Spa ทองหล่อ", "services", th_massage_page_body, massage_page_extra_css,
                 description="นวดอโรมาเธอราพี นวดไทยแบบดั้งเดิม และทรีตเมนต์สปาซิกเนเจอร์แรงบันดาลใจจากเวียดนามของ Zenva — ย่านทองหล่อ กรุงเทพฯ เริ่มต้น 590 บาท",
                 path="th/massage-spa-bangkok.html", group="massage-spa-bangkok.html", lang="th", en_href="../massage-spa-bangkok.html", og_image=IMG["signature"]))
print("th/massage-spa-bangkok.html v4 written (PREVIEW — pending native-speaker review)")

# th/membership.html — tier NAMES (Silver/Gold/Diamond/Platinum) are kept in
# English rather than given new Thai brand names, unlike zh's "静荟" identity.
# That zh naming was a specific client-requested creative rebrand for Chinese;
# no equivalent request was made for Thai, and English tier names are common
# practice in Thai spa/hotel membership programs, so surrounding copy is
# translated while the tier names themselves stay as-is. Flagged here for the
# client to confirm or override during native-speaker review.
def tier_th(name, pay, regular_amt, regular_bonus, promo_amt=None, promo_bonus=None, best=False, platinum=False):
    cls = "tier tier-platinum" if platinum else "tier"
    best_html = '<span class="best-value">คุ้มค่าที่สุด</span>' if best else ""
    if promo_amt:
        price_block = f"""
        <div class="regular-line">มูลค่าปกติ: <s>{regular_amt} เครดิต ({regular_bonus})</s></div>
        <div class="promo-box">
          <span class="promo-flag">อัปเกรดจำกัดเวลา</span>
          <div class="promo-amount">{promo_amt} <span class="unit">เครดิต</span></div>
          <span class="promo-bonus">{promo_bonus}</span>
        </div>
        """
    else:
        price_block = f"""<div class="regular-price"><span class="amount">{regular_amt}</span> เครดิต <span style="font-weight:400;">({regular_bonus})</span></div>"""
    return f"""<div class="{cls}">{best_html}
      <span class="tier-badge">ระดับ {name}</span>
      <span class="tier-name">{name}</span>
      <div class="pay-row">ชำระ {pay} บาท</div>
      {price_block}
      <ul><li>ใช้ได้กับบริการออนเซ็น สปา และนวดทั้งหมด</li><li>มีอายุ 12 เดือน</li><li>ไม่สามารถโอนสิทธิ์ได้</li></ul>
    </div>"""

th_membership_body = """
<div class="page-hero">
  <span class="eyebrow" style="color:var(--cream);">สิทธิพิเศษเพื่อสุขภาพ</span>
  <h1>สมาชิก</h1>
  <p>มูลค่าเครดิตปกติของทุกระดับ พร้อมโปรโมชั่นอัปเกรดจำกัดเวลาที่แสดงแยกต่างหาก</p>
</div>
<section class="section">
  <div class="tier-cards">
    """ + tier_th("Silver", "10,000", "11,000", "+1,000 โบนัส", promo_amt="13,000", promo_bonus="+3,000 โบนัส") + \
        tier_th("Gold", "30,000", "36,000", "+6,000 โบนัส", promo_amt="45,000", promo_bonus="+15,000 โบนัส") + \
        tier_th("Diamond", "50,000", "65,000", "+15,000 โบนัส") + \
        tier_th("Platinum", "100,000", "150,000", "+50,000 โบนัส", best=True, platinum=True) + """
  </div>
</section>
<section class="section" style="background:var(--cream-soft);">
  <div class="section-head"><span class="eyebrow">ข้อกำหนด</span><h2>ข้อกำหนดสมาชิก</h2></div>
  <div style="max-width:700px; margin:0 auto; font-size:13.5px; color:var(--ink-soft); line-height:1.9;">
    เครดิตสามารถใช้ได้กับบริการทั้งหมดของ Zenva เครดิตไม่สามารถโอนสิทธิ์หรือขอคืนเงินได้ สมาชิกภาพมีอายุ 12 เดือนนับจากวันที่ซื้อ และต้องใช้ก่อนวันหมดอายุ เครดิตไม่สามารถแลกเปลี่ยนเป็นเงินสดได้ Zenva ขอสงวนสิทธิ์ในการแก้ไขข้อกำหนดเหล่านี้โดยไม่ต้องแจ้งล่วงหน้า
  </div>
</section>
<section class="section">
  <div class="section-head"><span class="eyebrow">สำรวจเพิ่มเติม</span><h2>ใช้เครดิตของคุณ</h2></div>
  <div class="crosslink-grid" style="grid-template-columns:repeat(2,1fr); max-width:640px;">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="ห้องออนเซ็นส่วนตัว Bonsai พร้อมซาวน่า" loading="lazy"></div><div class="body"><h4>ห้องออนเซ็นส่วนตัว</h4><p>ใช้เครดิตกับห้อง Bonsai หรือ Sakura</p><div class="price-tag">เริ่มต้น 3,190+ บาท</div><a href="onsen-spa.html">ดูห้องพัก &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{reception}" alt="หน้าร้านและเคาน์เตอร์ต้อนรับ Zenva ที่ Seenspace Thonglor" loading="lazy"></div><div class="body"><h4>มาเยือนเรา</h4><p>ที่อยู่ เวลาทำการ และเส้นทาง</p><a href="location-thonglor-bangkok.html">ดูเส้นทาง &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center;">
  <span class="eyebrow">เริ่มต้นเป็นสมาชิก</span><h2 style="margin-bottom:14px;">สอบถามพนักงานต้อนรับของเรา</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons_th(), **IMG)

with open("/tmp/zenva_site/th/membership.html", "w") as f:
    f.write(page("สมาชิก | Zenva Private Onsen & Spa กรุงเทพฯ", "membership", th_membership_body, membership_extra_css,
                 description="ระดับเครดิตสมาชิกของ Zenva — Silver, Gold, Diamond และ Platinum — ใช้ได้กับบริการออนเซ็น สปา และนวดส่วนตัวทั้งหมดในกรุงเทพฯ",
                 path="th/membership.html", group="membership.html", lang="th", en_href="../membership.html", zh_href="../zh/membership.html"))
print("th/membership.html v4 written (PREVIEW — pending native-speaker review)")

# th/location-thonglor-bangkok.html — same NAP-completeness note as the
# English page: street/soi number and postal code are still not supplied
# (client chose "Skip for now" on P1-8), so nothing is invented here either.
# The address/hours facts translated below are the same facts already used
# sitewide (matching th footer/index), not new claims.
th_location_body = """
<div class="page-hero">
  <span class="eyebrow">ทองหล่อ กรุงเทพฯ</span>
  <h1>มาเยือน Zenva &mdash; ทองหล่อ กรุงเทพฯ</h1>
  <p>ที่อยู่แบบเต็ม เวลาทำการ และเส้นทางไปยัง Zenva Private Onsen &amp; Spa</p>
</div>
<section class="section">
  <div class="nap-grid">
    <div class="nap-block">
      <h3>ที่อยู่</h3>
      <p>Zenva &mdash; Private Onsen &amp; Spa<br>ซีนสเปซ ทองหล่อ ชั้น 3 (FL 03-01)<br>เลขที่ 251/1 ซอยทองหล่อ 13 แขวงคลองตันเหนือ เขตวัฒนา<br>กรุงเทพฯ 10110</p>
      <h3>เวลาทำการ</h3>
      <p>เปิดทุกวัน 12:00&ndash;00:00 น.</p>
      <h3>ติดต่อและการจอง</h3>
      <p>โทร: <a href="tel:+66802629191">+66 80 262 9191</a><br>หรือจองโดยตรงผ่าน LINE หรือ WhatsApp ด้านล่าง</p>
      <a class="btn-outline" href="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor" target="_blank" rel="noopener">ดูเส้นทาง &rarr;</a>
    </div>
    <div class="nap-block">
      <h3>การเดินทางมาที่นี่</h3>
      <p>Seenspace Thonglor สามารถเดินถึงได้จาก BTS ทองหล่อ โดยรถไฟฟ้า BTS มักเป็นวิธีที่เชื่อถือได้ในการเดินทางมายังพื้นที่นี้หากการจราจรบนถนนดูหนาแน่น &mdash; การจราจรในกรุงเทพฯ บนถนนใกล้เคียงอย่างสุขุมวิทมักหนาแน่นที่สุดในช่วงประมาณ 7:30&ndash;9:30 น. และ 17:00&ndash;19:30 น. การจองนอกช่วงเวลาดังกล่าว หรือเผื่อเวลาเดินทางเพิ่มเติม จะช่วยให้คุณมาถึงได้อย่างไม่เร่งรีบ</p>
    </div>
  </div>
  <div style="max-width:1100px; margin:0 auto; border-radius:8px; overflow:hidden; border:1px solid var(--line);">
    <iframe src="https://www.google.com/maps?q=Zenva+Private+Onsen+%26+Spa+Seenspace+Thonglor&output=embed" width="100%" height="360" style="border:0; display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Zenva location map"></iframe>
  </div>
</section>
<section class="section">
  <div class="section-head"><span class="eyebrow">สำรวจเพิ่มเติม</span><h2>สำรวจ Zenva</h2></div>
  <div class="crosslink-grid">
    <div class="crosslink-card"><div class="thumb"><img src="{room_bonsai}" alt="ห้องออนเซ็นส่วนตัว Bonsai พร้อมซาวน่า" loading="lazy"></div><div class="body"><h4>ห้องออนเซ็นส่วนตัว</h4><p>รายละเอียดห้อง Bonsai และ Sakura พร้อมราคา</p><div class="price-tag">เริ่มต้น 3,190+ บาท</div><a href="onsen-spa.html">ดูห้องพัก &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{menu_card_onsen}" alt="แขกกำลังผ่อนคลายในห้องซาวน่าเกลือหิมาลัยส่วนตัว" loading="lazy"></div><div class="body"><h4>การบำบัดความร้อนสลับเย็น อ่างน้ำแข็ง และซาวน่า</h4><p>เซสชันร้อนเย็นทำงานอย่างไร</p><div class="price-tag">เริ่มต้น 3,190+ บาท</div><a href="contrast-therapy-ice-bath-bangkok.html">เรียนรู้เพิ่มเติม &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{massage_card}" alt="นักบำบัดกำลังนวดในห้องทรีตเมนต์ส่วนตัว" loading="lazy"></div><div class="body"><h4>ประสบการณ์สปาคู่รัก</h4><p>แพ็กเกจออนเซ็นและนวดสำหรับสองท่าน</p><div class="price-tag">เริ่มต้น 4,900+ บาท</div><a href="couples-spa-bangkok.html">ดูแพ็กเกจ &rarr;</a></div></div>
    <div class="crosslink-card"><div class="thumb"><img src="{signature_card}" alt="ถาดทรีตเมนต์สปาซิกเนเจอร์ของ Zenva" loading="lazy"></div><div class="body"><h4>นวดและทรีตเมนต์สปา</h4><p>ทรีตเมนต์แบบเดี่ยว คิดราคาแยกต่างหาก</p><div class="price-tag">เริ่มต้น 590+ บาท</div><a href="massage-spa-bangkok.html">ดูเมนู &rarr;</a></div></div>
  </div>
</section>
<section class="section" style="text-align:center; background:var(--cream-soft);">
  <span class="eyebrow">พร้อมจองแล้วหรือยัง?</span><h2 style="margin-bottom:14px;">จองพิธีกรรมของคุณ</h2>
  <div class="cta-group" style="justify-content:center;">{ctas}</div>
</section>
""".format(ctas=cta_buttons_th(), **IMG)

with open("/tmp/zenva_site/th/location-thonglor-bangkok.html", "w") as f:
    f.write(page("มาเยือนเรา — Zenva Private Onsen & Spa ทองหล่อ กรุงเทพฯ", "location", th_location_body, location_extra_css,
                 description="Zenva Private Onsen & Spa เลขที่ 251/1 ซอยทองหล่อ 13 แขวงคลองตันเหนือ เขตวัฒนา กรุงเทพฯ 10110 เวลาทำการ เส้นทางจาก BTS ทองหล่อ และวิธีการจอง",
                 path="th/location-thonglor-bangkok.html", group="location-thonglor-bangkok.html", lang="th", en_href="../location-thonglor-bangkok.html", og_image=IMG["reception"]))
print("th/location-thonglor-bangkok.html v4 written (PREVIEW — pending native-speaker review)")

# ---------- PRIVACY & COOKIE POLICY (v2 — self-certified against official Thailand PDPC guidance, 2026-08-28) ----------
privacy_extra_css = """
  .legal-body{{max-width:760px; margin:0 auto; padding:50px 24px 70px; font-size:14.5px; line-height:1.85; color:var(--ink);}}
  .legal-body h1{{font-size:32px; margin-bottom:6px;}}
  .legal-body .updated{{font-size:12.5px; color:var(--ink-soft); margin-bottom:30px;}}
  .legal-body h2{{font-size:19px; margin:32px 0 12px;}}
  .legal-body h3{{font-size:15.5px; margin:22px 0 8px;}}
  .legal-body p{{margin-bottom:14px; color:var(--ink-soft);}}
  .legal-body ul{{margin:0 0 14px 20px; color:var(--ink-soft);}}
  .legal-body li{{margin-bottom:6px;}}
  .legal-body table{{width:100%; border-collapse:collapse; margin:14px 0 20px; font-size:13px;}}
  .legal-body th, .legal-body td{{border:1px solid var(--line); padding:8px 10px; text-align:left; vertical-align:top;}}
  .legal-body th{{background:var(--cream-soft);}}
  .legal-notice{{background:#fff8e6; border:1px solid var(--gold); border-radius:6px; padding:16px 20px; font-size:13px; color:var(--ink); margin-bottom:30px;}}
""".format()

privacy_body = """
<div class="legal-body">
  <span class="uxnote">DRAFT — for internal review before publishing. This policy was prepared with reference to Thailand's official PDPA guidance (the Personal Data Protection Committee's published guidelines and sub-regulations), at the business owner's direction, rather than reviewed by outside legal counsel. It is not a substitute for professional legal advice, and Zenva accepts the residual compliance risk of that choice. Please give this a final read before it is published.</span>
  <h1>Privacy &amp; Cookie Policy</h1>
  <div class="updated">Draft last updated: 28 August 2026 &middot; Not yet published</div>

  <div class="legal-notice">This policy is aligned to Thailand's Personal Data Protection Act B.E. 2562 (2019) ("PDPA") and the Personal Data Protection Committee's official guidelines: the <em>Guideline on Procedures for Notifying the Purpose and Details relating to the Collection of Personal Data from Data Subjects</em> and the <em>Guideline on Requesting Consent from the Data Subject</em> (both issued 7 September 2022), plus the 2023 sub-regulation on Data Protection Officer designation under Section 41(2). It has not been reviewed by outside legal counsel.</div>

  <h2>1. Who We Are</h2>
  <p>This website is operated by Zenva Management ("Zenva," "we," "us," or "our"), operating as Zenva &mdash; Private Onsen &amp; Spa, located at SEENSPACE Thonglor, FL 03-01, 251/1 Thong Lo 13 Alley, Khlong Tan Nuea, Watthana, Bangkok 10110, Thailand. For any privacy question or request, contact us at admin@zenvaspabkk.com or +66 80 262 9191.</p>

  <h2>2. What Personal Data We Collect</h2>
  <table>
    <tr><th>Category</th><th>Examples</th><th>How it's collected</th></tr>
    <tr><td>Booking &amp; contact data</td><td>Name, phone number, LINE/WhatsApp ID, email, booking date/time, party size</td><td>When you book by phone, LINE, WhatsApp, or a website form</td></tr>
    <tr><td>Membership data</td><td>Membership tier, credit balance, transaction history</td><td>When you join or use the membership program</td></tr>
    <tr><td>Sensitive personal data (health information)</td><td>Contraindication/health-screening answers (e.g., pregnancy, heart conditions, migraines) collected before Contrast Therapy or ice-bath treatments</td><td>Via a screening form at the time of booking or check-in, only with your separate, explicit consent &mdash; see Section 4</td></tr>
    <tr><td>Technical &amp; usage data</td><td>IP address, device/browser type, pages visited, referral source</td><td>Automatically, via cookies and similar technologies when you use the site (only after consent for non-essential categories &mdash; see Section 7)</td></tr>
    <tr><td>Marketing data</td><td>Your interactions with ads or messages, if you've opted in</td><td>Via Meta Pixel / LINE Tag, only after marketing consent</td></tr>
  </table>

  <h2>3. Why We Use Your Data (Purposes &amp; Legal Basis)</h2>
  <ul>
    <li><strong>To provide the service you booked</strong> &mdash; confirming and managing your reservation. Legal basis: performance of a contract with you.</li>
    <li><strong>To run our membership program</strong> &mdash; tracking credit balances and usage. Legal basis: performance of a contract with you.</li>
    <li><strong>To screen for treatment safety</strong> &mdash; checking contraindications before Contrast Therapy or the ice bath. Legal basis: your separate, explicit consent (required for sensitive/health data under PDPA Section 26).</li>
    <li><strong>To improve our website</strong> &mdash; understanding how visitors use the site (analytics). Legal basis: your consent.</li>
    <li><strong>To send marketing messages or show relevant ads</strong> &mdash; only where you've opted in. Legal basis: your consent, which you can withdraw at any time.</li>
    <li><strong>To meet legal obligations</strong> &mdash; e.g., financial record-keeping. Legal basis: legal obligation.</li>
  </ul>
  <p>We do not sell personal data to third parties.</p>

  <h2>4. Sensitive Personal Data &mdash; Extra Protection</h2>
  <div class="legal-notice">Health-related screening information is treated as sensitive personal data under PDPA Section 26, which requires a higher standard of consent than our other data collection.</div>
  <p>Before certain treatments (Contrast Therapy, the ice bath), we ask health-screening questions to check for contraindications such as pregnancy, cardiovascular conditions, or migraines. This is collected only with your separate, explicit, opt-in consent &mdash; never bundled with your general booking consent, and never through a pre-ticked box. You may decline to answer, though we may not be able to offer certain treatments without this safety check. We keep this information only as long as needed to safely deliver the treatment on the day of your visit, and do not retain it beyond 90 days unless you are a returning guest who chooses to have it kept on file, which we will confirm with you again at each visit.</p>

  <h2>5. Who We Share Data With</h2>
  <p>We may share limited data with service providers who help us run the business, such as messaging platforms (LINE, WhatsApp/Meta) and analytics providers (Google). At this time, bookings are made directly by phone, LINE, or WhatsApp rather than through a separate booking, POS, or CRM platform; this section will be updated if a dedicated booking or CRM system is adopted in the future. These providers only receive the data needed to perform their function and are not permitted to use it for their own purposes.</p>

  <h2>6. Cross-Border Data Transfers</h2>
  <p>Some of the service providers we use &mdash; Google (Google Analytics), Meta (Meta Pixel), and LINE &mdash; may process data on servers located outside Thailand. Thailand's Personal Data Protection Committee has not, as of the date of this policy, published a list of countries it recognizes as having data protection standards equivalent to Thailand's. Where we transfer data to these providers, we rely on the safeguards each provider maintains &mdash; including their own standard contractual clauses and international compliance certifications &mdash; as the basis for the transfer, consistent with PDPA Sections 28&ndash;29. We will update this section if Thailand's regulator publishes further guidance that changes how this should be documented or safeguarded.</p>

  <h2>7. Cookies &amp; Similar Technologies</h2>
  <p>We use three categories of cookies, described in the table below. Non-essential categories only load after you give consent through the cookie banner or the "Cookie Settings" link in the site footer, which you can use to change your choice at any time.</p>
  <table>
    <tr><th>Category</th><th>Purpose</th><th>Examples</th><th>Requires consent?</th></tr>
    <tr><td>Necessary</td><td>Core site function, security, remembering your cookie choice</td><td>Session/consent cookies</td><td>No &mdash; always on</td></tr>
    <tr><td>Analytics</td><td>Understand site usage to improve content and navigation</td><td>Google Analytics (GA4)</td><td>Yes</td></tr>
    <tr><td>Marketing</td><td>Measure and personalize ads/messages</td><td>Meta Pixel, LINE Tag</td><td>Yes</td></tr>
  </table>

  <h2>8. How Long We Keep Your Data</h2>
  <ul>
    <li><strong>Booking &amp; financial records:</strong> 5 years from the date of the transaction, aligned with the record-keeping period required for accounting and tax documents under Thailand's Revenue Code (Section 87/3).</li>
    <li><strong>Membership &amp; credit records:</strong> for as long as your membership is active, plus 2 years after closure, to handle any residual credit balance or re-enrollment.</li>
    <li><strong>Sensitive health-screening data:</strong> as described in Section 4 above &mdash; not retained beyond 90 days unless you are a returning guest who consents again to have it kept on file.</li>
    <li><strong>Marketing consent records:</strong> until you withdraw consent, or automatically after 24 months of inactivity, whichever is sooner.</li>
    <li><strong>Technical/analytics data:</strong> per the retention period configured in our Google Analytics account, which you can ask us about at any time.</li>
  </ul>

  <h2>9. Your Rights Under PDPA</h2>
  <p>Under Thailand's PDPA, you have the right to:</p>
  <ul>
    <li>Be informed about how your data is used (this policy);</li>
    <li>Access the personal data we hold about you and request a copy;</li>
    <li>Request correction of inaccurate data;</li>
    <li>Request deletion or de-identification of your data, subject to legal exceptions;</li>
    <li>Withdraw consent at any time, including for cookies, marketing, and the sensitive health-screening data described in Section 4;</li>
    <li>Object to certain processing, including direct marketing;</li>
    <li>Lodge a complaint with Thailand's Personal Data Protection Committee (PDPC) if you believe your rights have been violated.</li>
  </ul>
  <p>To exercise any of these rights, contact us at admin@zenvaspabkk.com.</p>

  <h2>10. Data Protection Officer</h2>
  <p>Under the 2023 sub-regulation to PDPA Section 41(2), a Data Protection Officer must be appointed only where a business's core activity involves regular, large-scale monitoring or profiling of individuals &mdash; in practice, this generally means processing personal data of more than 100,000 people a year, or operating in specific regulated sectors (large-scale behavioral-advertising platforms, insurance, certain telecommunications licensees). Based on Zenva's own current scale &mdash; well under 5,000 customers a year, with website analytics and advertising measurement as a supporting function rather than our core business activity &mdash; a formally appointed Data Protection Officer is not required at this time. We will revisit this assessment if the scale or nature of our data processing changes materially. For any data protection question, request, or concern, contact us using the details in Section 1.</p>

  <h2>11. Changes to This Policy</h2>
  <p>We may update this policy from time to time. Material changes will be reflected with a new "last updated" date at the top of this page.</p>

  <p style="margin-top:36px;"><a href="index.html" style="color:var(--ink); font-weight:700; text-decoration:none;">&larr; Back to home</a></p>
</div>
"""

with open("/tmp/zenva_site/privacy-policy.html", "w") as f:
    f.write(page("Privacy & Cookie Policy — Zenva", "none", privacy_body, privacy_extra_css, path="privacy-policy.html"))
print("privacy-policy.html v2 written (self-certified against official Thailand PDPA guidance, pending final owner read-through before publish)")

# ---------- SITEMAP.XML ----------
# Generated from SITEMAP_PATHS (== PAGE_ALTERNATES keys), so it can never drift
# out of sync with the pages this script actually produces. privacy-policy.html
# is intentionally left OUT of the sitemap (not a landing page worth Google
# actively crawling/indexing on its own), matching the existing low-priority
# treatment noted for that page in the deep-dive review.
# zh/*.html pages are ALSO deliberately left out for now — they're an unapproved
# PREVIEW build (see the ZH PREVIEW BUILD section above), not yet signed off by
# a native speaker. Once the translation is approved, add their paths here (loop
# over PAGE_ALTERNATES values instead of just keys) and remove the /zh/ line
# from robots.txt below in the same change.
_sitemap_urls = [p for p in SITEMAP_PATHS if p != "privacy-policy.html"]
_sitemap_entries = "\n".join(
    f"""  <url>
    <loc>{BASE_URL}/{p}</loc>
  </url>""" for p in _sitemap_urls
)
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{_sitemap_entries}
</urlset>
"""
with open("/tmp/zenva_site/sitemap.xml", "w") as f:
    f.write(sitemap_xml)
print(f"sitemap.xml written ({len(_sitemap_urls)} URLs)")

# ---------- ROBOTS.TXT ----------
# /zh/ and /th/ are blocked temporarily — same reasoning as privacy-policy.html:
# both are unapproved PREVIEW builds, not yet signed off by a native speaker,
# so neither should be crawled/indexed until that review happens. Remove the
# matching line the moment each translation is approved. /th/ is added here as
# soon as the first Thai page (th/index.html) exists and is linked from the
# English homepage's language switcher — not deferred until every Thai page is
# built — so there is never a window where a real, linked Thai URL is
# crawlable but unapproved.
robots_txt = f"""User-agent: *
Allow: /
Disallow: /privacy-policy.html
Disallow: /zh/
Disallow: /th/

Sitemap: {BASE_URL}/sitemap.xml
"""
with open("/tmp/zenva_site/robots.txt", "w") as f:
    f.write(robots_txt)
print("robots.txt written")
