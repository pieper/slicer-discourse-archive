# Marching Cubes implementation

**Topic ID**: 2738
**Date**: 2018-04-30
**URL**: https://discourse.slicer.org/t/marching-cubes-implementation/2738

---

## Post #1 by @MGM (2018-04-30 17:31 UTC)

<p>Hello,</p>
<p>I’m trying to implementation the marching cubes algorithm in c++; without any external libraries.</p>
<p>I’m looking for a good reference, so I can follow step by step this algorithm.</p>
<p>There is a lot of papers talking about this algorithm, but so hard to understand.</p>
<p>Also, I would like to know if 3DSlicer integrate the vtk solution or another one ?</p>
<p>I appreciate your help</p>

---

## Post #2 by @lassoan (2018-04-30 17:57 UTC)

<p>Slicer has been using marching cubes algorithm for image-&gt;mesh conversion, but recently we switched to flying edges algorithm, which is implemented in a way that is better optimized for multi-core CPUs. Slicer uses VTK’s implementation for both. You can still try marching cubes in Slicer-4.8.1, and flying edges in latest nightly.</p>

---

## Post #3 by @mschumaker (2018-04-30 19:10 UTC)

<p>You may have looked at this already, but you may be able to understand it by comparing what’s in the papers you’ve looked at with the VTK C++ code:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/master/Filters/Core/vtkMarchingCubes.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/master/Filters/Core/vtkMarchingCubes.cxx" target="_blank" rel="nofollow noopener">Kitware/VTK/blob/master/Filters/Core/vtkMarchingCubes.cxx</a></h4>
<pre><code class="lang-cxx">/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkMarchingCubes.cxx

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
#include "vtkMarchingCubes.h"

#include "vtkCellArray.h"
#include "vtkCharArray.h"
#include "vtkDoubleArray.h"
#include "vtkFloatArray.h"
</code></pre>

  This file has been truncated. <a href="https://github.com/Kitware/VTK/blob/master/Filters/Core/vtkMarchingCubes.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @MGM (2018-05-02 09:35 UTC)

<p>Hi</p>
<p>Thank you for your feedback.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/mschumaker">@mschumaker</a>; In fact, I tried both vtkMarchingCubes and vtkFlyingEdges3D directly on vtk; and results comes basically similar. wall time  and output file.<br>
Do you know any others MC implementations without vtk?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>; is there any available documentations of MarchingCubes / vtkFlyingEdges3D implementation under 3DSlicer.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2738">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>which is implemented in a way that is better optimized for multi-core CPUs</p>
</blockquote>
</aside>
<p>Do you mean, that MarchingCubes implementation under previous 3DSlicer release, doesn’t support multi-core CPUs ?</p>
<p>Please, how can I test both algorithm with 4.8.1; and there is any documentation on those implementation ?</p>
<p>Also, I takes a look on this topic : <a href="http://vtk.1045678.n5.nabble.com/Flying-Edges-td5730055.html" rel="noopener nofollow ugc">http://vtk.1045678.n5.nabble.com/Flying-Edges-td5730055.html</a></p>
<p>Thank you</p>

---

## Post #5 by @ihnorton (2018-05-02 13:04 UTC)

<aside class="quote no-group" data-username="MGM" data-post="4" data-topic="2738">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ebca7d/48.png" class="avatar"> MGM:</div>
<blockquote>
<p>is there any available documentations of MarchingCubes / vtkFlyingEdges3D implementation under 3DSlicer.</p>
</blockquote>
</aside>
<p>See the first reference here (paper by one of the original VTK authors):</p>
<aside class="onebox wikipedia" data-onebox-src="https://en.wikipedia.org/wiki/Marching_cubes#Sources">
  <header class="source">

      <a href="https://en.wikipedia.org/wiki/Marching_cubes#Sources" target="_blank" rel="noopener">en.wikipedia.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://en.wikipedia.org/wiki/Marching_cubes#Sources" target="_blank" rel="noopener">Marching cubes | Sources</a></h3>

<p>1.Image-based meshing |
 2.Marching tetrahedra</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Flying edges was published in IEEE so it’s not open, but there is a PDF on ResearchGate.</p>

---

## Post #6 by @lassoan (2018-05-02 22:39 UTC)

<aside class="quote no-group" data-username="MGM" data-post="4" data-topic="2738">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ebca7d/48.png" class="avatar"> MGM:</div>
<blockquote>
<p>In fact, I tried both vtkMarchingCubes and vtkFlyingEdges3D directly on vtk; and results comes basically similar. wall time  and output file</p>
</blockquote>
</aside>
<p>It is important that vtkFlyingEdges3D only uses multiple CPU cores if VTK is built with Threading Building Blocks (TBB) as SMP backend. By default VTK is built with Sequential SMP backend, which means no parallelization. My experience is that flying edges is significantly faster than marching cubes. Flying edges can also provide surface normals, so you can save time because there is no need for extra polydata normals computation.</p>
<p>Also note that for all labelmap conversions we use discrete versions of marching cubes and flying edges filters.</p>

---
