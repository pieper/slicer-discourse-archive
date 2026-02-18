# Radiomics won't work with a label volume from Segmentation Wizard

**Topic ID**: 4224
**Date**: 2018-09-29
**URL**: https://discourse.slicer.org/t/radiomics-wont-work-with-a-label-volume-from-segmentation-wizard/4224

---

## Post #1 by @Ella_Jones (2018-09-29 02:03 UTC)

<p>Operating system: MacOS 10.13.3<br>
Slicer version:4.9.0-2018-09-08 r27398<br>
Expected behavior: Radiomics will use the resampled volume as the Input image volume and the roi-threshold as input regions.  Then calculate the features and output it in the table<br>
Actual behavior: nothing happened and the table was blank.</p>

---

## Post #2 by @lassoan (2018-09-29 04:17 UTC)

<p>I would recommend to use <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment Editor module</a> for segmentation. If you have any problems with this module then let us know.</p>

---

## Post #3 by @JoostJM (2018-10-15 09:07 UTC)

<p>If the input table is empty, this is likely due to an error (e.g. a failing check).<br>
Is there anything visible in the python interaction window? This is where the module shows the warnings.<br>
Alternatively, it may show up in the slicer log (obtainable via the “report a bug”).</p>

---
