# Set linear transform parameter via python

**Topic ID**: 12742
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/set-linear-transform-parameter-via-python/12742

---

## Post #1 by @PaoloZaffino (2020-07-27 11:12 UTC)

<p>Hi all,<br>
I would like to set and control a linear transformation from python.</p>
<p>I created a linear transformation via the module GUI and then I changed a parameter (just to do a test).<br>
If I run this code nothing changes in the GUI (I would expect a reset to an identity matrix):</p>
<blockquote>
<p>t = slicer.mrmlScene.GetFirstNodeByName(“LinearTransform”)<br>
m = vtk.vtkMatrix4x4()<br>
t.SetMatrixTransformToParent(m)</p>
</blockquote>
<p>Of course I am missing something!<br>
Thanks a lot.</p>
<p>Paolo</p>

---

## Post #2 by @lassoan (2020-07-27 13:27 UTC)

<p>What you do is correct.</p>
<p>Maybe <code>slicer.mrmlScene.GetFirstNodeByName()</code> does not return you the transform that you expect because you have multiple transforms by that name in the scene.</p>

---

## Post #3 by @PaoloZaffino (2020-07-27 13:43 UTC)

<p>If I use GetNOdeByID it works, but it’s strange, because I’m trying this into an empty scene.</p>

---

## Post #4 by @lassoan (2020-07-27 15:41 UTC)

<p>By default, 3 transforms are created for some built-in nodes (cameras or slices). But other modules can create transforms by using any names any time, so <code>GetFirstNodeByName</code> is only recommended for debugging or testing.</p>

---

## Post #5 by @PaoloZaffino (2020-07-28 09:39 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I’ll go for the ID, much safer.</p>
<p>Paolo</p>

---
