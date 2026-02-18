# How to judge whether the order of 2 groups of points in 3D space has changed in space?

**Topic ID**: 24826
**Date**: 2022-08-19
**URL**: https://discourse.slicer.org/t/how-to-judge-whether-the-order-of-2-groups-of-points-in-3d-space-has-changed-in-space/24826

---

## Post #1 by @jumbojing (2022-08-19 05:00 UTC)

<p>As shown in the figure below, the points of the closed curve on the left are arranged counterclockwise. The open curve on the right has a change in the order of points in the square. The two groups of points are two-dimensional np.array with the point number as the index.  : How to judge that the group of points on the right has changed in spatial order?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae10a4d68e87d50ebf10be6ac7e49404c23270e4.jpeg" data-download-href="/uploads/short-url/oPQJPFgkxAqtBUdg5FzfXVgnRru.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae10a4d68e87d50ebf10be6ac7e49404c23270e4_2_690x425.jpeg" alt="image" data-base62-sha1="oPQJPFgkxAqtBUdg5FzfXVgnRru" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae10a4d68e87d50ebf10be6ac7e49404c23270e4_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae10a4d68e87d50ebf10be6ac7e49404c23270e4_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae10a4d68e87d50ebf10be6ac7e49404c23270e4_2_1380x850.jpeg 2x" data-dominant-color="B2BCC5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1616×996 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2022-08-19 06:35 UTC)

<p>If the point ordering outside the square remains constant, the first suggestion coming to mind is to compare distances along the curve between points inside and outside the square. If point 11 is closer to point 1 than point 10, you may know that point 11 is not in sequential ordering.</p>

---

## Post #3 by @jumbojing (2022-08-19 17:33 UTC)

<p><a href="https://drive.google.com/file/d/1EOMU-DaOfTugBsR5aa1ciot6WwLpBNIq/view?usp=sharing" rel="noopener nofollow ugc">The left points</a> and <a href="https://drive.google.com/file/d/1EOCaqFQMFjFNXC83aBXSuC3StNqI0o9A/view?usp=sharing" rel="noopener nofollow ugc">the right points</a></p>

---

## Post #4 by @chir.set (2022-08-20 07:55 UTC)

<ol>
<li>
<p>The problem to solve has changed. You declared open and closed curves in your OP. The markups files that you post are Fiducial ones.</p>
</li>
<li>
<p>How does ordering of points change ? By code that is controlled by the developer ? By user UI actions ?</p>
</li>
<li>
<p>How is ordering of points relevant for a Fiducial node ?</p>
</li>
</ol>
<p>It’s hard to <em>try</em> solving a vaguely posed problem, the more so if it’s dangling.</p>

---

## Post #5 by @jumbojing (2022-08-21 14:30 UTC)

<p>这个问题困惑了我好久–就是如何判断表面是否闭合, 尝试过一些方法都不理想, 后来我发现生成的点云的顺序在闭合时,按一定方向(这里是顺时针)规律排布, 而非闭合时, 其空间顺序发生了改变, 所以就有了上面👆🏻这个问题</p>
<blockquote>
<p>This question has puzzled me for a long time - how to judge whether the surface is closed…I have tried some methods, but none of them are ideal.Later, I found that the order of the generated point clouds is arranged in a certain direction (clockwise here) when it is closed, but when it is not closed, its spatial order has changed, so there is the above problem <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">.<br>
<a href="https://discourse.slicer.org/t/how-to-extract-the-vertex-coordinates-of-a-polygon-of-a-model-in-the-current-section/24380">How to extract the vertex coordinates of a polygon of a model in the current section?</a><br>
<a href="https://discourse.slicer.org/t/how-to-judge-a-curve-model-obtained-with-vtkplanecut-or-vtkcutter-is-closed/24470">How to judge a curve model obtained with vtkplanecut or vtkcutter is closed?</a></p>
</blockquote>

---

## Post #6 by @jumbojing (2022-08-21 14:34 UTC)

<p>昨天我搞出了一个函数,计算每个点相对于质心和初始点的夹角…如果按照夹角的角度排序, ‘闭合’状态顺序不变, 顺序发生改变就是非’闭合’.</p>
<blockquote>
<p>Yesterday I came up with a function that calculates the included angle of each point relative to the center of mass and the initial point… If you sort by the angle of the included angle, the order of the ‘closed’ state remains the same, and if the order changes, it is not ‘closed’.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687aa62446bd1118ca82e2c2f53f3db81e500f6a.png" data-download-href="/uploads/short-url/eUgqJrOiePhRBHIvZObhoualXnQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687aa62446bd1118ca82e2c2f53f3db81e500f6a_2_332x500.png" alt="image" data-base62-sha1="eUgqJrOiePhRBHIvZObhoualXnQ" width="332" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687aa62446bd1118ca82e2c2f53f3db81e500f6a_2_332x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687aa62446bd1118ca82e2c2f53f3db81e500f6a_2_498x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687aa62446bd1118ca82e2c2f53f3db81e500f6a_2_664x1000.png 2x" data-dominant-color="9C91C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">714×1074 84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7c0ae5ccc7c53298e4b418019aadf62b413925e.png" data-download-href="/uploads/short-url/qdyc3ttQTyfZEC2zY7gDNR41ZJI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7c0ae5ccc7c53298e4b418019aadf62b413925e_2_388x500.png" alt="image" data-base62-sha1="qdyc3ttQTyfZEC2zY7gDNR41ZJI" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7c0ae5ccc7c53298e4b418019aadf62b413925e_2_388x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7c0ae5ccc7c53298e4b418019aadf62b413925e_2_582x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7c0ae5ccc7c53298e4b418019aadf62b413925e_2_776x1000.png 2x" data-dominant-color="A199CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">878×1130 75.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
