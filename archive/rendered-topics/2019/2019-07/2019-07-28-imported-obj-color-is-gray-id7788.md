---
topic_id: 7788
title: "Imported Obj Color Is Gray"
date: 2019-07-28
url: https://discourse.slicer.org/t/7788
---

# Imported obj color is gray

**Topic ID**: 7788
**Date**: 2019-07-28
**URL**: https://discourse.slicer.org/t/imported-obj-color-is-gray/7788

---

## Post #1 by @Amine (2019-07-28 18:45 UTC)

<p>Version : 4.11.0 windows 10</p>
<p>imported obj files are stripped of their color and all shown gray, im i doing something wrong or is there a way to do it via scripts?<br>
Thanks</p>

---

## Post #2 by @lassoan (2019-07-29 03:54 UTC)

<p>What does the .obj file contain?</p>
<p>If the file is from a surface scanner and you want to display texture then you can follow these instructions: <a href="https://discourse.slicer.org/t/displaying-textured-3d-models/2521/2" class="inline-onebox">Displaying textured 3D models</a></p>
<p>If exported segmentation to .obj and trying to load that then you can restore the original segment colors but it requires manual steps, as .obj is primarily used as an export format in Slicer. When you read a .obj file then object IDs are stored in the model nodes as scalars. You can use these scalars to set different color for each segment (Models module / Scalars section). If you use the colormap of the original segmentation then you’ll get back those colors.</p>

---

## Post #3 by @Amine (2019-07-29 23:29 UTC)

<p>Thanks for your answer.<br>
The .obj only has diffuse color information given by slicer while exporting (in its .mtl i assume). I could not get it to work from scalars section no matter what i color table i used</p>

---

## Post #4 by @lassoan (2019-07-30 02:37 UTC)

<p>Material file is not used when an .obj file is read. You can create a color table file from the material file if you want to use the material colors.</p>
<p>There are many ways to approach import colored models into Slicer. If you give a bit more information about what kind of meshes you work with, what software generates them, and what you want to do with them in Slicer then we can give more specific advice.</p>

---

## Post #5 by @Amine (2019-07-30 03:10 UTC)

<p>My obj files are generated from slicer (goal = export model and import into another scene using .obj)<br>
and from blender (initially exported from slicer) (goal = give back models to slicer scene after modifications)<br>
the colors are originally set from slicer segment editor and models module</p>
<p>As a counter-measure i tried to iterate over model nodes and set new colors by name but i could not iterate over the model nodes visible in Models module only (class vtkMRMLModelNode contains slice intersections and ROIs too)</p>

---

## Post #6 by @lassoan (2019-07-30 04:11 UTC)

<p>If you set master representation to closed surface and save the segmentation then not just color, but all metadata are preserved. Each segment is saved as a mesh file in VTK .vtp that you can freely modify and then reload without losing metadata. I’m not sure if there are Blender plugins to provide .vtp file reading/writing, but if there is none then you can convert using a short Python script or using Slicer GUI.</p>
<p>What operation do you perform in Blender that is not available already in Slicer?</p>
<p>FYI, you can import Blender into Slicer as described <a href="https://projectweek.na-mic.org/PW32_2019_London_Canada/Projects/BronchoscopeLocalizationFromDepthMaps/#installing-and-importing-blender-within-slicer" rel="nofollow noopener">here</a> if you want to use Blender data processing features in Slicer.</p>

---

## Post #7 by @Amine (2019-07-30 04:39 UTC)

<p>Blender has a more intuitive GUI for working with models such as sculpting and mesh optimisation (decimation, remove doubles etc), also useful to merge multiple files into one .obj for some 3d viewers that only accept that format, already tried slicer’s surface toolbox module but it was not as complete.</p>
<p>Yes .vtp writing in blender could do the trick, i will look into that direction, still, directly taking .mtl’s in account could be a plus in slicer.<br>
Importing blender into slicer looks very promising to run scripted tasks.</p>

---

## Post #8 by @lassoan (2019-07-30 13:12 UTC)

<aside class="quote no-group" data-username="Amine" data-post="7" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>Blender has a more intuitive GUI for working with models such as sculpting</p>
</blockquote>
</aside>
<p>Slicer is intended to create models of an underlying image and not free sculpting, so if you need that then definitely go with Blender instead.</p>
<aside class="quote no-group" data-username="Amine" data-post="7" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>mesh optimisation (decimation, remove doubles etc)</p>
</blockquote>
</aside>
<p>These should be all already available in Slicer. Is there any specific that you cannot find?</p>
<aside class="quote no-group" data-username="Amine" data-post="7" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>useful to merge multiple files into one .obj for some 3d viewers</p>
</blockquote>
</aside>
<p>We created “Export to files” feature for exactly this reason. If you choose OBJ file format then all segments are saved into a single .obj file.</p>

---

## Post #9 by @Amine (2019-07-30 16:58 UTC)

<p>Here are some limitations that i encountered  with slicer’s surface toolbox:</p>
<ol>
<li>there is a need to select models by name in the input/output section, there is no 3D view click to highlight the model (which is not necessary in slicer’s original purpose)</li>
<li>sometimes effects don’t work if a model made externally to slicer is loaded; Models produced from slicer work fine though</li>
<li>It is not possible to undo the modifications</li>
<li>It is not possible to dynamically (real-time) visualize the effect’s intensity on the 3d view with sliding a bar like with blender’s modifiers</li>
<li>it is not possible to add a scripted reversible modifier stack then tune individual modifiers within the stack (modifiers in blender do not become definitively applied immediately and individually)</li>
</ol>
<p>Other than those limitations the effect’s algorythms themselves are good in slicer, but it can be hard to dynamically find the best combination for a multitude of models.<br>
However, blender’s algorythms produce cleaner results, as in this 90% decimation of the same model (left is slicer):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e00c0920a5acc833ffe0a3adb49f0aa15a2bdd8.jpeg" data-download-href="/uploads/short-url/6yXzFnWzo1cWdbcewf1rFJe8RKw.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e00c0920a5acc833ffe0a3adb49f0aa15a2bdd8_2_690x231.jpeg" alt="PNG" data-base62-sha1="6yXzFnWzo1cWdbcewf1rFJe8RKw" width="690" height="231" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e00c0920a5acc833ffe0a3adb49f0aa15a2bdd8_2_690x231.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e00c0920a5acc833ffe0a3adb49f0aa15a2bdd8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e00c0920a5acc833ffe0a3adb49f0aa15a2bdd8.jpeg 2x" data-dominant-color="AA5779"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1003×337 80.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Export to files works well for segments but that implies they don’t have any post-processing.</p>
<p>Another problem from slicer’s obj write is exported colors get darker, for example R 255  G100  B 30 will become R85  G 33  B 10 (All values gets divided by 3), i had to script blender to revert it</p>

---

## Post #10 by @lassoan (2019-07-30 19:15 UTC)

<aside class="quote no-group" data-username="Amine" data-post="9" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>there is a need to select models by name in the input/output section, there is no 3D view click to highlight the model (which is not necessary in slicer’s original purpose)</p>
</blockquote>
</aside>
<p>Currently, this requires two steps. 1. Use shift+mousemove in the 3D view to find a segment in 2D views. 2. Hover over the crosshair position in slice views to see which segment it is (easier to see if you enable crosshair on the toolbar and set jump mode to centered).</p>
<p>We will make this more convenient in the near future. If you give more details about how and when you would use it then we can take it into account when we design how the model picking feature will work.</p>
<aside class="quote no-group" data-username="Amine" data-post="9" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>sometimes effects don’t work if a model made externally to slicer is loaded; Models produced from slicer work fine though</p>
</blockquote>
</aside>
<p>Slicer assumes you have a background volume to work with. You can create a blank volume to enable editing (click on the button next to the master volume selector then choose to specify segmentation geometry based on the current segmentation), but it is kind of pointless because it would mean that you are not segmenting anymore just doing freehand sculpting (that modeling tools such as Blender are better suited for).</p>
<aside class="quote no-group" data-username="Amine" data-post="9" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>It is not possible to undo the modifications</p>
</blockquote>
</aside>
<p>You can undo any modifications in Segment editor.</p>
<aside class="quote no-group" data-username="Amine" data-post="9" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>It is not possible to dynamically (real-time) visualize the effect’s intensity on the 3d view with sliding a bar like with blender’s modifiers</p>
</blockquote>
</aside>
<p>You have real-time preview of some effects in Segment Editor. It would be also very easy to implement auto-update on slider change in Surface toolbox. Results of what operations you would like to preview in real-time?</p>
<aside class="quote no-group" data-username="Amine" data-post="9" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>it is not possible to add a scripted reversible modifier stack then tune individual modifiers within the stack (modifiers in blender do not become definitively applied immediately and individually)</p>
</blockquote>
</aside>
<p>Segmentation conversion parameters, such as smoothing and decimation can be reversed/tuned individually in Segment Editor. Parameters you set in the Surface toolbox can be also reversed/changed individually.</p>
<aside class="quote no-group" data-username="Amine" data-post="9" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>However, blender’s algorythms produce cleaner results, as in this 90% decimation of the same model (left is slicer):</p>
</blockquote>
</aside>
<p>I agree that vtkDecimatePro filter in VTK does not produce very good quality meshes. It would be quite easy to integrate other remeshers (such as the VTK-based <a href="https://github.com/valette/ACVD">ACVD</a>) or run Blender’s remesher in Slicer if there is a strong need for it. However, there has not been too many requests for improving remeshing in Slicer, because editing happens in labelmap domain and full-resolution meshes can be displayed and exported without problems.</p>

---

## Post #11 by @Amine (2019-07-30 20:56 UTC)

<p>Thanks for your answer,</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you give more details about how and when you would use it then we can take it into account when we design how the model picking feature will work.</p>
</blockquote>
</aside>
<p>It can be useful for picking segments on the go (on slice viewers/3D view), to pick a segment and continue painting on it for example, when Segment editor is the active module then segments would be pickable using the (none) cursor or a shortcut (Alt? ) + click<br>
and when surface toolbox/models modules are active the models would be pickable ( but until surface toolbox is enhanced i hardly see a usage for models)</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer assumes you have a background volume to work with</p>
</blockquote>
</aside>
<p>I was talking about 3D Models, not segments, some imported model nodes were not compatible with surface tool box and effects did not work</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="10" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<blockquote>
<p>It is not possible to undo the modifications</p>
</blockquote>
<p>You can undo any modifications in Segment editor.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Parameters you set in the Surface toolbox can be also reversed/changed individually.</p>
</blockquote>
</aside>
<p>Also talking about Effects applied to model nodes, once applied they are not reversible (Ctrl Z is not working to Surface toolbox applied effects)</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be also very easy to implement auto-update on slider change in Surface toolbox. Results of what operations you would like to preview in real-time?</p>
</blockquote>
</aside>
<p>As a basic addition, just a “show preview” check box that allows previewing the end result would be enough : for decimation its very useful (used with solid view and wireframe, it can allow quick optimisation of the decimate ratio to perform max reduction without altering the mesh quality)</p>
<p>ideally this would be integrated in the surface toolbox along with the interactive model picker:</p>
<ol>
<li>picked model gets set as input and output by default unless specified otherwise by a checkbox)</li>
<li>then there would be a combobox with available effects and an an “add effect” button to add effects to an empty stack (this is interesting to set custom filter orders like start with a smoothing then decimate then smooth again then auto orient normals…)</li>
<li>each effect in the stack has its own sliders</li>
<li>“preview” checkbox to visualize modifications in real time on the 3D view/slices, and “apply effects stack” to harden the effects.</li>
</ol>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>or run Blender’s remesher in Slicer if there is a strong need for it. However, there has not been too many requests for improving remeshing in Slicer,</p>
</blockquote>
</aside>
<p>I rarely use slicer’s surface toolbox even though i do extensive mesh processing and never asked for improvements because there are programs like blender that do it natively and i leave slicer for the segmentation work (and i believe more people are in the same situation)</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>because editing happens in labelmap domain and full-resolution meshes can be displayed and exported without problems</p>
</blockquote>
</aside>
<p>i don’t apply much effects at the Labelmap/segments step because the resolution is limited by the Master Geometry of the background volume and smoothing effects in segment editor can perform poorly for fine structures that get close to the vertex size (discontinuity made in a fine vessel for example). so i just export models once segmentation is done and that allows more freedom for post-processing the structures</p>

---
