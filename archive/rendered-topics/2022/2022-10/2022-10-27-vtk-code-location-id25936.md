# Vtk code location

**Topic ID**: 25936
**Date**: 2022-10-27
**URL**: https://discourse.slicer.org/t/vtk-code-location/25936

---

## Post #1 by @bserrano (2022-10-27 15:36 UTC)

<p>Hi,</p>
<p>I’m struggling to find the code for slicer.vtkImageSlicePaint().<br>
Does anyone know where I can find it?</p>
<p>Many thanks,</p>
<p>Belén</p>

---

## Post #2 by @Sunderlandkyl (2022-10-27 15:55 UTC)

<p>vtkImageSlicePaint was removed from 3D Slicer with the Editor module in this commit:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/39283db420baf502fa99865c9d5d58d0e5295a6e">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/39283db420baf502fa99865c9d5d58d0e5295a6e" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/39283db420baf502fa99865c9d5d58d0e5295a6e" target="_blank" rel="noopener nofollow ugc">ENH: Remove legacy Editor module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-11-05" data-time="12:57:51" data-timezone="UTC">12:57PM - 05 Nov 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 106 files with 24 additions and 18648 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/39283db420baf502fa99865c9d5d58d0e5295a6e" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+24</span>
          <span class="removed">-18648</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Remove Editor module to reduce maintenance workload and simplify user choice.
Ed<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/39283db420baf502fa99865c9d5d58d0e5295a6e" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">itor module has been deprecated for several years, Segment Editor offers more and improved feature set.

Also removed templates and vtkITK classes that are not used in Slicer core anymore.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Here is the code from before it was removed:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8245aa59d114e47fc9884c4baa5d66bf900329ff/Modules/Scripted/EditorLib/Logic/vtkImageSlicePaint.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8245aa59d114e47fc9884c4baa5d66bf900329ff/Modules/Scripted/EditorLib/Logic/vtkImageSlicePaint.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8245aa59d114e47fc9884c4baa5d66bf900329ff/Modules/Scripted/EditorLib/Logic/vtkImageSlicePaint.cxx" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/8245aa59d114e47fc9884c4baa5d66bf900329ff/Modules/Scripted/EditorLib/Logic/vtkImageSlicePaint.cxx</a></h4>


      <pre><code class="lang-cxx">/*=========================================================================

  Program:   Visualization Toolkit
  Module:    $RCSfile: vtkImageSlicePaint.cxx,v $

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
#include "vtkImageSlicePaint.h"

// VTK includes
#include &lt;vtkNew.h&gt;
#include &lt;vtkObjectFactory.h&gt;
#include &lt;vtkVersion.h&gt;
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/8245aa59d114e47fc9884c4baa5d66bf900329ff/Modules/Scripted/EditorLib/Logic/vtkImageSlicePaint.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
