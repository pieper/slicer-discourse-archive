# Obtain Centerline model from centerline curves

**Topic ID**: 35619
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/obtain-centerline-model-from-centerline-curves/35619

---

## Post #1 by @bserrano (2024-04-19 13:00 UTC)

<p>Hi all,</p>
<p>I have some markups curves. The points of the curves are created with an external software. I want to use some modules in 3D Slicer but they require a “Centerline model” instead of a centerline curve. How can I generate this model from my curves?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4663fcb9d3eb47f321fa5ca1ab3e358b7f9c5e45.png" alt="imagen" data-base62-sha1="a2HDXCoEQesFeD2M51hicosX1hX" width="414" height="325"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/749f44c873304905ddbe6fc0a2d430d2071d0a18.png" alt="imagen" data-base62-sha1="gDGCkbaA7RD8aFPnkKW709Et9kA" width="457" height="51"></p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @SANTIAGO_PENDON_MING (2024-04-23 12:19 UTC)

<p>Hi, me and  my team are also very interested on this feature. There any way to do it with a Python Script?</p>

---

## Post #3 by @chir.set (2024-04-23 13:18 UTC)

<p><code>model = slicer.modules.models.logic().AddModel(myCurve.GetCurveWorld())</code></p>
<p>The new model contains the ‘Radius’ array among others, and lacks 2 other arrays.</p>
<p>How is this useful?</p>
<p>Please note that the modules in SlicerVMTK requiring a centerline model as input expect it to have been created with the ‘Extract centerline’ module.</p>

---
