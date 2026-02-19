---
topic_id: 37790
title: "How To Handle Slider In The Slicer Widget"
date: 2024-08-09
url: https://discourse.slicer.org/t/37790
---

# How to handle slider in the slicer widget

**Topic ID**: 37790
**Date**: 2024-08-09
**URL**: https://discourse.slicer.org/t/how-to-handle-slider-in-the-slicer-widget/37790

---

## Post #1 by @maniron (2024-08-09 04:28 UTC)

<p>Hi,</p>
<p>I want to do an operation when ever there is a change in the value of the slider in the red widget</p>

---

## Post #2 by @maniron (2024-08-27 10:14 UTC)

<p>Hi I am trying to handle sequence browser frame slider , I found a way to get the index, but I want to connect a function when the slider value changes how can I achieve it</p>
<blockquote>
<p>sequenceBrowserNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLSequenceBrowserNode”)<br>
if sequenceBrowserNode:<br>
sequenceBrowserNode.AddObserver(sequenceBrowserNode.ModifiedEvent, self.onFrameChanged)</p>
</blockquote>
<p>this was the method I used Kindly help me out as</p>

---

## Post #3 by @lassoan (2024-09-12 03:25 UTC)

<p>You can add an observer to the sequence browser MRML node that calls your python function whenever the node is modified.</p>

---
