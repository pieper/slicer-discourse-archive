---
topic_id: 27804
title: "Combine Two Models With Some Strange Problems"
date: 2023-02-14
url: https://discourse.slicer.org/t/27804
---

# Combine two models with some strange problems

**Topic ID**: 27804
**Date**: 2023-02-14
**URL**: https://discourse.slicer.org/t/combine-two-models-with-some-strange-problems/27804

---

## Post #1 by @slicer365 (2023-02-14 10:26 UTC)

<p>I creat a model A in SegmentEditor，</p>
<p>then I import a stl file B into slicer and export  A to model ,</p>
<p>then I combine them with vtkAppendPolyData.</p>
<p>I get the model C</p>
<p>However when I import C into another software, magics, it tell me there are two shells.</p>
<p>Why?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d52043147526718d69ee7d545c6403b496f18d77.png" data-download-href="/uploads/short-url/upoOYSh3y1PgoZmTRWsk4rNUeq3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d52043147526718d69ee7d545c6403b496f18d77_2_517x207.png" alt="image" data-base62-sha1="upoOYSh3y1PgoZmTRWsk4rNUeq3" width="517" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d52043147526718d69ee7d545c6403b496f18d77_2_517x207.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d52043147526718d69ee7d545c6403b496f18d77_2_775x310.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d52043147526718d69ee7d545c6403b496f18d77_2_1034x414.png 2x" data-dominant-color="B3B4B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1558×624 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-02-14 16:48 UTC)

<p><code>vtkAppendPolyData</code> just adds the list of points and surfaces together without resolving the geometry, so what you describe makes sense.  Probably you need to cut and combine the surfaces.  Exactly how you do that depends on what features you need to preserve in the data, but one option would be to convert both models to labelmap representation, combine them with logical operations in the segment editor, and then re-mesh to a single polydata.</p>

---

## Post #3 by @mau_igna_06 (2023-02-14 17:51 UTC)

<p>The other option (staying on the surface domain) it’s to use the Combine Models module from the sandbox extension</p>
<p>Hope it helps</p>

---

## Post #4 by @slicer365 (2023-02-14 23:06 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="27804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>vtkAppendPolyData</p>
</blockquote>
</aside>
<p>In fact ,Combine Models is based on the vtkAppendPolyData. Model A is designed by SegmentEditor , Model B is designed by Blender.</p>

---

## Post #5 by @slicer365 (2023-02-14 23:31 UTC)

<p>Thank you for your answer,Mr Pieper,</p>
<p>as you see, it is a standard  rectangle model ,</p>
<p>if I import it into SegmentEditor, add them by Logical tool ,then export Model C ,the shape will be changed， especially the rectangle part</p>

---

## Post #6 by @pieper (2023-02-14 23:43 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="5" data-topic="27804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>shape will be changed</p>
</blockquote>
</aside>
<p>To preserve the original shape you need to do a mesh-based boolean operation.  I don’t do that myself much, but if you search for vtkbool and Slicer you will find a lot of discussion about when it works well and when it may have trouble with meshes.  Maybe someone else can chime in with their experiences.</p>

---

## Post #7 by @lassoan (2023-02-15 05:33 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="4" data-topic="27804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>Combine Models is based on the vtkAppendPolyData</p>
</blockquote>
</aside>
<p>Combine Models module in Sandbox extension does not use vtkAppendPolyData, but it performs proper Boolean operations using vtkbool package. Advantage of this method is that all details of the input meshes are preserved. Disadvantage is that even though vtkbool is a quite robust package, in some special cases it may still fail.</p>
<aside class="quote no-group" data-username="slicer365" data-post="5" data-topic="27804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>if I import it into SegmentEditor, add them by Logical tool ,then export Model C ,the shape will be changed， especially the rectangle part</p>
</blockquote>
</aside>
<p>You can set arbitrarily small spacing as segmentation geometry and then there will be no perceivable shape change. Disadvantage of this method is that memory need and computation time can increase very steeply as you reduce the spacing. The advantage of this method is that it works correctly every time - there are no problematic special cases.</p>

---
