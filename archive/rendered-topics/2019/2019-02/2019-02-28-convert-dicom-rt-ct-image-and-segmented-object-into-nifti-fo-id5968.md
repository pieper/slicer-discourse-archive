---
topic_id: 5968
title: "Convert Dicom Rt Ct Image And Segmented Object Into Nifti Fo"
date: 2019-02-28
url: https://discourse.slicer.org/t/5968
---

# Convert DICOM-RT CT image and segmented object into NIFTI format

**Topic ID**: 5968
**Date**: 2019-02-28
**URL**: https://discourse.slicer.org/t/convert-dicom-rt-ct-image-and-segmented-object-into-nifti-format/5968

---

## Post #1 by @Moran_Artzi (2019-02-28 15:09 UTC)

<p>For the following RTRSTRUCT data<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9da2718308c561aeb3e2d387a5127853f5a0119.png" data-download-href="/uploads/short-url/qw7ILCfTpKU5JAom5q564cm6rsR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9da2718308c561aeb3e2d387a5127853f5a0119_2_690x445.png" alt="image" data-base62-sha1="qw7ILCfTpKU5JAom5q564cm6rsR" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9da2718308c561aeb3e2d387a5127853f5a0119_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9da2718308c561aeb3e2d387a5127853f5a0119_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9da2718308c561aeb3e2d387a5127853f5a0119.png 2x" data-dominant-color="6F6F7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1271×820 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The data is loading successfully on slicer bet I</p>
<p>I am trying unsuccessfully to convert to NIFTI file the:</p>
<ul>
<li>The segmented objects</li>
<li>The CT image at the space of the segmented object</li>
</ul>
<p>I’ve seen some correspondence on this subject, but still didn’t successes to save my data as a nifti files, tring do save my data<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82b24d12ba409f5408d6186973078ea680c5a55a.png" alt="image" data-base62-sha1="iEc4Vl1pcBeC1fbXly0z4f41JQS" width="444" height="221"></p>
<p>Using the module to Export/import under Segmentation, does not save the files<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3838e7d17112846507d4c9d8594986195e3ba20.png" alt="image" data-base62-sha1="yKdSOcie6UwaFNJ10Yxk1JWFeko" width="441" height="220"></p>
<p>I’d appreciate your help<br>
Thanks<br>
Moran</p>

---

## Post #2 by @cpinter (2019-02-28 15:27 UTC)

<p>What you’re doing is correct, but it’s only half of the job. When you export the labelmap from a segmentation, it is exported to another MRML node in the Slicer scene, a labelmap volume node. You still need to save that labelmap to disk. You can do it by clicking on the Save button in the upper left corner, deselecting everything except for “2: RTSTRUCT: 1-label”, and choose nii.gz (or the format you want) in the dropdown menu in the row of the node.</p>

---

## Post #3 by @cpinter (2019-02-28 15:29 UTC)

<p>Btw I can see some triangulation error in the body structure, see coronal view in your screenshot. That gap will be there in the nii file as well. You can fix it in Segment Editor if you want, or we can take a look at the dataset and try to fix it, but it can take a long time.</p>

---

## Post #4 by @Moran_Artzi (2019-02-28 18:33 UTC)

<p>Thanks a lot of your reply</p>
<p>doing the follows i don get 2: RTSTRUCT: 1-label file but the  <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40b68ac3a2f04f5907d1d70fc5788634fe75c6ef.png" alt="image" data-base62-sha1="9etEsKU543lXGfS6wlxUqvs2ERF" width="114" height="24">file</p>
<p>it can be saved as ANELYZE file but its the CT image not not the segmented objects</p>
<p>what am i missing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebd8ad98554a29d5b64cfc8add9631a219568548.png" data-download-href="/uploads/short-url/xEor2XZZmOjz5LPDlmEbHNGoDry.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebd8ad98554a29d5b64cfc8add9631a219568548_2_690x239.png" alt="image" data-base62-sha1="xEor2XZZmOjz5LPDlmEbHNGoDry" width="690" height="239" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebd8ad98554a29d5b64cfc8add9631a219568548_2_690x239.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebd8ad98554a29d5b64cfc8add9631a219568548.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebd8ad98554a29d5b64cfc8add9631a219568548.png 2x" data-dominant-color="E4E4E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">955×332 54.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>
<p>Moran</p>

---

## Post #5 by @cpinter (2019-02-28 20:42 UTC)

<p>It seems you didn’t do the export to labelmap node.</p>

---
