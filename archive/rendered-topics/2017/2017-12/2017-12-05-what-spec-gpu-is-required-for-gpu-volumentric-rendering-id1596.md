# What spec GPU is required for GPU volumentric rendering?

**Topic ID**: 1596
**Date**: 2017-12-05
**URL**: https://discourse.slicer.org/t/what-spec-gpu-is-required-for-gpu-volumentric-rendering/1596

---

## Post #1 by @jdx-john (2017-12-05 14:39 UTC)

<p>On what type/age of PCs would the software based volumetric renderer be preferable/required compared to the GPU renderer? Realistically these days now that even integrated chipsets are DirectX10 compatible (good by and good riddance Intel GMA chipsets!) should any non-budget machine be able to do volumetric rendering on the GPU?</p>

---

## Post #2 by @pieper (2017-12-05 16:29 UTC)

<p>I don’t think we’ve done anything systematic to check but when things aren’t working we typically hear about it.  Slicer relies on the vtk volume rendering infrastructure, and it’s pretty widely compatible with recent GPUs (and even older ones).  You might try the vtk users mailing list for ideas of what is and isn’t supported (see <a href="http://vtk.org">vtk.org</a>).</p>

---

## Post #3 by @lassoan (2017-12-05 17:13 UTC)

<p>Slicer uses OpenGL for rendering, so DirectX compatibility is not needed.</p>
<p>Current Slicer stable version can use some integrated chipsets for GPU-based rendering, but they are not much faster than CPU (maybe 1.5x-3x faster, while a strong GPU is 20-100x faster).</p>
<p>Slicer will switch to a new rendering backend very soon (this week?). The new backend uses newer OpenGL API, which should improve compatibility with integrated chipsets and it should also be somewhat faster.</p>

---

## Post #4 by @jdx-john (2017-12-05 17:41 UTC)

<p>Sure - D3D version is just an easier check as you have to meet all features to pass, unlike OGL which is less clear <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I was mainly wondering if the software renderer is largely obsolete or should be a fall-back rather than the default, given that any decent computer in the last 5 years sounds like it will give better GPU rendering than software? Or do you find people have enough problems with GPU that software is still widely used?</p>

---

## Post #5 by @lassoan (2017-12-05 18:06 UTC)

<p>Many integrated boards are not compatible with the current (old) backend. With the new backend, the compatibility is much better, but sometimes you have no graphics card at all (headless systems on cloud) or there are limitations of the GPU (maximum memory, texture size, image size, etc.). For these cases, we’ll keep CPU volume rendering option functional.</p>

---
