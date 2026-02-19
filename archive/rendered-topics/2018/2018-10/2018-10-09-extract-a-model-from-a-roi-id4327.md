---
topic_id: 4327
title: "Extract A Model From A Roi"
date: 2018-10-09
url: https://discourse.slicer.org/t/4327
---

# Extract a model from a ROI

**Topic ID**: 4327
**Date**: 2018-10-09
**URL**: https://discourse.slicer.org/t/extract-a-model-from-a-roi/4327

---

## Post #1 by @Niels (2018-10-09 13:35 UTC)

<p>In my code I would like to extract the model data within a placed ROI and create two new models from that. Does anybody have any hints or examples on how to achieve this?</p>

---

## Post #2 by @lassoan (2018-10-09 14:06 UTC)

<p>I’m not sure if there is a model clipping tool that uses ROI box as input. You can try <a href="http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/EasyClip">EasyClip</a> (clips using a slice plane) and <a href="http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/ModelClip">ModelClip</a> (clips using a series of connected planes) extensions as they are, or modify them to clip using planes of an ROI box.</p>
<p>If you work with closed surface models then you have an extensive toolset to edit models (clip, cut, combine, edit, smooth, hollow, grow, shrink, etc.) in Segment Editor module. You need to either load the model file as segmentation (in Add data popup window); or - if you have already loaded your data as model node - then you can import the model node into a segmentation node using Segmentations module Import/export section.</p>

---
