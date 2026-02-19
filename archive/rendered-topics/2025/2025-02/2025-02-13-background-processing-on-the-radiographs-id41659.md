---
topic_id: 41659
title: "Background Processing On The Radiographs"
date: 2025-02-13
url: https://discourse.slicer.org/t/41659
---

# Background Processing on the Radiographs

**Topic ID**: 41659
**Date**: 2025-02-13
**URL**: https://discourse.slicer.org/t/background-processing-on-the-radiographs/41659

---

## Post #1 by @Robert_Chauvet (2025-02-13 00:29 UTC)

<p>Hi,<br>
Our group is having some difficulties making the 2D radiographs with enhanced edges in Autoscoper. We noticed that Autoscoper inverts the images, but we are wondering if there is any other background processing happening as well? Is there any histogram cropping or resolution altering?<br>
We typically use contrast enhanced radiographs that look good, and still look good via the world view in Autoscoper, but the 2D renderings lack some of the details needed to track smaller bones.<br>
I would be happy to jump on a quick zoom call to go over things if that is easier.<br>
Thanks,<br>
Robert</p>

---

## Post #2 by @Amy_Morton (2025-02-21 15:21 UTC)

<p>Hi Robert, great to hear from you. Yes the ‘set background’ option in the ‘Edit’ file menu is particularly helpful if you have circular IIs<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/478d146217cc1c5abe4d89ae9900b4e29847a8ee.png" data-download-href="/uploads/short-url/acYa36nz8bsRQ7M2tFNQyTyHIMS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/478d146217cc1c5abe4d89ae9900b4e29847a8ee.png" alt="image" data-base62-sha1="acYa36nz8bsRQ7M2tFNQyTyHIMS" width="388" height="368"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">388×368 10.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you’d like to take a closer look at the effects of your filters, you can also export full drr image<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7564fe24fee1a0f01f3a1fb310933b0d23e056ca.png" data-download-href="/uploads/short-url/gKweSCu8ys3QkeqX9aeZq5Nq0Sm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7564fe24fee1a0f01f3a1fb310933b0d23e056ca.png" alt="image" data-base62-sha1="gKweSCu8ys3QkeqX9aeZq5Nq0Sm" width="423" height="229"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">423×229 6.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But no, there is currently no background processes as you mention… though it does seem like a <a href="https://github.com/BrownBiomechanics/Autoscoper/issues" rel="noopener nofollow ugc">good first issue</a> if you’d like to add?</p>

---
