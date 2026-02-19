---
topic_id: 8908
title: "Inconsistent Incorrect Volume Value Of Segments"
date: 2019-10-25
url: https://discourse.slicer.org/t/8908
---

# Inconsistent / Incorrect volume value of segments

**Topic ID**: 8908
**Date**: 2019-10-25
**URL**: https://discourse.slicer.org/t/inconsistent-incorrect-volume-value-of-segments/8908

---

## Post #1 by @Raid (2019-10-25 21:20 UTC)

<p>Operating system: Windows 10 Enterprise<br>
Slicer version: 4.10.2</p>
<p>Hello, I’m working on a human fetal head stained with <strong>Phosphotungstic acid</strong> (PTA) to be able to visualize soft tissue.</p>
<p>After segmentation of the tongue and the hyoid bone using grow from seeds, I used the module segment statistics to calculate the volumes and the result is inconsistent value.</p>
<p>As you can see in the screenshot the tongue volume is only 0.00934818 mm3, while a younger sample has the volume of 116.839 mm3<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7675b4f7a1000bfc415291eb24598e7254b2de0a.jpeg" data-download-href="/uploads/short-url/gTWwHhYgiJw2h5BLTd1EhtYd7ZM.jpeg?dl=1" title="13%20wk_2493%20negative%20value" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7675b4f7a1000bfc415291eb24598e7254b2de0a_2_690x388.jpeg" alt="13%20wk_2493%20negative%20value" data-base62-sha1="gTWwHhYgiJw2h5BLTd1EhtYd7ZM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7675b4f7a1000bfc415291eb24598e7254b2de0a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7675b4f7a1000bfc415291eb24598e7254b2de0a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7675b4f7a1000bfc415291eb24598e7254b2de0a_2_1380x776.jpeg 2x" data-dominant-color="989598"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">13%20wk_2493%20negative%20value</span><span class="informations">1920×1080 426 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>what am I doing wrong, or need to be adjusted?</p>
<p>Thank you,<br>
Raid</p>

---

## Post #2 by @pieper (2019-10-25 21:42 UTC)

<p>Is the volume spacing correct for this volume (compare the Volume Information in the Volumes module for the volumes at the two timepoints).</p>

---

## Post #3 by @Raid (2019-10-28 19:35 UTC)

<p>Thank you for replying. I’ve cropped the volume to the desired area to be segmented just to reduce the size of the dicoms as the software used to crash. As you said I compared the image spacing in the cropped and the original dicoms and they’re much different.</p>
<p>Do you think that I should just enter the values of the image spacing from the original to the cropped one and re-segment again?</p>
<p>Regards,</p>

---

## Post #4 by @pieper (2019-10-28 20:34 UTC)

<p>If you know the correct pixel spacing for the volume you can just change it in the Volumes module.  Not sure you can change a segmentation once it’s created, but if you don’t want to resegment you could export to a labelmap, change the spacing, and re-import to a segmentation.</p>

---

## Post #5 by @lassoan (2019-10-28 21:03 UTC)

<p>You can modify scale of a segmentation by applying (and then hardening) a transform on it. Diagonal values in the transformation matrix contain the scaling factors.</p>

---
