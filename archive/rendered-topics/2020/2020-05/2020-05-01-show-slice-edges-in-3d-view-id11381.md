---
topic_id: 11381
title: "Show Slice Edges In 3D View"
date: 2020-05-01
url: https://discourse.slicer.org/t/11381
---

# Show slice edges in 3D view

**Topic ID**: 11381
**Date**: 2020-05-01
**URL**: https://discourse.slicer.org/t/show-slice-edges-in-3d-view/11381

---

## Post #1 by @lassoan (2020-05-01 19:14 UTC)

<p>Most medical image viewer software uses color coding to make it easier to distinguish slices in  3D  views. It would not be hard to do (you can try by copy-pasting a few lines of code into the Python console).</p>
<details>
<summary>
Code snippet to show slice edges</summary>
<pre data-code-wrap="python"><code class="lang-python">for sliceNode in getNodesByClass("vtkMRMLSliceNode"):
    sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
    displayNode = sliceLogic.GetSliceModelNode().GetDisplayNode()
    displayNode.SetEdgeColor(sliceNode.GetLayoutColor())
    displayNode.SetEdgeVisibility(True)
    displayNode.SetLineWidth(3)
</code></pre>
</details>
<p>Should we do it, too?</p>
<p>My concern would be that it may make the views a bit too busy:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1a672ba2b6f39a766975b4a5550c2296940b1db.jpeg" data-download-href="/uploads/short-url/rD6LrTfnJVcvvf8QWIORlJfORTR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a672ba2b6f39a766975b4a5550c2296940b1db_2_580x499.jpeg" alt="image" data-base62-sha1="rD6LrTfnJVcvvf8QWIORlJfORTR" width="580" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a672ba2b6f39a766975b4a5550c2296940b1db_2_580x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a672ba2b6f39a766975b4a5550c2296940b1db_2_870x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a672ba2b6f39a766975b4a5550c2296940b1db_2_1160x998.jpeg 2x" data-dominant-color="75747B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1437×1238 458 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It might be particularly confusing when the displayed image is smaller than the frame (this happens most of the case):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d85d37cf479516c564217d415f201f41dd67b69.jpeg" data-download-href="/uploads/short-url/mtvGplaX2EsokcDtCz49n8CyJ8R.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d85d37cf479516c564217d415f201f41dd67b69_2_522x500.jpeg" alt="image" data-base62-sha1="mtvGplaX2EsokcDtCz49n8CyJ8R" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d85d37cf479516c564217d415f201f41dd67b69_2_522x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d85d37cf479516c564217d415f201f41dd67b69_2_783x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d85d37cf479516c564217d415f201f41dd67b69_2_1044x1000.jpeg 2x" data-dominant-color="4E4E53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1289×1234 354 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It could be possible to set the boundary of the slice view to match the background volume boundaries, but it would be a bit more work and could be a bit confusing when we display other content, such as markups or segmentations (which are displayed over the entire slice, not over only the background volume).</p>
<p><strong>Should we show slice view edges in 3D views?</strong></p>

---

## Post #2 by @pieper (2020-05-01 19:48 UTC)

<p>I like it.  Perhaps they could be something like 30% opacity so they aren’t so busy.  We would just need to add a <code>SetEdgeOpacity</code> method to the display node and tweak the displayable manager.  Of course once we can see them it would also be tempting to make the widgets so you could manipulate the slices from the 3D view.</p>

---

## Post #3 by @rkikinis (2020-05-01 20:10 UTC)

<p>I like it too.</p>
<p>How about adding the ability to turn them on and off from the control panel of the slice viewer.</p>
<p>Ron</p>

---

## Post #4 by @lassoan (2020-05-01 20:42 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="11381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Of course once we can see them it would also be tempting to make the widgets so you could manipulate the slices from the 3D view</p>
</blockquote>
</aside>
<p>I had the same temptation, too. It would make sense, we could move it, maybe rotate it, have a right-click menu to hide it, etc. Unfortunately, it would be quite a bit of more work.</p>

---

## Post #5 by @Davide_Punzo (2024-10-25 09:32 UTC)

<p>PR <a href="https://github.com/Slicer/Slicer/pull/8008" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add option to display slice edges in 3D view by Punzo · Pull Request #8008 · Slicer/Slicer · GitHub</a> address this feature. Feedback would be very welcome <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">, thanks!</p>

---
