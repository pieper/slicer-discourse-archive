# Determine points in 3d pictures

**Topic ID**: 358
**Date**: 2017-05-21
**URL**: https://discourse.slicer.org/t/determine-points-in-3d-pictures/358

---

## Post #1 by @Joelle (2017-05-21 19:29 UTC)

<p>Hi<br>
I’m new to 3d slicer and for my dissertation I’m analyzing images of patients. I will receive 3d pictures of faces and would like to calculate the symmetry. The images are done with a 3d camera and therefore don’t are x-rays. To calculate the symmetry, I would like to split the face in the middle and insert points or define areas on both sides. Based on the position of the points/areas the symmetry could be calculated.</p>
<p>Is there a easy way to split a 3d image in half and insert points or areas and determine the position in the image?</p>

---

## Post #2 by @lassoan (2017-05-21 19:46 UTC)

<p>For simple cutting of surfaces you can use the EasyClip extension.</p>
<p>However, for automatic registration of the two half faces it’s better to not cut the surface mesh into two. You can perform surface registration using Model registration module in SlicerIGT extension and compute surface different metrics using Model to model distance extension.</p>
<p>For free-form editing of surfaces we usually convert them to closed surfaces (by linear extrusion in normal direction), import it into Segmentations module, and edit in Segment editor. There is no module for creating the closed surface, but you can run VTK filters directly from the Python console.</p>

---
