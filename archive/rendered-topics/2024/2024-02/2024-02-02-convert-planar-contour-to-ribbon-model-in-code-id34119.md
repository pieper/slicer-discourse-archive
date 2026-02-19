---
topic_id: 34119
title: "Convert Planar Contour To Ribbon Model In Code"
date: 2024-02-02
url: https://discourse.slicer.org/t/34119
---

# Convert planar contour to ribbon model in code

**Topic ID**: 34119
**Date**: 2024-02-02
**URL**: https://discourse.slicer.org/t/convert-planar-contour-to-ribbon-model-in-code/34119

---

## Post #1 by @susk (2024-02-02 12:07 UTC)

<p>Hi there,<br>
I have loaded a segmentation into 3D slicer as a planar contour, and am able to convert these planar contours into a Ribbon model representation manually in the segmentations module, by pressing ‘create’ for the Ribbon model under the Representations tab. I need to do this in order to see the contours in 2D view.</p>
<p>However, I have been searching but I cannot find out how I can do this conversion from planar contours to ribbon model programmatically in script. Could you help me?</p>

---

## Post #2 by @susk (2024-02-05 11:17 UTC)

<p>I found the solution, it was very simple. In case anyone is interested:<br>
segmentationNode = getNode(“Segmentation”)<br>
segmentationNode.GetSegmentation().CreateRepresentation(“Ribbon model”)</p>
<p>This will create a representation in all segments, using the conversion path with the lowest cost. Conversion starts from the master representation, which in my case was “Planar contour”</p>

---
