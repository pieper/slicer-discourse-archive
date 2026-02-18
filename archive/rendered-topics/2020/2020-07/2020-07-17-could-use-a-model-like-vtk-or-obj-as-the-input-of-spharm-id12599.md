# Could use a model like *.vtk or *.obj as the input of SPHARM?

**Topic ID**: 12599
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/could-use-a-model-like-vtk-or-obj-as-the-input-of-spharm/12599

---

## Post #1 by @Yoda0612 (2020-07-17 14:28 UTC)

<p>I would like to obtain the spherical harmonic coefficients for a model.<br>
However, SPHARM ask me to input the binary image or vtk model with para model.<br>
I just have a model without para model.<br>
How could I obtain spherical harmonic coefficients by using SPHARM?</p>

---

## Post #2 by @styner (2020-07-17 17:16 UTC)

<p>You will need to first generate label voxel representation from your surface mesh using the “Model to Label Map” or “Mesh To Label Map” module (they operate slightly differently, and I have found that if one does not work well, then the other does, but neither works for all settings).</p>
<p>Martin</p>

---

## Post #3 by @Yoda0612 (2020-07-20 07:51 UTC)

<p>Dear Martin,</p>
<p>Thanks.</p>
<p>I used “Mesh To Label Map” and used the output volume as the input of GenParaMesh, I received errors.</p>
<p>I checked the output volume, nothing inside.<br>
Regarding “Model to Label Map”, it ask me to specify another volume as the input.<br>
I don’t know how to specify this volume.</p>
<p>Regards<br>
Cheng</p>
<p>Martin Styner via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; 於 2020年7月18日 週六 上午2:26寫道：</p>

---

## Post #4 by @styner (2020-07-27 21:15 UTC)

<p>For “Model to Label Map”, you need to first create (e.g. using Slicer) an input volume that fits with your surface.<br>
You may actually be able to generate that input volume via the “Mesh To Label Map” module. Load the volume that was generated (and is empty, according to your email) and see whether the surface is inside the volume (using Slicer and select “show slice intersections” in the “models” module). Also, did you make sure to use appropriate settings for “Model to Label Map" (i.e. sufficiently fine spacing)?</p>
<p>Martin</p>

---
