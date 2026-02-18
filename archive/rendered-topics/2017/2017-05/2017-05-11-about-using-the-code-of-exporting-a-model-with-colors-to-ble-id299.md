# About using the code of exporting a model with colors to Blender

**Topic ID**: 299
**Date**: 2017-05-11
**URL**: https://discourse.slicer.org/t/about-using-the-code-of-exporting-a-model-with-colors-to-blender/299

---

## Post #1 by @Mohamed (2017-05-11 12:37 UTC)

<p>Hello,<br>
I was trying to use the code of exporting a model with colors to Blender in the repository here: <a href="https://www.slicer.org/wiki/Documentation/4.5/ScriptRepository" rel="nofollow noopener">Export a model to Blender, including color </a><br>
but it seems like the function of GetOutputPolyData has been modified in the new version of VTK. As it keeps giving me an error in the integrator.<br>
Anyone know a way to get its alternative?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2017-05-11 14:25 UTC)

<p>I’ve fixed the obvious syntax errors (due to VTK library upgrades) in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color">fiber tract export snippet</a>.</p>
<p>If you export generic models (not fiber tracts) then you can either <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_entire_scene_as_VRML">export the whole scene as VRML</a> or <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_to_Blender.2C_including_color_by_scalar">export a colored model to ply</a>.</p>

---
