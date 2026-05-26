---
topic_id: 46488
title: "3D-view segmentation smoothing and stl export"
date: 2026-03-17
url: https://discourse.slicer.org/t/46488
last_bumped: 2026-03-18T10:50:46.280Z
---

# 3D-view segmentation smoothing and stl export

**Topic ID**: 46488
**Date**: 2026-03-17
**URL**: https://discourse.slicer.org/t/3d-view-segmentation-smoothing-and-stl-export/46488

---

## Post #1 by @Eva91 (2026-03-17 22:31 UTC)

<p>Hi,</p>
<p>I have a working manual workflow in Slicer, where I load a segmentation, then show it in 3D, and increase the surface smoothness via that tiny arrow on the “Show 3D” button. After that, i export the segmentation to stl.<br>
Now I wish to do this on many cases; can you help me and guide me through how I could do all this via Python, without having to open Slicer?<br>
So basically, how do I, via scripting, load segmentation and smooth it (in the sense of smoothing the 3Dview) with a specific smoothing factor, and then export the new (smoothed) view into stl?</p>
<p>Thank you! (Also, I’m completely new to Slicer scripting, so even the most basic advice is welcome!)</p>

---

## Post #2 by @cpinter (2026-03-18 10:50 UTC)

<p>Something like this should work:</p>
<pre><code class="lang-auto">segmentationNode = slicer.util.loadSegmentation(filePath)  # Need to define filePath
segmentationNode.CreateClosedSurfaceRepresentation()
folderItemID = shNode.CreateFolderItem(shNode.GetSceneItemID(), segmentationNode.GetName())
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, folderItemID)
modelItemIDs = slicer.util.getSubjectHierarchyItemChildren(folderItemID)
for modelItemID in modelItemIDs:
  modelNode = shNode.GetItemDataNode(modelItemID)
  slicer.util.exportNode(m, stlFilePath)  # Need to define stlFilePath
</code></pre>
<p>Note that you need to specify the file names.</p>

---
