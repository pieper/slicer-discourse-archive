---
topic_id: 26336
title: "Fuse Volumes Together"
date: 2022-11-20
url: https://discourse.slicer.org/t/26336
---

# Fuse Volumes together.

**Topic ID**: 26336
**Date**: 2022-11-20
**URL**: https://discourse.slicer.org/t/fuse-volumes-together/26336

---

## Post #1 by @Dimitrios_Rallios (2022-11-20 20:21 UTC)

<p>Hi there!</p>
<p>I faced a problem with an MRI scan of the patient. When I added the DICOM data to the system, the images of sagital, coronal and axial view were saved as volumes and I could not create a 3d model because if I chooses one of them, then the resolution of the other vies would be really bad.</p>
<p>Is there any way to fuse all those volume under one volume so it will be easier for me to custom it.</p>
<p>I am brand new here. Sorry, if the question is too stupid.</p>
<p>Have a nice one,<br>
Dimitrios Rallios<br>
Charité Universitätsmedizin Berlin<br>
<a href="mailto:dimitrios.rallios@charite.de">dimitrios.rallios@charite.de</a></p>

---

## Post #2 by @lassoan (2022-11-20 20:43 UTC)

<p>You may find this answer useful:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>


---
