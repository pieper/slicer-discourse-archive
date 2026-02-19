---
topic_id: 15792
title: "Segmenting Pulmonary Fibrosis"
date: 2021-02-02
url: https://discourse.slicer.org/t/15792
---

# Segmenting pulmonary fibrosis

**Topic ID**: 15792
**Date**: 2021-02-02
**URL**: https://discourse.slicer.org/t/segmenting-pulmonary-fibrosis/15792

---

## Post #1 by @joachim (2021-02-02 10:26 UTC)

<p>I was asked to create a model of pulmonary fibrosis (3D-printing). It’s easy to see the structure of cells and thin walls on the images, but it is difficult to segment this structure.</p>
<p><em>Cells drawn by hand</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c02ad5649b395f055c3ba80a340f932902a3ef9.jpeg" data-download-href="/uploads/short-url/1IfsQCiDGsQrBFCpIsyrES7ZdXP.jpeg?dl=1" title="manual" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c02ad5649b395f055c3ba80a340f932902a3ef9_2_345x202.jpeg" alt="manual" data-base62-sha1="1IfsQCiDGsQrBFCpIsyrES7ZdXP" width="345" height="202" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c02ad5649b395f055c3ba80a340f932902a3ef9_2_345x202.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c02ad5649b395f055c3ba80a340f932902a3ef9_2_517x303.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c02ad5649b395f055c3ba80a340f932902a3ef9_2_690x404.jpeg 2x" data-dominant-color="787175"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">manual</span><span class="informations">1389×817 565 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>Interpolated and non-interpolated view</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1332a5497c76145bb107a4bd58e3b05369bad3f9.jpeg" data-download-href="/uploads/short-url/2JPzWylIU0DFAO1AH8npqDvAWh3.jpeg?dl=1" title="Interpolate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1332a5497c76145bb107a4bd58e3b05369bad3f9_2_345x170.jpeg" alt="Interpolate" data-base62-sha1="2JPzWylIU0DFAO1AH8npqDvAWh3" width="345" height="170" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1332a5497c76145bb107a4bd58e3b05369bad3f9_2_345x170.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1332a5497c76145bb107a4bd58e3b05369bad3f9_2_517x255.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1332a5497c76145bb107a4bd58e3b05369bad3f9_2_690x340.jpeg 2x" data-dominant-color="414141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Interpolate</span><span class="informations">761×376 34.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see with non-interpolated pixels, the walls are not clearly defined so thresholding is difficult. What should I do? I have some ideas:</p>
<ul>
<li>Create a volume with higher pixel resolution and interpolate the pixels so it looks like the interpolated view.  How can this be done in Slicer?</li>
<li>Sharpen the image so that the structure becomes clearer. How can this be done in Slicer? Is there a useful filter in ITK Simple Filters?</li>
</ul>
<p>You can try <a href="https://1drv.ms/u/s!AoVqWdO9AjfwgXxhvvFZFrultWlI?e=bF2taN" rel="noopener nofollow ugc">my project here</a>.</p>

---

## Post #2 by @lassoan (2021-02-02 13:38 UTC)

<aside class="quote no-group" data-username="joachim" data-post="1" data-topic="15792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Create a volume with higher pixel resolution and interpolate the pixels so it looks like the interpolated view. How can this be done in Slicer?</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>
<aside class="quote no-group" data-username="joachim" data-post="1" data-topic="15792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Sharpen the image so that the structure becomes clearer. How can this be done in Slicer? Is there a useful filter in ITK Simple Filters?</p>
</blockquote>
</aside>
<p>Yes, there are many ITK filters available in Simple Filters module that may be used for sharpening. For example, type <code>sharp</code> or <code>anisotropic</code> into the search field to find relevant filters. You can also ask advice for filter selection in the <a href="https://discourse.itk.org/">ITK forum</a>.</p>
<p>You can learn more about segmentation in Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a>.</p>

---

## Post #3 by @joachim (2021-02-04 10:19 UTC)

<p>Thank you. The Slicer documentation has become better, I see.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough" rel="noopener nofollow ugc">Your link</a> tells you how to increase the resolution of the segmentation volume (binary label map). This lets me segment with better details. However, when doing a thresholding from the original volume, the details in the segmentation volume will not increase since it uses a volume with less resolution as basis.</p>
<p>If you take a look at the interpolated image above, the walls between the cells looks more defined. Therefore I want to know if I can create a new volume with higher resolution containing the interpolated pixels (so it looks like the interpolated image)? My plan was to then use some filter to sharpen the walls, and then do the segmentation (thresholding).</p>

---

## Post #4 by @lassoan (2021-02-04 14:39 UTC)

<aside class="quote no-group" data-username="joachim" data-post="3" data-topic="15792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Therefore I want to know if I can create a new volume with higher resolution containing the interpolated pixels (so it looks like the interpolated image)?</p>
</blockquote>
</aside>
<p>See “Option A” at the link provided above.</p>

---
