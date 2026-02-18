# Error when exporting 3d mesh model to VTU file, and invisible VTK file in Paraview

**Topic ID**: 25150
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/error-when-exporting-3d-mesh-model-to-vtu-file-and-invisible-vtk-file-in-paraview/25150

---

## Post #1 by @torquil (2022-09-08 07:29 UTC)

<p>I have created a model by using Segment Mesher with tetgen to create a 3d tetrahedral mesh. However, when I go to the Data module and try to export the model to file, I get the following error when selecting the VTU format:</p>
<ul>
<li>Error: No writer found to write file /path/to/folder/Model.vtu of type ModelFile.</li>
<li>Error: Error encountered while exporting Model.</li>
</ul>
<p>Do I need to install something for this to work?</p>
<p>When exporting to the VKT file format instead, I do get an output file which seems to contain the mesh, however, in Paraview this mesh is invisible for some reason, no matter which Display Representation or Colouring I use. I was able to see it using a pyvista visualization within Python.</p>
<p>Update: This was when using the mouse right click menu in the Data module for the export. However, if I go to the “save data” button, and select the Model.vtk that is on the list of data to save, I can save to VTU by selecting VTU in the drop-down menu there. Also, if I select VKT there, the resulting file IS visible in Paraview…</p>
<p>So for some reason there is a big difference between using the “Export to file” dropdown menu for the Model in the Data module, and to do it within the “Save data” function of Slicer.</p>
<p>This is with 3D Slicer 5.1.0-2022-09-01 on Debian Linux.</p>

---

## Post #2 by @ebrahim (2022-09-08 14:56 UTC)

<p>The difference between export and save should be that export does not modify the nodes in the scene (adjusting storage nodes or marking nodes as already saved since the last changes).</p>
<p>When I create a model node in Slicer I don’t see the VTU option, not in the save dialog and not in the export dialog. Maybe I am not checking the correct node type.</p>

---

## Post #3 by @Xiaojie_Guo (2024-05-22 10:00 UTC)

<p>I found that, after saving the mesh file, the mesh format was changed to vtkPolyData, not vtkUnstructuredGrid.</p>

---

## Post #4 by @lassoan (2024-05-22 14:49 UTC)

<p>A model node can store surface mesh (vtkPolyData) or volumetric mesh (vtkUnstructuredGrid). Surface mesh files can be stored in many formats (vtk, vtp, ply, stl, obj, …), while volumetric meshes can only be stored in a few (vtk, vtu).</p>
<p><em>Saving</em> of volumetric meshes works well, but indeed <em>exporting</em> is currently broken due to small bug. I’ve <a href="https://github.com/Slicer/Slicer/pull/7760">submitted a fix</a>, which should be available in the Slicer Preview Release from tomorrow. Until you get the fix, you can use “Save data” instead of export.</p>

---

## Post #5 by @Xiaojie_Guo (2024-05-24 09:08 UTC)

<p>Yeah, great. What I said saving the mesh means exporting the model node.</p>

---

## Post #6 by @lassoan (2024-05-24 10:59 UTC)

<p>Saving (menu: File / Save data) and exporting (Data module: right-click / Export to file) are two different features. Saving has been working well. Export was failing for volumetric meshes but it is fixed now in the Slicer Preview Release.</p>

---

## Post #7 by @Xiaojie_Guo (2024-05-27 02:13 UTC)

<p>Got it. Thanks very much.</p>

---
