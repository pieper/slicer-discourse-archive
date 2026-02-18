# How to cut multi-segments in a segmentation node with scissors at the same time?

**Topic ID**: 20620
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/how-to-cut-multi-segments-in-a-segmentation-node-with-scissors-at-the-same-time/20620

---

## Post #1 by @Hualin (2021-11-15 06:55 UTC)

<p>Hi, My slicer version is:</p>
<pre><code class="lang-nohighlight">Operating system: Arch Linux
Kernel: x86_64 Linux 5.14.16-arch1
Slicer version: 4.11.20210226
</code></pre>
<p>I tried to use <code>ApplyToAllVisibleSegments</code> effect parameter:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#scissors" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#scissors</a></p>
<pre><code class="lang-python">volumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
segmentationNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
segmentationNode.CreateClosedSurfaceRepresentation()
segmentationNode.GetDisplayNode().SetAllSegmentsVisibility(1)
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)

segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)

segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(volumeNode)
segmentEditorWidget.setActiveEffectByName("Scissors")
effect = segmentEditorWidget.activeEffect()
effect.setParameter('ApplyToAllVisibleSegments', 1)
</code></pre>
<p>Then I used mouse to cut the segments in 3D view, but only worked on the first segment.<br>
So, is there a way to cut multi-segments with scissors at the same time?</p>
<p>Thanks</p>

---

## Post #2 by @Hualin (2021-11-15 12:25 UTC)

<p>By the way, is there a way to cut multiple segments in different segmentation nodes?And How is the performance?</p>

---

## Post #3 by @lassoan (2021-11-15 13:20 UTC)

<aside class="quote no-group" data-username="Hualin" data-post="1" data-topic="20620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/f6c823/48.png" class="avatar"> Hualin:</div>
<blockquote>
<p>is there a way to cut multi-segments with scissors at the same time?</p>
</blockquote>
</aside>
<p>Yes, you are lucky, <a class="mention" href="/u/rbumm">@rbumm</a> has already implemented this for you in July. Use a recent Slicer Preview Release and cCheck the “all segments” checkbox if you want to cut/fill all visible segments, not just the current one.</p>
<aside class="quote no-group" data-username="Hualin" data-post="2" data-topic="20620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/f6c823/48.png" class="avatar"> Hualin:</div>
<blockquote>
<p>is there a way to cut multiple segments in different segmentation nodes?And How is the performance?</p>
</blockquote>
</aside>
<p>Segment Editor only modifies the selected segmentation. However, it is easy to move or copy segments between segmentations: drag-and-drop in the Data module, or use the Copy/move segments feature in Segmentation module.</p>

---

## Post #4 by @rbumm (2021-11-15 14:22 UTC)

<aside class="quote no-group" data-username="Hualin" data-post="2" data-topic="20620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/f6c823/48.png" class="avatar"> Hualin:</div>
<blockquote>
<p>How is the performance?</p>
</blockquote>
</aside>
<p>Very good, the multi-segment cut through 15 segmented vertebrae from a CT takes 2.5s on a gaming laptop.</p>

---
