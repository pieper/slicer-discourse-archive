---
topic_id: 1733
title: "Rescaling The Dicom Images Using The Rescaleintercept And Re"
date: 2017-12-27
url: https://discourse.slicer.org/t/1733
---

# Rescaling the DICOM images using the RescaleIntercept and RescaleSlope

**Topic ID**: 1733
**Date**: 2017-12-27
**URL**: https://discourse.slicer.org/t/rescaling-the-dicom-images-using-the-rescaleintercept-and-rescaleslope/1733

---

## Post #1 by @fukiracs (2017-12-27 16:59 UTC)

<p>Hello Everyone,</p>
<p>I am new to the 3D Slicer software and I wanted to know if there is an option to rescale the DICOM images (For example from a Cone Beam CT) using the RescaleSlope and RescaleIntercept. To convert from the normal units found in CT data (a typical data set ranges from 0 to 4000 or so) we have to apply a linear transformation of the data using an equation given as:</p>
<p>hu = pixel_value * slope + intercept</p>
<p>(Citation : <a href="http://www.idlcoyote.com/fileio_tips/hounsfield.html" rel="nofollow noopener">http://www.idlcoyote.com/fileio_tips/hounsfield.html</a>)</p>
<p>While I can apply this transformation in Matlab, but it requires a lot of time to rescale every *.dcm file. Is there an option in 3D Slicer to do it? or is it automatically applied while loading the data into the software?. I will be grateful for the help.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2017-12-27 17:18 UTC)

<p>Rescaling is applied automatically. You can verify this by hovering the mouse pointer over the image and checking the voxel values displayed in the panel in the lower left corner.</p>

---
