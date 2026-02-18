# How to convert BMP CT scan slices into properly scaled viewable model ?

**Topic ID**: 19094
**Date**: 2021-08-06
**URL**: https://discourse.slicer.org/t/how-to-convert-bmp-ct-scan-slices-into-properly-scaled-viewable-model/19094

---

## Post #1 by @mdear (2021-08-06 04:35 UTC)

<p>I received an airway scan from radiology and I want to create a viewable rotatable correctly scaled model.  I plan to scan a prototype tracheostomy tube and check for fit prior to insertion into the patient.</p>
<p>The scan came in the form of 2GB of BMP files, a selection of which (anonymized) are shown below.</p>
<p>What is the correct procedure to convert this into a model that is a correctly scaled digital twin of the patient ?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f679e5f86b6a69da5bc3d7dca6ed243b7211f526.png" alt="image" data-base62-sha1="zaqCFqwK20baX0En866rAJbDUge" width="676" height="211"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f679e5f86b6a69da5bc3d7dca6ed243b7211f526.png" alt="image" data-base62-sha1="zaqCFqwK20baX0En866rAJbDUge" width="676" height="211"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8207bdf2287e467cf4624c0cb809b0e12c99a699.jpeg" alt="image" data-base62-sha1="iyiEOneMtzi4FMfcvZZKJIygRL3" width="675" height="491"></p>

---

## Post #2 by @pieper (2021-08-06 11:28 UTC)

<p>Unfortunately it would be very hard to accurately reconstruct this data to perform the task you described.  BMP is just a picture format and these appear to be screen captures of reformatted data.  You might be able to somehow recalibrate using the burned in ruler but that would be inaccurate and error-prone.</p>
<p>What you need is the original DICOM data so that you know the exact pixel and slice spacing and can easily use the standard tools in Slicer.  If you are working with the radiology department they should be able to provide this to you easily.</p>

---

## Post #3 by @lassoan (2021-08-07 16:36 UTC)

<p>In addition to unknown pixel spacing, screenshots are also problematic because they are much more noisy than the original DICOM images: DICOM CT images typically use 12 bits per pixel, while BMP only uses 8 bits per pixel. This noise may not entirely prevent the segmentation, but may make segmented surfaces uneven, which can either be reduced by automatic smoothing methods (but those might remove some relevant details) or by tedious manual corrections.</p>

---

## Post #4 by @mdear (2021-08-08 17:49 UTC)

<p>Thanks for the responses, everybody, and for putting me back in school.  So far I tried using FileStar to convert the BMP files to DICOM but this was unsuccessful.  I finally approached the radiology department and got a DICOM-only disk, and I was able to get a 3D model rendered from this data.</p>

---

## Post #5 by @mira_mira (2024-01-28 02:18 UTC)

<p>Hi,</p>
<p>Thank you for sharing this topic. I saw this topic is in 2021. So, Is there any possibilities to save in stl file from bmp file (Xray Ct Scan) nowadays? May be doing some segmentation? FYI, I am not able to retrieve the dicom file since I have the file quite long time ago and the scan was done in different country as mine.<br>
Thanks</p>

---

## Post #6 by @muratmaga (2024-01-29 16:55 UTC)

<p>You can import non-dicom (BMP/JPG/PNG) image sequences into slicer using SLicerMorph extension’s <code>ImageStacks</code> module, and then you can use segmentation pipeline to create 3D models out of them. If you are working with microCT data, see our tutorials at <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a>.</p>
<p>However, the problem in the original post was provided data was not original CT slices, but secondary screencapture. It is hard to work with that data as it will be missing some crucial metadata such as correct image spacing, coordinate systems etc…</p>

---
