# Non-rigid registration of meshes

**Topic ID**: 2247
**Date**: 2018-03-06
**URL**: https://discourse.slicer.org/t/non-rigid-registration-of-meshes/2247

---

## Post #1 by @stevenagl12 (2018-03-06 02:52 UTC)

<p>Hi, I was wondering if it is possible to perform non-rigid registrations of meshes between each other in slicer, or potentially in SPHARM-PDM? I know that SPHARM has Procrustes but I am looking for a deformation field to be applied to models to distort the mesh for my purposes.</p>

---

## Post #2 by @lassoan (2018-03-06 03:48 UTC)

<p>We usually do deformable surface registration based on landmarks, using <code>Fiducial registration wizard</code> module in SlicerIGT extension. If you can identify enough corresponding landmarks then the method works extremely well.</p>

---

## Post #3 by @thewtex (2018-03-07 01:22 UTC)

<p>Non-rigid registration of meshes <a href="http://www.insight-journal.org/browse/publication/317" rel="nofollow noopener">is available in ITK</a>.</p>

---

## Post #4 by @lassoan (2018-03-10 18:32 UTC)

<p>I just remember, <a href="https://github.com/SlicerRt/SegmentRegistration">Segment registration</a> extension can do deformable mesh registration, too. It can work directly from segmentation nodes. If you have your input in model nodes then import those into a segmentation node using Segmentations module.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a>, the mesh registration sounds interesting, too. Is it in ITK proper? Is it available in SimpleITK?</p>

---

## Post #5 by @thewtex (2018-03-10 20:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes, the metrics that Nick Tustison wrote are very impressive and state-of-the-art. These are available in ITK proper. They are not available in SimpleITK.</p>

---

## Post #6 by @stevenagl12 (2019-08-19 12:15 UTC)

<p>3 questions, 1) I am working in Slicer 4.11.0 nightly. When I went to download and install the Segment Registration module, it is displaying that it is downloaded in the extension manager, but is not showing up in the list of modules. Should I just download a new nightly build? 2) I did not find any documentation on how to perform mesh registration in ITK, are there code examples, and are there examples using 3D slicer to perform the registration? 3) Finally, is there any way to perform PCA modelling with the 3D models in Slicer?</p>

---

## Post #7 by @stevenagl12 (2019-08-19 12:36 UTC)

<p>Actually, one more question, does anyone know the algorithm being applied for the deformable registration between the segments in Segment Registration? Is it Iterative Closest Points, or some variation thereof?</p>

---

## Post #8 by @stevenagl12 (2019-08-19 13:17 UTC)

<p>I think that it was that particular nightly build that wasn’t able to load the Segment Registration module, but when I run the module with 2 meshes (in this case a lion and a sabretooth tiger skull), to perform deformable registration after registration with fiducials, it is not warping the model at all?</p>

---

## Post #9 by @lassoan (2019-08-19 14:09 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="7" data-topic="2247" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Actually, one more question, does anyone know the algorithm being applied for the deformable registration between the segments in Segment Registration? Is it Iterative Closest Points, or some variation thereof?</p>
</blockquote>
</aside>
<p>The method uses intensity-based b-spline registration of distance maps. See details at the links in this post:</p>
<aside class="quote" data-post="15" data-topic="2570">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/align-two-segments-to-each-other/2570/15">align two segments to each other </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Segment Registration extension supports non-linear warping (based on b-spline registration of distance maps). We tried various approaches and this worked the best for our applications. It was <a href="http://perk.cs.queensu.ca/contents/open-source-image-registration-mri-trus-fusion-guided-prostate-interventions" rel="nofollow noopener">tested extensively on prostate US/MRI registration</a>, <a href="http://perk.cs.queensu.ca/contents/validation-mri-us-registration-focal-hdr-prostate-brachytherapy-treatment" rel="nofollow noopener">used successfully in clinical work</a>, and worked surprisingly well for other applications, too.
  </blockquote>
</aside>

<aside class="quote no-group" data-username="stevenagl12" data-post="8" data-topic="2247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>perform deformable registration after registration with fiducials, it is not warping the model at all?</p>
</blockquote>
</aside>
<p>You need to harden the landmark-based transform before starting the new registration.</p>

---

## Post #10 by @stevenagl12 (2019-09-05 15:29 UTC)

<p>I already hardened the landmark transforms, but, what I’m nto sure about is, can you convert a model into a binary volume and use this volume along with the segmentations to perform the morphable registration?</p>

---

## Post #11 by @lassoan (2019-09-05 20:42 UTC)

<p>There is no need to convert models to binary volumes. You can import your models into segmentation (few clicks in Segmentations module) and register them to each other or to other segments using Segment registration module.</p>

---

## Post #12 by @stevenagl12 (2019-09-11 06:02 UTC)

<p>Is it ok to leave the fixed and moving image sections blank? Also, when I try to run it this way, it looks like it’s just duplicating the same mesh that was the moving mesh without doing any deformations? Finally, is there any way to get the transform out? In the following image, there’s supposed to be 3 meshes. The blue is supposed to be the fixed mesh, the yellowish/white is supposed to be the original moving mesh, and the brown is supposed to be the deformed mesh:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8a41c47a1e589d438cdb0129e1e034f680d8088.jpeg" data-download-href="/uploads/short-url/o3ROQqMZ3Yn0VN2ZUzHJoR3ZAQU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8a41c47a1e589d438cdb0129e1e034f680d8088_2_690x288.jpeg" alt="image" data-base62-sha1="o3ROQqMZ3Yn0VN2ZUzHJoR3ZAQU" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8a41c47a1e589d438cdb0129e1e034f680d8088_2_690x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8a41c47a1e589d438cdb0129e1e034f680d8088_2_1035x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8a41c47a1e589d438cdb0129e1e034f680d8088_2_1380x576.jpeg 2x" data-dominant-color="23252E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×803 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
If it’s actually doing deformations to the moving mesh, then it should be creating a new deformed mesh right?</p>

---

## Post #13 by @lassoan (2019-09-11 13:09 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="12" data-topic="2247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Is it ok to leave the fixed and moving image sections blank?</p>
</blockquote>
</aside>
<p>Fixed and moving images seems to be necessary (I got an error message when I did not set something - check your logs to confirm). You can load any of the Slicer sample data sets and use those.</p>
<p>I’ve submitted an issue for this (see <a href="https://github.com/SlicerRt/SegmentRegistration/issues/5">here</a>). It would be great if you could fix it and send a pull request - it is just a Python script, that you need to modify so that if fixed or moving image is missing then skip any operations on them (do not try to resample).</p>

---
