---
topic_id: 31958
title: "What Is The Algorithm Applied To Curve Setting Option"
date: 2023-09-29
url: https://discourse.slicer.org/t/31958
---

# What is the algorithm applied to curve setting option?

**Topic ID**: 31958
**Date**: 2023-09-29
**URL**: https://discourse.slicer.org/t/what-is-the-algorithm-applied-to-curve-setting-option/31958

---

## Post #1 by @dsa934 (2023-09-29 06:27 UTC)

<p>Hi, slicer users,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f320b9f9b04f405140546a109f99c90bd035134.png" alt="image" data-base62-sha1="i9dRlSBBt8t9ixKoqk3RNUM7dyY" width="509" height="242"></p>
<p>Where can I find the implementation part of the above function on github?</p>
<p>I’m trying to create a function where the fiducialNode has a ‘maximum projection distance’ of 1% for the constrain model (some_mesh), but 3d slicer doesn’t seem to have that function.</p>

---

## Post #2 by @Jeff_Zeyl (2023-09-29 14:58 UTC)

<p>SetSurfaceConstraintMaximumSearchRadiusTolerance()</p>
<p>I don’t have my computer to check but I believe this function applied to the markup curve node is related</p>
<p><a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsCurveNode.html#a98aef56e120a5fabf748a1f158880d49" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/main/classvtkMRMLMarkupsCurveNode.html#a98aef56e120a5fabf748a1f158880d49</a></p>

---
