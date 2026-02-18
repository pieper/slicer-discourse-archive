# Markups Plane rotation

**Topic ID**: 34564
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/markups-plane-rotation/34564

---

## Post #1 by @soukup.la (2024-02-27 09:46 UTC)

<p>Hello,<br>
is it possible to rotate a  markups plane around its axes?</p>
<p>best regards<br>
Ladislav</p>

---

## Post #2 by @RafaelPalomar (2024-02-27 11:28 UTC)

<p>Hello <a class="mention" href="/u/soukup.la">@soukup.la</a>. Yes, it is possible. If you right-click in one of the plane points you can enable the rotations in the <code>Interaction options --&gt; Rotate</code> option.</p>

---

## Post #3 by @soukup.la (2024-02-27 11:33 UTC)

<p>Great! Is it possible to make it somehow using Python code?</p>

---

## Post #4 by @RafaelPalomar (2024-02-27 12:39 UTC)

<p>I guess you can always retrieve the points of the plane, do the transforms you need to them and set the new coordinates to  the plane markup in Python. I’m not sure on whether the functionality of the rotation widget is exposed in Python for an easier solutio. Perhaps <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> knows about this?</p>

---

## Post #5 by @Sunderlandkyl (2024-02-27 14:40 UTC)

<p>Yeah, you can enable the rotation handles with SetRotationHandleVisibility:</p>
<pre><code class="lang-auto">planeNode.GetDisplayNode().SetRotationHandleVisibility(True)
</code></pre>

---

## Post #6 by @RafaelPalomar (2024-02-27 14:57 UTC)

<p>I think <a class="mention" href="/u/soukup.la">@soukup.la</a> probably meant to do the rotation directly in python without the markups widgets? Are there any functions in the logic driving these rotations? Thanks for the quick reaction <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #7 by @Sunderlandkyl (2024-02-27 15:11 UTC)

<p>No, there isn’t a logic function for calculating those rotations.</p>
<p>The easiest might be to get the axes with vtkMRMLMarkupsPlaneNode::GetAxes/GetAxesWorld and then use vtkTransform::RotateWXYZ to calculate the rotation around a specific axis.</p>
<p>After that you can just apply the transform with planeNode.ApplyTransform().</p>

---

## Post #8 by @soukup.la (2024-02-28 08:43 UTC)

<p>Thank you very much!</p>

---
