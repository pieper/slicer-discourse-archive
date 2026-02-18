# X ray Image enhancement extension in slicer?

**Topic ID**: 15469
**Date**: 2021-01-12
**URL**: https://discourse.slicer.org/t/x-ray-image-enhancement-extension-in-slicer/15469

---

## Post #1 by @drvarunagarwal (2021-01-12 12:02 UTC)

<p>Hi,</p>
<p>Is there an image enhancement extension for slicer that can take a poor quality x ray and enhance the structures (esp. bone) automatically and then maybe some contrast brightness sliders to manually fine tune it?</p>
<p>Can this be done in slicer?</p>
<p>Please advise.<br>
Thanks</p>

---

## Post #2 by @lassoan (2021-01-12 17:44 UTC)

<p>Simple Filters module contains lots of image processing tools that you can use to improve X-ray image visualization, such as various noise filters and smoothing methods, intensity rescaling or equalization. I don’t think any of these can fix a poor quality X-ray, but it may be able to improve it.</p>
<p>If you identify a few filters that are useful then you put them into a dedicated scripted module, with a simplified user interface.</p>

---

## Post #3 by @lassoan (2021-01-12 18:37 UTC)

<p>A post was split to a new topic: <a href="/t/acquire-images-from-c-arm/15478">Acquire images from C-arm</a></p>

---

## Post #4 by @drvarunagarwal (2021-01-19 17:23 UTC)

<p>Hi,</p>
<p>I have tried using simple filters module on a static x ray image but am unable to get any proper output.</p>
<p>Please advise how to achieve this.</p>

---

## Post #5 by @lassoan (2021-01-20 05:40 UTC)

<p>What are the problems in the image that you are trying to fix? Which filters did you try? Can you attach a few example images of what you have now and what you would like to get after processing?</p>

---

## Post #6 by @drvarunagarwal (2021-01-20 15:33 UTC)

<p>I just imported a JPG/PNG file of a poor quality X ray of pelvis - just to test waters.</p>
<p>I dragged it in one of the window panes.</p>
<p>And tried to apply some random filters.</p>
<p>Mostly I get an error</p>
<p>Please advise</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18892df10e8b3b06646f1a257b7dffec6a7f2a30.jpeg" data-download-href="/uploads/short-url/3v3mCMnB6zgmr2zM9HerRKRsTg4.jpeg?dl=1" title="WhatsApp Image 2021-01-15 at 15.24.03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18892df10e8b3b06646f1a257b7dffec6a7f2a30_2_580x500.jpeg" alt="WhatsApp Image 2021-01-15 at 15.24.03" data-base62-sha1="3v3mCMnB6zgmr2zM9HerRKRsTg4" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18892df10e8b3b06646f1a257b7dffec6a7f2a30_2_580x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18892df10e8b3b06646f1a257b7dffec6a7f2a30_2_870x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18892df10e8b3b06646f1a257b7dffec6a7f2a30_2_1160x1000.jpeg 2x" data-dominant-color="3C4D5D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2021-01-15 at 15.24.03</span><span class="informations">2752×2369 486 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8ddb08d72c13d90bde50b981fc2bd7f8de9fa3ce.jpeg" data-download-href="/uploads/short-url/keUBmBVDMFhfuvEGAHehX1PEWAu.jpeg?dl=1" title="WhatsApp Image 2021-01-16 at 17.10.44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ddb08d72c13d90bde50b981fc2bd7f8de9fa3ce_2_288x500.jpeg" alt="WhatsApp Image 2021-01-16 at 17.10.44" data-base62-sha1="keUBmBVDMFhfuvEGAHehX1PEWAu" width="288" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ddb08d72c13d90bde50b981fc2bd7f8de9fa3ce_2_288x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ddb08d72c13d90bde50b981fc2bd7f8de9fa3ce_2_432x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ddb08d72c13d90bde50b981fc2bd7f8de9fa3ce_2_576x1000.jpeg 2x" data-dominant-color="92979F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2021-01-16 at 17.10.44</span><span class="informations">718×1246 80.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2021-01-20 16:38 UTC)

<p>Probably you want to first convert your color image to grayscale using “Vector to scalar volume” module.</p>

---
