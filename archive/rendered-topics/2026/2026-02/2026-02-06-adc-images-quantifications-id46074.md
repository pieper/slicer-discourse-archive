---
topic_id: 46074
title: "Adc Images Quantifications"
date: 2026-02-06
url: https://discourse.slicer.org/t/46074
---

# ADC images Quantifications 

**Topic ID**: 46074
**Date**: 2026-02-06
**URL**: https://discourse.slicer.org/t/adc-images-quantifications/46074

---

## Post #1 by @a.altairan (2026-02-06 14:20 UTC)

<p>hello everyone</p>
<p>I’m doing study involving Lumber spine, I’m trying to calculate the ADC mean and median values</p>
<p>but I’m getting values with ( - ), how to overcome this issue ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f7ae85d3636ee003f8f5de9a88d2fafbcc6b396.jpeg" data-download-href="/uploads/short-url/2cWupB4Jh7rFCjvMpuYQ8TTWrmm.jpeg?dl=1" title="Screenshot 2026-02-06 at 9.30.07 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f7ae85d3636ee003f8f5de9a88d2fafbcc6b396_2_690x388.jpeg" alt="Screenshot 2026-02-06 at 9.30.07 AM" data-base62-sha1="2cWupB4Jh7rFCjvMpuYQ8TTWrmm" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f7ae85d3636ee003f8f5de9a88d2fafbcc6b396_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f7ae85d3636ee003f8f5de9a88d2fafbcc6b396_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f7ae85d3636ee003f8f5de9a88d2fafbcc6b396_2_1380x776.jpeg 2x" data-dominant-color="373738"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-02-06 at 9.30.07 AM</span><span class="informations">1920×1080 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2026-02-06 18:30 UTC)

<p>What does the Data Probe show when you hover over these regions (voxel values under the mouse cursor are shown in the lower left area of the Slicer window, under where it says Data Probe)?  If it shows these negative values, then the problem is in how you are loading or importing these images, yielding negative voxel values for diffusion coefficients.  If it shows only positive voxel values, then something is going wrong in the Segment Statistics module.  My guess is that the voxel values are actually negative and the Segment Statistics module is just compiling those values for you. When your ADC image data is imported, perhaps the voxel information is being misinterpreted (bad DICOM header, corrupt file, something else?).</p>

---

## Post #3 by @a.altairan (2026-02-09 19:22 UTC)

<p>Hi Mr. Bindschadler, thank you for your valuable input.<br>
As you suggested, the results include negative values. I would appreciate your advice on how to address this issue.</p>
<p>Much appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5c728c95f43b6a22d48c1727ed0fe3369595b3c.jpeg" data-download-href="/uploads/short-url/nExtJdtUP4rP6QKV0NeVYyrLxOA.jpeg?dl=1" title="Screenshot 2026-02-09 at 9.51.04 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5c728c95f43b6a22d48c1727ed0fe3369595b3c_2_690x388.jpeg" alt="Screenshot 2026-02-09 at 9.51.04 PM" data-base62-sha1="nExtJdtUP4rP6QKV0NeVYyrLxOA" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5c728c95f43b6a22d48c1727ed0fe3369595b3c_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5c728c95f43b6a22d48c1727ed0fe3369595b3c_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5c728c95f43b6a22d48c1727ed0fe3369595b3c_2_1380x776.jpeg 2x" data-dominant-color="1B1C1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-02-09 at 9.51.04 PM</span><span class="informations">1920×1080 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mikebind (2026-02-09 23:08 UTC)

<p>I have not run into this exact issue.  To help troubleshoot, we would need to know how you load this imaging data into Slicer (e.g. DICOM import?, exported file from some other software?).  If DICOM import, I might look through the DICOM metadata to see if it seems like the voxel data is supposed to be scaled/offset in some way.  Do you have another way to look at the data where you can compare voxel values?</p>

---
