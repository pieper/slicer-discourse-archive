---
topic_id: 6723
title: "Create Segmentation From Simpleitk Image"
date: 2019-05-07
url: https://discourse.slicer.org/t/6723
---

# Create segmentation from simpleItk Image

**Topic ID**: 6723
**Date**: 2019-05-07
**URL**: https://discourse.slicer.org/t/create-segmentation-from-simpleitk-image/6723

---

## Post #1 by @n2018 (2019-05-07 16:51 UTC)

<p>Hello! Could you please help me, is there a way to create a new segmentation and add  asegment into it from simpleItk Image object (I mean the way through the python code)</p>

---

## Post #2 by @lassoan (2019-05-07 22:41 UTC)

<p>You can read the SimpleITK image into a temporary labelmap volume node, <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#adf111c9bcd3ceb28d49028f6fc6a2506" rel="nofollow noopener">import the labelmap volume node into the segmentation</a>, then delete the labelmap volume node.</p>
<p>You can also use SimpleITK to create additional effects in Segment Editor. See an example of a SimpleITK-based segment editor effect here: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorWatershed" rel="nofollow noopener">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorWatershed</a></p>

---
