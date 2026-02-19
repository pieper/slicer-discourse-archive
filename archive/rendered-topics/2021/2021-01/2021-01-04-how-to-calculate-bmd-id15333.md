---
topic_id: 15333
title: "How To Calculate Bmd"
date: 2021-01-04
url: https://discourse.slicer.org/t/15333
---

# How to calculate BMD

**Topic ID**: 15333
**Date**: 2021-01-04
**URL**: https://discourse.slicer.org/t/how-to-calculate-bmd/15333

---

## Post #1 by @Farhan (2021-01-04 14:10 UTC)

<p>Sir, how to calculate BMD of bone in 3d slicer.<br>
Sir, I am working on upper cervical spine and I have to find Young’s modules of elasticity(E) and Poisson’s ratio(u) of different parts of c1, c2 spine.<br>
What is the relationship between BMD and E and u.<br>
Kindly reply the questions.</p>

---

## Post #2 by @lassoan (2021-01-04 14:31 UTC)

<p>There is no universal formula to convert between radiologic density (voxel value on CT, in Hounsfield units) and BMD; or BMD to mechanical properties. There are lots of papers that use various assumptions and approximations to set mechanical properties directly from CT voxel values. I would recommend to use the method described in one of the recent, highly cited papers.</p>

---

## Post #3 by @manjula (2021-01-04 15:30 UTC)

<p>Hi,</p>
<p>We have calculated BMD with MircoCT using the method described <a href="https://www.bruker.com/fileadmin/user_upload/8-PDF-Docs/PreclinicalImaging/MolecularImaging/Albira_App_Notes/AP0123_-_PMOD_Software_Protocol_for_Obtaining_Bone_Mineral_Density_Units.pdf" rel="noopener nofollow ugc">here</a>.</p>
<p>We are yet to publish our papers based on this yet.</p>
<p>Basically, the main prerequisite  is  to have a <strong>Calibrated</strong> machine.<br>
Then we measured the HU means in 3 phantoms with know density.  And as Prof Lasso suggested in the final version we took 5 samples to get the</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="11010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/bone-mineral-density-bmd-measurement-method/11010/2">Bone Mineral Density (BMD) measurement method</a></div>
<blockquote>
<p>3 measurement points are very few. At least for initial exploration, I would add at least 5-10 points, just to have an idea about shape and amount of noise in the curve.</p>
</blockquote>
</aside>
<p>You can pretty much replicate this process in 3D Slicer provided you have a calibrated machine and phantoms with know density.</p><div class="youtube-onebox lazy-video-container" data-video-id="eYEzVD6W0YU" data-video-title=" - YouTube" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=eYEzVD6W0YU" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="" title=" - YouTube" width="" height="">
  </a>
</div>

<p>The resources we used are,<br>
Fortunately, we did not have to (research team) do the calibration by ourself but it was done by the professionals.<br>
<a href="https://drive.google.com/file/d/1-NBlVGr5gSFJzyYT9wlulZBkykQnhYLr/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1-NBlVGr5gSFJzyYT9wlulZBkykQnhYLr/view?usp=sharing</a></p><div class="youtube-onebox lazy-video-container" data-video-id="l0D4gjwsDI0" data-video-title="Bruker microCT tutorial: Calibration and measurement of bone mineral density (BMD and TMD) in bone." data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=l0D4gjwsDI0" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/l0D4gjwsDI0/maxresdefault.jpg" title="Bruker microCT tutorial: Calibration and measurement of bone mineral density (BMD and TMD) in bone." width="" height="">
  </a>
</div>


---

## Post #4 by @Farhan (2021-01-14 13:51 UTC)

<p>Sir, please share paper which set mechanical properties directly from CT voxel value as you described earlier. I am finding difficulties to find such paper.<br>
Kindly share.</p>

---

## Post #5 by @Joseph_L (2023-12-05 00:13 UTC)

<p>Is it possible for you to update these links? Most of them are broken</p>

---

## Post #6 by @NIE_XIUPING (2024-11-13 10:05 UTC)

<p>Could you please update these broken links?</p>

---
