# What does the B-spline transformation mean in Elastix?

**Topic ID**: 30935
**Date**: 2023-08-02
**URL**: https://discourse.slicer.org/t/what-does-the-b-spline-transformation-mean-in-elastix/30935

---

## Post #1 by @Drake (2023-08-02 14:28 UTC)

<p>Hello,<br>
I registered the MRI and the CT of the same subject using Elastix module. (MRI is the reference image and CT is movable image. ） The result contains B-spline transform:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02e965c15d29fa72ede9ed54dc259ffb64a8ed1f.png" alt="图片2" data-base62-sha1="pL0pUaD9mhnREOV189ZYG7s1Gv" width="687" height="325"></p>
<p>And it seems the B-spline transformation alone is non-rigid (shown as the figure below):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db657681737039ac26ca310897f799a3da0482ab.jpeg" data-download-href="/uploads/short-url/viRWRaFNazsgR4XZdKZyiFCJ511.jpeg?dl=1" title="图片1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db657681737039ac26ca310897f799a3da0482ab_2_585x499.jpeg" alt="图片1" data-base62-sha1="viRWRaFNazsgR4XZdKZyiFCJ511" width="585" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db657681737039ac26ca310897f799a3da0482ab_2_585x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db657681737039ac26ca310897f799a3da0482ab_2_877x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db657681737039ac26ca310897f799a3da0482ab.jpeg 2x" data-dominant-color="746974"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片1</span><span class="informations">1109×947 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also use SPM to do the registration, and just got a linear matrix. And I have validated the correctness of the result.</p>
<p>What does the B-spline transformation here really mean?<br>
Does it correspond to the “reslice” step of registration?  Or maybe it really means a free-form deformation? if so, why does a whithin-subject transformation contain non-rigid transformation?</p>
<p>These questions have been bothering me for days.</p>
<p>Thanks!<br>
Drake</p>

---

## Post #2 by @lassoan (2023-08-02 14:45 UTC)

<aside class="quote no-group" data-username="Drake" data-post="1" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>What does the B-spline transformation here really mean?</p>
</blockquote>
</aside>
<p>It means that B-spline transformation parameters are adjusted by the registration optimizer while trying to align the moving and fixed image. B-spline is a warping transformation that uses a sparse grid of control points and b-spline interpolation to compute displacement vectors between the control points.</p>
<aside class="quote no-group" data-username="Drake" data-post="1" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>Does it correspond to the “reslice” step of registration?</p>
</blockquote>
</aside>
<p>It is not related to reslice. You can use any kind of transform for reslicing (resampling) a volume.</p>
<aside class="quote no-group" data-username="Drake" data-post="1" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>Or maybe it really means a free-form deformation?</p>
</blockquote>
</aside>
<p>Free-form deformation usually refers to warping an image with a dense displacement field, where each point of the fixed image may mapped to anywhere in 3D space. B-spline uses a sparse set of control points, so I would not consider it free-form deformation.</p>
<aside class="quote no-group" data-username="Drake" data-post="1" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>why does a whithin-subject transformation contain non-rigid transformation?</p>
</blockquote>
</aside>
<p>There can be many reasons, including changes in shape of the patient (different posture, different jaw position, different padding of the scanner pushing soft tissue around, internal swelling, different filling of internal structures, patient gains/loses weight, etc.), different cropping of images (e.g., nose is cut off in one image but not in the other) or image artifacts. Visual inspection should clearly answer this question.</p>
<p>If you prefer to use a rigid transformation - for example: you want to register a bones in two images that were taken at almost the same time - then you can choose a rigid registration preset that does not attempt to get better alignment by warping.</p>

---

## Post #3 by @pieper (2023-08-02 14:56 UTC)

<p>Slicer relies on <a href="https://itk.org">ITK</a> for registration primitives.  See the <a href="https://itk.org/ItkSoftwareGuide.pdf">ITK book</a> for more details.</p>

---

## Post #4 by @ebrahim (2023-08-02 15:03 UTC)

<aside class="quote no-group" data-username="Drake" data-post="1" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>why does a whithin-subject transformation contain non-rigid transformation?</p>
</blockquote>
</aside>
<p>Humans are squishy!</p>
<p>More info on elastix: <a href="https://elastix.lumc.nl/download/elastix-5.1.0-manual.pdf" rel="noopener nofollow ugc">https://elastix.lumc.nl/download/elastix-5.1.0-manual.pdf</a><br>
On using b-splines for medical image registration: <a href="http://image.diku.dk/imagecanon/material/Rueckert-IEEETMI1999.pdf" rel="noopener nofollow ugc">http://image.diku.dk/imagecanon/material/Rueckert-IEEETMI1999.pdf</a></p>

---

## Post #5 by @Drake (2023-08-03 01:50 UTC)

<p>Thank you so much for your reply!!</p>
<p>I did want to register skull in two images and also try the ‘generic rigid(all)’ preset, that I’m not sure correct or not. But the results still contain B-spline transformation, it also made me confused.</p>
<p>By the way，</p>
<ol>
<li>Does the result world-to-world transformation matrix (RAS space), rather than voxel-to-voxel (image space)?</li>
<li>If I just want to use the B-spline results to transform the skull COR from CT scan into MRI space in codes, what information or document can I access to? I only know the GUI method for B-spline transformation now.</li>
</ol>

---

## Post #6 by @lassoan (2023-08-03 04:35 UTC)

<aside class="quote no-group" data-username="Drake" data-post="5" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>try the ‘generic rigid(all)’ preset, that I’m not sure correct or not. But the results still contain B-spline transformation</p>
</blockquote>
</aside>
<p>You’ve found a bug! (result of some recent code refactoring) When you selected the rigid preset, it got reverted to the default preset because the two presets had the same ID. The issue is now <a href="https://github.com/lassoan/SlicerElastix/commit/d98ebdeec1552ffc78b54821e6cdc9379e4ddd5c">fixed</a>, update SlicerElastix extension to get the updated version of the extension (only on latest Slicer Stable Release or very latest Slicer Preview Release).</p>
<aside class="quote no-group" data-username="Drake" data-post="5" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>voxel-to-voxel (image space)</p>
</blockquote>
</aside>
<p>It is up to each library and application to decide how to organize the voxels in memory and assign IJK coordinates to voxels. However, medical imaging file formats unambiguously specify where the voxels are in physical space. Therefore specifying transformation in voxel space is not an option, but registration methods must always provide transformation in physical space.</p>
<aside class="quote no-group" data-username="Drake" data-post="5" data-topic="30935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5fc32e/48.png" class="avatar"> Drake:</div>
<blockquote>
<p>what information or document can I access to?</p>
</blockquote>
</aside>
<p>You have access to all information (most notably the computed transform) and you can do anything with it (save to ITK transform file, use it to resample the moving image, warp segmentations, models, markups with the transform, etc. each by a few lines of Python script). You can find examples in the Slicer script repository, in Slicer forum posts, tests, and examples, which you can find using Google, you can often get fully functional Python code by asking Bing chat, and you can of course also ask specific questions here from us.</p>

---
