---
topic_id: 27089
title: "Merge 3 Mri Volumes With Different Orientations Into One"
date: 2023-01-06
url: https://discourse.slicer.org/t/27089
---

# Merge 3 MRI volumes with different orientations into one

**Topic ID**: 27089
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/merge-3-mri-volumes-with-different-orientations-into-one/27089

---

## Post #1 by @Audrina_Fernandez (2023-01-06 14:14 UTC)

<p>Hi,<br>
I’m working on MRI to segment cheek fat volume and often I have one serie of few images for axial axe, one serie for coronal axe, one serie for sagittal axe (for one patient, one IRM). To get a better volume segmentation I would like to stitch these series. Stitch volume module can help me to match differents axes or it is for differents series of the same axe?</p>
<p>Sorry for my English <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @mikebind (2023-01-09 22:16 UTC)

<p>As currently written, the Stitch Volumes module only works for stitching together image volumes which are distributed along one axis (like a series of CT or MR volumes taken at different table position stations).  Trying to combine overlapping MR imaging with higher resolution in differing orientations is a very different problem and would require a different approach.  This is a common desire because this is often how clinical imaging is collected, but there is not a commonly-used, effective way to generate a high resolution volume from multiple anisotropic image volumes (at least not that I am aware of).</p>
<p>Here are some links to other discussions where someone wanted to do this where you can find some explanations and suggestions:</p><aside class="quote" data-post="1" data-topic="5939">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/9e8a1a/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-multiple-directional-series/5939">Combining Multiple Directional Series </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have DICOM files from a brain MRI but they are separated into axial, coronal, and sagittal series and thus I cant work with them together as one volume. If I try the other two planes appear blurry. Is there  way to combined the three series?
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac - High Sierra 
Slicer version: 4.8.1 
Expected behavior: One perfect, high resolution volume 
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse) 
I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models. 
After loading CT scans from their DICOM folder I always get several volumes, often with the …
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="5791">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/e95f7d/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/can-i-use-axial-coronal-and-sagittal-from-different-scans/5791">Can I Use Axial Coronal and Sagittal from Different Scans?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have loaded a DICOM file into Slicer. When I look at the Data module, I can see the separate scans done for each plane (a scan for axial, sagittal, and coronal) and each is listed as a volume. When looking at one of these volumes - axial for example - it shows the red, yellow, and green slices, and if I turn on the sight for the volume in Volume Rendering, I can see it there as a 3D rendering. The red slice window is the axial window, and in it shows the master information that the green and y…
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="2" data-topic="5478">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-model-from-dicoms/5478/2">3D model from dicoms</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    First of all, what would you like to segment? Simple thresholding works well in cases when structures of interest have highly distinctive intensity value on the image (bone on CT, contrasted vessels, etc.). If you want to segment bone on MRI then you need to use more sophisticated tools than thresholding. 
Another problem is that, quite often 3 anisotropic MRI images are acquired (high resolution along two axes, very low resolution along a third axis) to reduce time spent in the MRI scanner. How…
  </blockquote>
</aside>


---

## Post #3 by @Vikas_Rajpurohit (2023-11-27 07:19 UTC)

<p>Actually, I have a solution to these to this problem, but should i tell it or not because like literally spent over more than 46 hours for solving this problem. But i can give u a hint that , try to think this problem as an vein diagram. You will find its solution for sure. Thanks</p>

---

## Post #4 by @nakcali (2026-02-14 14:13 UTC)

<p>Could you help me? I</p>

---
