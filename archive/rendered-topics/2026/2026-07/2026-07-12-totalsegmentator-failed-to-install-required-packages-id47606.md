---
topic_id: 47606
title: "TotalSegmentator failed to install required packages"
date: 2026-07-12
url: https://discourse.slicer.org/t/47606
last_bumped: 2026-07-13T19:31:51.103Z
---

# TotalSegmentator failed to install required packages

**Topic ID**: 47606
**Date**: 2026-07-12
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-install-required-packages/47606

---

## Post #1 by @johny723 (2026-07-12 12:28 UTC)

<p>I keep having a similar issue - how do I fix this? Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355.jpeg" data-download-href="/uploads/short-url/oILbyexMiGlxXMrhb20MEluuBCZ.jpeg?dl=1" title="Snímek obrazovky 2026-07-12 142815" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_690x380.jpeg" alt="Snímek obrazovky 2026-07-12 142815" data-base62-sha1="oILbyexMiGlxXMrhb20MEluuBCZ" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_1380x760.jpeg 2x" data-dominant-color="A5A4A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímek obrazovky 2026-07-12 142815</span><span class="informations">1920×1059 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ebrahim (2026-07-13 19:31 UTC)

<p>Does it work in Slicer 5.12.1? We made a fix related to this in the 5.12.1 patch (<a href="https://github.com/Slicer/Slicer/commit/c2975f21536bc5c6eff0ea91bf279fbb712c20c9" class="inline-onebox">BUG: Disable pip install UI off main thread · Slicer/Slicer@c2975f2 · GitHub</a>)</p>
<p>Related discussion: <a href="https://discourse.slicer.org/t/nninteractive-slicer-client-is-stuck/47550" class="inline-onebox">Nninteractive (slicer client) is stuck</a></p>

---
