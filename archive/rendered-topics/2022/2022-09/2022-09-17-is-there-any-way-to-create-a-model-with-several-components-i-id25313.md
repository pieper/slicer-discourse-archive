# Is there any way to create a model with several components in CLI

**Topic ID**: 25313
**Date**: 2022-09-17
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-create-a-model-with-several-components-in-cli/25313

---

## Post #1 by @wpgao (2022-09-17 06:18 UTC)

<p>Is there any way to create a model with several components, and each component (a mesh model) with different color in CLI. Then, output the model and automatic loaded by Slicer.<br>
Thanks!</p>

---

## Post #2 by @pieper (2022-09-17 15:26 UTC)

<p>Yes, you can look at the ModelMaker module.  It’s slightly legacy at this point since we move to the Segmentation infrastructure but it still works to convert labelmaps to multiple colored models (meshes).</p>

---

## Post #3 by @wpgao (2022-09-18 01:12 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="25313">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>orks to convert labelmaps to multiple colored mod</p>
</blockquote>
</aside>
<p>Thanks Steve! It’s a good suggestion. I developed a CLI using python, Slicer can be imported, but its modules cannot be found. Is it possible to save the model with color  into a single vtk file and loaded it in Slicer? I had tried but the model can be loaded without color information.</p>

---

## Post #4 by @pieper (2022-09-18 16:26 UTC)

<p>You can make a single VTK polydata file with scalar colors but they won’t be turned on by default (user would need to turn them on in the Models module).  The way the ModelMaker works is by writing out a mini-mrml scene that includes the color information for each polydata.  The CLI infrastructure is intended to make it easy to do simple things, but if you need to do something more complex you might want to put the implementation in a module logic instead so you can use the full Slicer API.</p>

---

## Post #5 by @wpgao (2022-09-19 01:29 UTC)

<p>Did you mean that if I want to use the full SlicerAPI, I should implement the module as a loadable module or scripted module rather than a CLI?</p>

---

## Post #6 by @pieper (2022-09-19 12:41 UTC)

<p>Yes, that’s right.  CLI modules are a special case.</p>

---
