# Exporting DICOM with Segmentation Mask applied

**Topic ID**: 8600
**Date**: 2019-09-27
**URL**: https://discourse.slicer.org/t/exporting-dicom-with-segmentation-mask-applied/8600

---

## Post #1 by @Michael_Medvedskiy (2019-09-27 22:20 UTC)

<p>Hello. I was planning on segmenting brain from the rest of the head (given the head as a DICOM archive with 320 images in it). So I segmented it fairly proper with Threshold and Grow From seeds, now I have a 3d brain (both as selection and a form), and what I’d like to do is simply save only those pixels (of 3D space) of DICOM array (that of 320 images), which are present in the segment. Can I do that?</p>

---

## Post #2 by @Amine (2019-09-27 23:06 UTC)

<p>Hi, yes you can, first get SegmentEditorExtraEffects module then go to segment editor&gt; Mask Volume, select your segment, operation= Fill outside, fill value= -1000 (ideally the lowest intensity on your volume) and hit apply, then export the resulting volume as in <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM" rel="nofollow noopener">here</a> .</p>

---
