---
topic_id: 47320
title: "Airway segmentation of mouse lung"
date: 2026-06-11
url: https://discourse.slicer.org/t/47320
last_bumped: 2026-06-11T20:54:21.297Z
---

# Airway segmentation of mouse lung

**Topic ID**: 47320
**Date**: 2026-06-11
**URL**: https://discourse.slicer.org/t/airway-segmentation-of-mouse-lung/47320

---

## Post #1 by @ljuno (2026-06-11 20:54 UTC)

<p>Hello,</p>
<p>I am working with 3D slicer in hopes to segment the airway of this mouse lung, acquired from lightsheet microscopy. I would like to segment the main airways, but not the alveoli (at least not yet - I am hoping to do this in the future though) to measure the diameter of the airways and how they change in diameter as they get further away from the main bronchial tree. I have tried to use the threshold tool since it is dark in the airways, but I am still picking up the alveoli. I have also tried the grow from seeds module but it seems like it would require a lot of manual effort to get my segments how I would like them. That is fine and I can do the manual painting to fix it, but I was just wondering if there would be a more effective way to do this? I have not been able to use any of the lung/airway modules/extensions since my data is of a single (left) lung of a mouse from lightsheet microscopy and the ones I have seen are for both human lungs from CT. Thank you very much in advance for any advice you have!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9.jpeg" data-download-href="/uploads/short-url/dmt4PydSASLHW7O6cPf0mXxxY7v.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_690x353.jpeg" alt="image" data-base62-sha1="dmt4PydSASLHW7O6cPf0mXxxY7v" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5da679dad74bac258895c69e7d51a47027c325e9_2_1380x706.jpeg 2x" data-dominant-color="3C3530"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×984 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7.jpeg" data-download-href="/uploads/short-url/mYniXAn95EbZtDoxTqJ1LDS8hdd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_690x355.jpeg" alt="image" data-base62-sha1="mYniXAn95EbZtDoxTqJ1LDS8hdd" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a10300aba3348dcafe5e3a4ab478c8104709ccf7_2_1380x710.jpeg 2x" data-dominant-color="4B4747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×988 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
