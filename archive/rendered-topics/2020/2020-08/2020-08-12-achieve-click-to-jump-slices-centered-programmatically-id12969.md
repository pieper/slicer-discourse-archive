---
topic_id: 12969
title: "Achieve Click To Jump Slices Centered Programmatically"
date: 2020-08-12
url: https://discourse.slicer.org/t/12969
---

# Achieve "Click to jump Slices -> centered" programmatically

**Topic ID**: 12969
**Date**: 2020-08-12
**URL**: https://discourse.slicer.org/t/achieve-click-to-jump-slices-centered-programmatically/12969

---

## Post #1 by @mangotee (2020-08-12 20:57 UTC)

<p>Hi all,<br>
I would like to achieve the fiducial feature “Click to Jump Slices” programmatically. I know how to achieve this for the Red/Green/Yellow <em>offsets</em>, but I would like the slice views to get centered on the fiducial location as well. Here’s how I set the offset:</p>
<pre><code>lm = slicer.app.layoutManager()
# for a point with coordinates x/y/z (floats in mm)
for slice, loc in zip(['Yellow','Green','Red'], [x,y,z]):
    sliceNode = lm.sliceWidget(slice) # can be Red/Yellow
    sliceLogic = sliceNode.sliceLogic()
    sliceLogic.SetSliceOffset(loc)
</code></pre>
<p>Unfortunately, I cannot see sth like “SetSliceCenter” in sliceLogic.<br>
Thx for your help in advance!</p>

---

## Post #2 by @pieper (2020-08-12 21:48 UTC)

<p>You can search the source code for <code>vtkMRMLSliceNode::JumpSliceByCentering</code></p>

---

## Post #3 by @mangotee (2020-08-13 09:32 UTC)

<p>Thank you Steve, that helped a lot. I realized that the sliceNode that I retrieved above was not a sliceNode at all, but actually a widget of class <code>qMRMLSliceWidget</code>. The function <code>JumpSliceByCentering</code> is a method of class <code>vtkMRMLSliceNode</code> though. If somebody else stumbles across this, the code above should be modified. It should <em>not</em> make the slice jump through the widget’s <code>sliceLogic</code>, instead it should read:</p>
<pre><code>lm = slicer.app.layoutManager()
# for a point with coordinates x/y/z (floats in mm)
# (better denoted as r/a/s, as in Slicer source code)
for slice in ['Yellow','Green','Red']:
    sliceNode = lm.sliceWidget(slice).mrmlSliceNode()
    sliceNode.JumpSliceByCentering(x,y,z) # or r,a,s

    # NOTE: in case you only want to offset, not center:
    # sliceNode.JumpSliceByOffsetting(x,y,z) # or r,a,s</code></pre>

---
