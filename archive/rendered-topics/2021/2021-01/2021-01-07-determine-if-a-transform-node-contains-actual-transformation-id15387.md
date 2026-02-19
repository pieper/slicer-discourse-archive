---
topic_id: 15387
title: "Determine If A Transform Node Contains Actual Transformation"
date: 2021-01-07
url: https://discourse.slicer.org/t/15387
---

# Determine if a transform node contains actual transformation or is identity

**Topic ID**: 15387
**Date**: 2021-01-07
**URL**: https://discourse.slicer.org/t/determine-if-a-transform-node-contains-actual-transformation-or-is-identity/15387

---

## Post #1 by @cpinter (2021-01-07 11:58 UTC)

<p>I wonder if there is a simple way to determine if a transform node is identity or not. The reason why it is not trivial is that such a node can contain a linear transform in which case it is simple, but can also contain various types of deformable transforms, in which case it is not trivial.</p>
<p>So for example if there is a method already existing for this, then I’d appreciate if someone could point it out.</p>
<p>An idea that I have for checking it for deformable transforms is seeing whether the transform and its inverse are the same, but it might take too long for a simple check (in my case it is for determining whether a button should be enabled or not).</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-01-07 16:41 UTC)

<p>The method to determine if a non-linear transform is identity is different for each transform type.</p>
<ul>
<li>linear: compare with slicer.vtkAddonMathUtilities.MatrixAreEqual() to an identity matrix</li>
<li>thin-plate spline: source and target landmark point positions are the same</li>
<li>grid and bspline: coefficient image values are all 0 (minimum and maximum scalar range is 0)</li>
</ul>
<p>You can get the list of transforms in a node using FlattenGeneralTransform and then use the rules above to check if each component is identity.</p>

---

## Post #3 by @cpinter (2021-01-07 16:45 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> ! Would it be useful to have one method in Slicer for this?</p>

---

## Post #4 by @lassoan (2021-01-07 16:53 UTC)

<p>Yes, I it could be useful. You could add them as static functions to vtkTransform class.</p>

---
