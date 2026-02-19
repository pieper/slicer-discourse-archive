---
topic_id: 33985
title: "Attributeerror Type Object Vtkslicersegmentationsmodulemrmlp"
date: 2024-01-26
url: https://discourse.slicer.org/t/33985
---

# AttributeError: type object 'vtkSlicerSegmentationsModuleMRMLPython.vtkMRMLSegm' has no attribute 'PaintAllowedEverywhere'

**Topic ID**: 33985
**Date**: 2024-01-26
**URL**: https://discourse.slicer.org/t/attributeerror-type-object-vtkslicersegmentationsmodulemrmlpython-vtkmrmlsegm-has-no-attribute-paintallowedeverywhere/33985

---

## Post #1 by @paleomariomm (2024-01-26 09:10 UTC)

<p>I am creating a script to run iteratively over subfolders with baboon skull CTs in DICOM format.</p>
<p>In the pipeline, I need to do a segmentation of the full skulls via Thresholding (which works nice in the script) and and Removing small islands (which is not).</p>
<p>This is part of the code with the segmentation part:</p>
<pre><code class="lang-auto">    # SEGMENTATION
    # Start the segmentation subroutine (threshold + island tools + smoothing and morphological closing)
    # https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9
    
    # Create segmentation
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(croppedVolume)
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(baboon_skull)
    
    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode) # (yourOutputSegmentation)
    segmentEditorWidget.setMasterVolumeNode(croppedVolume)    # (yourVolume)
    
    # Segmentation: Thresholding
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold","60")
    effect.setParameter("MaximumThreshold","3071")
    effect.self().onApply()

    # Segmentation: Systematically remove small islands
    # https://discourse.slicer.org/t/islands-segmentation-via-python-script/21021
    segmentEditorNode.SetSelectedSegmentID("baboon_skull")
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumSize","1000")
    effect.setParameter("Operation","KEEP_LARGEST_ISLAND")
    segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone) 
    segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere)  
    effect.self().onApply()
</code></pre>
<p>My Python console returns an error in the before last line:</p>
<p><code>segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere)</code></p>
<p>This is the error that I get:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 84, in &lt;module&gt;
AttributeError: type object 'vtkSlicerSegmentationsModuleMRMLPython.vtkMRMLSegm' has no attribute 'PaintAllowedEverywhere'
</code></pre>
<p>I don’t know where the problem might be. Any idea?</p>
<p>I followed <a class="mention" href="/u/rbumm">@rbumm</a> script that was inserted in another Slicer question (link in the code)</p>

---

## Post #2 by @paleomariomm (2024-01-26 10:53 UTC)

<p>I solved the problem by commenting three extra lines:</p>
<pre><code class="lang-auto"># Segmentation: Systematically remove small islands
# https://discourse.slicer.org/t/islands-segmentation-via-python-script/21021
# segmentEditorNode.SetSelectedSegmentID("baboon_skull")
segmentEditorWidget.setActiveEffectByName("Islands")
effect = segmentEditorWidget.activeEffect()
# effect.setParameter("MinimumSize","1000")
# effect.setParameter("Operation","KEEP_LARGEST_ISLAND")
segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone) 
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere)  
effect.self().onApply()
</code></pre>

---
