---
topic_id: 48592
title: "Extentions cant be loaded"
date: 2026-10-24
url: https://discourse.slicer.org/t/48592
last_bumped: 2026-10-25T08:00:20.680Z
---

# Extentions cant be loaded

**Topic ID**: 48592
**Date**: 2026-10-24
**URL**: https://discourse.slicer.org/t/extentions-cant-be-loaded/48592

---

## Post #1 by @DrAssadawy (2026-10-24 18:10 UTC)

<p>connection time out</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f6f51a2c36b88c926eabbc7aa27817435fb81e1.png" data-download-href="/uploads/short-url/fTNuVxRf8aCm8k50A2zLIabQ3zb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f6f51a2c36b88c926eabbc7aa27817435fb81e1_2_690x337.png" alt="image" data-base62-sha1="fTNuVxRf8aCm8k50A2zLIabQ3zb" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f6f51a2c36b88c926eabbc7aa27817435fb81e1_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f6f51a2c36b88c926eabbc7aa27817435fb81e1_2_1035x505.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f6f51a2c36b88c926eabbc7aa27817435fb81e1_2_1380x674.png 2x" data-dominant-color="FDFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×936 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Rei_Kurosawa (2026-10-25 08:00 UTC)

<p>That looks like the Extensions Manager failing to reach the Slicer Extensions Catalog. The Slicer user guide lists two usual causes: the catalog server being temporarily overloaded (it recommends retrying after an hour or so), or the application not getting network access - Slicer uses the system proxy settings, so a proxy or firewall can block it. As an offline workaround you can download the extension package from the Extensions Catalog website in a normal browser and install it with the “Install from file…” button inside the Extensions Manager.</p>

---
