# Export ROI box to json file

**Topic ID**: 5210
**Date**: 2018-12-28
**URL**: https://discourse.slicer.org/t/export-roi-box-to-json-file/5210

---

## Post #1 by @akhila_perumalla (2018-12-28 05:42 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.0<br>
Expected behavior: Implementation of bounding box for Segmentation using 3D slicer<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-12-28 16:03 UTC)

<p>What would you like the bounding box to do?<br>
Would you like to fill a box shaped region with a segment?</p>

---

## Post #3 by @akhila_perumalla (2018-12-31 05:29 UTC)

<p>Thank you for the response.</p>
<p>Yes, I would like to segment using a box(cuboid). And, I would like to export the box information in either json or fav formats.</p>

---

## Post #4 by @lassoan (2018-12-31 16:08 UTC)

<p>You can place an annotation ROI (select ROI on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Annotations" rel="nofollow noopener">annotation toolbar</a> and click in the image at the center and corner of the intended box). Then you can save the annotation as a .csv file (menu: File / Save) or <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Write_annotation_ROI_to_JSON_file" rel="nofollow noopener">write directly to a json file using this code snippet</a>.</p>

---
