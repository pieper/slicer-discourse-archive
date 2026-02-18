# Couldn't not copy segmentation

**Topic ID**: 11375
**Date**: 2020-05-01
**URL**: https://discourse.slicer.org/t/couldnt-not-copy-segmentation/11375

---

## Post #1 by @codecrazer (2020-05-01 06:39 UTC)

<p>I couldn’t copy segmentation, what should I do? Thanks for your help!</p>

---

## Post #2 by @lassoan (2020-05-01 14:52 UTC)

<p>You can clone a segmentation node by right-clicking on it in Data module.</p>

---

## Post #3 by @TMrt (2020-05-03 23:08 UTC)

<p>Hello-once the segmentation node is cloned or copied, can it be moved to another area in the image?<br>
Thank you</p>

---

## Post #4 by @lassoan (2020-05-03 23:24 UTC)

<p>Yes, you can move it anywhere by applying a transform using Transforms module. You can manually adjust a linear transform (translation, rotation, scaling, shearing), but more commonly you determine the transform by automatical registration.</p>
<p>Slicer has many registration methods. If you tell us more about your clinical use case then we can give you more specific advice.</p>

---

## Post #5 by @lassoan (2020-05-04 03:11 UTC)

<p>A post was split to a new topic: <a href="/t/spine-segmentation/11393">Spine segmentation</a></p>

---
