---
topic_id: 10840
title: "New Lightbox Contact Image Mode In Screen Capture Module"
date: 2020-03-25
url: https://discourse.slicer.org/t/10840
---

# New lightbox (contact image) mode in screen capture module

**Topic ID**: 10840
**Date**: 2020-03-25
**URL**: https://discourse.slicer.org/t/new-lightbox-contact-image-mode-in-screen-capture-module/10840

---

## Post #1 by @lassoan (2020-03-25 23:28 UTC)

<p>A new “lightbox image” output type has been added in latest Slicer Preview Release. In this mode captured images are exported as a large grid of images:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b737f2e84e22dbe5725e57b74040dfa74fc7e38.jpeg" data-download-href="/uploads/short-url/mbbsraigdO5OdE17N7EAXim06Gk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b737f2e84e22dbe5725e57b74040dfa74fc7e38_2_690x236.jpeg" alt="image" data-base62-sha1="mbbsraigdO5OdE17N7EAXim06Gk" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b737f2e84e22dbe5725e57b74040dfa74fc7e38_2_690x236.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b737f2e84e22dbe5725e57b74040dfa74fc7e38_2_1035x354.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b737f2e84e22dbe5725e57b74040dfa74fc7e38_2_1380x472.jpeg 2x" data-dominant-color="525150"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">5188×1775 1.75 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Images can be exported from any views, with any animation mode, just select “Output type” → “lightbox image”. Number of columns is adjustable in Advanced section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c7fa019c8ddd0bf1957e63551324a6e76df0fc5.jpeg" data-download-href="/uploads/short-url/mkrV8nslGxYE7hYKKQO4HxFTQHj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c7fa019c8ddd0bf1957e63551324a6e76df0fc5_2_690x461.jpeg" alt="image" data-base62-sha1="mkrV8nslGxYE7hYKKQO4HxFTQHj" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c7fa019c8ddd0bf1957e63551324a6e76df0fc5_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c7fa019c8ddd0bf1957e63551324a6e76df0fc5_2_1035x691.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c7fa019c8ddd0bf1957e63551324a6e76df0fc5_2_1380x922.jpeg 2x" data-dominant-color="CCCACB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1773×1186 471 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We plan to further improve this lightbox view generation in the future and retire dynamic lightbox views. Any comments and suggestions are welcome.</p>

---

## Post #2 by @sophiasol (2025-09-18 18:24 UTC)

<p>Thank so much for the quick reply! Can this be applied to a specific ROI?</p>
<p>Thank you again,</p>
<p>Sophia</p>

---

## Post #3 by @lassoan (2025-09-18 22:40 UTC)

<p>Yes, you can choose any ROI: you set the first and last slice in the module and zoom in/out the view to select the relevant part within the slice. An alternative ia tonuae Crop Volume module before capturing the screenshots.</p>
<p>Note that all these are just for producing visuals for presentations, papers, etc. If you need to extract slices for data processing (preserving the data in full fidelity) then you can simply crop and resample the volume.</p>

---

## Post #4 by @mohammed_alshakhas (2025-09-19 04:21 UTC)

<p>the control is bit not clear .  im trying to do from lateral to medial but seem awkward . with column and number of slices .</p>
<p>can we in addition to capture first preview / view the lightbox first ? live preview is gonna be great for this</p>

---

## Post #5 by @sophiasol (2025-09-19 14:37 UTC)

<p>You were very helpful! Thank you again for such a quick reply.</p>
<p>Best,</p>
<p>Sophia</p>

---

## Post #6 by @sophiasol (2025-09-19 14:46 UTC)

<p>Understood, this is exactly why I need it. Apart from choosing the first and last slide and the number of images, is there a way to define the step and thickness of each slice? For example, an image taken every 1mm of the volume with 1mm thickness?</p>

---

## Post #7 by @lassoan (2025-09-19 16:04 UTC)

<p>Step size: the step size comes from dividing the difference between the <code>start sweep offset</code> and <code>end sweep offset</code> by (<code>number of images</code> - 1)</p>
<p>Slice thickness: you can set it in the slice view controller<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/481f7ec44f4ddf50b5a3fa0047d594f83385aa54.jpeg" data-download-href="/uploads/short-url/ai1R4qwEpc4wsa0Ina7MJhn7nYo.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f7ec44f4ddf50b5a3fa0047d594f83385aa54_2_690x253.jpeg" alt="image" data-base62-sha1="ai1R4qwEpc4wsa0Ina7MJhn7nYo" width="690" height="253" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f7ec44f4ddf50b5a3fa0047d594f83385aa54_2_690x253.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f7ec44f4ddf50b5a3fa0047d594f83385aa54_2_1035x379.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/481f7ec44f4ddf50b5a3fa0047d594f83385aa54_2_1380x506.jpeg 2x" data-dominant-color="5B5257"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1656×609 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2025-09-19 16:28 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="4" data-topic="10840" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>the control is bit not clear . im trying to do from lateral to medial but seem awkward . with column and number of slices .</p>
<p>can we in addition to capture first preview / view the lightbox first ? live preview is gonna be great for this</p>
</blockquote>
</aside>
<p><code>Main view</code>: Choose the slice that has the orientation you need as “main view”. Lateral to medial would be sagittal slicer → <code>Yellow</code> slice.</p>
<p><code>Capture mode</code> → <code>slice sweep</code>.</p>
<p><code>Start sweep offset</code> and <code>End sweep offset</code> → set visually.</p>
<p><code>Output type</code> → <code>lightbox image</code>.</p>
<p><code>Number of images</code>: rows x columns. You can set something like 36.</p>
<p><code>Advanced / Lightbox image columns</code> → you can leave the default 6.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd0ec32886478a567db83448120733dac6a8e6be.jpeg" data-download-href="/uploads/short-url/qYtRWzx2iKc6eJxvBWYUBLCfHIy.jpeg?dl=1" title="SlicerCaptureLightboxS"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd0ec32886478a567db83448120733dac6a8e6be_2_690x404.jpeg" alt="SlicerCaptureLightboxS" data-base62-sha1="qYtRWzx2iKc6eJxvBWYUBLCfHIy" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd0ec32886478a567db83448120733dac6a8e6be_2_690x404.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd0ec32886478a567db83448120733dac6a8e6be.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd0ec32886478a567db83448120733dac6a8e6be.jpeg 2x" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerCaptureLightboxS</span><span class="informations">1000×586 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
