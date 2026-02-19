---
topic_id: 25554
title: "Python Call For Segmentation Node Selector In The View Contr"
date: 2022-10-05
url: https://discourse.slicer.org/t/25554
---

# Python call for segmentation node selector in the view controller

**Topic ID**: 25554
**Date**: 2022-10-05
**URL**: https://discourse.slicer.org/t/python-call-for-segmentation-node-selector-in-the-view-controller/25554

---

## Post #1 by @BraDan (2022-10-05 05:40 UTC)

<p>Hi everybody,</p>
<p>I am working with multiple segmentations. When entering:<br>
sliceController = slicer.app.layoutManager().sliceWidget(“Red”).sliceController()<br>
sliceController.toggleSegmentationOutlineFill()<br>
I am able to toggle through the fill states of the segmentation selected in the segmentation node selector. But I struggle to find a python call to switch to another segmentation - I have to select it manually out of the dropdown menu in the slice viewer window.<br>
So my Question is: Is there any way I can specify in the Python Interactor which segmentation the .toggleSegmentationOutlineFill() Method refers to?</p>
<p>Thanks!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/015f2b9c49a6aa51ea47dbe3040d3c64e92653d1.jpeg" alt="Screenshot 2022-10-04 214919" data-base62-sha1="c8nuVhuKILfdqIZVgup7z6sARb" width="424" height="187"></p>
<p>Operating system: WIn11<br>
Slicer version: 5.0.3</p>

---

## Post #2 by @BraDan (2022-10-16 18:48 UTC)

<p>In case anybody is interested, another approach works using the display node of the segmentation node in question, for example to enable 2D FIll and Outline:</p>
<p><code>segmentationNode.GetDisplayNode().SetVisibility2DFill(True)</code><br>
<code>segmentationNode.GetDisplayNode().SetVisibility2DOutline(True)</code></p>

---

## Post #3 by @lassoan (2022-10-20 20:58 UTC)

<p>Node selector in that widget is not exposed via MRML, so you need to drill down in the GUI to get to the segmentation node selector widget in the slice view controller. There are examples in the script repository and there have been similar questions on this forum that should get you there, but if you get stuck then let us know how far you got and we’ll help you with the rest.</p>

---
