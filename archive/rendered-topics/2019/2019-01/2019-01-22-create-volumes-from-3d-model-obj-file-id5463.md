---
topic_id: 5463
title: "Create Volumes From 3D Model Obj File"
date: 2019-01-22
url: https://discourse.slicer.org/t/5463
---

# Create volumes from 3D model (*.obj file)

**Topic ID**: 5463
**Date**: 2019-01-22
**URL**: https://discourse.slicer.org/t/create-volumes-from-3d-model-obj-file/5463

---

## Post #1 by @selector24 (2019-01-22 14:12 UTC)

<p>Hello,<br>
i would like to ask you, how can i create and save volumes (DICOM data) from 3D model saved in *.obj file.<br>
Thank you</p>
<p>Selector</p>

---

## Post #2 by @Hamburgerfinger (2019-01-22 17:16 UTC)

<p>Hi,</p>
<p>There are several ways to do this; here’s one straightforward but not so efficient one…  (Assuming I understand what you want to do (create voxel volume from a polygonal surface))</p>
<ol>
<li>
<p>Install the Image Maker extension from the extensions manager, and create a volume by defining a resolution, and set the origin/spacing such that all the coordinates of your *.obj will be contained within it.</p>
</li>
<li>
<p>Import your *.obj into Slicer as a Model.</p>
</li>
<li>
<p>Create a segmentation using the “Segmentations” module</p>
</li>
<li>
<p>Navigate to the “Export/import models and labelmaps” drop-down in this module.  Select “import” and “models” and select the model that you imported earlier.</p>
</li>
<li>
<p>Go to the “Segment editor” module.  Select your segment.</p>
</li>
<li>
<p>Use the “Mask volume” function and fill inside your segment with some value.</p>
</li>
</ol>
<p>If your model consists of a bunch of components, separate it into individual components and repeat this.  If the components need to overlap, start with the outermost and work inward.</p>
<p>And then export your final volume as DICOM</p>

---

## Post #3 by @lassoan (2019-01-22 21:15 UTC)

<p>In most recent nightly builds you can do it even simpler:</p>
<ul>
<li>Drag-and-drop the .obj file to Slicer application (or use menu: File / Add data and select the .obj file)</li>
<li>In “Description” column select “Segmentation” and click OK</li>
<li>Go to “Segmentations” module and in “Export/import…” section click “Export” button (by default select “Export” and “Labelmap” are selected, which create a new labelmap node)</li>
</ul>

---
