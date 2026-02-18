# Blank lines after ACPC transform

**Topic ID**: 19040
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/blank-lines-after-acpc-transform/19040

---

## Post #1 by @YingHsu (2021-08-03 13:46 UTC)

<p>Dear experts:<br>
When I use segment editor, I often encountered some blank lines when I tried to paint on sagittal view after doing ACPC transform. And there are patches appear in adjacent slices.</p>
<p>Can you give me some advice. Thank you in advance.</p>

---

## Post #2 by @lassoan (2021-08-03 13:49 UTC)

<p>This is the expected behavior when the orientation of the slice view differs from the orientation of the segmentation’s labelmap representation. See more information <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments">here</a>.</p>

---
