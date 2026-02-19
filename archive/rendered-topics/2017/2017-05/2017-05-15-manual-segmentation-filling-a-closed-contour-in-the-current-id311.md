---
topic_id: 311
title: "Manual Segmentation Filling A Closed Contour In The Current"
date: 2017-05-15
url: https://discourse.slicer.org/t/311
---

# Manual Segmentation, Filling a closed contour in the current slice

**Topic ID**: 311
**Date**: 2017-05-15
**URL**: https://discourse.slicer.org/t/manual-segmentation-filling-a-closed-contour-in-the-current-slice/311

---

## Post #1 by @brhoom (2017-05-15 17:52 UTC)

<p>Dear all,<br>
Is there a tool that fills a contour (drawn by me) in the current slice? this will help to segment difficult areas manually in a simple way.<br>
Have a nice evening!<br>
Ibraheem</p>

---

## Post #2 by @hgueziri (2017-05-15 18:24 UTC)

<p>Hi Braheem,</p>
<p>Check the ‘draw’ tool in the Segment Editor. Use the mouse buttons: left button to draw and right button clic to close the contour.</p>
<p>Is that what you’re looking for ?</p>

---

## Post #3 by @brhoom (2017-05-15 18:30 UTC)

<p>Thanks a lot, that is exactly what I am looking for :).</p>

---

## Post #4 by @lassoan (2017-05-17 12:29 UTC)

<p>A post was split to a new topic: <a href="/t/draw-segment-contour-with-attracted-to-edges/333">Draw segment contour with attracted to edges</a></p>

---

## Post #5 by @lassoan (2017-05-17 12:27 UTC)

<p>If there are actual edges (intensity differences) then you don’t want to segment slice-by-slice. In that case use the Grow from seeds effect. It allows you to just approximately segment on a couple of slices and you automatically get a full 3D segmentation. You can always make adjustments (by adding a few more strokes) if you don’t like the automatic segmentation results at some places.</p>

---

## Post #6 by @brhoom (2017-05-17 13:10 UTC)

<p>Thanks for the suggestion. The edges are clear to see but not to segment automatically that is why I am using the manual segmentation.</p>

---

## Post #7 by @lassoan (2023-03-21 02:48 UTC)



---
