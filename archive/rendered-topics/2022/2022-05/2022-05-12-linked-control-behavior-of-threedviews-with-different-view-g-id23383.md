# Linked control behavior of ThreeDViews with different view groups: linked control ignores view group setup?

**Topic ID**: 23383
**Date**: 2022-05-12
**URL**: https://discourse.slicer.org/t/linked-control-behavior-of-threedviews-with-different-view-groups-linked-control-ignores-view-group-setup/23383

---

## Post #1 by @mrlongzhang (2022-05-12 03:46 UTC)

<p>Here is my settings: A customized layout with 3 three-D Views. The view group of the first one is 0. And the rest two are assigned to be 1. Using the following code:</p>
<pre><code class="lang-python">viewNode = slicer.mrmlScene.GetSingletonNode('1', 'vtkMRMLViewNode')
viewNode.SetViewGroup(0)
viewNode.LinkedControlOff()

viewNode = slicer.mrmlScene.GetSingletonNode('2', 'vtkMRMLViewNode')
viewNode.SetViewGroup(1)
viewNode.LinkedControlOn()
viewNode = slicer.mrmlScene.GetSingletonNode('3', 'vtkMRMLViewNode')
viewNode.SetViewGroup(1)
viewNode.LinkedControlOn()
</code></pre>
<p>What I want is to synchronize operations on view 2 and 3 (view group 1), but not on view 1 (view group 0). However, view 1 remains synchronize with view 2 and 3 and vice versa.</p>
<p>Did I miss something? Or I did something wrong?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2022-05-12 20:35 UTC)

<p>Thanks for reporting and providing a script that reproduces the issue. Using this I was able to reproduce and fix it. The problem was that there was a check for the view group but it always ended up comparing the view group ID with itself, therefore synchronizing all views regardless of group IDs. I’ll push a fix later today.</p>

---

## Post #3 by @mrlongzhang (2022-05-16 12:55 UTC)

<p>Thank you very much, Andras. Glad to have a little contribution to this great project <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---
