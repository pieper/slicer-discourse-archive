---
topic_id: 22003
title: "How To Find Out If A Point Is Inside Or Outside A 3D Model"
date: 2022-02-16
url: https://discourse.slicer.org/t/22003
---

# How to find out if a point is inside or outside a 3d model?

**Topic ID**: 22003
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/how-to-find-out-if-a-point-is-inside-or-outside-a-3d-model/22003

---

## Post #1 by @jumbojing (2022-02-16 19:35 UTC)

<p>how to find out if a point is inside or outside  3d model?</p>
<p>我在网上查到有个用raycasting的交点的奇数和偶数来判断,…在Slicer里有没有特殊的方法呢?</p>
<p>I found on the Internet that there is a use of raycasting to judge the odd and even numbers of the intersection points… but I want to know are there some special methods in Slicer?</p>

---

## Post #2 by @lassoan (2022-02-18 04:52 UTC)

<p>The simplest is to use <code>vtkImplicitPolyDataDistance</code>, as it is shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-distance-of-points-from-surface">this example</a>. It may struggle (can be slow and unreliable) if the mesh is complex or has errors.</p>
<p>The fastest and most robust method is to convert the model to a labelmap (by importing to segmentation and exporting to labelmap) and then check if the voxel corresponding to the probed position is inside the volume and has non-zero label value.</p>

---

## Post #3 by @jumbojing (2022-02-19 03:39 UTC)

<p>谢谢老师, 我也是这么想的, 就是通过segmentation染色model, 然后通过位置点的颜色判断这个点是否为model的一部分,老师有没有script的示例呢?</p>
<blockquote>
<p>Thank you, teacher, I think so too, that is to dye the model through segmentation, and then judge whether the point is part of the model by the color of the position point. Does the teacher have an example of script?</p>
</blockquote>

---

## Post #4 by @lassoan (2022-02-19 04:01 UTC)

<p>Probably the simplest is to ask the displayable managers, for example this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-segments-visible-at-a-selected-position">example script</a> shows how to check if a position is inside a segment.</p>

---

## Post #5 by @jumbojing (2022-02-19 04:16 UTC)

<p>但是, 我想问的问题是"内"和"外",如果model内部有空隙, 而这个点正好位于其中,用这个方法会判断为"外"…</p>
<blockquote>
<p>However, the question I want to ask is “inside” and “outside”. If there is a gap inside the model, and this point is located in it, it will be judged as “outside” by this method…</p>
</blockquote>

---

## Post #6 by @lassoan (2022-02-19 05:15 UTC)

<p>You can fill internal holes in a segmentation using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>.</p>

---

## Post #7 by @jumbojing (2022-02-19 07:48 UTC)

<p>Thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=12" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @jumbojing (2022-03-04 09:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22003">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The fastest and most robust method is to convert the model to a labelmap (by importing to segmentation and exporting to labelmap) and then check if the voxel corresponding to the probed position is inside the volume and has non-zero label value.</p>
</blockquote>
</aside>
<p>这个方法确实不错, 可我还是不知道该怎么做…</p>
<blockquote>
<p>This method is really good, but I still don’t know how to do it…</p>
</blockquote>

---

## Post #9 by @mikebind (2022-03-04 16:43 UTC)

<p>Open the “Segmentations” module and go down the “Export/import mdels and labelmaps” section.  Choose “Import” and “Models”, and select the model you want to convert as the “Input node”.  Then press the “Import” button.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a51d1da3d8281294fe5dcfd4e47e11372892e1.png" data-download-href="/uploads/short-url/iMAiNoeplGN5dCbZZTLgZCxWEPD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a51d1da3d8281294fe5dcfd4e47e11372892e1_2_433x499.png" alt="image" data-base62-sha1="iMAiNoeplGN5dCbZZTLgZCxWEPD" width="433" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a51d1da3d8281294fe5dcfd4e47e11372892e1_2_433x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a51d1da3d8281294fe5dcfd4e47e11372892e1_2_649x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a51d1da3d8281294fe5dcfd4e47e11372892e1_2_866x998.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1140×1315 44.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This will create a new segment in the segmentation corresponding to the interior of your model.  You can then export that to a new labelmap by using the same section of the Segmentations module; just choose “Export” and “Labelmap” instead of import and models, and then click the “Export” button (leaving “Export to new labelmap” selected as the “Output node”).</p>

---
