---
topic_id: 511
title: "Segmenting Semi Circular Canals"
date: 2017-06-15
url: https://discourse.slicer.org/t/511
---

# Segmenting Semi-Circular Canals

**Topic ID**: 511
**Date**: 2017-06-15
**URL**: https://discourse.slicer.org/t/segmenting-semi-circular-canals/511

---

## Post #1 by @victoria.rose (2017-06-15 17:32 UTC)

<p>Hello,</p>
<p>I am working with the semicircular canals and want to output measurements from the outer edge of each canal to the sagittal plane. I was wondering if there is a consistent way to make this measurement after marking the canal with a fiducial point? Or do I have to manually use the ruler for this?</p>
<p>I am also trying to segment the canals for volume calculations, however these structures are very small and faint. Would the segmentation module with thresholding and manual clean-up be best for this purpose? Are there any image filters you recommend to make thresholding better apply to the MRI?</p>
<p>Thanks!<br>
Victoria</p>
<p>Slicer version: 4.6.2</p>

---

## Post #2 by @lassoan (2017-06-15 17:45 UTC)

<p>Could you attach a few typical images so that we have a better idea about the kind of data you work with?</p>
<p>Measuring volumes by manual segmentation using Segment editor and Segment statistics module should work well. You probably need to crop and resample your input volume using Crop volumes module prior segmentation if the structures are small. Use the latest nightly version of Slicer, it is stable and has lots of fixes and improvements compared to the latest stable.</p>
<p>For distance measurement, probably the simplest is to write a Python script (probably a few lines of code) that computes fiducial positions from a specific plane. You can also wrap those few lines of code in a Python scripted module to make it more user-friendly.</p>

---
