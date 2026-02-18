# Modify saved annotation

**Topic ID**: 2102
**Date**: 2018-02-16
**URL**: https://discourse.slicer.org/t/modify-saved-annotation/2102

---

## Post #1 by @a.mortazi (2018-02-16 22:25 UTC)

<p>Hello,<br>
I have done some annotation on 3D images and I saved them as nrrd files. Now I want to modify annotations in some slices. But when I opened the annotation file I can not modify it (i.e remove annotation from one slice and do new annotation).<br>
I am using slicer 4.6 in Ubnutu 16.<br>
Any help is appreciated.</p>

---

## Post #2 by @lassoan (2018-02-17 03:19 UTC)

<p>What do you mean by annotation? Ruler, ROI, and markup fiducials? You cannot save those as nrrd files.</p>
<p>If by annotation you mean segmentation, then use Segment editor module to create and edit segmentation.</p>
<p>Important: You are using a Slicer version that is more than a year old!! Upgrade to the latest stable (Slicer 4.8.1). Segmentation capabilities hugely improved since 4.6.</p>

---

## Post #3 by @a.mortazi (2018-02-18 02:32 UTC)

<p>Thanks,<br>
Yes I meant segmentation and it worked as you mentioned.<br>
But I have already done some segmentation with Editor tool and when I am trying to load them(nrrd files) as segmentation, the program stuck and it couldn’t load those files as segmentation. (but it can load them as volume).<br>
Anyways, thanks for response.</p>
<p>Ali</p>

---

## Post #4 by @timeanddoctor (2018-02-18 03:36 UTC)

<p>Maybe you can modify it in Editor module not the segment.</p>

---

## Post #5 by @lassoan (2018-02-18 05:08 UTC)

<p>Load old labelmap as volumes and then import them into a segmentation node using Segmentations module (Import/Export section).</p>

---
