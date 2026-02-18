# Disable Histogram Brush in Segment Editor Threshold effect

**Topic ID**: 17501
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/disable-histogram-brush-in-segment-editor-threshold-effect/17501

---

## Post #1 by @pll_llq (2021-05-07 07:07 UTC)

<p>Hi <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20"></p>
<p>I’m using the segment editor threshold effect in a custom UI to segment a CT. The effect conveniently handles all the nodes that are required for visualization and gives me python access to processing functions. To accomplish this I’ve used the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-run-segment-editor-effects-from-a-script" rel="noopener nofollow ugc">references from the script repository</a>.</p>
<p>I like the sliders and the python interface to setting threshold values and I like how the segment editor handles the display. My problem is that when I set active effect in the temporary <code>qMRMLSegmentEditorWidget</code> it hijacks the interaction mode to the HistogramBrush (circle ROI for threshold values selection by default).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7372a98b0f0f2059192b09bb8264fbb360c0d316.jpeg" alt="image" data-base62-sha1="gtizsnFzfhO9pKeWiBCRbneYLB4" width="464" height="410"></p>
<p>Is there a way to disable the interactive functionality related to clicking the slice views?</p>

---

## Post #2 by @lassoan (2021-05-10 03:57 UTC)

<p>You can add an effect parameter (without a GUI widget) to enable/disable local histogram region drawing and send a pull request to integrate this option into Slicer core.</p>
<aside class="quote no-group" data-username="pll_llq" data-post="1" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>My problem is that when I set active effect in the temporary <code>qMRMLSegmentEditorWidget</code> it hijacks the interaction mode to the HistogramBrush</p>
</blockquote>
</aside>
<p>Why is this a problem?</p>

---

## Post #3 by @pll_llq (2021-05-10 12:38 UTC)

<p>Thanks for the advice. I’ll look into the segment editor source code to see if I can add this parameter.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Why is this a problem?</p>
</blockquote>
</aside>
<ul>
<li>no visual feedback that the interaction mode has changed (it was a surprize to me that there is an interaction mode)</li>
<li>inability to use window/level interaction mode while the unconfirmed segmentation is on screen (my use case)</li>
</ul>
<p>So, when I choose the threshold segmentation I get no feedback that the interaction mode has changed. Other segmentation effects (draw, erase etc) change the mouse pointer.<br>
Since the module panel shows the threshold sliders my assumption was that this is the way the tool works.</p>

---

## Post #4 by @lassoan (2021-05-11 05:36 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="3" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>no visual feedback that the interaction mode has changed (it was a surprize to me that there is an interaction mode)</p>
</blockquote>
</aside>
<p>Good point. I’ll enable custom view cursor for threshold effect.</p>
<aside class="quote no-group" data-username="pll_llq" data-post="3" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>inability to use window/level interaction mode while the unconfirmed segmentation is on screen (my use case)</p>
</blockquote>
</aside>
<p>Several keyboard&amp;mouse gestures would clash between window/level interaction mode and interactive segmentation, so the two mouse modes are mutually exclusive.</p>
<aside class="quote no-group" data-username="pll_llq" data-post="3" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>So, when I choose the threshold segmentation I get no feedback that the interaction mode has changed.</p>
</blockquote>
</aside>
<p>You can see the current interaction mode on the toolbar. If you switch to a segment editor effect then it exits from point placement or window/level adjustment.</p>

---

## Post #5 by @pll_llq (2021-05-11 05:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Good point. I’ll enable custom view cursor for threshold effect.</p>
</blockquote>
</aside>
<p>I was thinking about this and actually if the cursor change was there I would not have any expectations about the interaction with the effect and thus no problems integrating it into the workflow.<br>
So yeah, the adding a custom cursor is the best solution.</p>

---

## Post #6 by @pll_llq (2021-05-11 05:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>custom view cursor</p>
</blockquote>
</aside>
<p>Shall I create an icon for it?</p>

---

## Post #7 by @lassoan (2021-05-11 05:41 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="5" data-topic="17501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>So yeah, the adding a custom cursor is the best solution.</p>
</blockquote>
</aside>
<p>Done. See <a href="https://github.com/Slicer/Slicer/commit/5b02b00ea3cb618c74e3e21485c8a0f61bc739a9">here</a>.</p>

---

## Post #8 by @mau_igna_06 (2022-01-13 12:24 UTC)

<p>Hi. I would like to disable the histogram cursor and functionality completely on localThreshold effect because it is not needed as the segmentation parameters are selected with GUI. So I can have the previsualization of segmentation without been possible to change it via the mouse.</p>
<p>I tried with this line but it doesn’t work:</p>
<pre><code class="lang-auto">localThreshold.self().histogramFunctionItem.removeEventFilter(localThreshold.self().histogramEventFilter)
</code></pre>
<p>Also it would be interesting to me to be able to place a fiducial over the sliceView while the preview of segmentation is on. Changing to fiducial placement mode, disables the previsualization of segmentation</p>

---

## Post #9 by @mau_igna_06 (2022-01-14 13:06 UTC)

<p>I solved it by creating a copy of LocalThreshold effect and overriding <em>processInteractionEvents</em> to this:</p>
<pre><code class="lang-auto">  def processInteractionEvents(self, callerInteractor, eventId, viewWidget):
    return False
</code></pre>
<p>Hope it helps someone</p>

---
