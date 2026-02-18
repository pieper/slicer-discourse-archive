# Show the segment of previous frame on the next frame

**Topic ID**: 32342
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/show-the-segment-of-previous-frame-on-the-next-frame/32342

---

## Post #1 by @nimifa (2023-10-20 12:01 UTC)

<p>Hello,</p>
<p>I’m new to 3D Slicer. I did some segmentation on separate frames, but now I want to segment videos (There are no volumes, just 2D frames).<br>
I’ve some question regarding that.</p>
<p>Can we segment a frame, and see a trace (or something like a contour) of it on the next frame(s)? And decide to whether to fill it or not? Or is it possible to copy a segmentation (a shape / mask that is drawn on a frame) from one frame and paste it to another?</p>
<p>For example, if we use <em>draw</em> tool to draw a shape (but not fill it), it is possible to see the trace on other frames. Also, we can choose to fill it on any frame that we want by right-clicking.</p>
<p>Also, is it possible to select a segmentation in a frame, and move it around? I’ve seen the cloning and transformation in the Data module, but it seems that it moves the segmentation on all frames (also it’s a bit tedious!)</p>
<p>If this requires any extensions, please feel free to point it out.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2023-10-24 18:23 UTC)

<p>We developed the <a href="https://discourse.slicer.org/t/need-help-about-the-module-of-single-slice-segmentation-here/22038">Single Slice Segmentation module</a> for the task of segmenting time sequence of 2D frames, such as ultrasound image acquisitions.</p>
<p>Making it easy to copy the previous frame would introduce bias, because users would be tempted to accept the previous contour as is, even if it is slighly inaccurate. You would also end up with highly redundant data set, because neighbor frames in a time sequence are typically very similar. Therefore, we do not make it easy for users to copy the segment from the previous time point but instead we make it easy to skip frames (segment every N-th frame of the input sequence).</p>

---

## Post #3 by @nimifa (2023-10-25 03:22 UTC)

<p>Thank you for your response,<br>
I was thinking of situations where the shape of the object (ROI) doesn’t change, but the location does. So we could copy the exact mask and move it around.</p>
<p>I looked in the Module Finder and even Extensions Mangaer for the this module, but couldn’t find it. Where is it?</p>

---

## Post #4 by @lassoan (2023-10-26 02:20 UTC)

<p>Single Slice Segmentation module is in SlicerAIGT extension. Its source code is <a href="https://github.com/SlicerIGT/aigt/tree/master/SlicerExtension/LiveUltrasoundAi/SingleSliceSegmentation">here</a>.</p>

---
