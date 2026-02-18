# Dicom series folder read and use for creating a node

**Topic ID**: 2563
**Date**: 2018-04-11
**URL**: https://discourse.slicer.org/t/dicom-series-folder-read-and-use-for-creating-a-node/2563

---

## Post #1 by @anandmulay3 (2018-04-11 07:41 UTC)

<p>In python scriptable module  -<br>
How can use dicom series to import and use it a segmentation node or volume node.<br>
Or every time we need to import .nrrd file to use it as a node.</p>

---

## Post #2 by @lassoan (2018-04-11 13:27 UTC)

<p>See this and similar posts in the forum: <a href="https://discourse.slicer.org/t/how-to-convert-dicom-files-to-nrrd/540/11">How to convert dicom files to nrrd</a></p>

---

## Post #3 by @anandmulay3 (2018-04-11 13:42 UTC)

<p>Yeah, i mean i’m doing same thing, that getting dicom series and saving it to nrrd and use that node…<br>
but my question is can i load dicom series and use that is as my volume node or segmentation node.??</p>

---

## Post #4 by @lassoan (2018-04-12 19:45 UTC)

<p>Most DICOM images are loaded as volume nodes; RTSTRUCT and DICOM segmentation objects are loaded as segmentation nodes. You can just use load them and use them.</p>

---
