# DICOM image info

**Topic ID**: 15464
**Date**: 2021-01-12
**URL**: https://discourse.slicer.org/t/dicom-image-info/15464

---

## Post #1 by @Ash_Alarfaj (2021-01-12 00:22 UTC)

<p>Operating system: MAC<br>
Slicer version: 4.11 OR 4.10.2<br>
Expected behavior: show image field of view and reconstructed matrix size.<br>
Actual behavior: can not find these info in DICOM or image volume</p>

---

## Post #2 by @pieper (2021-01-12 00:53 UTC)

<p>You can turn on the ruler in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">view controller</a> and see the image size in the Volumes module, but no, there’s no option to overlay that information.</p>

---

## Post #3 by @lassoan (2021-01-12 03:10 UTC)

<p>You can write any text into a corner of any view as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Display_text_in_a_3D_view_or_slice_view">this example</a>. With 5-10 more lines of Python code you can retrieve any information about the current volume and display it in a view corner.</p>
<p>What is your use case? How would you use this information? We have been planning to improve view annotations (DataProbe module) for a long time (see <a href="https://github.com/Slicer/Slicer/issues/4854" class="inline-onebox">Improve slice view annotations · Issue #4854 · Slicer/Slicer · GitHub</a>). If you can describe your requirements here then we’ll add a reference to this discussion and when we will take those into account when implementing the improvements.</p>

---
