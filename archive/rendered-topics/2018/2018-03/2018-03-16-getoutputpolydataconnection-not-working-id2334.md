---
topic_id: 2334
title: "Getoutputpolydataconnection Not Working"
date: 2018-03-16
url: https://discourse.slicer.org/t/2334
---

# GetOutputPolyDataConnection() not working

**Topic ID**: 2334
**Date**: 2018-03-16
**URL**: https://discourse.slicer.org/t/getoutputpolydataconnection-not-working/2334

---

## Post #1 by @anandmulay3 (2018-03-16 12:16 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.8.1<br>
Expected behavior:I’m tryinng to write .ply file using python interactor but i think because of this error(GetOutputPolyDataConnection() ) it is not generating the output though plywriter.write() returns 1<br>
Actual behavior: showing error this attribute is not part of some vtk class</p>
<p>can you please give me a code which is use for exporting obj also…</p>
<p>thanks…</p>

---

## Post #2 by @ihnorton (2018-03-16 13:08 UTC)

<p>Please see below (and in future, please copy/link the code you are running and output, to give people here enough context to explain errors).</p>
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

## Post #3 by @anandmulay3 (2018-03-16 13:36 UTC)

<p>AttributeError: ‘vtkCommonCorePython.vtkMRMLScalarVolumeDisplayNode’ object has no attribute ‘GetOutputPolyDataConnection’</p>
<p>Sorry , but this is the actual error , and i’m using same code that you have referred , still no luck…</p>

---

## Post #4 by @lassoan (2018-03-16 13:42 UTC)

<p>Volume nodes don’t store polydata (surface mesh), but an image volume. You can create mesh from volume by segmenting it, for example by using Segment Editor module.</p>

---

## Post #5 by @anandmulay3 (2018-03-16 13:48 UTC)

<p>Ohh, okay. So i have to get segment data first…<br>
Thanks for the support…<br>
is it possible to export obj rather than .ply file??</p>

---

## Post #6 by @lassoan (2018-03-16 14:11 UTC)

<p>Yes, you can save geometry of the model as .obj file.</p>

---
