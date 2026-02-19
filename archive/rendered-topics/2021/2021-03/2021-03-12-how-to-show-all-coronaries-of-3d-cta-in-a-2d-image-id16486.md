---
topic_id: 16486
title: "How To Show All Coronaries Of 3D Cta In A 2D Image"
date: 2021-03-12
url: https://discourse.slicer.org/t/16486
---

# How to show all coronaries of 3D CTA in a 2D image?

**Topic ID**: 16486
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/how-to-show-all-coronaries-of-3d-cta-in-a-2d-image/16486

---

## Post #1 by @yee_lu (2021-03-12 03:49 UTC)

<p>How to show all coronaries  of 3D CTA in a 2D image, using multi-planner reformation technology? I see the "curved planner reformat "module just straighten the volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/659589c015d481af4dec4ee85e8a640129a2732a.png" data-download-href="/uploads/short-url/euEBIEia545GqG8d1vfkLZmqgC6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/659589c015d481af4dec4ee85e8a640129a2732a.png" alt="image" data-base62-sha1="euEBIEia545GqG8d1vfkLZmqgC6" width="690" height="194" data-dominant-color="F0F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">704×198 3.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-03-27 18:42 UTC)

<p>If you want to see a vessel tree, not just a specific branch then you need to use 3D view (this 3D rendering appears on a desktop screen as a 2D image - as everything else on a 2D screen).</p>
<p>You can also generate maximum-minimum intensity projection (MIP) image so that you can display this 3D data in a slice view (see script <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections">here</a>), but it is not that helpful, because you cannot make distance measurements anyway.</p>
<p>Do you have an example image that you would like to get in Slicer?<br>
What is your overall goal?</p>

---
