# Python conversion between model and segment

**Topic ID**: 10765
**Date**: 2020-03-20
**URL**: https://discourse.slicer.org/t/python-conversion-between-model-and-segment/10765

---

## Post #1 by @Franz (2020-03-20 15:52 UTC)

<p>Hi,<br>
thanks for providing this great Software.</p>
<p>I am trying to change Models to Segments and Segments to Models using Python. This can easily be done using the GUI.<br>
Model to Segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/549f3f34019e5dbd3e46041b8648cbbf66a3e944.png" data-download-href="/uploads/short-url/c4Bi7Zackq5NGv2bA6mnccCXLVO.png?dl=1" title="Model_to_segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/549f3f34019e5dbd3e46041b8648cbbf66a3e944.png" alt="Model_to_segment" data-base62-sha1="c4Bi7Zackq5NGv2bA6mnccCXLVO" width="285" height="215"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Model_to_segment</span><span class="informations">571×430 29.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Segmentation to Model</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce7f3407bcb9410ae8f21f79208a44ea46a83dca.png" data-download-href="/uploads/short-url/tsKTdtPRvHMHAkCNNqY32YC9gkq.png?dl=1" title="Segments_to_models" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce7f3407bcb9410ae8f21f79208a44ea46a83dca.png" alt="Segments_to_models" data-base62-sha1="tsKTdtPRvHMHAkCNNqY32YC9gkq" width="219" height="228"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segments_to_models</span><span class="informations">438×456 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what I have found so far.<br>
Converting Models to Segments</p>
<h1><a name="p-37522-create-segmentation-1" class="anchor" href="#p-37522-create-segmentation-1" aria-label="Heading link"></a>Create segmentation</h1>
<pre><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() 
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("Segment")

modelNode = slicer.util.getNode('Model')
segmentationNode = slicer.util.getNode('Segmentation')

slicer.modules.segmentations.logic().CreateSegmentFromModelNode(modelNode, segmentationNode)
</code></pre>
<p>The segmentation is then empty somehow.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2020-03-20 15:56 UTC)

<p>I would recommend to use higher-level (import/export) methods of <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html">segmentations logic</a>. See examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">script repository</a>.</p>

---
