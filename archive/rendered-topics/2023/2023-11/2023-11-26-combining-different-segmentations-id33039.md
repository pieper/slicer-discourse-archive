---
topic_id: 33039
title: "Combining Different Segmentations"
date: 2023-11-26
url: https://discourse.slicer.org/t/33039
---

# Combining different segmentations

**Topic ID**: 33039
**Date**: 2023-11-26
**URL**: https://discourse.slicer.org/t/combining-different-segmentations/33039

---

## Post #1 by @aleq_g (2023-11-26 17:38 UTC)

<p>Hello,<br>
I have a problem with creating a model from a scan: instead of 1 scan with all 3 axes done simultaneously, I have 3 scans from 3 axes. For each of the scans, 1 is of great quality and 2 are of worse quality (probably interpolated). How can i combine them into 1 (as in the picture) for the purpose of creating a 3d model from all of them?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78af338f3b2a337b7604949ca21cef996f5e958f.png" data-download-href="/uploads/short-url/hdCF9nM0fHFZmXT70c849ayk4RF.png?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78af338f3b2a337b7604949ca21cef996f5e958f_2_690x245.png" alt="Capture2" data-base62-sha1="hdCF9nM0fHFZmXT70c849ayk4RF" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78af338f3b2a337b7604949ca21cef996f5e958f_2_690x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78af338f3b2a337b7604949ca21cef996f5e958f_2_1035x367.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78af338f3b2a337b7604949ca21cef996f5e958f.png 2x" data-dominant-color="232321"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1262×449 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66a094ec4b8b4fe46cac2f746353f12d165559c.png" data-download-href="/uploads/short-url/uANmlRmXZDn9lj9TImEzaHxVG0c.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d66a094ec4b8b4fe46cac2f746353f12d165559c_2_690x228.png" alt="Capture1" data-base62-sha1="uANmlRmXZDn9lj9TImEzaHxVG0c" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d66a094ec4b8b4fe46cac2f746353f12d165559c_2_690x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d66a094ec4b8b4fe46cac2f746353f12d165559c_2_1035x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66a094ec4b8b4fe46cac2f746353f12d165559c.png 2x" data-dominant-color="131313"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1263×418 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-11-26 22:20 UTC)

<p>This question comes up fairly often, but we don’t have a good solution for it.  This kind of scan is done to allow review by radiologists of high res images in the three scan planes.  It’s possible that if they acquired one higher resolution volume and used reslicing to get the other views it would be better overall, but this is not the common practice.</p>

---

## Post #3 by @mikebind (2023-11-26 22:48 UTC)

<p>Looking at images like this, it <em>feels</em> like it should be straightforward to combine them into a 3D isotropic image volume, but it is not. If the image slice voxels are 0.5 mm x 0.5 mm in-plane and slices are 4 mm apart, then we’re actually missing quite a bit of information if we wanted to construct an image volume which had voxels which were 0.5 mm^3.  Looking only at the high resolution slices obscures how blurry the data acquisition actually is perpendicular to the that plane. I can imagine ways to fill in the data via interpolation, but I expect the results are much less than satisfactory, because I think if they looked good we would already have tools available which do this, and instead this apparently remains an unsolved problem.</p>

---

## Post #4 by @pieper (2023-11-26 22:56 UTC)

<p>Agreed, this seems like something where a superresolution machine learning tool would be really useful but I’ve never seen one for this problem.  It could be trained on high res data and then take the three orthogonal thick slice images as input and generate a synthetic isotropic volume.</p>

---

## Post #5 by @lassoan (2023-11-27 04:56 UTC)

<p>See more information here (and in topics mentioned in that post):</p>
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
