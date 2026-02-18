# Segment editor: Draw does not work if master volume and segmentation are under a linear transform

**Topic ID**: 6352
**Date**: 2019-04-01
**URL**: https://discourse.slicer.org/t/segment-editor-draw-does-not-work-if-master-volume-and-segmentation-are-under-a-linear-transform/6352

---

## Post #1 by @stephan (2019-04-01 13:54 UTC)

<p>Version: 4.10.1 (Windows 10)<br>
Expected behavior: A segmentation and its master volume are under the same linear transform. When using the draw effect to segment, the segment appears where it is drawn (just like it does with the paint effect).<br>
Actual behavior: As opposed to the paint effect, drawing seems not to take into account the transform. So the segment is actually drawn somewhere else.</p>

---

## Post #2 by @cpinter (2019-04-02 21:13 UTC)

<p>Thanks for the report, I was able to reproduce it. I created a Mantis issue for this with high priority: <a href="https://issues.slicer.org/view.php?id=4685" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4685</a></p>

---

## Post #3 by @lassoan (2019-04-03 01:04 UTC)

<p>Until the bug is fixed, as a workaround, you can place the segmentation node under the same transform as the master volume (or harden the transform on the nodes).</p>

---

## Post #4 by @stephan (2019-04-03 02:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="6352">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Until the bug is fixed, as a workaround, you can place the segmentation node under the same transform as the master volume</p>
</blockquote>
</aside>
<p>Thanks for the follow-up, <a class="mention" href="/u/lassoan">@lassoan</a><br>
Just to clarify: What you describe is actually the situation in which I first noticed this bug: Both the master volume and the segmentation were under the same linear transformation while I tried to draw.</p>
<p>As a workaround I simply removed the transform from both of them, performed the segmentation, and placed them under the transform again. So this is not a disruptive bug at all, but I thought I report it anyway.</p>

---
