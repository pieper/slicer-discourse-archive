---
topic_id: 1789
title: "Using Glsl Post Process 2D Pixel Shader With Slicer"
date: 2018-01-09
url: https://discourse.slicer.org/t/1789
---

# Using GLSL post-process (2D) pixel shader with Slicer

**Topic ID**: 1789
**Date**: 2018-01-09
**URL**: https://discourse.slicer.org/t/using-glsl-post-process-2d-pixel-shader-with-slicer/1789

---

## Post #1 by @jdx-john (2018-01-09 13:47 UTC)

<p><em>I assume this is a dev rather than user question, that we cannot do it using an extension?</em></p>
<p>We have some GLSL shaders used to post-process a textured quad. In our application we use this in conjunction with 3D rendering and vertex/pixel shaders on polygonal models, but this shader is applied after all the transforms and normal rendering - essentially just on the contents of the render buffer applied to a quad and then run several passes.</p>
<p>This means - we think - we can take our shader and apply it to <em>any</em> source image using standard OpenGL. <a class="mention" href="/u/lassoan">@lassoan</a> has previously told us we can do anything VTK can in Slicer and VTK has shader support but he’s not a shader developer and I’m not a slicer developer so any help figuring out what I can do, and where I “get into” Slicer to do this sort of thing, would be wonderful.<br>
e.g. how to attach my shader to a render pipeline or to a view, how to bind any arguments/parameters it needs. We’re in the situation we have shader/OpenGL developers and Slicer developers and a VTK developer but no cross-over between them for this specific case!</p>

---

## Post #2 by @Davide_Punzo (2018-01-09 15:48 UTC)

<p>I am not sure that it will help, there is this VTK class:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/master/Rendering/OpenGL2/vtkOpenGLImageAlgorithmHelper.h" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/master/Rendering/OpenGL2/vtkOpenGLImageAlgorithmHelper.h" target="_blank" rel="nofollow noopener">Kitware/VTK/blob/master/Rendering/OpenGL2/vtkOpenGLImageAlgorithmHelper.h</a></h4>
<pre><code class="lang-h">/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkOpenGLImageAlgorithmHelper.h

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
/**
 * @class   vtkOpenGLImageAlgorithmHelper
 * @brief   Help image algorithms use the GPU
 *
 * Designed to make it easier to accelerate an image algorithm on the GPU
*/
</code></pre>

  This file has been truncated. <a href="https://github.com/Kitware/VTK/blob/master/Rendering/OpenGL2/vtkOpenGLImageAlgorithmHelper.h" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
in which you can provide your shader and input data (as a vtkImageData) and get the output data (again as a vtkImageData).</p>
<p>Instead, if you’d like to “add” your shader to the regular VTK rendering pipeline, you may try to ask <a class="mention" href="/u/pieper">@pieper</a>. He worked on something similar.</p>

---

## Post #3 by @Davide_Punzo (2018-01-09 15:54 UTC)

<p>see also this link: <a href="https://www.vtk.org/Wiki/Shaders_In_VTK" rel="nofollow noopener">https://www.vtk.org/Wiki/Shaders_In_VTK</a></p>

---

## Post #4 by @jcfr (2018-01-10 12:53 UTC)

<p>Hi,</p>
<p>This project shows an example of customized rendering shader. See <a href="https://github.com/KitwareMedical/vtkColorCodedDepthVolume">https://github.com/KitwareMedical/vtkColorCodedDepthVolume</a></p>

---

## Post #5 by @pieper (2018-01-10 22:05 UTC)

<p>Here’s the other GLSL code <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> mentioned.  It’s less coupled to the vtk rendering process so it can make it simpler to do generic algorithms.  At some point I plan to revisit this and see how it compares to the shader options recently added to VTK core and see if it’s still needed.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/CommonGL">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/CommonGL" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/1f4901ee563f59092640f820b8cd2f57ddf2fc238a5030b85aaf66916c023678/pieper/CommonGL" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/CommonGL" target="_blank" rel="noopener">GitHub - pieper/CommonGL: Experiments in GLSL shading for Slicer and other...</a></h3>

  <p>Experiments in GLSL shading for Slicer and other environments - GitHub - pieper/CommonGL: Experiments in GLSL shading for Slicer and other environments</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
