# Correction of misaligned slices in cardiac segmentation from MRI image

**Topic ID**: 26716
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/correction-of-misaligned-slices-in-cardiac-segmentation-from-mri-image/26716

---

## Post #1 by @bmoscoloni (2022-12-13 20:32 UTC)

<p>Hello,</p>
<p>I am currently working on the segmentations from a multi-vendor dataset of CMR of which I have the ED frame and the corresponding segmentation for LV, RV, and myocardium. When uploading both the frame and the segmentation, the two are correctly aligned however when reconstructing the 3D segmentation (attached picture) there i still misalignment in-between slices.<br>
Is there a way or any extension in Slicer to correct for such misalignment or to go around this problem?</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d084af201bb9f664f3bf52e4c4a6ff71b63923d.jpeg" data-download-href="/uploads/short-url/aZsx0qQAkBKATbWuFIGsIZqFhy5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d084af201bb9f664f3bf52e4c4a6ff71b63923d_2_690x457.jpeg" alt="image" data-base62-sha1="aZsx0qQAkBKATbWuFIGsIZqFhy5" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d084af201bb9f664f3bf52e4c4a6ff71b63923d_2_690x457.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d084af201bb9f664f3bf52e4c4a6ff71b63923d_2_1035x685.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d084af201bb9f664f3bf52e4c4a6ff71b63923d_2_1380x914.jpeg 2x" data-dominant-color="34343C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1406×932 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-12-13 20:56 UTC)

<p>It seems that ECG gating did not work very well and the frames were acquired in slightly different phases. The easiest could be to skip those few slices that are off and use “Fill between slices” or other tools to fill the gap (without using those slightly off-phase slices).</p>

---
