# Error using SegmentEditorExtraEffects with Python script

**Topic ID**: 6560
**Date**: 2019-04-22
**URL**: https://discourse.slicer.org/t/error-using-segmenteditorextraeffects-with-python-script/6560

---

## Post #1 by @smrolfe (2019-04-22 21:56 UTC)

<p>Hello,<br>
I’m getting an error when I set SegmentEditorExtraEffects using Python. The code is still functional, as it looks like the error is generated when the GUI is updated from the scene. Other segment editor effects work just fine using the same syntax. With any segmentation and volume loaded, this code will produce an error:</p>
<pre><code class="lang-auto">segmentationNode=slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
masterVolumeNode=slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
segmentEditorWidget.setActiveEffectByName("Mask volume")
</code></pre>
<p>Here’s the error:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:/Users/srolfe/AppData/Roaming/NA-MIC/Extensions-28152/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py”, line 181, in updateGUIFromMRML<br>
operationButton = [key for key, value in self.buttonToOperationNameMap.iteritems() if value == self.scriptedEffect.parameter(“Operation”)][0]<br>
AttributeError: ‘dict’ object has no attribute ‘iteritems’</p>
</blockquote>
<p>Any advice is appreciated, thanks.</p>

---

## Post #2 by @lassoan (2019-04-22 22:35 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="1" data-topic="6560">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>AttributeError: ‘dict’ object has no attribute ‘iteritems’</p>
</blockquote>
</aside>
<p>In Python3, <code>iteritems</code> is removed from <code>dict</code>, so you need to replace it by <code>items</code>. I’ll push a fix soon.</p>

---

## Post #3 by @smrolfe (2019-04-22 22:43 UTC)

<p>Great, thanks for your help <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---
