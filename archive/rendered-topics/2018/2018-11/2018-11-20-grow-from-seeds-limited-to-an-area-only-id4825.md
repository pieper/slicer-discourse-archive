# Grow from seeds limited to an area only

**Topic ID**: 4825
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/grow-from-seeds-limited-to-an-area-only/4825

---

## Post #1 by @drmaestro (2018-11-20 21:42 UTC)

<p>Operating system: Windows 7<br>
Slicer version:4.10<br>
Expected behavior: Grow from seed is applied to entire image<br>
Actual behavior: Grow from seed is applied to a box sized ROI</p>
<p>Hi,</p>
<p>I am trying to use “grow from seed” to segment arteries and kidneys. After creating a few segments and painting with the paint tool I use the grow from seed option however the result seems to be limited by an invisible bounding box, which occupies a small postion of the DICOM image (please see tha attached picture below), instead of the whole image. It is as if there is an invisible ROI being applied to the operation but I didn’t choose any ROI. How can I correct this behaviour?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f9f97eb6b2b838580a3f255f846ce2c3761ffdf.jpeg" data-download-href="/uploads/short-url/bmnE95lKzn5311Jmi7ixlPJkgcD.jpeg?dl=1" title="Cropped" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9f97eb6b2b838580a3f255f846ce2c3761ffdf_2_690x489.jpeg" alt="Cropped" data-base62-sha1="bmnE95lKzn5311Jmi7ixlPJkgcD" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9f97eb6b2b838580a3f255f846ce2c3761ffdf_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9f97eb6b2b838580a3f255f846ce2c3761ffdf_2_1035x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f9f97eb6b2b838580a3f255f846ce2c3761ffdf.jpeg 2x" data-dominant-color="575560"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cropped</span><span class="informations">1365×968 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks…</p>

---

## Post #2 by @lassoan (2018-11-20 21:55 UTC)

<p>What you see is the expected behavior. Typically you remove the background segment after growing is completed, so it would not be useful to compute the segmentation for the entire extent (and it would make computation longer and use more memory).</p>
<p>You can make the growth region arbitrarily large: add seeds as far as you want the segments to grow.</p>

---

## Post #3 by @drmaestro (2018-11-20 22:02 UTC)

<p>Thank you very much for the reply. I have tried to add to the segments after calculating “grow from seed” effect, however it doesn’t add the newly added selection:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cbc6ae97acf651978463066b837f33f2168a7c8.jpeg" data-download-href="/uploads/short-url/8FikwQPHBjot4kaV8Jpt9jarnCg.jpeg?dl=1" title="Cropped2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cbc6ae97acf651978463066b837f33f2168a7c8_2_690x360.jpeg" alt="Cropped2" data-base62-sha1="8FikwQPHBjot4kaV8Jpt9jarnCg" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cbc6ae97acf651978463066b837f33f2168a7c8_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cbc6ae97acf651978463066b837f33f2168a7c8_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cbc6ae97acf651978463066b837f33f2168a7c8_2_1380x720.jpeg 2x" data-dominant-color="343131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cropped2</span><span class="informations">1920×1004 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On the picture, you can see where grow from seed stopped, so I added the ascending aorta (red part) but it didn’t update the selection to include the ascending aorta.</p>

---

## Post #4 by @lassoan (2018-11-20 23:32 UTC)

<p>To change extent, you need to re-initialize (click Cancel and then Initialize). See <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html#grow-from-seeds-grow-from-seeds">documentation</a> for details.</p>

---
