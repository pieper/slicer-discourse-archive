---
topic_id: 25896
title: "How To Rotate Or Change Orientation Of Plane Node"
date: 2022-10-25
url: https://discourse.slicer.org/t/25896
---

# How to rotate or change orientation of plane node

**Topic ID**: 25896
**Date**: 2022-10-25
**URL**: https://discourse.slicer.org/t/how-to-rotate-or-change-orientation-of-plane-node/25896

---

## Post #1 by @seanchoi0519 (2022-10-25 13:31 UTC)

<p>Hello,</p>
<p>Sorry if this is a dumb question!</p>
<p>Once I’ve set the origin and axes of my newly created plane node, how can I change the orientation of the plane? Is there a way to simply initialize it with initial orientation parameter or do I need to apply a transform using linear algebra?</p>
<p>Programmatically please.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @Sunderlandkyl (2022-10-25 14:54 UTC)

<p>If you only care about the normal direction, you can initialize the orientation with the plane using SetNormal/SetNormalWorld.</p>
<p>You can also define the orientation matrix of the plane directly using:</p>
<pre><code class="lang-python">orientationMatrix = vtk.vtkMatrix4x4()
#... update orientation matrix
planeNode.GetObjectToBaseMatrix().DeepCopy(orientationMatrix)
</code></pre>

---
