---
topic_id: 13711
title: "Rt Structure Misalignment With Image"
date: 2020-09-26
url: https://discourse.slicer.org/t/13711
---

# Rt structure misalignment with image

**Topic ID**: 13711
**Date**: 2020-09-26
**URL**: https://discourse.slicer.org/t/rt-structure-misalignment-with-image/13711

---

## Post #1 by @Iman_Shokatian (2020-09-26 13:02 UTC)

<p>Hi,</p>
<p>I have US images with its corresponding rt structure. I am using slicerrt module for visualizing rt structure but as you can see in the attached image, rt structure is not aligned correctly with the image. what should I do to align them correctly?</p>
<p>I would be appreciated for your help in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/100cc3b5158b3470a544d2679787e0a936523439.png" data-download-href="/uploads/short-url/2hYZdc3SRoPqQeo1ymrXFBynhe9.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/100cc3b5158b3470a544d2679787e0a936523439_2_472x500.png" alt="Screenshot" data-base62-sha1="2hYZdc3SRoPqQeo1ymrXFBynhe9" width="472" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/100cc3b5158b3470a544d2679787e0a936523439_2_472x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/100cc3b5158b3470a544d2679787e0a936523439_2_708x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/100cc3b5158b3470a544d2679787e0a936523439.png 2x" data-dominant-color="2E2724"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">798×845 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2020-09-26 13:51 UTC)

<p>Did you load the US images also through the DICOM browser?</p>
<p>Also, if you use 4.10.2 or older, please download a recent preview version and try again.</p>

---

## Post #3 by @Iman_Shokatian (2020-09-27 08:56 UTC)

<p>Hi cpinter,</p>
<p>I load US images through DICOM browser and do all the process by using both nightly and stable 3d slicer latest version.</p>

---

## Post #4 by @lassoan (2020-09-27 13:04 UTC)

<p>Is the structure set a full 3D volume of the prostate or just a flat single-slice segmentation? Is the ultrasound a single slice, a non-position-tracked time sequence of slices, or a reconstructed 3D volume?</p>
<p>If you want a 3D structure set line up with the ultrasound then you need to export the reconstructed 3D volume from Oncentra, not the uncalibrated, unregistered input image sequence.</p>

---
