# Automatic paint tool along curve

**Topic ID**: 25800
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/automatic-paint-tool-along-curve/25800

---

## Post #1 by @bserrano (2022-10-20 07:36 UTC)

<p>Hello,</p>
<p>I want to implement a paint tool that can automatically follow a path so I can set the radius and threshold and get the segmentation from the beginning to the end of the curve. Can anyone give some idea how to do it?</p>
<p>Thanks,</p>

---

## Post #2 by @pieper (2022-10-20 13:13 UTC)

<p>With some python scripts you can do that.  You could look at the Endoscopy module and the Segment Editor code to find the logic parts you would need.  Tracing along a curve with threshold painting could be a good way to segment faint vessels.</p>

---

## Post #3 by @chir.set (2022-10-20 13:21 UTC)

<p>You may have a look  at the ‘Curve centerline extraction’ module in SlicerVMTK extension, that you can install from the ‘Extension manager’. It segments along a curve using ‘Flood filling’ and not ‘Paint’ tool. You can specify the radius, and tune the intensity range until you get a satisfactory result. Very poorly contrasted vessels may be out of scope though.</p>

---

## Post #4 by @lassoan (2022-10-20 14:45 UTC)

<p>Filling a segment around a curve with a specified radius is already available in the “Draw tube” effect in Segment Editor, after you install “SegmentEditorExtraEffects” extension.</p>

---

## Post #5 by @bserrano (2022-10-20 15:08 UTC)

<p>Thanks.<br>
But we are interested in adjust radius and intensity in each point given some conditions. Maybe the easiest way to do it is modify “Draw tube” code?</p>

---

## Post #6 by @chir.set (2022-10-20 15:32 UTC)

<p>Sample images would be helpful.</p>

---

## Post #7 by @lassoan (2022-10-20 15:50 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="5" data-topic="25800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>But we are interested in adjust radius and intensity in each point given some conditions. Maybe the easiest way to do it is modify “Draw tube” code?</p>
</blockquote>
</aside>
<p>What would you like to achieve? Generate a vascular network? Would you like to get a surface mesh or synthetic CT as output? Where do the input curves come from?</p>

---

## Post #8 by @bserrano (2022-10-21 10:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="25800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Generate a vascular network?</p>
</blockquote>
</aside>
<p>Yes, we want to generate vessels having in count the curve points neighbourhood, so we can adjust parameters like radius or threshold.<br>
Pseudocode may look like:</p>
<pre><code class="lang-auto">curve = MarkupsCurve(...)
for point in curve:
      radius = adjustRadius(point)
      threshold = adjustThreshold(point)
      applyPaint(point, radius, threshold)
</code></pre>
<p>We want a segment as output.</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
