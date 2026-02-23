---
topic_id: 46245
title: "Brain Ct Segmentation Grow From Seed Leak Rectangle Appears"
date: 2026-02-22
url: https://discourse.slicer.org/t/46245
---

# Brain CT segmentation - grow from seed leak - rectangle appears

**Topic ID**: 46245
**Date**: 2026-02-22
**URL**: https://discourse.slicer.org/t/brain-ct-segmentation-grow-from-seed-leak-rectangle-appears/46245

---

## Post #1 by @mechanical_orange (2026-02-22 20:03 UTC)

<p>Operating system: mac os<br>
Slicer version: 5.6.2<br>
Expected behavior: grow from seed only segments parts of the brain without the background<br>
Actual behavior: grow from seed segments the background in a rectangle form.</p>
<p>Hi!</p>
<p>Segmenting brain CT: painting then using grow from seed. I am surely not putting painted points in the background. And regardless this all, a rectangle appears in the color of one of my segments, or the whole background become part of my segment. Mostly of the darkest segment.</p>
<p>I set the background to -10000 but the issue persists. How could I resolve this issue?</p>
<p>Thank you,</p>
<p>ervin</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f35ff5b9c3284d42f3178d96d6186882f3c1e92b.jpeg" data-download-href="/uploads/short-url/yIZCl43JWK0RZ33FrorLej1pHPZ.jpeg?dl=1" title="Screenshot 2026-02-22 at 21.58.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f35ff5b9c3284d42f3178d96d6186882f3c1e92b_2_596x500.jpeg" alt="Screenshot 2026-02-22 at 21.58.10" data-base62-sha1="yIZCl43JWK0RZ33FrorLej1pHPZ" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f35ff5b9c3284d42f3178d96d6186882f3c1e92b_2_596x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f35ff5b9c3284d42f3178d96d6186882f3c1e92b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f35ff5b9c3284d42f3178d96d6186882f3c1e92b.jpeg 2x" data-dominant-color="4B483C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-02-22 at 21.58.10</span><span class="informations">850×712 64.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @drnoorfatima (2026-02-23 01:55 UTC)

<p>Hi Ervin!</p>
<p>This is a known issue with Grow from Seeds on brain CT, the algorithm leaks into the background because CT background intensities overlap with certain brain regions. Setting background to -10000 alone won’t fix it, the solution involves a specific masking step before running the segmentation.<br>
Completely fixable though. I work with Slicer segmentation professionally you can dm me.</p>

---
