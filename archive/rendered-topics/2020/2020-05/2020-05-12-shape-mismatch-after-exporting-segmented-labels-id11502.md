# Shape mismatch after exporting segmented labels

**Topic ID**: 11502
**Date**: 2020-05-12
**URL**: https://discourse.slicer.org/t/shape-mismatch-after-exporting-segmented-labels/11502

---

## Post #1 by @Flash (2020-05-12 11:34 UTC)

<p>Hello,</p>
<p>I have generated mask labels for brain tumor with nvidia clara…I am overlaying these mask labels on the original brain tumor image.I have edited the generated the mask lables with segment editor and later tried to export with data-&gt;export visible segments to binary label maps and save it as a nifti file.</p>
<p>However,the newly exported image has a different shape<br>
For eg: original mask file shape(224,224,155)<br>
modified mask file shape(91,95,76)</p>
<p>I want to retain the shape of the modified file just like the original mask file(224,224,155)</p>
<p>If anyone could guide me as to how to go about this…</p>
<p>Thanks</p>

---

## Post #2 by @Sunderlandkyl (2020-05-12 15:31 UTC)

<p>Hi, what version of Slicer are you using?</p>

---

## Post #3 by @lassoan (2020-05-12 19:15 UTC)

<p>Slicer version is important because in Slicer-4.10 you had to export to labelmap with a chosen reference volume before saving, while in recent Slicer-4.11 versions, labelmaps are saved by default with the master volume’s geometry.</p>

---

## Post #4 by @Flash (2020-05-14 04:07 UTC)

<p>Hello,</p>
<p>I am using Slicer version 4.11.0-2020-03-01!</p>

---

## Post #5 by @Sunderlandkyl (2020-05-15 14:37 UTC)

<p>I haven’t been able to reproduce this. Can you send me an example scene where this occurs?</p>

---

## Post #6 by @Flash (2020-05-19 10:16 UTC)

<p>Sorry for the late reply…</p>
<p>The issue has been resolved…Earlier I had set the reference volume to None…<br>
Now when i set the reference volume to the referred image and then save the file with .nii extension…the original file’s shape is retained</p>

---
