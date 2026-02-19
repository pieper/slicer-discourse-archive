---
topic_id: 4854
title: "Is Vtkguisupportqtopengl Available In 8 2 0 With Vtk Renderi"
date: 2018-11-22
url: https://discourse.slicer.org/t/4854
---

# Is vtkGUISupportQtOpenGL available in 8.2.0 with VTK_RENDERING_BACKEND=OpenGL2 ?

**Topic ID**: 4854
**Date**: 2018-11-22
**URL**: https://discourse.slicer.org/t/is-vtkguisupportqtopengl-available-in-8-2-0-with-vtk-rendering-backend-opengl2/4854

---

## Post #1 by @yurivict (2018-11-22 23:52 UTC)

<p>I couldn’t build the 3dslicer project because 8.1.2 only has vtkGUISupportQtOpenGL when VTK_RENDERING_BACKEND=OpenGL, which is limiting in other respects.</p>
<p>Also see here: <a href="http://vtk.1045678.n5.nabble.com/Find-reason-for-exclusion-of-vtkGUISupportQtOpenGL-in-build-output-td5738976.html" rel="nofollow noopener">http://vtk.1045678.n5.nabble.com/Find-reason-for-exclusion-of-vtkGUISupportQtOpenGL-in-build-output-td5738976.html</a></p>

---

## Post #2 by @lassoan (2018-11-22 23:54 UTC)

<p>Slicer requires OpenGL2 backend. By now most (maybe all) of the old OpenGL backend are implemented, there are huge improvements and new features in OpenGL2, and the old backend will be removed from VTK soon, so sticking to old OpenGL backend is not an option.</p>

---

## Post #3 by @yurivict (2018-11-23 00:23 UTC)

<p>Which VTK version do you build it with? I tried it with <code>8.1.2</code> and failed for the above reason.<br>
Is this fixed in <code>8.2.0</code> (which is still RC), should I try it? Or, otherwise, which vtk works?</p>

---

## Post #4 by @lassoan (2018-11-23 00:56 UTC)

<p>Slicer downloads and builds all its dependencies, including VTK. Slicer configures VTK for optimal performance, for example uses TBB as SMP backend. So, I would strongly recommend to let Slicer build VTK for itself.</p>
<p>If you really want to configure Slicer to use your VTK build then use VTK 8.2.</p>

---

## Post #5 by @yurivict (2018-11-23 01:12 UTC)

<p>What you recommend would only work on Linux, because VTK doesn’t build on BSDs without patches.<br>
I want to create the FreeBSD port for slicer.</p>

---

## Post #6 by @lassoan (2018-11-23 03:01 UTC)

<aside class="quote no-group" data-username="yurivict" data-post="5" data-topic="4854">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/838e76/48.png" class="avatar"> yurivict:</div>
<blockquote>
<p>VTK doesn’t build on BSDs without patches</p>
</blockquote>
</aside>
<p>Please send your patches to VTK developers. Until the patches are integrated into the official VTK repository (and <a href="https://github.com/Slicer/VTK/">Slicer’s VTK fork</a>), you can build Slicer with your own VTK fork: use Slicer’s VTK fork as a basis and specify set Slicer_VTK_GIT_REPOSITORY and Slicer_VTK_GIT_TAG in CMake when you configure your Slicer build to point to your fork.</p>

---
