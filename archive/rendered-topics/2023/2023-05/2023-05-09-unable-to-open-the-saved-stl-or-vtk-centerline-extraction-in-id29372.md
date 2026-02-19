---
topic_id: 29372
title: "Unable To Open The Saved Stl Or Vtk Centerline Extraction In"
date: 2023-05-09
url: https://discourse.slicer.org/t/29372
---

# Unable to open the saved stl or vtk centerline extraction in other modelling software

**Topic ID**: 29372
**Date**: 2023-05-09
**URL**: https://discourse.slicer.org/t/unable-to-open-the-saved-stl-or-vtk-centerline-extraction-in-other-modelling-software/29372

---

## Post #1 by @Yvonne (2023-05-09 09:03 UTC)

<p>Hi</p>
<p>I’m trying to export the vessel center line and open file in Solidworks and Cura in order to 3D print the structure. However, all of the 3D modelling software showed that the file is corrupted.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d1f31197f36c4791e36543f94c8e0a452c05542.png" alt="image" data-base62-sha1="6raju6xCVRLcJWZfDpWOsOqNCMO" width="612" height="185"></p>
<p>Can anyone suggest a possible solution? Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-05-10 04:23 UTC)

<p>The error message indicates that you attempted to save a centerline model (a polyline) into STL format. STL file can only store triangles, so the generated file is empty. You can export the segmentation to a surface mesh and save that, or convert the segmentation to a volumetric mesh (using SegmentMesher extension) and load that into your CAD software.</p>
<p>Usually CAD software, such as Solidworks and Cura cannot deal with complex meshes coming from medical images. You may need to simplify the model to have less than 10k points (you can do that using Surface Toolbox module’s Uniform remesh option) before saving it.</p>

---

## Post #3 by @Yvonne (2023-05-10 22:52 UTC)

<p>Hi Andras,</p>
<p>Thank you a million times!</p>

---
