---
topic_id: 23420
title: "Dynamic Modeler Add Model Glyph And Boolean Operations"
date: 2022-05-14
url: https://discourse.slicer.org/t/23420
---

# Dynamic modeler: Add model, Glyph and Boolean Operations

**Topic ID**: 23420
**Date**: 2022-05-14
**URL**: https://discourse.slicer.org/t/dynamic-modeler-add-model-glyph-and-boolean-operations/23420

---

## Post #1 by @mau_igna_06 (2022-05-14 00:27 UTC)

<p>Hi devs and users. I would be interesting in developing Dinamyc Modeler’s tools for:</p>
<ul>
<li>adding parametric models for all available vtkSourceFilters that give a 3d mesh.</li>
<li>also adding a glyph tool that according to markup points and optionally the normals of a model uses the Glyph filter of vtk for creating copies of the input model with the corresponding position and orientation</li>
</ul>
<p>This features would be helpful on surgicalGuides creation, considering making guideBases is already possible with the dynamic modeler.</p>
<p>Also I have a question:<br>
Looking at the vtkbool code that is used on the CombineModels module… there is an AtoB matrix that is hardcoded to the identity… what if I define it according to the input transforms and make the processing cost less for transformed inputs… may be we could also do a Dynamic Modeler Boolean operations tool that is fast and parametric (transform-wise)</p>
<p>Please give comments about your interest on these features if you’d be user or implementation suggestion if you are a developer.</p>
<p>Thank you</p>

---

## Post #2 by @mau_igna_06 (2022-05-14 13:23 UTC)

<p>I’ve started working on the add models tool as weekend project.</p>
<p>Comments are welcomed</p>
<p>I’ll post my branch soon</p>
<p>I added another argument to the dynamicModelerWidgets that let’s you filter parametersWidgets depending on the value of another parameterWidget so they are not shown. This is needed since each sourceFilter has at least 3 parameters and right now I’m adding 15 sources to choose from on a combobox</p>

---

## Post #3 by @mau_igna_06 (2022-05-14 13:42 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="2" data-topic="23420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I added another argument to the dynamicModelerWidgets that let’s you filter parametersWidgets depending on the value of another parameterWidget so they are not shown. This is needed since each sourceFilter has at least 3 parameters and right now I’m adding 15 sources to choose from on a combobox</p>
</blockquote>
</aside>
<p>I’m thinking this solution it is not good. It would be better just to add a “addGeometry” menu on the Dynamic modeler module where the user can select one of the different 15 different sources (each one would be a Tool and an action on the menu). This will result in at least 1 order of magnitude less qtWidgets hidden on the mainWindow.</p>

---

## Post #4 by @lassoan (2022-05-14 20:04 UTC)

<p>You can add a “Shape” tool to Dynamic modeler. It could have a type selector combobox where you would choose between sphere, cylinder, cube, etc.</p>
<p>Code quality and complexity of vtkbool library is not well suited to be included in Slicer core. Ideally, vtkbool would need to be cleaned up and converted into a VTK remote module. But as a temporary solution, we could move over the files from Sandbox extension into the SurfaceToolbox.</p>

---

## Post #5 by @mau_igna_06 (2022-05-14 20:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="23420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can add a “Shape” tool to Dynamic modeler. It could have a type selector combobox where you would choose between sphere, cylinder, cube, etc.</p>
</blockquote>
</aside>
<p>Wouldn’t be easier to just use a menu button “Add geometry” and when it’s clicked a list of available Add-Geometry-Tools appear (e.g: “Add Arrow”, “Add Cube”, “Add Elypsoid”, etc)?</p>
<p>What do you think about my concern of too many parameter widgets per tool?.. I want to add 15 different sources and each has 3 parameters at least. That’s 45 parameter widgets per tool (if there is only one that is general). Maybe the GUI will become too slow…<br>
I think it’s best to have 15 different new tools, each one with a parameter, I know it sound like too much at first but I think the other option is less optimal.</p>

---

## Post #6 by @lassoan (2022-05-14 22:26 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="23420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Wouldn’t be easier to just use a menu button “Add geometry” and when it’s clicked a list of available Add-Geometry-Tools appear (e.g: “Add Arrow”, “Add Cube”, “Add Elypsoid”, etc)?</p>
</blockquote>
</aside>
<p>Adding a dropdown menu to the tool list would take considerable effort to implement and would not address all problems, such much larger amount of code to maintain (one class for each shape instead of 1) and users would not be able to easily switch between primitives.</p>
<p>If we just have 3-4 shape primitives then we may consider adding each as a separate tool, otherwise it would be simpler to manage all shapes with a single tool.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="23420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>“Add Arrow”, “Add Cube”, “Add Elypsoid”,</p>
</blockquote>
</aside>
<p>We need to review the shape list we want to support. Ellipsoid (sphere is special case), cylinder, prism (cube is special case), and cone would cover most use cases. If we add more complex shapes, such as arrow, needle, coordinate system axes, etc. then the number can go up, but I’m not sure if that these need to be dynamic models (e.g., we use SlicerIGT extension’s Create Models module for creating such models and it works fine).</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="23420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>What do you think about my concern of too many parameter widgets per tool?.. I want to add 15 different sources and each has 3 parameters at least. That’s 45 parameter widgets per tool (if there is only one that is general). Maybe the GUI will become too slow…</p>
</blockquote>
</aside>
<p>If we have a single tool for all shapes, we still have only a handful of parameters (diameter x/y/z, number of sides, maybe a secondary diameter). It would be nice to implement a way to allow hiding parameter widgets depending on parameter values (e.g., do not show number of sides for a cube).</p>
<p>There should be no perceivable slowdown, even if you display a few hundred widgets.</p>

---

## Post #7 by @mau_igna_06 (2022-05-29 01:13 UTC)

<p>Hi. Here is how this pull request looks right now.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ba45e5c863469bca2c21dd693f0909e76b6167.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ba45e5c863469bca2c21dd693f0909e76b6167.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ba45e5c863469bca2c21dd693f0909e76b6167.mp4</a>
    </source></video>
  </div><p></p>
<p>Wanna try it to give feedback? <a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2" rel="noopener nofollow ugc">Here is the branch</a></p>
<p>The idea is that according to the feedback I’ll add all the other remaining sources, and then create the glyph tool</p>

---
