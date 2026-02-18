# NRRD contour  to Dicom 

**Topic ID**: 8936
**Date**: 2019-10-29
**URL**: https://discourse.slicer.org/t/nrrd-contour-to-dicom/8936

---

## Post #1 by @John.ryan3 (2019-10-29 11:46 UTC)

<p>Operating system: Windows 7 Enterprise<br>
Slicer version:4:11.0</p>
<p>I am not sure did my last question post correctly. It is my first time asking a question here, I douth it will be my last <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I have a CT and Segmentation/Contour in .NRRD format<br>
I have the same CT in Dicom format.<br>
I want to get the segmentation/contour into Dicom format</p>
<p>When I load the CT and Segmentation/Contour in .NRRD format, the scale and orientation is off</p>
<p>I can fix the orientation by applying a flip transform</p>
<p>I am looking for a scale transform so that I can scale the CT + Segmentation/Contour by the same amount.</p>
<p>Appreciate any help. It looks like like the .nrrd files are scaled by a magnitude of 10 wrong. mm instead of cm.</p>
<p>Any help appreciated.<br>
John</p>

---

## Post #2 by @John.ryan3 (2019-10-29 11:48 UTC)

<p>Operating system:Windows 7 Enterprise<br>
Slicer version:4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I have an original CT in Dicom format<br>
I have the same CT in .NRRD format<br>
I have a segmentation/contour in .NRRD format</p>
<p>I want the segmentation/contour in Dicom format with the same scale and orientation as original CT</p>
<p>When I load CT + segmentation/contour in NRRD format the scale and orientation are incorrect.</p>
<p>I can fix the orientation by applying a flip transformation</p>
<p>I don’t know how to create a scale transformation</p>
<p>Best wishes,<br>
John</p>

---
