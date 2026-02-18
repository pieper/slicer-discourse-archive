# .nrrd files segments to label map volume

**Topic ID**: 19841
**Date**: 2021-09-24
**URL**: https://discourse.slicer.org/t/nrrd-files-segments-to-label-map-volume/19841

---

## Post #1 by @alyssan (2021-09-24 14:19 UTC)

<p>Hello,<br>
I have four segmentations I would like to create one labelmap volume. The segmentations are .nrrd files. How do i do this?</p>

---

## Post #2 by @alyssan (2021-09-24 14:20 UTC)

<p>The four segmentation files are on my desktop to be loaded into 3d slicer.</p>

---

## Post #3 by @muratmaga (2021-09-24 21:08 UTC)

<p>If all these segmentation derived from the same volume, this should work:</p>
<ol>
<li>Load all your segmentation nrrd files as “segmentations” into Slicer</li>
<li>Switch to Segmentations module and copy and paste individual segments from different into one of the segmentations.</li>
<li>Use Import/Export tab of the segmentations module to export the resultant segmentation as label map.</li>
</ol>

---
