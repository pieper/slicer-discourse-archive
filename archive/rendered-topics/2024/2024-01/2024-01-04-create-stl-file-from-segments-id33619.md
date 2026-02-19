---
topic_id: 33619
title: "Create Stl File From Segments"
date: 2024-01-04
url: https://discourse.slicer.org/t/33619
---

# Create .stl file from segments

**Topic ID**: 33619
**Date**: 2024-01-04
**URL**: https://discourse.slicer.org/t/create-stl-file-from-segments/33619

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-01-04 09:57 UTC)

<p>Hi to everyone. Today’s question is quite ‘easy’ but, after look the wiki and older post I didn’t see anything… I’m trying to convert my segment into .stl files with Python code.</p>
<p>I’m acquainted with segmentations and segment editor modules and I know you can export segments to .stl file using a volume reference and specifying the coordinates system. However, I couldn’t find the code lines to do that.</p>
<p>I guess it should start something like:</p>
<pre><code class="lang-auto">node = slicer.util.getNode('Segmentation')
segmentName = 'Segment_1'
segmentIndex= node.GetSegmentation().GetSegmentIdBySegmentName(segmentName )
node.Function.....
</code></pre>
<p>Has somebody idea of what function performs this? And what parameters uses?</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @SANTIAGO_PENDON_MING (2024-01-04 11:18 UTC)

<pre><code class="lang-auto">segmentationNode = getNode("Segmentation")
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Segments")
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)
</code></pre>
<p>I think using this will work. Also what I have to do if I only one one segment and not all?</p>

---
