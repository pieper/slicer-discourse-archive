---
topic_id: 19880
title: "Adjust Segment Opacity In Segment Editor"
date: 2021-09-27
url: https://discourse.slicer.org/t/19880
---

# Adjust segment opacity in Segment Editor

**Topic ID**: 19880
**Date**: 2021-09-27
**URL**: https://discourse.slicer.org/t/adjust-segment-opacity-in-segment-editor/19880

---

## Post #1 by @Alex_Vergara (2021-09-27 13:43 UTC)

<p>Is there a way to include also the opacity of each segment as you do in the Segments module?<br>
That way you will have visibility, color, opacity, name, flag<br>
It is really tedious to go to Segmentations module just for opacity change</p>

---

## Post #2 by @lassoan (2021-09-27 14:31 UTC)

<p>The segment list can display opacities, but considering how much space is needed by the opacity column and how rarely you need to adjust individual segment opacities it did not seem to worth to show this option.</p>
<p>You can go to Segmentations module by a single button click (the green right arrow button) and get back to Segment Editor by a single click. Have you tried to use this? Is the issue that segment selection is only synchronized when switching from Segmentations to Segment Editor and not in the other direction? That should be easy to fix.</p>
<p>If the two extra clicks are unacceptable then you can submit a pull request with a new feature that allows displaying the opacity column using the context menu (similarly to how the “Layer” column can be displayed).</p>

---

## Post #3 by @Alex_Vergara (2021-09-28 10:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>then you can submit a pull request with a new feature that allows displaying the opacity column using the context menu (similarly to how the “Layer” column can be displayed)</p>
</blockquote>
</aside>
<p>This is genius! I will see what can I do. But this will be the actual solution.</p>

---

## Post #4 by @Alex_Vergara (2021-09-28 11:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but considering how much space is needed by the opacity column</p>
</blockquote>
</aside>
<p>I don’t think space is ever an issue as most Slicer users need a large screen anyways, and by large, these days it means wide enough</p>

---

## Post #5 by @lassoan (2021-09-28 11:23 UTC)

<p>Screen space is an issue on laptops. Also, exposing rarely used features makes the user interface look complex - intimidating new users and making a bit harder than find commonly needed features.</p>

---
