# What are the necessary DICOM header fields for import into 3D Slicer?

**Topic ID**: 8637
**Date**: 2019-10-01
**URL**: https://discourse.slicer.org/t/what-are-the-necessary-dicom-header-fields-for-import-into-3d-slicer/8637

---

## Post #1 by @stevenagl12 (2019-10-01 16:22 UTC)

<p>I have output images that are numpy arrays. I am trying to convert them directly into DICOM images through the use of SimpleITK but I need to know what header fields are necessary to allow for them to be imported into Slicer for viewing. Also, is there a method to create SimpleITK images from numpy arrays and then write them to dicom through slicer itself?</p>

---

## Post #2 by @pieper (2019-10-01 16:38 UTC)

<p>Slicer should be pretty tolerant of missing dicom ags, but as a baseline you could consider the ones listed here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/CreateDICOMSeries" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/CreateDICOMSeries</a></p>
<p>Or, if you <a href="https://discourse.slicer.org/t/creating-volume-from-numpy/658/2">load the numpy data</a> you can create a volume node and then export it as DICOM via the Data module.</p>

---
