---
topic_id: 42163
title: "Why Does The Ras Data Probe Point Coord Not Match Visually I"
date: 2025-03-15
url: https://discourse.slicer.org/t/42163
---

# Why does the RAS data probe point coord not match visually in the volume?

**Topic ID**: 42163
**Date**: 2025-03-15
**URL**: https://discourse.slicer.org/t/why-does-the-ras-data-probe-point-coord-not-match-visually-in-the-volume/42163

---

## Post #1 by @William_Kuo (2025-03-15 21:39 UTC)

<p>Why does my data probe not match the markup visually? I had to apply a negative to the superior value to make the markup point match with my cursor on the data probe. If I were to markup the same as the data probe RAS coords suggests, it would be outside of the volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52b340ac5f9860e083d153f7d765827c7c23e990.png" data-download-href="/uploads/short-url/bNBcn87USNueHbSQ9B0ATRwLBT2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b340ac5f9860e083d153f7d765827c7c23e990_2_459x374.png" alt="image" data-base62-sha1="bNBcn87USNueHbSQ9B0ATRwLBT2" width="459" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b340ac5f9860e083d153f7d765827c7c23e990_2_459x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b340ac5f9860e083d153f7d765827c7c23e990_2_688x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b340ac5f9860e083d153f7d765827c7c23e990_2_918x748.png 2x" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1120×914 17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-03-15 21:43 UTC)

<p>The data probe is indicating “I” (inferior) while the markup control point is reporting “S” (superior) coordinates.</p>

---

## Post #3 by @William_Kuo (2025-03-15 21:52 UTC)

<p>Thank you! I didn’t notice that.</p>

---
