---
topic_id: 29354
title: "Convert Dicom Rt Structure Set Rs To Nifti"
date: 2023-05-08
url: https://discourse.slicer.org/t/29354
---

# Convert DICOM RT structure set (RS) to NIFTI

**Topic ID**: 29354
**Date**: 2023-05-08
**URL**: https://discourse.slicer.org/t/convert-dicom-rt-structure-set-rs-to-nifti/29354

---

## Post #1 by @Luana_CONTE (2023-05-08 14:04 UTC)

<p>Operating system: Windows 11 Pro<br>
Slicer version: 5.2.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello everybody,<br>
I have got some DICOM series with their RS structures and I need to convert them in NIFTI format in a batch. Is there any solution?</p>

---

## Post #2 by @lassoan (2023-05-10 04:33 UTC)

<p>After you install SlicerRT extension, you <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene">can load RT structure sets from DICOM</a> and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">export the segmentation to NIFTI files</a>.</p>
<p>In general, I would recommend not to use NIFTI files, as they have many issues and limitations. For example, they cannot store overlapping labels; they just store label values (but not what each label value means - segment name, standard terminology codes, color, etc.), cannot store segmentations acquired with tilted gantry, etc. Segmentation NRRD files (.seg.nrrd) do not have these limitations.</p>

---

## Post #3 by @Luana_CONTE (2023-05-11 07:39 UTC)

<p>Many thanks for your reply.</p>
<p>I have followed the procedure you suggested. When I have tried to save the RT struct in NIFTI, there was not the extensions. The only possible extensions in the drop-menu were nnrd and nhdr only.<br>
In addition, after converting in seg.nrrd format, I checked the file in an external envoronment (I have used matlab) but I could not see any value. It seems that there wasn’t any conversion at all.<br>
Can you please help me?</p>
<p>I was also wondering if there is an option to convert in NIFTI the images (not only RT struct), as well?</p>
<p>Many thanks!!!</p>

---

## Post #4 by @lassoan (2023-05-11 22:44 UTC)

<aside class="quote no-group" data-username="Luana_CONTE" data-post="3" data-topic="29354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luana_conte/48/65924_2.png" class="avatar"> Luana_CONTE:</div>
<blockquote>
<p>The only possible extensions in the drop-menu were nnrd and nhdr only</p>
</blockquote>
</aside>
<p>Make sure you use the export function in Segmentations module and that you use the current Slicer version (5.2.2).</p>

---
