# Rotation handle in view plane

**Topic ID**: 24254
**Date**: 2022-07-09
**URL**: https://discourse.slicer.org/t/rotation-handle-in-view-plane/24254

---

## Post #1 by @mau_igna_06 (2022-07-09 23:58 UTC)

<p>Hi everyone,</p>
<p>Dear <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, since you have developed a lot around the topic of markups interaction handles: I would like to ask you for a roadmap of the necessary changes to add a rotation around the cameraViewPlane or slicePlane if it is not too much of a hassle.</p>
<ul>
<li>My objetive would be to have something like the blue ring that is seeing here <a href="https://youtu.be/7RMermYOOYY?t=99" class="inline-onebox">Virtual surgical planning using a DCIA free flap for mandibular reconstruction - YouTube</a>
</li>
</ul>
<p>Till now I think I can draw the corresponding glyph with the correct transform but I cannot get it to update with camera movements. Do you know how to achieve this is c++?</p>
<p>I have seen this example:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/VTK/blob/6a9c565da01bcd6295d0bcbb66c0a9d0d2eaa69e/Filters/Core/Testing/Cxx/TestGlyph3DFollowCamera.cxx">
  <header class="source">

      <a href="https://github.com/Kitware/VTK/blob/6a9c565da01bcd6295d0bcbb66c0a9d0d2eaa69e/Filters/Core/Testing/Cxx/TestGlyph3DFollowCamera.cxx" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/6a9c565da01bcd6295d0bcbb66c0a9d0d2eaa69e/Filters/Core/Testing/Cxx/TestGlyph3DFollowCamera.cxx" target="_blank" rel="noopener">Kitware/VTK/blob/6a9c565da01bcd6295d0bcbb66c0a9d0d2eaa69e/Filters/Core/Testing/Cxx/TestGlyph3DFollowCamera.cxx</a></h4>


      <pre><code class="lang-cxx">/*=========================================================================

  Program:   Visualization Toolkit
  Module:    TestExtractSelection.cxx

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/

#include "vtkActor.h"
#include "vtkCamera.h"
#include "vtkCommand.h"
#include "vtkExecutive.h"
#include "vtkGlyph3D.h"
</code></pre>



  This file has been truncated. <a href="https://github.com/Kitware/VTK/blob/6a9c565da01bcd6295d0bcbb66c0a9d0d2eaa69e/Filters/Core/Testing/Cxx/TestGlyph3DFollowCamera.cxx" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
But it appeared too hard to integrate</p>

---
