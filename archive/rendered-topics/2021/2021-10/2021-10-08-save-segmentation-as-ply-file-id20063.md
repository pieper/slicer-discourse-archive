---
topic_id: 20063
title: "Save Segmentation As Ply File"
date: 2021-10-08
url: https://discourse.slicer.org/t/20063
---

# Save segmentation as PLY file

**Topic ID**: 20063
**Date**: 2021-10-08
**URL**: https://discourse.slicer.org/t/save-segmentation-as-ply-file/20063

---

## Post #1 by @Saima (2021-10-08 03:38 UTC)

<p>Hi Andras,<br>
I am saving PLY file but it is still saving STL file.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2021-10-08 03:41 UTC)

<p>Please provide more details.</p>

---

## Post #3 by @Saima (2021-10-08 03:43 UTC)

<p>I am saving the segments using</p>
<pre><code>slicer.modules.segmentations.logic().ExportSegmentsClosedSurfaceRepresentationToFiles("/home/saima/2021_5_28/slicer work/modelFiles/", segmentationNode, None,"PLY", True, 1.0, False )
</code></pre>
<p>The function saves as stl not ply</p>
<p>Regards,<br>
saima Safdar</p>

---

## Post #4 by @Saima (2021-10-08 03:50 UTC)

<p>I am saving the segments using</p>
<pre><code class="lang-auto">slicer.modules.segmentations.logic().ExportSegmentsClosedSurfaceRepresentationToFiles("/home/saima/2021_5_28/slicer work/modelFiles/", segmentationNode, None,"PLY", True, 1.0, False )
</code></pre>
<p>The function saves as stl not ply</p>
<p>Regards,<br>
saima Safdar</p>

---

## Post #5 by @lassoan (2021-10-08 03:51 UTC)

<p>This method supports STL and OBJ - see <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a4b5328985b2d98cbbc93a5b2ae7fde6b">documentation</a>. You can export to PNG by exporting the segmentation to model nodes and then save the model nodes to files.</p>

---
