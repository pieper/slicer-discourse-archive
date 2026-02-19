---
topic_id: 27104
title: "How To Measure The Boundary Ct Value Of A Circular Section"
date: 2023-01-08
url: https://discourse.slicer.org/t/27104
---

# How to measure the boundary CT value of a circular section?

**Topic ID**: 27104
**Date**: 2023-01-08
**URL**: https://discourse.slicer.org/t/how-to-measure-the-boundary-ct-value-of-a-circular-section/27104

---

## Post #1 by @jumbojing (2023-01-08 01:15 UTC)

<details>
<summary>
Chinese</summary>
<p>如图👇: 我想测量在椎弓根内的圆柱体某个截面的边界(骨和圆柱的接触界面)的CT值, 怎么做呢?</p>
</details>
<p>As shown in figure <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">:  I want to measure the CT value of the boundary (the contact interface between the bone and the cylinder) of a certain section of the cylinder in the vertebral pedicle. What should I do?</p>
<details>
<summary>
Chinese</summary>
<p>我曾经尝试通过测量截面圆上每个点的voxel之和来测量, 可是这样似乎不能反映周长与CT值之间的关系, (我是说, 圆柱体创建时如果seg相等的情况下).</p>
</details>
<p>I once tried to measure by measuring the sum of voxels of each point on the section circle, but this does not seem to reflect the relationship between the circumference and the CT value (I mean, if the <code>SetResolution</code> are equal when the 'vtk.vtkCylinderSource()` is created.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/522a0cfc3f4c2680cb1f9e3e60f1657f0c2a68be.jpeg" data-download-href="/uploads/short-url/bIRfeZWUFDk6uD06B6kyqNGXMse.jpeg?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/522a0cfc3f4c2680cb1f9e3e60f1657f0c2a68be_2_570x499.jpeg" alt="图片" data-base62-sha1="bIRfeZWUFDk6uD06B6kyqNGXMse" width="570" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/522a0cfc3f4c2680cb1f9e3e60f1657f0c2a68be_2_570x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/522a0cfc3f4c2680cb1f9e3e60f1657f0c2a68be.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/522a0cfc3f4c2680cb1f9e3e60f1657f0c2a68be.jpeg 2x" data-dominant-color="595753"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">655×574 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/juicy">@Juicy</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @lassoan (2023-01-08 03:25 UTC)

<p>This feature (bone density measurement at the pedicle screw surface) is implemented in the final step of the <a href="https://github.com/lassoan/PedicleScrewSimulator">Pedicle Screw Planner extension</a>.</p>

---

## Post #3 by @jumbojing (2023-01-08 03:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="27104" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This feature (bone density measurement at the pedicle screw surface) is implemented in the final step of the <a href="https://github.com/lassoan/PedicleScrewSimulator" rel="noopener nofollow ugc">Pedicle Screw Planner extension </a>.</p>
</blockquote>
</aside>
<details>
<summary>
Chinese</summary>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">这个测量骨密度的方法, 获得的CT值似乎也是根据模特上的点来, 比如一个截面圆(正6边形)只有6个点, 无论直径多大, 都只是取6个点是这样吗?</p>
</details>
<p>It seems that the CT value obtained by "bone density measurement at the pedicle screw surface"<img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> is also based on the (<code>vtkPolyData</code>)  points on the model. For example, a cross section circle (regular hexagon) has only 6 points. No matter how large the diameter is, are only 6 points taken?</p>

---

## Post #4 by @jumbojing (2023-01-08 04:02 UTC)

<details>
<summary>
Chinese</summary>
<p>骨和螺钉界面面积和螺钉的固定强度相关, 所以我是想获取截面圆周边上的所有像素之和, 怎么做呢?</p>
</details>
<p>The interface area between bone and screw is related to the fixation strength of screw, so I want to get the sum of all pixels (not density <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">) around the section circle. What should I do?</p>

---

## Post #5 by @lassoan (2023-01-08 04:17 UTC)

<aside class="quote no-group quote-modified" data-username="jumbojing" data-post="3" data-topic="27104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>t seems that the CT value obtained by “bone density measurement at the pedicle screw surface”<img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> is also based on the (<code>vtkPolyData</code>) points on the model. For example, a cross section circle (regular hexagon) has only 6 points. No matter how large the diameter is, are only 6 points taken?</p>
</blockquote>
</aside>
<p>You can use Surface Toolbox uniform remesh feature to ensure that the points are representative for the entire screw surface.</p>
<aside class="quote no-group" data-username="jumbojing" data-post="4" data-topic="27104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>The interface area between bone and screw is related to the fixation strength of screw, so I want to get the sum of all pixels (not density <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">) around the section circle. What should I do?</p>
</blockquote>
</aside>
<p>You can compute the sum by multiplying the average value by the number of points. However, this will not be representative of the fixation strength. Multiplying by the surface area may be more meaningful. However, you cannot ignore the distribution of the bone density (very high density in one region cannot compensate for lack of density in another region), so probably you need a metric that evaluates the density along the length of the screw (as it is done in Pedicle Screw Planner extension).</p>

---
