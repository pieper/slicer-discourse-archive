---
topic_id: 34797
title: "How To Access Labelmap Indexes And Change Them"
date: 2024-03-09
url: https://discourse.slicer.org/t/34797
---

# How to access Labelmap indexes and change them?

**Topic ID**: 34797
**Date**: 2024-03-09
**URL**: https://discourse.slicer.org/t/how-to-access-labelmap-indexes-and-change-them/34797

---

## Post #1 by @apparrilla (2024-03-09 12:29 UTC)

<p>Hi everyone!</p>
<p>I´m trying to manage imports from mask volumes and have some trouble with index of segments inside them.</p>
<p>For example:<br>
I have a mask.nii.gz with 3 segments inside (1:bone, 2:fat , 3:muscle)<br>
I also have a ColorTable with values:<br>
1 muscle 255 0 0 255<br>
2 bone 0 255 0 255<br>
3 fat 0 0 255 255</p>
<p>I want to import mask file, reorder segments to match each one with ColorTable and then import LBM into SegmentationNode</p>
<p>It could be something like:</p>
<pre><code class="lang-auto">maskFilePath = ("//mask.nii.gz")
maskLBMNode = slicer.util.loadLabelVolume(maskFilePath)
label = slicer.util.arrayFromVolume(maskLBMNode)
# code to change indexes
slicer.util.arrayFromVolumeModified(maskLBMNode)
maskLBMNode.GetDisplayNode().SetAndObserveColorNodeID(colorTable.GetID())
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(maskLBMNode,outputSegmentationNode)
slicer.mrmlScene.RemoveNode(importLBMNode)
</code></pre>
<p>Thanks in advance!!!</p>

---
