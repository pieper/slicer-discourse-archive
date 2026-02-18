# How can I change HU values into normal range?

**Topic ID**: 45379
**Date**: 2025-12-05
**URL**: https://discourse.slicer.org/t/how-can-i-change-hu-values-into-normal-range/45379

---

## Post #1 by @ChrisMak (2025-12-05 15:37 UTC)

<p>So, I have a bunch of dental cbct’s that are way too dark to be useful.</p>
<p>The source data came from transforming Viewer vol files into nhdr/nrrd, and I’m guessing all calibration (window/level) is gone (or I can’t find it).</p>
<p>The result is really dark, low contrast image, that cannot be used in AI workflows and does not work in other programs. When exported to dicom and opened in 3rd party dental software, I only see a few bright spots corresponding to metal, and nothing else.</p>
<p>Segment statistics show readings of -17.000 for bone. I don’t know its real HU value, but I’ guessing it’s too low.</p>
<p>How can I correct this, make it work with AI segmentation/registration and create usable dicom exports?</p>
<p>Things I tried and did not work:</p>
<p>Window/level, Rescale Intensity Image Filter, Intensity Windowing Image Filter.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d4b8b342c7c5e0f2feebbc460ef429dd96637f.jpeg" data-download-href="/uploads/short-url/nF0xfymExW7uwvEgGeI4y6VIFwH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5d4b8b342c7c5e0f2feebbc460ef429dd96637f_2_483x500.jpeg" alt="image" data-base62-sha1="nF0xfymExW7uwvEgGeI4y6VIFwH" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5d4b8b342c7c5e0f2feebbc460ef429dd96637f_2_483x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5d4b8b342c7c5e0f2feebbc460ef429dd96637f_2_724x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d4b8b342c7c5e0f2feebbc460ef429dd96637f.jpeg 2x" data-dominant-color="696969"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">776×802 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-12-05 17:22 UTC)

<aside class="quote no-group" data-username="ChrisMak" data-post="1" data-topic="45379">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chrismak/48/80228_2.png" class="avatar"> ChrisMak:</div>
<blockquote>
<p>Rescale Intensity Image Filter, Intensity Windowing Image Filter</p>
</blockquote>
</aside>
<p>These filters should be simply working and set intensity ranges as specified. You may also try <code>ShiftScaleImageFilter</code>, shifting right. Providing sample data is always a good idea.</p>

---

## Post #3 by @ChrisMak (2025-12-05 17:55 UTC)

<p>Thank you for your response!</p>
<p>Here is the same sample (a bit cropped).</p>
<p><a href="https://drive.google.com/file/d/11S9chRYO8emYh2c-KZRg6vzijKvBVGvM/view?usp=sharing" rel="noopener nofollow ugc">Sample volume</a></p>
<p>Would any other info help?</p>

---

## Post #4 by @chir.set (2025-12-05 20:00 UTC)

<aside class="quote no-group" data-username="ChrisMak" data-post="1" data-topic="45379">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chrismak/48/80228_2.png" class="avatar"> ChrisMak:</div>
<blockquote>
<p>Things I tried and did not work:</p>
</blockquote>
</aside>
<p>The intensities are effectively rescaled with <code>RescaleIntensityImageFilter</code>. It therefore depends on what you mean by <code>did not work</code>.</p>
<p>You may combine with <code>Percentile Rescaling</code> module, <code>CastImageFilter</code> afterwards, <code>ShiftScaleImageFilter</code> and experiment multiple combinations.</p>

---
