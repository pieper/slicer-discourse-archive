---
topic_id: 10826
title: "Python Wrapping On The New External Vtkaddon"
date: 2020-03-25
url: https://discourse.slicer.org/t/10826
---

# Python wrapping on the new external vtkAddon

**Topic ID**: 10826
**Date**: 2020-03-25
**URL**: https://discourse.slicer.org/t/python-wrapping-on-the-new-external-vtkaddon/10826

---

## Post #1 by @RafaelPalomar (2020-03-25 10:14 UTC)

<p>Hello.</p>
<p>I like very much the idea of having vtkAddon as a separated project as introduced in <a href="https://github.com/Slicer/Slicer/commit/aaf75e2aaa70a92f16b3ea544b7a8901a98cd509" rel="nofollow noopener">aaf75e2aaa</a>. In this logic, one can think about vtkAddon being a dependency of Slicer --this helps e.g., supporting the idea of having 3D Slicer installed in a system alongside other related projects, where the common dependencies are shared.</p>
<p>In the current implementation, the python wrapping of vtkAddon relies on macros defined in vtkMacroKitPythonWrap.cmake (which is part of 3D Slicer), making impossible to build vtkAddon by itself and producing a cyclic dependency vtkAddon–&gt;Slicer–&gt;vtkAddon.</p>
<p>I would suggest to move a copy of vtkMacroKitPythonWrap.cmake to vtkAddon/CMake as a temporary solution, assuming that the integration of the official VTK will soon come, and that VTK will be the provider of the wrapping functions. Does it make sense? Any thoughts?</p>

---

## Post #2 by @RafaelPalomar (2020-03-25 11:14 UTC)

<p>I see that the Slicer fork of vtkAddon is much more tangled to Slicer than I thought; there are also some specific Slicer variables.</p>
<p>Would it make sense to make like a neutral vtkAddon with all the additions over the original by Lorensen (python wrapping, extra components)? Slicer could get the same configuration by passing cmake variables to the external project and let other projects use it.</p>

---

## Post #3 by @jcfr (2020-03-25 14:42 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="1" data-topic="10826">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>I would suggest to move a copy of vtkMacroKitPythonWrap.cmake to vtkAddon/CMake as a temporary solution, assuming that the integration of the official VTK will soon come, and that VTK will be the provider of the wrapping functions. Does it make sense? Any thoughts?</p>
</blockquote>
</aside>
<p>We will revisit the approach when transitioning to use the latest version of VTK (in the coming days), and will most likely get ride of <code>vtkMacroKitPythonWrap.cmake</code> and use the latest build-system infrastructure made available in VTK.</p>

---
