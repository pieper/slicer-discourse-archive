# Wrap Solidify only for vtk models

**Topic ID**: 19030
**Date**: 2021-08-02
**URL**: https://discourse.slicer.org/t/wrap-solidify-only-for-vtk-models/19030

---

## Post #1 by @siaeleni (2021-08-02 16:21 UTC)

<p>Hello,<br>
I want to use the functionality from Wrap Solidify to a vtk model, without having any DICOM file,<br>
Is it possible to do that, if yes can you give me a hint?</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2021-08-02 16:59 UTC)

<p>If you import the vtk model into Slicer, right click on it in Data module and convert to a segmentation. After that you should be able to use all Segment Editor effects (including Wat Solidify) on it. You will have to export it as a model after you are done editing.</p>

---

## Post #3 by @lassoan (2021-08-03 12:14 UTC)

<p>If a surface representation exists in the segmentation (e.g., because you imported the segmentation from a model node, or loaded a surface mesh file as segmentation) then <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/a9512a05f4203f4ae75211a9efde2bcab8bb549e/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L404">Wrap Solidify effect takes that surface from the segmentation node</a>, so what <a class="mention" href="/u/muratmaga">@muratmaga</a> described should work well. Therefore, the Wrap Solidify effect should work as is.</p>
<p>For reference, this topic seems to be a continuation of this topic: <a href="https://discourse.slicer.org/t/converting-open-surface-model-into-segmentation/19034" class="inline-onebox">Converting open surface model into segmentation</a></p>

---
