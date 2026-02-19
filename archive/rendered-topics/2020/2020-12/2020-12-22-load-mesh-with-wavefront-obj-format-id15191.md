---
topic_id: 15191
title: "Load Mesh With Wavefront Obj Format"
date: 2020-12-22
url: https://discourse.slicer.org/t/15191
---

# Load mesh with wavefront (obj) format

**Topic ID**: 15191
**Date**: 2020-12-22
**URL**: https://discourse.slicer.org/t/load-mesh-with-wavefront-obj-format/15191

---

## Post #1 by @Yixun_Liu (2020-12-22 15:00 UTC)

<p>Hi,<br>
I use 3DSlicer to load a mesh, which was created from a volume with suffix .mhd.<br>
The volume is loaded using ITK and the mesh is generated using vtk marchingcube by an in-house tool. The mesh is saved into wavefront format with suffix obj.</p>
<p>I have several questions:</p>
<ol>
<li>Is the mesh created in the LPS space no matter what AnatomicalOrientation is in the mhd file?</li>
<li>As I load the mesh into 3DSlicer, is it rendered in the RAS space?</li>
</ol>
<p>Thank a lot!</p>
<p>Yixun</p>

---

## Post #2 by @lassoan (2020-12-22 20:36 UTC)

<p>In recent Slicer versions, surface meshes are assumed to be in LPS coordinate system, unless you specify RAS coordinate system in the file header. See more information here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default</a></p>

---

## Post #3 by @Yixun_Liu (2020-12-23 01:28 UTC)

<p>Many thanks for your promptly reply.</p>
<p>For the mesh creation, I use ITK to load a .mhd file and then convert it to vtkImage and then use vtkMarchingcube to generate a mesh. Is the mesh created in the volume space determined by the offset and the transformMatrix (offset and transformMatrix are tags in .mhd file ) no matter what the AnatomicalOrientation is?</p>

---

## Post #4 by @lassoan (2020-12-23 02:12 UTC)

<p>ITK follows current guidance on interpretation of mha files in that it ignores the AnatomicalOrientation field and assumes the image is defined in LPS coordinate system. Since   current Slicer versions expect meshes to be in LPS coordinate system, there should be no need for conversion.</p>
<p>Note that you don’t need to use marching cubes in an external software. You can load the mha file directly into Slicer as a segmentation node (select “Segmentation” in Add data dialog in the description column). Mesh representation of the segmentation will be created automatically when needed, using methods that are better than simple marching cubes (flying edges filter followed by Taubin smoothing) - when you right-click on the segmentation and choose export to model, or click show 3D in Segment Editor.</p>
<p>What is the end goal of your project? What are the steps in your workflow that have not been completed yet?</p>

---

## Post #5 by @Yixun_Liu (2020-12-24 02:52 UTC)

<p>Thanks Andras.<br>
We are developing a specific surgery planning system with segmentation and mesh generation. Slicer has powerful edit functionality and we often use it to edit our segmentation results and visualize the mesh.<br>
But sometimes the mesh and the segmentation volume do not align well in the 3D rendering window. Now I understand it is because the mesh might not be created in the LPS space.</p>
<p>Thanks a lot for your help!</p>

---

## Post #6 by @lassoan (2020-12-24 03:58 UTC)

<p>Thanks for the information. In case you don’t know, Slicer is used as a basis of several surgical planning and real-time guidance systems (including commercial ones, with regulatory approval), with completely custom GUI layer (you would not recognize that the engine of the application is Slicer). Check out these links for some more details:</p>
<ul>
<li><a href="http://www.slicerigt.org">www.slicerigt.org</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-use">https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-use</a></li>
<li><a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></li>
</ul>

---

## Post #7 by @Yixun_Liu (2020-12-25 01:13 UTC)

<p>Yes, I know and also use them too.<br>
Thank you so much for your help!</p>

---
