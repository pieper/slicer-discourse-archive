# Adding a text annotation to a DICOM dataset that will volume-render…

**Topic ID**: 34874
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/adding-a-text-annotation-to-a-dicom-dataset-that-will-volume-render/34874

---

## Post #1 by @JJ_Harvey (2024-03-13 18:42 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85fb6c6169e5fb87160cbfe8b742170d7eb3d5f5.jpeg" data-download-href="/uploads/short-url/j7gaT9gF741N0dzFdVcknfXc1Mx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85fb6c6169e5fb87160cbfe8b742170d7eb3d5f5_2_690x388.jpeg" alt="image" data-base62-sha1="j7gaT9gF741N0dzFdVcknfXc1Mx" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85fb6c6169e5fb87160cbfe8b742170d7eb3d5f5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85fb6c6169e5fb87160cbfe8b742170d7eb3d5f5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85fb6c6169e5fb87160cbfe8b742170d7eb3d5f5_2_1380x776.jpeg 2x" data-dominant-color="2A1B15"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 508 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5c332926dcf7c26297f401bcff707e0b0a568e6.jpeg" data-download-href="/uploads/short-url/pVWD7r0uf7mvDFHlYJhzPoij3JI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5c332926dcf7c26297f401bcff707e0b0a568e6_2_690x388.jpeg" alt="image" data-base62-sha1="pVWD7r0uf7mvDFHlYJhzPoij3JI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5c332926dcf7c26297f401bcff707e0b0a568e6_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5c332926dcf7c26297f401bcff707e0b0a568e6_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5c332926dcf7c26297f401bcff707e0b0a568e6_2_1380x776.jpeg 2x" data-dominant-color="432F23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 654 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74995cabe24d926d50a3ff80bf69e798ef057d28.jpeg" data-download-href="/uploads/short-url/gDtXIiu2PpFQCEr4yNEAGNGizd6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74995cabe24d926d50a3ff80bf69e798ef057d28_2_690x388.jpeg" alt="image" data-base62-sha1="gDtXIiu2PpFQCEr4yNEAGNGizd6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74995cabe24d926d50a3ff80bf69e798ef057d28_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74995cabe24d926d50a3ff80bf69e798ef057d28_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74995cabe24d926d50a3ff80bf69e798ef057d28_2_1380x776.jpeg 2x" data-dominant-color="73664A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 868 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could someone please tell me if the annotations that can be seen in these volume-rendered images (from DICOM) were likely to have been added with Slicer and, if so, how is this done?</p>
<p>Thanks in advance for any/all assistance.</p>

---

## Post #2 by @lassoan (2024-03-13 18:53 UTC)

<p>It seems that the text was burnt into the image (with bone-like voxel values). I would not recommend to modify an image by burning in annotations like this, as it may interfere with interpretation and analysis of the image (especially if automated) and may occlude potentially relevant details.</p>
<p>Anyway, if you still want to so it then you can use Segment Editor module’s <code>Draw text</code> effect to create the 3D text and then use <code>Mask volume</code> effect to paint it into the image.</p>

---

## Post #3 by @JJ_Harvey (2024-03-13 20:31 UTC)

<p>Many thanks - this is being used for presentation purposes, rather than medical analysis… but I appreciate your notes.</p>

---

## Post #4 by @lassoan (2024-03-13 20:32 UTC)

<p>For presentation purposes you can add text to the rendering using Markups module. They are rendered in a much nicer way, text always facing the camera, you can set any color, etc. and of course it is much easier to add and modify the text.</p>

---

## Post #5 by @vandg (2024-04-24 12:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="34874">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Anyway, if you still want to so it then you can use Segment Editor module’s <code>Draw text</code> effect to create the 3D text and then use <code>Mask volume</code> effect to paint it into the image.</p>
</blockquote>
</aside>
<p>Thank you, I did as you suggested and I have now 3D text as mask. But I cant perform “Mask volume” to have now this text in white inside my original volume. How should I do it correctly? the idea is to put some labels (text) inside volume to see them as a white text, and after export this volume with text to DICOM. Thank you for help!</p>
<p>How to do this - " use <code>Mask volume</code> effect to paint it into the image."`?</p>

---
