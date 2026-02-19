---
topic_id: 5146
title: "Vtk Render To Target Texture"
date: 2018-12-19
url: https://discourse.slicer.org/t/5146
---

# [VTK] Render to target/texture?

**Topic ID**: 5146
**Date**: 2018-12-19
**URL**: https://discourse.slicer.org/t/vtk-render-to-target-texture/5146

---

## Post #1 by @adamrankin (2018-12-19 18:24 UTC)

<p>Hello all,</p>
<p>Does anyone have any experience with rendering to a texture instead of an on-screen window? For the life of me I cannot find a VTK example that does this.</p>
<p>Links to examples or a high-level description should be more than enough for me to sort this out…</p>
<p>Edit: typo</p>

---

## Post #2 by @pieper (2018-12-19 19:07 UTC)

<p>Hi <a class="mention" href="/u/adamrankin">@adamrankin</a> -</p>
<p>Yes, GLSL rendering to/from 3D texture is something I’ve been working on for a while.  See this commit for info:</p>
<p><a href="https://github.com/Slicer/Slicer/commit/16a4878de6f17f097618cfb4472cb209538bf82c" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/16a4878de6f17f097618cfb4472cb209538bf82c</a></p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and I have been working on this in the context of fractional segmentation effects (e.g. for soft edged paint brushes).</p>
<p>Everything was working pretty well in Slicer 4.8, but once we switched to the OpenGL2 backend some OpenGL runtime errors have popped up and so some debugging is needed.  Would be great to work with you on this!</p>
<p>I should mention that I have been playing around with the same functionality using WebGL2 and it works great there.  My long-term goal is to have libraries of GLSL code that can work well in either context.</p>
<p>Of course we also want this to be native in VTK and integrate smoothly with the GPU volume rendering.  Several of us <a href="https://na-mic.github.io/ProjectWeek/PW28_2018_GranCanaria/Projects/MultiVolumeRendering/" rel="nofollow noopener">worked on customizing VTK’s shaders at the last Las Palmas Project Week</a>.  At this point the vtkOpenGLTextureImage and vtkOpenGLShaderComputation code in Slicer’s vtkAddons provides features not available (yet) in regular VTK.</p>
<p>-Steve</p>

---
