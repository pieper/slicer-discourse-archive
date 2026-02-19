---
topic_id: 44650
title: "How To Copy A Segmentation From One Slice To The Next In Seg"
date: 2025-10-02
url: https://discourse.slicer.org/t/44650
---

# How to copy a segmentation from one slice to the next in Segment Editor?

**Topic ID**: 44650
**Date**: 2025-10-02
**URL**: https://discourse.slicer.org/t/how-to-copy-a-segmentation-from-one-slice-to-the-next-in-segment-editor/44650

---

## Post #1 by @labixin (2025-10-02 15:08 UTC)

<p>Hello,</p>
<p>I am currently using the Segment Editor module in 3D Slicer (version 5.6.1, Windows 11) to edit liver contours. I would like to ask: if I have already defined the contour on one slice, is it possible to directly copy this contour to the next slice?</p>
<p>Does Segment Editor have such a function, or is there any recommended way to achieve a similar effect?</p>
<p>Thank you very much for your help!</p>
<p>Best regards,</p>
<p>Crayon</p>

---

## Post #2 by @pieper (2025-10-02 16:18 UTC)

<p>You can use the “Fill between slices” effect for this.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#fill-between-slices">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#fill-between-slices</a></p>

---

## Post #3 by @lassoan (2025-10-02 21:14 UTC)

<p>I fully support <a class="mention" href="/u/pieper">@pieper</a>’s suggestion. Propagating segmentation from slice-to-slice would introduce terrible bias into the segmentation. If absolutely none of the 3D methods work and you don’t want to segment many 2D slices, then you can cut down the segmentation time by segmenting only a few slices and interpolate using “Fill between slices”.</p>
<p>However, since nnInteractive model is available (in nnInteractive extension), I can no longer recommend anyone to do slice-by-slice manual segmentation. This AI-assisted tool just works so well that very likely you will not need to segment slice by slice.</p>

---

## Post #4 by @labixin (2025-10-03 03:36 UTC)

<p>Thank you very much for your quick reply. I tried the <em>Fill between slices</em> module, and it works pretty well. I truly appreciate your help!</p>
<p>Best regards,</p>
<p>Crayon</p>

---
