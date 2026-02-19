---
topic_id: 6887
title: "Curvature Analysis"
date: 2019-05-22
url: https://discourse.slicer.org/t/6887
---

# Curvature Analysis

**Topic ID**: 6887
**Date**: 2019-05-22
**URL**: https://discourse.slicer.org/t/curvature-analysis/6887

---

## Post #1 by @stevenagl12 (2019-05-22 18:59 UTC)

<p>I know that 3D Slicer utilizes VTK, is there any modules, or directions out there with python to be able to color a model based off from the curvature value of the surface? I know VTK has an implementation of this here: <a href="https://lorensen.github.io/VTKExamples/site/Python/PolyData/CurvaturesDemo/" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Python/PolyData/CurvaturesDemo/</a>, but it’s a little complicated and I am trying to go for something more straight forward?</p>

---

## Post #2 by @lassoan (2019-05-22 19:54 UTC)

<p>We are adding these kind of simple metrics to markups curves, but it may take up to a few more months to get there. If you need it sooner then you can temporarily use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CurveMaker" rel="nofollow noopener">CurveMaker</a> module.</p>

---

## Post #3 by @stevenagl12 (2019-05-22 21:41 UTC)

<p>The CurveMaker doesn’t seem to be able to perform any curvature analysis on an object, unless I’m wrong?</p>

---

## Post #4 by @pieper (2019-05-22 21:54 UTC)

<p>We don’t have anything built in for curvature display, but it should be pretty easy to set up a vtk pipeline to that adds the scalars and set up Slicer to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Models#Panels_and_their_use" rel="nofollow noopener">display it on a model</a>.  Of course you’ll need to learn some vtk in order to do that.</p>

---

## Post #5 by @lassoan (2019-05-22 22:03 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="3" data-topic="6887">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>curvature analysis on an object,</p>
</blockquote>
</aside>
<p>CurveMaker is only for curves. The VTK example that you have found is a complete guide of how to compute it for surfaces. You can then use Slicer for showing it as point or cell scalar, as <a class="mention" href="/u/pieper">@pieper</a> suggested above.</p>

---
