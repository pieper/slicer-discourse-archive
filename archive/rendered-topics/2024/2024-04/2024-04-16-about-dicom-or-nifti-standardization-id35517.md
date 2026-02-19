---
topic_id: 35517
title: "About Dicom Or Nifti Standardization"
date: 2024-04-16
url: https://discourse.slicer.org/t/35517
---

# About dicom or nifti standardization

**Topic ID**: 35517
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/about-dicom-or-nifti-standardization/35517

---

## Post #1 by @Berk_Gezgin (2024-04-16 08:12 UTC)

<p>Hello.<br>
I have 2 different nifti. One of them comes in the same way on the same axes as the original dicom. The other one is inverted or axial, sagittal displaced. What should I do to apply a standardization? Is there a python code to make them all look and come in the same way? Is there a module that I can examine the code on Slicer?</p>
<p>A nifti that looks wrong<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9754af01fbe51e07407a3b2a04c8fb575812aec.jpeg" data-download-href="/uploads/short-url/qsDD5Nub3gIuLxNMEgDMQg1xVZW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9754af01fbe51e07407a3b2a04c8fb575812aec_2_690x176.jpeg" alt="image" data-base62-sha1="qsDD5Nub3gIuLxNMEgDMQg1xVZW" width="690" height="176" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9754af01fbe51e07407a3b2a04c8fb575812aec_2_690x176.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9754af01fbe51e07407a3b2a04c8fb575812aec_2_1035x264.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9754af01fbe51e07407a3b2a04c8fb575812aec_2_1380x352.jpeg 2x" data-dominant-color="41403E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1426×365 92.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The right-looking nifti<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e21bdd87c0656c55c87d95c0b8bc8bbebec5e17.jpeg" data-download-href="/uploads/short-url/b9bx5zcBvGRYkuia6nEI910Ntt5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e21bdd87c0656c55c87d95c0b8bc8bbebec5e17_2_690x168.jpeg" alt="image" data-base62-sha1="b9bx5zcBvGRYkuia6nEI910Ntt5" width="690" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e21bdd87c0656c55c87d95c0b8bc8bbebec5e17_2_690x168.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e21bdd87c0656c55c87d95c0b8bc8bbebec5e17_2_1035x252.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e21bdd87c0656c55c87d95c0b8bc8bbebec5e17_2_1380x336.jpeg 2x" data-dominant-color="373737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1407×343 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-04-16 13:28 UTC)

<p>There’s no general solution for this, since nifti files can be created by many different tools making different assumptions.  You need to take care through whatever process you use that the geometry information of the scans is preserved.  We try to be very careful about this within the Slicer code but can’t control for external software.</p>

---

## Post #3 by @Berk_Gezgin (2024-04-16 13:43 UTC)

<p>Can I make their postures similar to each other? Or should I do this when converting from dicom to nifti? I have many nifti in this way. I guess I can’t translate them all according to a fixed rule.</p>

---

## Post #4 by @lassoan (2024-04-16 15:39 UTC)

<p>Probably the best way to deal with this is to fix incorrect/ambiguous NIFTI images before loading them into Slicer. For example, you can use <a href="https://nipy.org/nibabel/nifti_images.html">nibabel</a> to read the file, fix information in the header, and then write to file.</p>

---

## Post #5 by @pieper (2024-04-16 16:03 UTC)

<p>Be aware that it’s possible for there to be a left-right flip as well, so even manual correction may not be definitive depending on the pipeline used.</p>

---
