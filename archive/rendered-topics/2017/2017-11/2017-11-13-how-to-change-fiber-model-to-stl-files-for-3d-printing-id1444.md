# How to change fiber model to STL files for 3D printing

**Topic ID**: 1444
**Date**: 2017-11-13
**URL**: https://discourse.slicer.org/t/how-to-change-fiber-model-to-stl-files-for-3d-printing/1444

---

## Post #1 by @Unique157 (2017-11-13 14:30 UTC)

<p>how to change fiber model to STL files for 3D printing??<br>
just like the question, i had convert the model to stl successfully before, but i cant finish it now with the software of the same version or latest version.<br>
i expect ur help ,my friends!</p>

---

## Post #2 by @ihnorton (2017-11-13 15:07 UTC)

<p>Here is example Python code to export fiber bundles to PLY. If you need STL you could change <code>vtkPLYWriter</code> to <code>vtkSTLWriter</code>, then need to comment the following two lines because STL doesn’t support colors (as far as I understand).</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color</a></p>

---

## Post #3 by @ihnorton (2017-11-13 15:07 UTC)

<p>See also:</p>
<aside class="quote" data-post="2" data-topic="299">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/about-using-the-code-of-exporting-a-model-with-colors-to-blender/299/2">About using the code of exporting a model with colors to Blender</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve fixed the obvious syntax errors (due to VTK library upgrades) in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color">fiber tract export snippet</a>. 
If you export generic models (not fiber tracts) then you can either <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_entire_scene_as_VRML">export the whole scene as VRML</a> or <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_to_Blender.2C_including_color_by_scalar">export a colored model to ply</a>.
  </blockquote>
</aside>


---
