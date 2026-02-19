---
topic_id: 11599
title: "Set And Observe Transform Node To Markups Curve Node Bug Or"
date: 2020-05-18
url: https://discourse.slicer.org/t/11599
---

# Set and observe transform node to markups curve node: bug or feature?

**Topic ID**: 11599
**Date**: 2020-05-18
**URL**: https://discourse.slicer.org/t/set-and-observe-transform-node-to-markups-curve-node-bug-or-feature/11599

---

## Post #1 by @Mik (2020-05-18 11:31 UTC)

<p>Greeting,</p>
<p>Transformation of vtkMRMLMarkupsClosedCurveNode looks like a little bit buggy.  Points of the curve are transformed correctly, but not the curve itself.</p>
<p>There is no such problem with markups line node, where both line and points are transformed correctly.</p>
<p>Code <code>closedCurveNode-&gt;SetAndObserveTransformNodeID(transformNode-&gt;GetID());</code></p>
<p>gives such results<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7240caca3e2318ead746fe1294674800dd672a49.png" data-download-href="/uploads/short-url/giJfnXDUlaVpXcOMT1iLeAbdq4x.png?dl=1" title="Screenshot_Markups1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7240caca3e2318ead746fe1294674800dd672a49.png" alt="Screenshot_Markups1" data-base62-sha1="giJfnXDUlaVpXcOMT1iLeAbdq4x" width="690" height="434" data-dominant-color="010101"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_Markups1</span><span class="informations">968×610 5.04 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af38361d09fe1970807ae575f5256e0c1ea1bdb6.png" data-download-href="/uploads/short-url/p03ZmeKX3z7b0V7BkHPT2rZsPXg.png?dl=1" title="Screenshot_Markups2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af38361d09fe1970807ae575f5256e0c1ea1bdb6_2_690x420.png" alt="Screenshot_Markups2" data-base62-sha1="p03ZmeKX3z7b0V7BkHPT2rZsPXg" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af38361d09fe1970807ae575f5256e0c1ea1bdb6_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af38361d09fe1970807ae575f5256e0c1ea1bdb6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af38361d09fe1970807ae575f5256e0c1ea1bdb6.png 2x" data-dominant-color="9A9DD2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_Markups2</span><span class="informations">1000×610 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2020-05-18 15:11 UTC)

<p>Thanks for reporting this, I’ll take a look at it.</p>

---

## Post #3 by @lassoan (2020-05-18 17:12 UTC)

<p><a class="mention" href="/u/mik">@mik</a> Can you reproduce the problem with the latest Slicer Preview Release?</p>

---

## Post #4 by @Mik (2020-05-18 19:54 UTC)

<p>Build from the source, the problem remains.</p>
<p>Slicer 4.11.0-2020-05-14 r29057 / 0bc7cb1</p>
<p>curve node without transformation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d274fcf01af6ec73c270caf961186a35ad4eb097.png" data-download-href="/uploads/short-url/u1MUHnE26GbnDx3ZTv51Ad1uZnh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d274fcf01af6ec73c270caf961186a35ad4eb097_2_690x289.png" alt="image" data-base62-sha1="u1MUHnE26GbnDx3ZTv51Ad1uZnh" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d274fcf01af6ec73c270caf961186a35ad4eb097_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d274fcf01af6ec73c270caf961186a35ad4eb097_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d274fcf01af6ec73c270caf961186a35ad4eb097_2_1380x578.png 2x" data-dominant-color="B2B4DC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1686×708 44.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>curve node with transformation (points and curve are separated)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fb6f1a9060edb856f02aaa6cdd3026130ec05c1.png" data-download-href="/uploads/short-url/bnbFTX7uaHkA1KGQt0vf0vbV9Bv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fb6f1a9060edb856f02aaa6cdd3026130ec05c1_2_690x282.png" alt="image" data-base62-sha1="bnbFTX7uaHkA1KGQt0vf0vbV9Bv" width="690" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fb6f1a9060edb856f02aaa6cdd3026130ec05c1_2_690x282.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fb6f1a9060edb856f02aaa6cdd3026130ec05c1_2_1035x423.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fb6f1a9060edb856f02aaa6cdd3026130ec05c1_2_1380x564.png 2x" data-dominant-color="B1B4DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1734×709 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Sunderlandkyl (2020-05-20 14:19 UTC)

<p>I’ve made a fix, could you try the latest version of Slicer?</p>

---

## Post #6 by @lassoan (2020-05-20 15:18 UTC)

<p>The fix will be included in Slicer Preview Release that you download tomorrow or later.</p>

---

## Post #7 by @Mik (2020-05-20 20:05 UTC)

<p>Thank you, the major problem has been fixed.</p>
<p>I have one more minor issue with markups node. How to update markups data in loadable module correctly?</p>
<p>I have markups node with four points (rectangle). When i update markups control point position <a href="https://github.com/MichaelColonel/SlicerRT/blob/drr/PlmDrr/Logic/vtkSlicerPlmDrrLogic.cxx#L246-#L290" rel="nofollow noopener">the code</a> the point change it position, but not the curve.</p>
<p>The have found the solution by removing node and creating it with a new positions.</p>

---

## Post #8 by @lassoan (2020-05-20 20:33 UTC)

<p>Can you send a link to the code lines where you set the control point positions?</p>

---

## Post #9 by @Mik (2020-05-21 05:23 UTC)

<p>Here is a <a href="https://github.com/MichaelColonel/SlicerRT/blob/drr/PlmDrr/Logic/vtkSlicerPlmDrrLogic.cxx#L435-#L486" rel="nofollow noopener">method</a>, which creates a curve node, other curve nodes use the same technique.</p>

---

## Post #10 by @Sunderlandkyl (2020-05-21 14:32 UTC)

<p>I made the following snippet based on the code from the CreateImagerBoundary function, but it doesn’t seem to cause the issue:</p>
<pre><code class="lang-auto">c = slicer.vtkMRMLMarkupsClosedCurveNode()
slicer.mrmlScene.AddNode(c)
c.SetCurveTypeToLinear()
c.SetHideFromEditors(1)
c.AddControlPoint(vtk.vtkVector3d(0.0, 0.0, 0.0))
c.AddControlPoint(vtk.vtkVector3d(1.0, 0.0, 0.0))
c.AddControlPoint(vtk.vtkVector3d(1.0, 1.0, 0.0))
c.AddControlPoint(vtk.vtkVector3d(0.0, 1.0, 0.0))
</code></pre>

---

## Post #11 by @Mik (2020-05-21 15:47 UTC)

<p>What would happen if you modify a z coordinate of each point and try to update a curve node? Will the curve change it position as well, not just control points?</p>
<p>Static curve is not a problem anymore, thanks to your fix, but in GUI i have a slider which change z coordinates of the curve and only control points move.</p>

---

## Post #12 by @lassoan (2020-05-24 14:46 UTC)

<p>Updating a control point position updates the curve correctly. For example, this code updates first point of curve “C” correctly (point and curve are both updated):</p>
<pre><code class="lang-python">c = getNode('C')
p = [0,0,0]
c.GetNthControlPointPosition(0, p)
p[2] = p[2] + 10
c.SetNthControlPointPosition(0, *p)
</code></pre>

---

## Post #13 by @Mik (2020-05-25 14:52 UTC)

<p>Thank you!</p>
<p>After some trials and errors, i have found the code</p>
<p><code>double p[3];</code><br>
<code>imagerMarkupsNode-&gt;GetNthControlPointPosition( 0, p);</code><br>
<code>p[2] = value</code><br>
<code>imagerMarkupsNode-&gt;Modified()</code></p>
<p>didn’t work, but code</p>
<p><code>double p[3];</code><br>
<code>imagerMarkupsNode-&gt;GetNthControlPointPosition( 0, p);</code><br>
<code>p[2] = value</code><br>
<code>imagerMarkupsNode-&gt;SetNthControlPointPosition( 0, p[0], p[1], p[2]);</code></p>
<p>works as it should.</p>
<p>The topic is closed.</p>

---

## Post #14 by @lassoan (2020-05-25 14:56 UTC)

<aside class="quote no-group" data-username="Mik" data-post="13" data-topic="11599">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p><code>double p[3];</code><br>
<code>imagerMarkupsNode-&gt;GetNthControlPointPosition( 0, p);</code><br>
<code>p[2] = value</code><br>
<code>imagerMarkupsNode-&gt;Modified()</code></p>
</blockquote>
</aside>
<p>Would you recommend to make any changes to the documentation to clarify that no permanent synchronization mechanism is created between the input Python array and a markups node when you call GetNthControlPointPosition?</p>

---

## Post #15 by @Mik (2020-05-26 16:09 UTC)

<p>It will good to have a some kind of warning about such feature, and something like:</p>
<p>Warning: In order to update position of markups as well as a curve, one always must use <code>SetNthControlPointPosition</code> method.</p>

---
