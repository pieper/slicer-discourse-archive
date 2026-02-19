---
topic_id: 45156
title: "Synchronisation Window Level Across Multiple Volumes"
date: 2025-11-20
url: https://discourse.slicer.org/t/45156
---

# Synchronisation window/level across multiple volumes

**Topic ID**: 45156
**Date**: 2025-11-20
**URL**: https://discourse.slicer.org/t/synchronisation-window-level-across-multiple-volumes/45156

---

## Post #1 by @ashkanpakzad (2025-11-20 02:38 UTC)

<p>Hi all, I’ve had a search and can’t find much on this.</p>
<p>Before I embark on trying to implement this myself, is there an obvious way to link multiple scalar volume nodes window/level, such that if you change the window/level in one image, it will change it in the other in real time?</p>
<p>Cheers,</p>
<p>Ashkan</p>

---

## Post #2 by @pieper (2025-11-20 19:04 UTC)

<p>I don’t recall anything that specifically does this, but it would be straightforward to add observers to all the display nodes of interest and copy over the window level to the others when any of them changes.  Be sure to avoid event loops; this should be automatic since no ModifiedEvent will be triggered if you are setting the value to the exactly what it already is (that is, when any of the display nodes changes you can just set them all without triggering a cascade of events).</p>

---

## Post #3 by @ashkanpakzad (2025-11-21 07:41 UTC)

<p>Thank you for confirming! Indeed I went down that route.</p>
<p>Here is my implementation in case anyone comes across this trying to do the same thing:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/ashkanpakzad/817ba3708f7ea2249f9985d7eb52d8f2">
  <header class="source">

      <a href="https://gist.github.com/ashkanpakzad/817ba3708f7ea2249f9985d7eb52d8f2" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/ashkanpakzad/817ba3708f7ea2249f9985d7eb52d8f2" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/ashkanpakzad/817ba3708f7ea2249f9985d7eb52d8f2</a></h4>

  <h5>autoSyncWLSlicer.py</h5>
  <pre><code class="Python"># run startSyncWL() to start and stopSyncWL() to stop.

import slicer
import vtk

observerTags = {}
displayNodes = []
isSyncingWL = False

def startSyncWL():</code></pre>
   This file has been truncated. <a href="https://gist.github.com/ashkanpakzad/817ba3708f7ea2249f9985d7eb52d8f2" target="_blank" rel="noopener nofollow ugc">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
