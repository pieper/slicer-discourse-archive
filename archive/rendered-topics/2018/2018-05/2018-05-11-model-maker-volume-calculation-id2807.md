---
topic_id: 2807
title: "Model Maker Volume Calculation"
date: 2018-05-11
url: https://discourse.slicer.org/t/2807
---

# Model Maker - Volume Calculation

**Topic ID**: 2807
**Date**: 2018-05-11
**URL**: https://discourse.slicer.org/t/model-maker-volume-calculation/2807

---

## Post #1 by @cphillips (2018-05-11 16:02 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1</p>
<p>I am working with MRI data (.nii or NIFTI format, 8 slices) and trying to calculate the volume of a particular segment in each slice where it appears. For each slice, I am using the segment editor to make a segment for the area of interest (using threshold for masking and then paint), exporting it to a labelmap, and then using model maker to make a model of that label. From there, I can view the volume under the Models menu, under “Information”.</p>
<p>I am wondering if/how 3D slicer takes into account the slice thickness (specified by the DICOM header in the original DICOM directory) when performing this volume calculation, and if this slice-by-slice method will be an accurate way to calculate the entire volume (i.e. does it interpolate between slices when calculating the volume, or does it only calculate the volume for the specified slice?)</p>
<p>Any information on this would be fantastic! Thank you.</p>

---

## Post #2 by @lassoan (2018-05-11 16:20 UTC)

<p>You can measure segment surfaces and volumes from much easier, using Segment Statistics module.</p>
<aside class="quote no-group" data-username="cphillips" data-post="1" data-topic="2807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/848f3c/48.png" class="avatar"> cphillips:</div>
<blockquote>
<p>I am wondering if/how 3D slicer takes into account the slice thickness</p>
</blockquote>
</aside>
<p>It takes into account when constructs a 3D image from slices.</p>
<aside class="quote no-group" data-username="cphillips" data-post="1" data-topic="2807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/848f3c/48.png" class="avatar"> cphillips:</div>
<blockquote>
<p>if this slice-by-slice method will be an accurate way to calculate the entire volume</p>
</blockquote>
</aside>
<p>Yes, it is. It accurately quantifies the volume that you see. If that representation is accurate then the measured volume and surface will be accurate, too.</p>

---

## Post #3 by @cphillips (2018-05-11 17:42 UTC)

<p>thank you, this helps a lot. I was also wondering, does 3D Slicer know to exclude the gap between slices when calculating the volume (i.e. the MRI data I am working with has a slice thickness of 1mm and a distance between adjacent slices of 1mm)?</p>

---

## Post #4 by @lassoan (2018-05-11 18:41 UTC)

<p>DICOM defines the exact position of each image slice, so geometry can be reconstructed accurately. Slice thickness just defines image blurring (thickness of the region that is averaged to generate the image slice) and has no effect on the reconstruction.</p>

---

## Post #5 by @cphillips (2018-05-11 19:52 UTC)

<p>So say the segment being calculated is approximately an ellipsoid (volume = (4/3)<em>pi</em>a<em>b</em>c, where c is the thickness of the slice (not including the gap between slices). Does 3D Slicer use the Slice Thickness used during imaging to calculate the volume of this type of segment?</p>

---

## Post #6 by @cphillips (2018-05-11 20:50 UTC)

<p>Which method is more accurate, Segment Statistics, or constructing the model like I have been doing?</p>

---

## Post #7 by @lassoan (2018-05-11 21:35 UTC)

<p>Accuracy of measured volume primarily depends on how accurately you segment the structures.</p>
<p>We report surfaces and volumes of the structures that you see, as you see, very accurately (the error is probably less than 0.001%).</p>
<p>Some smoothing is applied during labelmap to closed surface conversion, so there is typically a small volume difference there (typically well below 1%). But again, you can see both representations exactly and based on that you can decide which value to use.</p>
<p>There are no gaps between slices. If you want, you can leave gaps in the segmentation but then you will very clearly see them so you you do not have to worry about accidentally having some gaps that affect the results.</p>
<p>Segment Statistics computes the same volumes for the same inputs, but it is more convenient to use. It relies on Segmentations module to convert between labelmap and closed surface representations, so the generated surface may be slightly different compared to model maker.</p>

---

## Post #8 by @cphillips (2018-05-15 15:24 UTC)

<p>Thank you. Just to clarify, the error is probably less than 0.001% for both methods?</p>

---

## Post #9 by @lassoan (2018-05-16 20:05 UTC)

<p>Yes, you get the volume of the segmentation or model node what you see very accurately.</p>

---

## Post #10 by @Ash_Alarfaj (2018-06-13 09:16 UTC)

<p>So if I measure volume of some slices, using segment static,I don’t need to multiply the slice thickness to total volume?</p>

---

## Post #11 by @cpinter (2018-06-13 18:01 UTC)

<p>No, the volume measurements calculated by Segment Statistics are not only in voxels, but also in mm3 and cc, see header of the resulting table:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/865c861fb8efbabb3ae6c0c5c966eda6f60e5212.png" alt="image" data-base62-sha1="jaCdblayudtXLKQBN6DCX1r64g2" width="409" height="57"></p>

---

## Post #12 by @Ash_Alarfaj (2018-06-14 10:54 UTC)

<p>Hi<br>
thanks for your response. Actually, I am so struggling, I’ve tried to compare 3Dslicer result with another manual programme but the result doesn’t match. our MRI images with slice thickness 5 mm and space 5mm. so how I can add this values to my segmentation?</p>

---

## Post #13 by @Ash_Alarfaj (2018-06-14 11:30 UTC)

<p>then when I have tried to meagre the slices, the same calculation I have got when I missed 2 slices gab?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ab110bc333b5474dd13cb6e1878f05ebe874466.png" data-download-href="/uploads/short-url/3O7M3fXFBIlIwSxPqzb9k3cKU4u.png?dl=1" title="merge%20slices" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ab110bc333b5474dd13cb6e1878f05ebe874466_2_690x387.png" alt="merge%20slices" data-base62-sha1="3O7M3fXFBIlIwSxPqzb9k3cKU4u" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ab110bc333b5474dd13cb6e1878f05ebe874466_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ab110bc333b5474dd13cb6e1878f05ebe874466_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ab110bc333b5474dd13cb6e1878f05ebe874466.png 2x" data-dominant-color="A8A9AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">merge%20slices</span><span class="informations">1366×768 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @lassoan (2018-06-14 11:43 UTC)

<p>The stripes on the image indicate that you are looking at the preview of “Fill between slices” effect result.</p>
<p>Click “Fill between slices” effect button and click “Apply” to complete the segmentation.</p>

---
