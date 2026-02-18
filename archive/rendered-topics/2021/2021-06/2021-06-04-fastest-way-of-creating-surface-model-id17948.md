# Fastest way of creating surface model?

**Topic ID**: 17948
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/fastest-way-of-creating-surface-model/17948

---

## Post #1 by @jumbojing (2021-06-04 12:47 UTC)

<p>In my slicer plugin, I need to model the bones and skin in the ROI and make a model. I used <a class="mention" href="/u/lassoan">@lassoan</a>’s <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="noopener nofollow ugc">extract skin surface</a> method , But the speed is a bit slow, is there a faster method? In fact, I only need the back surface, is there a faster and more effective method?</p>
<details>
<summary>
translated from original</summary>
<p>在我开发slicer插件中,需要对ROI中的骨骼和皮肤建模,做出model,我用了@lassoan 的<a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="noopener nofollow ugc">extract skin surface</a> 的方法,可是速度有点慢,有没有更快的方法呢?其实我只需要后表面,有没有更快,更有效的方法呢?</p>
</details>

---

## Post #2 by @lassoan (2021-06-04 13:41 UTC)

<p>There are many ways to do this. What is the clinical application? How the segmentation will be used? What are your time and accuracy constraints?</p>

---

## Post #3 by @jumbojing (2021-06-04 17:11 UTC)

<p>I only need, for example, the back surface of the vertebral body. I want to use the <a href="https://pyscience.wordpress.com/2014/09/21/ray-casting-with-python-and-vtk-intersecting-linesrays-with-surface-meshes/" rel="noopener nofollow ugc">Ray Casting</a> function to determine the bone entry point of pedicle puncture.</p>
<details>
<summary>
translated from original</summary>
<p>我只需要比如椎体的后表面,我想借助<a href="https://pyscience.wordpress.com/2014/09/21/ray-casting-with-python-and-vtk-intersecting-linesrays-with-surface-meshes/" rel="noopener nofollow ugc">Ray Casting</a>函数来确定椎弓根穿刺的入骨点.</p>
</details>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31891794fd0811656b69af144019b8e26cf7f83c.jpeg" alt="image" data-base62-sha1="74d76msB4KGRWEEtsvRxqNjpzic" width="333" height="466"></p>

---

## Post #4 by @jumbojing (2021-06-04 17:20 UTC)

<p>I used the method of reducing the volume, and it seems to be effective… Is there a better way? For example, is there a way to make a model in a cylinder?</p>
<details>
<summary>
translated from original</summary>
<p>我用了缩小体积的方法,似乎有效…是不是还有更好的方法呢?比如有没有一个方法,在一个圆柱里里面建模呢?</p>
</details>

---

## Post #5 by @lassoan (2021-06-04 23:47 UTC)

<p>If you need intersection point of a line and a surface mesh then you can <a href="https://vtk.org/doc/nightly/html/classvtkCellLocator.html#a18c5f9154bc37cdb9654c55050c25da3">IntersectWithLine</a> method of cell locators.</p>
<p>To get intersection of a line with a volume, you can compute a line profile (probe the image with a line) using “Line Profile” module in Sandbox extension; or you can implement yourself using vtkProbeFilter. You can then find the intersection point by finding the point where the voxel value goes above a chosen threshold value.</p>
<p>I would recommend to use/extend/customize the <a href="https://github.com/lassoan/PedicleScrewSimulator">PedicleScrewSimulator</a> extension.</p>

---

## Post #6 by @jumbojing (2021-06-05 11:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="17948">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>vtkProbeFilter</p>
</blockquote>
</aside>
<p>Perfect solution, thank you teacher! ! Use vtkProbeFilter</p>
<details>
<summary>
translated from original</summary>
<p>完美解决,谢谢老师!!用vtkProbeFilter</p>
</details>

---
