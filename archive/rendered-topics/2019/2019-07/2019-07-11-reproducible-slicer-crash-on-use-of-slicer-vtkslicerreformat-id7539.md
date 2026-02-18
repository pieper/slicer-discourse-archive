# Reproducible Slicer crash on use of slicer.vtkSlicerReformatLogic.SetSliceOrigin()

**Topic ID**: 7539
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/reproducible-slicer-crash-on-use-of-slicer-vtkslicerreformatlogic-setsliceorigin/7539

---

## Post #1 by @mikebind (2019-07-11 19:06 UTC)

<p>I am trying to get the hang of positioning a slice view within an image volume (as you can do interactively with the Reformat widget or module).  Changing the slice normal seems to work fine and as I expect, but it Slicer has crashed every time I try to use the analogous function to set the slice origin.  Here is code which reproducibly crashes slicer 4.10.1:</p>
<pre><code class="lang-python"># Load sample image volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
sampleDataLogic.downloadMRHead()
# Get a slice node and the logic which does slice reformatting
redNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
reformatLogic = slicer.vtkSlicerReformatLogic()
# Pick a new slice normal
newNormal = [0,1,0]
# Apply that normal
reformatLogic.SetSliceNormal(redNode, newNormal) # this works fine
# Pick a new RAS origin
newOrigin = [0.0, 0.0, 0.0]
# Apply the origin change
reformatLogic.SetSliceOrigin(redNode, newOrigin) # this one crashes Slicer
</code></pre>
<p>And Slicer crashes.  I am using 4.10.1 on Windows 10. I am happy to provide more info if you can tell me what you would want to know.  Maybe the new origin is supposed to be supplied in some other form?  It looks to me like the underlying C++ function is expecting either 3 separate coordinates or a single list of 3 coordinates, just like SetSliceNormal().</p>
<p>Any suggestions?</p>
<p>Thanks!</p>

---

## Post #2 by @jcfr (2019-07-11 19:13 UTC)

<p>Instead of instantiating your own reformat logic, use the one provided by the instantiated Reformat module.</p>
<p>Here is how you could update the code. It also include some indentation fixes and an simpler way of using <code>SampleDataLogic</code></p>
<pre><code class="lang-python"># Load sample image volume
from SampleData import SampleDataLogic
SampleDataLogic().downloadMRHead()

# Get a slice node and the logic which does slice reformatting
redNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
reformatLogic = slicer.modules.reformat.logic()

# Pick a new slice normal
newNormal = [0, 1, 0]
# Apply that normal
reformatLogic.SetSliceNormal(redNode, newNormal)

# Pick a new RAS origin
newOrigin = [0.0, 0.0, 0.0]

# Apply the origin change
reformatLogic.SetSliceOrigin(redNode, newOrigin)
</code></pre>

---

## Post #3 by @mikebind (2019-07-11 19:18 UTC)

<p>Thanks, this fixes the problem!  I was lulled into a false sense of security by the SetSliceNormal working fine the way I was doing it.</p>

---

## Post #4 by @jcfr (2019-07-11 19:43 UTC)

<p>After integrating this PR, the crash will also be fixed and the code you initially will be working.</p>
<p>Since the provided slice node is already associating with a scene, there was no need to explicitly require the logic to be associated with a scene.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1173" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/jcfr" target="_blank" rel="nofollow noopener">
    <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/Slicer/Slicer/pull/1173" target="_blank" rel="nofollow noopener">ReformatLogic: Fix crash and improve GetVolumeBounds()</a>
</h4>

<div class="date">
  by <a href="https://github.com/jcfr" target="_blank" rel="nofollow noopener">jcfr</a>
  on <a href="https://github.com/Slicer/Slicer/pull/1173" target="_blank" rel="nofollow noopener">07:29PM - 11 Jul 19 UTC</a>
</div>

<div class="github-commit-stats">
  <strong>2 commits</strong>
  changed <strong>1 files</strong>
  with <strong>7 additions</strong>
  and <strong>2 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It will even allow to simplify your example further:</p>
<pre><code class="lang-auto">from SampleData import SampleDataLogic
from slicer import vtkSlicerReformatLogic

# Load sample image volume
SampleDataLogic().downloadMRHead()

# Get a slice node and the logic which does slice reformatting
redNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')

# Pick a new slice normal
newNormal = [0, 1, 0]

# Apply that normal
vtkSlicerReformatLogic.SetSliceNormal(redNode, newNormal)

# Pick a new RAS origin
newOrigin = [0.0, 0.0, 0.0]

# Apply the origin change
vtkSlicerReformatLogic.SetSliceOrigin(redNode, newOrigin)
</code></pre>

---
