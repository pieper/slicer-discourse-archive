---
topic_id: 32418
title: "How To Access Advanced Option In Code"
date: 2023-10-26
url: https://discourse.slicer.org/t/32418
---

# How to access advanced option in code?

**Topic ID**: 32418
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/how-to-access-advanced-option-in-code/32418

---

## Post #1 by @dsa934 (2023-10-26 00:09 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.4</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7867727c350ae271fac65f7a1e629e723da4002.png" data-download-href="/uploads/short-url/x2anXZ6AQxkmnkNdZpDTM012WDE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7867727c350ae271fac65f7a1e629e723da4002_2_364x500.png" alt="image" data-base62-sha1="x2anXZ6AQxkmnkNdZpDTM012WDE" width="364" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7867727c350ae271fac65f7a1e629e723da4002_2_364x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7867727c350ae271fac65f7a1e629e723da4002.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7867727c350ae271fac65f7a1e629e723da4002.png 2x" data-dominant-color="ECEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">523×717 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Where is the function that accesses the ‘control point labels’ option in this advance tab inherited?<br>
I don’t seem to see any related functions in ‘displayNode’s function’.</p>

---

## Post #2 by @lassoan (2023-10-26 02:23 UTC)

<p>All the display properties are stored in the display node of the markup node. I would recommend the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab Bootcamp Slicer programming tutorial</a> to get started with Python programming in Slicer.</p>

---

## Post #3 by @dsa934 (2023-10-26 04:03 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a32b0cbc6acb45ad1539b781ed500069cc34861.png" alt="image" data-base62-sha1="f9tdoicQh3U1OHoN5quBPDc2soh" width="575" height="158"><br>
oh… here it is… sorry</p>

---
