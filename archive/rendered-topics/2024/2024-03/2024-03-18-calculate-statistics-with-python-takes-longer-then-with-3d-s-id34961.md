---
topic_id: 34961
title: "Calculate Statistics With Python Takes Longer Then With 3D S"
date: 2024-03-18
url: https://discourse.slicer.org/t/34961
---

# Calculate Statistics with Python takes longer then with 3D Slicer GUI

**Topic ID**: 34961
**Date**: 2024-03-18
**URL**: https://discourse.slicer.org/t/calculate-statistics-with-python-takes-longer-then-with-3d-slicer-gui/34961

---

## Post #1 by @thorbenjt (2024-03-18 18:23 UTC)

<p>Hi there,<br>
i am currently working on a script the automates tresholding and in addition splitting the segments into islands.<br>
this works just as fine as if i would do it per hand in the 3D Slicer GUI.<br>
The critical part is the calculation of the Statistics. As stated in the title, it takes up to 2 mins to calculate the statistics when using the code, but only 17 seconds when using ther 3D Slicer GUI.</p>
<p>Here is the code which is based on code snippets i found in previous discussions:<br>
node=slicer.util.loadVolume(filename)</p>
<pre><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode") # Creates Empty Segmentation
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(node)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin") #add segment

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget() #-&gt; [Qt] QLayout::addChildLayout: layout "" already has a parent
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode) #-&gt;[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1
segmentEditorWidget.setSourceVolumeNode(node)

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","125.00")
effect.setParameter("MaximumThreshold","255.00")
effect.self().onApply()

segmentEditorWidget.setActiveEffectByName("Islands")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumSize","25")
effect.setParameter("Operation","SPLIT_ISLANDS_TO_SEGMENTS")
effect.self().onApply()
segmentEditorWidget.setActiveEffect(None)
segmentEditorWidget = None

segmentationNode  =  slicer.util.getNode('Segmentation')



resultsTableNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableNode')


import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled","True")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin","False")
segStatLogic.getParameterNode().SetParameter("CloseSurfaceStatisticsPlugin","False")
segStatLogic.computeStatistics()
stats = segStatLogic.getStatistics()
</code></pre>
<p>This is the file i want to segment:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/490750d96a45de627d31778d2a7cd9f680ca6eab.jpeg" data-download-href="/uploads/short-url/aq2wP36bIMoPMdBripIbBuZDwPV.jpeg?dl=1" title="test001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/490750d96a45de627d31778d2a7cd9f680ca6eab_2_690x194.jpeg" alt="test001" data-base62-sha1="aq2wP36bIMoPMdBripIbBuZDwPV" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/490750d96a45de627d31778d2a7cd9f680ca6eab_2_690x194.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/490750d96a45de627d31778d2a7cd9f680ca6eab_2_1035x291.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/490750d96a45de627d31778d2a7cd9f680ca6eab_2_1380x388.jpeg 2x" data-dominant-color="E2E2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test001</span><span class="informations">1920×540 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance for any help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
