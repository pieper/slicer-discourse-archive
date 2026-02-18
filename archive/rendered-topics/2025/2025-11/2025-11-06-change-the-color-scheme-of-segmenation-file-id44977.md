# Change the color scheme of segmenation file

**Topic ID**: 44977
**Date**: 2025-11-06
**URL**: https://discourse.slicer.org/t/change-the-color-scheme-of-segmenation-file/44977

---

## Post #1 by @Ruolin_Li (2025-11-06 13:00 UTC)

<p>Hello!</p>
<p>I’m trying to change the color scheme for the segmentation file I loaded in the 3D Slicer. My segmentation has 126 labels, and they’re currently displayed under the default color GenericAnatomyColors, which is not ideal for visualization. I wanted to change the color scheme to other built-in colors (e.g., Labels, Random), but couldn’t do it for all the labels, so I had to change the colors one by one. May I ask if there’re any ways that I can change the color scheme for all my labels together? Thank you very much!</p>

---

## Post #2 by @lassoan (2025-11-06 14:03 UTC)

<p>Creating a color table that specifies segment name, color, and standard terminology for each label value is an essential task for segmentation and recent Slicer versions provide excellent support for this. I would recommend to create a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-csv-file-format-csv">color table .csv file</a> either in Slicer GUI or in Excel and then use that when you load or create a segmentation.</p>
<p>See more details and step-by-step instructions in the <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/colors-and-terms/README.md">Segment Colors and Terminology tutorial</a> (by SlicerMorph).</p>

---
