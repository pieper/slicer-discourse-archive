# How to select an existing ROI in LocalTreshold of SegmentEditor with code?

**Topic ID**: 25100
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/how-to-select-an-existing-roi-in-localtreshold-of-segmenteditor-with-code/25100

---

## Post #1 by @KKLOVECOCO (2022-09-05 11:56 UTC)

<p>Operating system:windows 10<br>
Slicer version: 5.0.3</p>
<p>Hi, all,<br>
I just started learning slicer+jupyter and recently I have a problem that I can’t solve, I would appreciate if someone tell me：</p>
<p>Before activating LocalTreshold(from extensions module named “SegmentEditorExtraEffects”), I followed the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume" rel="noopener nofollow ugc">link</a> to fit ROI to volume.</p>
<p>Then, I have set the basic parameters as shown, but how can I set the ROI with code?<br>
"effect.setParameter(“ROI”,<em>)"  doesn’t seem to work (</em>: sampleID/name/vtkMRMLAnnotationROINode).</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Local Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold",str(40000))
effect.setParameter("MaximumThreshold",str(200000))
effect.setParameter("MinimumDiameterMm",str(4))
#How to select a ROI?
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d660b97243ee74b821fd727dbbef62058ae996fd.png" alt="Snipaste_2022-09-05_13-21-42" data-base62-sha1="uAtpp4akJOrnuZm02Ygq840lt2R" width="651" height="271"></p>

---

## Post #2 by @KKLOVECOCO (2022-09-05 11:56 UTC)

<p>Hi, all,<br>
I just started learning slicer+jupyter and recently I have a problem that I can’t solve, I would appreciate if someone tell me:</p>
<p>Before activating the effect of LocalThreshold (an effect of SegmentEditorExtraEffects), I followed the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume" rel="noopener nofollow ugc">link</a> to fit an existing ROI to volume, the ROI is smaller than the volume. Then,I have set the basic parameters as shown, how can I set the ROI with code?<br>
"effect.setParameter(“ROI”,<em>)" seems to have no effect (</em>: sampleID/name/vtkMRMLAnnotationROINode)</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Local Threshold")
effect = segmentEditorWidget.activeEffect()
# You can change parameters by calling: effect.setParameter("MyParameterName", someValue)
effect.setParameter("MinimumThreshold",str(40000))
effect.setParameter("MaximumThreshold",str(200000))
effect.setParameter("MinimumDiameterMm",str(4))
#How to selcet ROI?
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d660b97243ee74b821fd727dbbef62058ae996fd.png" alt="Snipaste_2022-09-05_13-21-42" data-base62-sha1="uAtpp4akJOrnuZm02Ygq840lt2R" width="651" height="271"></p>

---

## Post #3 by @lassoan (2022-09-05 12:10 UTC)

<p>It seems that thw. ROI is not stored in MRML, but it is <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/719b242faf301c899fb8ec7a448440ae54ca762c/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L366">directly read from the GUI</a>. This is not ideal, but it happens for extensions that are still somewhat experimental, being in the the “SegmentEditorExtraEffects” extension.</p>
<p>Until this is fixed (by adding a MRML node reference), you may access the effect’s GUI and set the ROI node calling <code>effectWidget.roiSelector.setCurrentNode(SomeROI)</code>.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> when you find some time could you update the Local Threshold effect to store the ROI in a node reference and post here when it is done? Thank you!</p>

---

## Post #4 by @KKLOVECOCO (2022-09-05 12:24 UTC)

<p>Sincerely thank you for your reply, I am very excited, I will be back with the results in a while! <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @KKLOVECOCO (2022-09-05 15:09 UTC)

<p>I’m ashamed to be back…begging you to tell me how to define “effectWidget”. <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_tear.png?v=12" title=":smiling_face_with_tear:" class="emoji" alt=":smiling_face_with_tear:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @chir.set (2022-09-05 19:42 UTC)

<aside class="quote no-group" data-username="KKLOVECOCO" data-post="5" data-topic="25100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kklovecoco/48/16521_2.png" class="avatar"> KKLOVECOCO:</div>
<blockquote>
<p>tell me how to define “effectWidget”</p>
</blockquote>
</aside>
<p>Sorry to interfere.</p>
<p>This code snippet may give you enough insight for a workaround.</p>
<pre><code class="lang-auto"># The segment editor module must have been shown at least once.
mainWindow = slicer.util.mainWindow()
mainWindow.moduleSelector().selectModule('SegmentEditor')
# Select an effect.
widgetEditor = slicer.modules.SegmentEditorWidget.editor
widgetEditor.setActiveEffectByName("Local Threshold")
activeEffect = widgetEditor.activeEffect()
# Get the ROI combobox.
roiSelector = activeEffect.optionsFrame().children()[14]

"""
'activeEffect.optionsFrame().children()' lists all widgets of an effect.

If a widget has a name you can access it as such :
activeEffect.optionsFrame().findChild(qt.QPushButton, "SegmentEditorEffectApply")

If a widget does not have a name, guess and count its index sequentially.
An MRML node reference for this effect would be nicer of course.
"""
</code></pre>

---

## Post #7 by @KKLOVECOCO (2022-09-06 05:30 UTC)

<p>Final solution for the parameter setting section:</p>
<pre><code class="lang-auto"># Run segmentation
segmentEditorWidget.setActiveEffectByName("Local Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold",str(40000))
effect.setParameter("MaximumThreshold",str(200000))
effect.setParameter("MinimumDiameterMm",str(4))
roiSelector = effect.optionsFrame().children()[14]
roiSelector.setCurrentNode(roiNode)
</code></pre>
<p>Thanks to <a class="mention" href="/u/chir.set">@chir.set</a></p>

---

## Post #8 by @KKLOVECOCO (2022-09-06 05:32 UTC)

<p>This solution is useful, thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2022-09-06 15:51 UTC)

<p>In the meantime, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> made the ROI node accessible via a node reference (available in the Extensions Manager from tomorrow).</p>

---
