# CoodinateSystem mismatch when applying transform to mesh

**Topic ID**: 29117
**Date**: 2023-04-25
**URL**: https://discourse.slicer.org/t/coodinatesystem-mismatch-when-applying-transform-to-mesh/29117

---

## Post #1 by @suranga (2023-04-25 14:09 UTC)

<p>Hi,</p>
<p>I have a trasform file and I want to apply this transform to a volumetric mesh which is in vtk unstructured grid format.</p>
<p>I first load the mesh in RAS format and then apply the transformation and save to the disk using following script.</p>
<pre><code class="lang-auto">ref_mesh_path = './MCR.vtk'
transform_file_path = "./LinearTransform_scan_1.h5"

[success, transform] = slicer.util.loadTransform(transform_file_path, returnNode=True)

ref_mesh = slicer.modules.models.logic().AddModel(ref_mesh_path, slicer.vtkMRMLStorageNode.CoordinateSystemRAS)
ref_mesh.SetAndObserveTransformNodeID(transform.GetID())
slicer.vtkSlicerTransformLogic().hardenTransform(ref_mesh)

slicer.util.saveNode(ref_mesh, './MCR_temp_scan_1.vtk')
</code></pre>
<p>However, when I compare the saved file with the original mesh coodiantes, I realised that the sign of the first two coordinates are inverted.</p>
<p>How can I save the transformed mesh without having this problem?</p>
<p>After applying the transformation, I believe all I need to do is switch to LPS and save the file again. How do I go about doing this?</p>
<p>I’d appreciate any code or assistance.</p>

---
