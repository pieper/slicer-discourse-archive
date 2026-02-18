# Diffusion-weighted DICOM Import (DWIConvert) standard error

**Topic ID**: 3086
**Date**: 2018-06-06
**URL**: https://discourse.slicer.org/t/diffusion-weighted-dicom-import-dwiconvert-standard-error/3086

---

## Post #1 by @Egor (2018-06-06 08:07 UTC)

<p>I have the problem with with DWIConvert module (DICOM to nrrd).<br>
In the window below:</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>W: DcmItem: Length of element (5a4d,0090) is odd<br>
E: DcmElement: Unknown Tag &amp; Data (1024,488b) larger (138951436) than remaining bytes in file<br>
W: DcmItem: Dataset not in ascending tag order, at element (1024,488b)<br>
W: DcmItem: Length of element (5a4d,0090) is odd<br>
W: DcmItem: Length of element (7777,7777) is odd<br>
E: DcmElement: Unknown Tag &amp; Data (7777,7777) larger (2021095287) than remaining bytes in file<br>
W: DcmItem: Dataset not in ascending tag order, at element (7777,7777)<br>
Error: no DICOMfiles found in inputDirectory: .<br>
Unable to create converter!</p>

---

## Post #2 by @ihnorton (2018-06-06 12:31 UTC)

<p>DWIConvert requires all files to be from the same sequence. If you have SlicerDMRI extension installed, the DICOM Diffusion Volume plugin may be able to sort your files (but does not support all scanners/models).  If you are using an older Slicer version, please try a recent nightly build.</p>
<p>If that does not help, then please post your scanner model and Slicer version.</p>

---

## Post #3 by @Egor (2018-07-31 08:53 UTC)

<p>I have SlicerDMRI extension but there is no DICOM Diffusion Volume plugin.</p>
<p>GE 1,5T, Slicer - 4.8.1</p>

---

## Post #4 by @ihnorton (2018-07-31 13:34 UTC)

<aside class="quote no-group" data-username="Egor" data-post="3" data-topic="3086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/6de8d8/48.png" class="avatar"> Egor:</div>
<blockquote>
<p>there is no DICOM Diffusion Volume plugin.</p>
<p>GE 1,5T, Slicer - 4.8.1</p>
</blockquote>
</aside>
<p>It is available in recent SlicerPreview (nightly) builds.</p>

---
