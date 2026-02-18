# Error with maskvolumewithsegment with python

**Topic ID**: 12169
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/error-with-maskvolumewithsegment-with-python/12169

---

## Post #1 by @stl (2020-06-23 04:26 UTC)

<p>Hi,</p>
<p>Slicer 4.10.2 , Windows</p>
<p>I’ve been trying to access the mask volume effect with python and keep running into the following problem:</p>
<p>This is the relevant code for segment labeled “Tumor”:</p>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
slicer.mrmlScene.AddNode(segmentEditorNode)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</p>
<p>segmentEditorWidget.setActiveEffectByName(“Mask volume”)<br>
effect = segmentEditorWidget.activeEffect()<br>
maskedVolume = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, “masked volume”)<br>
effect.self().maskVolumeWithSegment(segmentationNode,“Tumor”,“FILL_OUTSIDE”,-1,masterVolumeNode,maskedVolume)</p>
<p>This is the error I get:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/Neeraja/AppData/Roaming/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py”, line 400, in maskVolumeWithSegment<br>
stencil.SetBackgroundValue(fillValues[0])<br>
TypeError: ‘int’ object has no attribute ‘<strong>getitem</strong>’</p>
<p>I’ve checked each of the inputs for maskVolumeWithSegment and reviewed the source code(<a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorMaskVolume/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py#L400" rel="nofollow noopener">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorMaskVolume/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py#L400</a>) but can’t seem to figure out what is wrong.</p>
<p>If I switch to “FILL_INSIDE” the error shifts to Line 390 but is otherwise the same.</p>
<p>I would appreciate any suggestions/ideas.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-06-26 13:03 UTC)

<p>As you can see <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/d28b9218342f57cc04ba1d5a61f50628a5884500/SegmentEditorMaskVolume/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py#L339-L342">here</a>, <code>maskVolumeWithSegment</code> method now expects a <em>list</em> of one or two values. Where did you find the example code snippet that still used a number instead of a list?</p>

---

## Post #3 by @stl (2020-06-26 19:19 UTC)

<p>Thank you!</p>
<p>I used the same linked script but did not see that it had to be a list.</p>
<p>Thanks again.</p>

---
