# How to import/export segmentation as nrrd file?

**Topic ID**: 3509
**Date**: 2018-07-17
**URL**: https://discourse.slicer.org/t/how-to-import-export-segmentation-as-nrrd-file/3509

---

## Post #1 by @margherita (2018-07-17 11:40 UTC)

<p>how do you export /import .nrrd files ?</p>

---

## Post #2 by @cpinter (2018-07-17 13:25 UTC)

<p>Import: drag&amp;drop nrrd on Slicer, and in the popup window, choose Segmentation in the Description column.</p>
<p>Export: if you want to export the segmentation as a single nrrd file (all segments in the same file, which means overlapping segments are not permitted), then you can export the segmentation into a labelmap in the Segmentations module or in the Data module by right-clicking the segmentation, then click the Save button and save the labelmap as an nrrd.</p>
<p>As a side note, next time please create a new topic instead of commenting a new question to an only tangentially related topic. Thanks!</p>

---

## Post #3 by @Mikolaj (2020-02-06 15:46 UTC)

<p>For me, the import doesnt work. Just black screens and nothing happens.</p>

---

## Post #4 by @cpinter (2020-02-08 08:38 UTC)

<p>Please start a new topic with a much more detailed description. Tell us exactly what you tried to do step by step and how, using what files, coming from where, etc., and then what happened instead of what you expected.</p>

---

## Post #5 by @lassoan (2020-02-08 17:42 UTC)

<p>Loading of plain nrrd files as segmentation is implemented in latest Slicer Preview release (Slicer-4.11.x, downloaded February 2020 or later).</p>

---
