# Overlay a segmentation over a grayscale volume

**Topic ID**: 19314
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/overlay-a-segmentation-over-a-grayscale-volume/19314

---

## Post #1 by @LHJ (2021-08-23 12:04 UTC)

<p>I want to visualize the ground truth segmentation overlayed on the chest CT volume. Last time I managed to get a clear visible segmentation overlay (shown below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78628387813d15ed749ceb0bd91943f0fdf768fd.jpeg" data-download-href="/uploads/short-url/haYmoIeu7RTIte2SkOGD6VqdRgN.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78628387813d15ed749ceb0bd91943f0fdf768fd_2_626x500.jpeg" alt="Screenshot" data-base62-sha1="haYmoIeu7RTIte2SkOGD6VqdRgN" width="626" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78628387813d15ed749ceb0bd91943f0fdf768fd_2_626x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78628387813d15ed749ceb0bd91943f0fdf768fd_2_939x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78628387813d15ed749ceb0bd91943f0fdf768fd.jpeg 2x" data-dominant-color="B5B2AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1190×949 97.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when I try again today, I do not get the same result. Actually, I forgot the exact procedures that I have taken last time. What I get now is<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/119f4bdf1281497772dffd23e9fc5695f620046c.jpeg" data-download-href="/uploads/short-url/2vTphYqxFW1OeLYnHR40bUL1vKA.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119f4bdf1281497772dffd23e9fc5695f620046c_2_400x500.jpeg" alt="Capture.PNG" data-base62-sha1="2vTphYqxFW1OeLYnHR40bUL1vKA" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119f4bdf1281497772dffd23e9fc5695f620046c_2_400x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119f4bdf1281497772dffd23e9fc5695f620046c_2_600x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/119f4bdf1281497772dffd23e9fc5695f620046c.jpeg 2x" data-dominant-color="A69884"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">662×827 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The segmentation is barely visible. Anyone has an idea how to get the first volume overlay?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @lassoan (2021-08-23 12:09 UTC)

<p>You need to make the segmentation a bit larger so that the volume rendering does not occlude it. You can achieve it by lowering the threshold value or expand using margin effect. Making the volume rendering semi-transparent may help, too.</p>

---
