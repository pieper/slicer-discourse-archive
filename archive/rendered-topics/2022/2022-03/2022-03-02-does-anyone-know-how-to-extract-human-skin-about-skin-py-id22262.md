---
topic_id: 22262
title: "Does Anyone Know How To Extract Human Skin About Skin Py"
date: 2022-03-02
url: https://discourse.slicer.org/t/22262
---

# Does anyone know how to extract human skin?(about skin.py)

**Topic ID**: 22262
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/does-anyone-know-how-to-extract-human-skin-about-skin-py/22262

---

## Post #1 by @zhuyingxinxs (2022-03-02 14:11 UTC)

<p>I found the code for extracting skin in the following url,But how do I import my own DICOM data instead of using the MRHEAD example?</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9">
  <header class="source">

      <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9</a></h4>

  <h5>ExtractSkin.py</h5>
  <pre><code class="Python">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRHead()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")
</code></pre>
    This file has been truncated. <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @Chuan (2023-10-09 17:19 UTC)

<p>Hi Yingxin</p>
<p>Did you solve it? I need to extract skin from CT images, not sure whether we have the same problem.</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #3 by @slicer365 (2023-10-09 23:09 UTC)

<p>Open the python console<br>
change the following code to your data name,</p>
<p>and then paste it in the console to run.</p>
<pre><code class="lang-auto">masterVolumeNode = slicer.util.getNode('你自己的数据名称')

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # 用于展示
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")

segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","35")
effect.setParameter("MaximumThreshold","695")
effect.self().onApply()

# 平滑
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MEDIAN")
effect.setParameter("KernelSizeMm", 11)
effect.self().onApply()


segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

segmentationNode.CreateClosedSurfaceRepresentation()

</code></pre>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f2dae62cf293a3499c8b7772111a8f8820f497.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f2dae62cf293a3499c8b7772111a8f8820f497.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f2dae62cf293a3499c8b7772111a8f8820f497.mp4</a>
    </video>
  </div><p></p>

---
