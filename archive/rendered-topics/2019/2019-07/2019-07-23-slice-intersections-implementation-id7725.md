# Slice intersections implementation

**Topic ID**: 7725
**Date**: 2019-07-23
**URL**: https://discourse.slicer.org/t/slice-intersections-implementation/7725

---

## Post #1 by @rprueckl (2019-07-23 12:32 UTC)

<p>Hi,</p>
<p>I’m looking for some help in understanding an implementation detail: I am unable to find the implementation of the slice intersection lines that are displayed in the slice viewers when they are activated via the menu. How are they rendered and how are the colors and positions set/updated?</p>
<p>Looking for forward for some insight.<br>
Thanks<br>
Robert</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47afffb30aa4c0125282decec07021d58db121c4.png" data-download-href="/uploads/short-url/aeaYwj8G60pwCdU0lXhT9jwQ3B2.png?dl=1" title="intersections" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47afffb30aa4c0125282decec07021d58db121c4.png" alt="intersections" data-base62-sha1="aeaYwj8G60pwCdU0lXhT9jwQ3B2" width="342" height="500" data-dominant-color="515051"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">intersections</span><span class="informations">384×561 21.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-07-23 13:57 UTC)

<p>Hi Robert -</p>
<p>It’s a somewhat complex topic, but you could start here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionWidget.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionWidget.cxx" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionWidget.cxx</a></h4>
<pre><code class="lang-cxx">/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkMRMLSliceIntersectionWidget.cxx

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
#include "vtkMRMLSliceIntersectionWidget.h"

#include "vtkMRMLAbstractSliceViewDisplayableManager.h"
#include "vtkMRMLApplicationLogic.h"
#include "vtkMRMLCrosshairDisplayableManager.h"
#include "vtkMRMLCrosshairNode.h"
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionWidget.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2019-07-23 18:41 UTC)

<p><a class="mention" href="/u/rprueckl">@rprueckl</a> What would you like to do?</p>

---

## Post #4 by @rprueckl (2019-07-24 07:27 UTC)

<p>Thanks for the answer - i found what I was looking for - also in the file</p>
<p><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLModelSliceDisplayableManager.cxx" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLModelSliceDisplayableManager.cxx</a></p>
<p>This concrete question was merely out of interest, but in general we are currently starting the process of building a customized application on top of the slicer libraries. Therefore, I was investigating different parts of the code. Currently, I make myself familiar with slicelets and the custom application template. It could easily be that you will see me more often in this forum <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
