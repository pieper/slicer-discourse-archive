---
topic_id: 16516
title: "After Loading Dicom Files Coronal View Is Ok But Saggital Ho"
date: 2021-03-12
url: https://discourse.slicer.org/t/16516
---

# After loading DICOM files. Coronal view is OK, but Saggital, Horisontal is only can be be seen with in a small line

**Topic ID**: 16516
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/after-loading-dicom-files-coronal-view-is-ok-but-saggital-horisontal-is-only-can-be-be-seen-with-in-a-small-line/16516

---

## Post #1 by @Tamas_Egyed (2021-03-12 22:15 UTC)

<p>Operating system: Windos 10<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:<br>
<em>(screenshot removed for potential patient health information content)</em></p>

---

## Post #2 by @lassoan (2021-03-13 01:01 UTC)

<p>This appears to be a single-slice volume. Series with series number in the hundreds or thousands are typically reformatted or reprocessed images that you can ignore (and just use the original images, which has numbers 1, 2, …).</p>

---

## Post #3 by @Tamas_Egyed (2021-03-13 05:26 UTC)

<p>Dear Andras,</p>
<p>I open that DICOM files and after it i am tryeing to create liver segments and other vascular structures. But when i open segment editor only one plain is in good quality, the other two plains are are awful. I send you a screenshot attached. And from it the softawre can’t create a 3D model as well.</p>
<p>What can be the problem.<br>
Thanks for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/338353ae516e295b0c8a53a564bea35c44b0e807.jpeg" data-download-href="/uploads/short-url/7lHIuc8CEpRsXGiddMInwdi9FUr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/338353ae516e295b0c8a53a564bea35c44b0e807_2_690x341.jpeg" alt="image" data-base62-sha1="7lHIuc8CEpRsXGiddMInwdi9FUr" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/338353ae516e295b0c8a53a564bea35c44b0e807_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/338353ae516e295b0c8a53a564bea35c44b0e807_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/338353ae516e295b0c8a53a564bea35c44b0e807_2_1380x682.jpeg 2x" data-dominant-color="9B9CAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1871×925 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-03-13 13:56 UTC)

<p>This is because the image is acquired with large gaps between image slices. This reduces acquisition time (therefore reduces cost, chances of motion artifacts, increases patient comfort, and allows acquiring more images with different acquisition protocols), and if the slices are reviewed in 2D then it does not have impact the image interpretation. However, the big limitation is that such images are not well suited for 3D analysis or reformatted views. Often these sparse acquisitions are created in 3 different orientation, which mostly solves the reformatted view problem, but still not offer high-resolution 3D views. See more information here: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2" class="inline-onebox">Combining volumes - what am I missing? - #2 by lassoan</a></p>

---
