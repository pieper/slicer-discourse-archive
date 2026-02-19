---
topic_id: 408
title: "Convert Triangle Strips To Polygons"
date: 2017-05-31
url: https://discourse.slicer.org/t/408
---

# Convert TRIANGLE_STRIPS to POLYGONS

**Topic ID**: 408
**Date**: 2017-05-31
**URL**: https://discourse.slicer.org/t/convert-triangle-strips-to-polygons/408

---

## Post #1 by @pieper (2017-05-31 18:46 UTC)

<p>From the mailing list:</p>
<p>Hi, I am just one beginner of 3D slicer and try to generate VTK file from MRI<br>
image to import into mapping system. However, 3D slicer generated VTK file<br>
with TRIANGLE_STRIPS and I need POLYGONS format to upload the information.<br>
Can someone give me any suggestion?</p>
<p>Best Regards,</p>
<p>Ting-Yung Chang</p>

---

## Post #2 by @pieper (2017-05-31 18:46 UTC)

<p>Hi -</p>
<p>You can use a vtkTriangleFilter [1], like what is done here [2].</p>
<p>[1] <a href="http://www.vtk.org/doc/nightly/html/classvtkTriangleFilter.html">http://www.vtk.org/doc/nightly/html/classvtkTriangleFilter.html</a></p>
<p>[2] <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_to_Blender.2C_including_color_by_scalar">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_to_Blender.2C_including_color_by_scalar</a></p>

---
