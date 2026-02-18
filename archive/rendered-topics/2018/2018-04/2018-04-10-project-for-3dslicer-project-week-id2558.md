# Project for 3DSlicer project week

**Topic ID**: 2558
**Date**: 2018-04-10
**URL**: https://discourse.slicer.org/t/project-for-3dslicer-project-week/2558

---

## Post #1 by @Davide_Punzo (2018-04-10 16:36 UTC)

<p>Hi all,</p>
<p>many users asked me for having a 3D views linking functionalities such as the 2D one.</p>
<p>My idea is to implement such functionality in the 3DSlicer core as a small project for the 28th project week.<br>
The implementation will be similar to the 2D views linking (with MRMLLogic) and it will have similarly the two options as well:</p>
<ol>
<li>simple link: only the 3DViewControllers are linked</li>
<li>hot link: also the 3DDisplayViews are linked (i.e. the cameras are in sync)</li>
</ol>
<p>Please let me know if you think it will be useful to have this feature in the 3DSlicer core (otherwise I have to find another project (<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> ).</p>
<p>Davide.</p>

---

## Post #2 by @lassoan (2018-04-10 18:26 UTC)

<p>Some level of property synchronization between 3D views would be definitely useful.</p>
<p>What would you need synchronize?</p>
<ul>
<li>displayed content (what models, volumes, segmentations, etc. are visible in each view)</li>
<li>view properties (show/hide ruler, orientation marker, background color, etc)</li>
<li>camera (position, focal point, up vector, orthogonal/perspective, field of view, etc.)</li>
</ul>
<p>Would you synchronize only modified properties? For example if you only change camera orthogonal/perspective projection mode, would you also synchronize camera position, focal point, etc.?</p>
<p>It would be also nice to have a relative camera motion mode (where relative pose between cameras would be maintained while moving or rotating cameras) so that you can have orthogonal views.</p>
<p>I’m not sure about the link/hot-link name. Hot-link in slice views mainly affect when the changes are synchronized and not what is synchronized.</p>
<p>It is already possible to use the same camera for multiple 3D views (using Cameras module).</p>

---

## Post #3 by @pieper (2018-04-10 22:34 UTC)

<p>Sounds like a good project to me.</p>
<p>If you didn’t already find it, the slice link logic is implemented here and it would be good to think about how to reuse concepts and logic across multiple view types where meaningful.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx" target="_blank">Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx</a></h4>
<pre><code class="lang-cxx">/*=auto=========================================================================

  Portions (c) Copyright 2005 Brigham and Women's Hospital (BWH) All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Program:   3D Slicer
  Module:    $RCSfile: vtkMRMLSliceLinkLogic.cxx,v $
  Date:      $Date$
  Version:   $Revision$

=========================================================================auto=*/

// MRMLLogic includes
#include "vtkMRMLSliceLinkLogic.h"
#include "vtkMRMLSliceLogic.h"
#include "vtkMRMLApplicationLogic.h"

// MRML includes
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Davide_Punzo (2018-04-11 08:36 UTC)

<p>thanks for the feedback.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ol>
<li>displayed content (what models, volumes, segmentations, etc. are visible in each view)</li>
<li>view properties (show/hide ruler, orientation marker, background color, etc)</li>
<li>camera (position, focal point, up vector, orthogonal/perspective, field of view, etc.)</li>
</ol>
</blockquote>
</aside>
<p>at the moment, the users requested me only 2 and 3, of course we can further discuss all the options.<br>
I’ll also check up if 1 is a wanted feature. It will be good if you can also get some more user feedback about to it. Of course we can further discuss this (design, etc…) during the calls or here, now I was mainly interested to see if the project is fine.</p>
<p><strong>Comments point 2:</strong></p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="2558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If you didn’t already find it, the slice link logic is implemented here and it would be good to think about how to reuse concepts and logic across multiple view types where meaningful.</p>
</blockquote>
</aside>
<p>yes I saw it, I was thinking indeed to implement 2 in the same way as for the 2d views controllers.</p>
<p><strong>Comments point 3:</strong></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is already possible to use the same camera for multiple 3D views (using Cameras module).</p>
</blockquote>
</aside>
<p>that’s true, but I think having a button in the 3D view controller it will be much better. Moreover, I think it will be better to not use the same camera node for all the views when it is “linked”. See below.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would you synchronize only modified properties?</p>
</blockquote>
</aside>
<p>Yes, and I think using a cameraNode for each view it is possible</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be also nice to have a relative camera motion mode (where relative pose between cameras would be maintained while moving or rotating cameras) so that you can have orthogonal views.</p>
</blockquote>
</aside>
<p>Yeah I think that it will be good to have this too (e.g., investigating the same object in two 3D views). This can be done updating the camera nodes (when one is modified) instead to give to all the views the same camera node. From the point of view of the GUI, we can design the link button with the option of the angle distance.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m not sure about the link/hot-link name. Hot-link in slice views mainly affect when the changes are synchronized and not what is synchronized.</p>
</blockquote>
</aside>
<p>I agree</p>

---

## Post #5 by @Davide_Punzo (2018-05-15 12:21 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>, do you have some time to further discuss this next Tuesday (22nd) at the project week hangout (or any following one)? It will be nice to agree what to do, so at the project week I can start immediately on the implementation.</p>

---

## Post #6 by @pieper (2018-05-15 22:12 UTC)

<p>Hi <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> yes, I should be able to join next week’s call (I’ll be driving out of town but with the zoom conference I can easily call in).   Awesome if you can get started in advance.</p>

---

## Post #7 by @lassoan (2018-05-16 20:15 UTC)

<p>I plan to join, too.</p>

---
