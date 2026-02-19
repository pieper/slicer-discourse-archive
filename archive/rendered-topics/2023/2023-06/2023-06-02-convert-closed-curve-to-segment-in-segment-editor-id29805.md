---
topic_id: 29805
title: "Convert Closed Curve To Segment In Segment Editor"
date: 2023-06-02
url: https://discourse.slicer.org/t/29805
---

# Convert closed curve to segment in Segment Editor

**Topic ID**: 29805
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/convert-closed-curve-to-segment-in-segment-editor/29805

---

## Post #1 by @mangotee (2023-06-02 15:44 UTC)

<p>Hi,<br>
I am trying to annotate (manually segment) 2D images, the closed-curve markup is of particular use. How can I convert the curve into a segment in Segment Editor? Apart from closed curve, is there a way to simply place/edit ellipse markups? It’s rare, but sometimes I am missing these simpler tools like closed curve/polygon/ellipse in the Segment Editor toolbar (even the SegmentEditorExtraEffects extension does not have those). Usually, these tools are too simplistic. But in my case, I am trying to segment iris/pupil in eye closeup images, and ellipses would be particularly useful.<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2023-06-02 23:24 UTC)

<p>Polygon drawing is called “Draw” effect. For multiple slices you can use “Scissors” effect.</p>
<p>Circle and sphere drawing is available in “Paint” effect. Circle, sphere, and cylinder drawing is in “Scissors” effect (we could add ellipse here, too, but there hasn’t been significant demand).</p>
<p>You can draw/edit closed curves on multiple slices and convert to segment using “Surface Cut” effect (provided by SegmentEditorExtraEffects extension). You can draw open curves and convert them to segment using “Draw curve” effect (in SegmentEditorExtraEffects extension, too).</p>

---

## Post #3 by @rxl (2024-06-18 17:23 UTC)

<p>Sorry if the topic is too old; I wasn’t able to figure out from the UI or documentation how to use an existing closed curve to a segmentation using Surface cut (within segment editor, if there’s another way). All options seemed to be based on creating new fiducials to define the segmentation, rather than using an existing curve.</p>

---

## Post #4 by @lassoan (2024-06-18 17:42 UTC)

<p>If you don’t want to draw/modify the curve interactively in the Segment Editor then you can:</p>
<ul>
<li>use <code>Markups to model</code> module to create a tube model from a curve</li>
<li>drag-and-drop the tube model into a segmentation node to add it as a segment (or right-click on the model to convert to a segmentation)</li>
</ul>

---

## Post #5 by @rxl (2024-06-18 17:59 UTC)

<p>I’m not sure why the segmentation is being produced as such from the model (both yellow, original CC red)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae3541c842c85d5665a5d3606c16b101b9cd67b9.png" alt="image" data-base62-sha1="oR7bj2A8rvMVv6uaaQ4n5FKB35v" width="643" height="363"></p>
<p>The model was created per MarkupsToModel closed surface (I didn’t see tube model)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d88df1d45b70fbb2e4759623a2783341e44c53b2.png" alt="image" data-base62-sha1="uTJfpH28UKKPzi1EDNnq4hLh39M" width="615" height="298"></p>
<p>I wasn’t able to right click the model; I imported the model in the segmentations module</p>

---

## Post #6 by @lassoan (2024-06-18 17:59 UTC)

<p>If you want a tube model, choose <code>Curve</code> model type.</p>

---

## Post #7 by @rxl (2024-06-18 18:02 UTC)

<p>I see, thank you. I may have misunderstood the intent of the original post: they had mentioned ellipse markups so I had thought the area enclosed by the curve would be segmented. Is this only for the path of the curve itself?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0cb984c0a5bab4768452fd2cbd45e91d3a75f86.png" alt="image" data-base62-sha1="pe0eyT6196OpvrjtfBNaGZtnDJc" width="640" height="364"></p>

---

## Post #8 by @lassoan (2024-06-18 19:14 UTC)

<p>What is your overall goal?</p>

---
