# Mouse click to open selected segment in Segment Editor

**Topic ID**: 26524
**Date**: 2022-12-01
**URL**: https://discourse.slicer.org/t/mouse-click-to-open-selected-segment-in-segment-editor/26524

---

## Post #1 by @xerox (2022-12-01 03:00 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.0.3</p>
<p>Hi,</p>
<p>I have a Slicer extension built that creates 2D segmentations. I want the user to be able to highlight the segments when they hover with their mouse and when they click on the segments to open up Slicer’s Segmentation Editor allowing the user to further edit the segments as necessary.</p>
<p>Currently, I’m using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view" rel="noopener nofollow ugc">this code</a> to get the user’s mouse position and I’m able to highlight the hovered segment based on that. Now, I’d like it so that if the user clicks on that hovered segment, the Segmentation Editor opens. I’d appreciate any guidance on how I would proceed about doing that. Thanks!</p>

---

## Post #2 by @lassoan (2022-12-01 03:14 UTC)

<p>You can switch to the Segment Editor module and select a segmentation / segment like this:</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
segmentID = "Segment_2"
slicer.util.selectModule('SegmentEditor')
slicer.util.getModuleWidget('SegmentEditor').parameterSetNode.SetAndObserveSegmentationNode(segmentationNode)
slicer.util.getModuleWidget('SegmentEditor').parameterSetNode.SetSelectedSegmentID(segmentID)
</code></pre>
<p>However, instead of switching between modules, I would recommend to offer all features that your users need in your module. You can easily embed a Segment Editor widget inside your own module (you can use the Segment Editor module in Slice core as an example of how to embed the Segmen Editor widget into a Pythons scripted module). You can put the widget into a collapsible section to only take up space when needed.</p>

---

## Post #3 by @xerox (2022-12-01 03:53 UTC)

<p>Thanks for the fast response and the suggestion, I’ll keep that in mind!</p>
<p>For the code you provided, if I wanted to get the string “Segment_2” after the user left clicks the segment region once in the transverse section view, how would I go about doing that using Python. Thanks again!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/217aca061dd71372f565fe930ef4a60726381002.jpeg" data-download-href="/uploads/short-url/4MaPwF8iFOfypq2oXVIfyTPWGoa.jpeg?dl=1" title="output" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/217aca061dd71372f565fe930ef4a60726381002_2_690x370.jpeg" alt="output" data-base62-sha1="4MaPwF8iFOfypq2oXVIfyTPWGoa" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/217aca061dd71372f565fe930ef4a60726381002_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/217aca061dd71372f565fe930ef4a60726381002_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/217aca061dd71372f565fe930ef4a60726381002_2_1380x740.jpeg 2x" data-dominant-color="38383E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">output</span><span class="informations">4412×2371 807 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-12-01 04:50 UTC)

<aside class="quote no-group" data-username="xerox" data-post="3" data-topic="26524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/x/898d66/48.png" class="avatar"> xerox:</div>
<blockquote>
<p>if I wanted to get the string “Segment_2” after the user left clicks the segment region once in the transverse section view, how would I go about doing that using Python.</p>
</blockquote>
</aside>
<p>See this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-segments-visible-at-a-selected-position">example in the script repository</a>.</p>

---

## Post #6 by @yaraabdelazim (2024-03-20 14:15 UTC)

<p>Hello,</p>
<p>I was wondering how you’re able to highlight the segments based on the mouse position?</p>
<p>Thanks in advance</p>

---

## Post #7 by @lassoan (2024-03-22 11:54 UTC)

<p>Segmentation displayable manager can provide a list of segments visible at the current position. DataProbe is a scripted module, you can have a look at the source code to see what exact methods are called.</p>

---
