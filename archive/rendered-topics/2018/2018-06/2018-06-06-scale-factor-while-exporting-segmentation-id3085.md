# Scale factor while exporting segmentation

**Topic ID**: 3085
**Date**: 2018-06-06
**URL**: https://discourse.slicer.org/t/scale-factor-while-exporting-segmentation/3085

---

## Post #1 by @anandmulay3 (2018-06-06 06:48 UTC)

<p>can we set the scale factor of the 3D model while exporting segmentation.or do we have the scaling information in export segmentation method?</p>
<p>Thanks.</p>

---

## Post #2 by @timeanddoctor (2018-06-06 11:43 UTC)

<p>I think it is simple by some other softwares which could open stl file, such as CURA, blender…</p>

---

## Post #3 by @anandmulay3 (2018-06-06 12:44 UTC)

<p>yeah, but i want it in my scriptable module. so if slicer itself write the .obj file in that scale it will be helpful</p>

---

## Post #4 by @lassoan (2018-06-06 21:42 UTC)

<p>Yes, it is sometimes useful to be able to apply scale on export (for example, some non-medical-imaging people use meters as units in their model files). I’ve added a size scale field to the file export options and in the segmentations module logic (in r27236), it’ll be available in tomorrow’s nightly build.</p>

---
