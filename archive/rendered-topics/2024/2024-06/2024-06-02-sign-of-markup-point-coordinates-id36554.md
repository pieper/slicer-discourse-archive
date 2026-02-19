---
topic_id: 36554
title: "Sign Of Markup Point Coordinates"
date: 2024-06-02
url: https://discourse.slicer.org/t/36554
---

# Sign of markup point coordinates

**Topic ID**: 36554
**Date**: 2024-06-02
**URL**: https://discourse.slicer.org/t/sign-of-markup-point-coordinates/36554

---

## Post #1 by @YLX (2024-06-02 12:24 UTC)

<p>When selecting coordinate points in 3D Slicer software, you can see the specific values on the RSA axis. According to my observation, usually the RA axis is negative, while the S axis is positive, but in the output fscv file, all the three-dimensional coordinates have become positive numbers. How can I solve this problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d29d66fbc138aa00c2d65c29870bda5d5dde6f5.png" data-download-href="/uploads/short-url/6rx7CrSiKpGBfcKVUznbPYLRfjn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d29d66fbc138aa00c2d65c29870bda5d5dde6f5.png" alt="image" data-base62-sha1="6rx7CrSiKpGBfcKVUznbPYLRfjn" width="481" height="500" data-dominant-color="EFF1F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">552×573 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/854aade14d66f54ce8833ca2418ec45197d40479.png" alt="image" data-base62-sha1="j19vbKYCZFK1bD1ukjRc0Qzf2SB" width="682" height="214"></p>
<p>Operating system:<br>
Slicer version:5.7.0<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @Sunderlandkyl (2024-06-03 13:45 UTC)

<p>Internally 3D Slicer represents data in RAS coordinate system.</p>
<p>When data is saved to file, it is written in LPS coordinates, so the first two components are multiplied by -1.</p>

---
