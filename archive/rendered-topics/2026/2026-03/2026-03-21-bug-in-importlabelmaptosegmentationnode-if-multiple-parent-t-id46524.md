---
topic_id: 46524
title: "Bug In Importlabelmaptosegmentationnode If Multiple Parent T"
date: 2026-03-21
url: https://discourse.slicer.org/t/46524
---

# Bug in ImportLabelmapToSegmentationNode if multiple parent transforms

**Topic ID**: 46524
**Date**: 2026-03-21
**URL**: https://discourse.slicer.org/t/bug-in-importlabelmaptosegmentationnode-if-multiple-parent-transforms/46524

---

## Post #1 by @mikebind (2026-03-21 00:27 UTC)

<p>A labelmap imported to a segmentation using ImportLabelmapToSegmentationNode is transformed incorrectly if there are multiple parent transforms soft-applied. I have been using ImportLabelmapToSegmentationNode successfully for a long time with a transformed labelmap with no problem, but I just ran a case where there were multiple parent transforms (i.e. the parent transform had a parent transform applied) and the converted segmentation node put the segments in the wrong place.  With a little testing, it appears that each transform is at least partially applied, but the total transformation is incorrect.</p>
<p>I reproduced this effect with SampleData and saved the scene, it is available here: <a href="https://drive.google.com/file/d/1fXu8EHHY4jzL3COEn8sjXXz1FmgdGdiq/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1fXu8EHHY4jzL3COEn8sjXXz1FmgdGdiq/view?usp=sharing</a></p>
<p>In that scene, I created a segmentation with 3 segments and exported that to a labelmap (these align perfectly). Then I created two transforms which each apply a rotation around the AP axis and a SI translation.  Then I soft-applied the first transform to the labelmap and the original segmentation, and then soft-applied the second transform to the first transform.  Lastly, I ran ImportLabelmapToSegmentationNode on the transformed labelmap, creating the segmentation node labeled SegmentationFromLabelMap in the scene.  With both the SegmentationFromLabelMap and LabelMapFromSegmentation shown, you can see that they do not align the way they should.  It looks like an equal amount of rotation has been applied, but not an equal total translation.  So, it’s not the case that only the first parent transform has been applied, because then the rotation amounts would not be equal. If I combine the two transforms into one (clone the first, apply the second, and harden) and use that, then the output segmentation is aligned with the transformed labelmap (correct behavior). Is it possible that the parent transforms are being applied in the wrong order?</p>
<p>Using Slicer 5.10.0 on Windows 11. The conversion was carried out using the following convenience wrapper around ImportLabelmapToSegmentationNode</p>
<pre data-code-wrap="python"><code class="lang-python">def labelMapToSeg(labelmapNode, createClosedSurfaces=True):
    """Converts an input labelmap node to a segmentation node"""
    segNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(
        labelmapNode, segNode
    )
    if createClosedSurfaces:
        segNode.CreateClosedSurfaceRepresentation()
    return segNode
</code></pre>
<p>To recreate:</p>
<pre data-code-wrap="python"><code class="lang-python"># Load scene linked above, then run
labelNode = getNode('LabelMapFromSegmentation')
segNode = labelMapToSeg(labelNode)
segNode.SetName('NewSegmentationFromLabelMap')
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2a397ebc08997f3c91a3f7e0bb981cae9663eb8.png" data-download-href="/uploads/short-url/u3oLuZ6cIoFxWPxME5i2Yav3CiI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2a397ebc08997f3c91a3f7e0bb981cae9663eb8.png" alt="image" data-base62-sha1="u3oLuZ6cIoFxWPxME5i2Yav3CiI" width="570" height="491"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">570×491 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
