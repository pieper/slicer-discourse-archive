# ITK image to mesh to vtk polydata

**Topic ID**: 12717
**Date**: 2020-07-24
**URL**: https://discourse.slicer.org/t/itk-image-to-mesh-to-vtk-polydata/12717

---

## Post #1 by @Zhiy (2020-07-24 03:40 UTC)

<p>Dear all,</p>
<p>Recently I am trying to extract the surface geometry from a binary ITK image (resulting from ostu_threshold_image_filter) into ITK mesh. Then convert this ITK MESH to a vtk polydata.</p>
<p>The filters I used include BinaryThresholdImageFilter, BinaryMask3DMeshSource and MeshToPolyDataFilter. I program in python. The result turns out to be of type itk.itkPolyDataPython.itkPolyDataF instead of expected vtkPolyData.</p>
<p>Moreover, I am not sure the result of BinaryMask3DMeshSource output a triangle mesh. Could anyone kindly provide some advise?</p>
<p>Appreciate.</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2020-07-24 06:03 UTC)

<p>ITK’s mesh infrastructure is still quite far behind VTK (similarly how VTK’s image processing capabilities are much more limited compared to ITK), so I would recommend to use VTK for mesh processing and ITK for image processing. I don’t think there is a functional ITK-VTK glue package available for Python, so if you would want to pass data between ITK and VTK then you may need to write/read files or implement serialization to/from numpy arrays (but check with Kitware folks before you invest too much time into implementing numpy serialization, as maybe there is already some ongoing effort that you can join).</p>
<p>Anyway, most likely you won’t need to implement low-level features from scratch. All the features that you described (and much more sophisticated segmentation methods) are already all conveniently available in segmentations infrastructure and in segment editor effects. You can access these features via GUI (<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">Segmentations and Segment Editor module</a>) or from Python scripting (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a> for examples).</p>

---

## Post #3 by @Zhiy (2020-07-24 14:59 UTC)

<p>Thanks for your reply.</p>
<p>I work around by writing/reading files between ITK/VTK meshes.</p>

---
