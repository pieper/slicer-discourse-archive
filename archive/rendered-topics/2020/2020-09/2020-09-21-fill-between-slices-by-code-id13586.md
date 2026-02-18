# Fill between slices by code

**Topic ID**: 13586
**Date**: 2020-09-21
**URL**: https://discourse.slicer.org/t/fill-between-slices-by-code/13586

---

## Post #1 by @luigi-palladino (2020-09-21 14:23 UTC)

<p>Hi,</p>
<p>I would like to perform the effect “Fill between slices” of the Segment Editor in my application on  a Segment Node that I have.<br>
I can’t figure out how to do that by code. Is there a way to do that?</p>
<p>I’m in Slicer 4.11.0-2019-09-25</p>
<p>Thank you for your help.</p>

---

## Post #2 by @lassoan (2020-09-21 14:43 UTC)

<p>See examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>
<p>“Fill between slices” effect works the same way as “Grow from seeds” effect, so the “<a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b">brain tumor segmentation using grow from seeds effect</a>” example should work as is, you just need to change the effect name.</p>

---

## Post #3 by @luigi-palladino (2020-09-21 15:15 UTC)

<p>Thank you very much, editing this piece of code from your link worked.</p>
<pre><code># Run filter
################################################

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Run segmentation
segmentEditorWidget.setActiveEffectByName("Fill between slices")
effect = segmentEditorWidget.activeEffect()
# You can change parameters by calling: effect.setParameter("MyParameterName", someValue)
# Most effect don't have onPreview, you can just call onApply
effect.self().onPreview()
effect.self().onApply()</code></pre>

---
