# Retrieve the segmentation and source volume from Segment Editor (segmentEditorWidget)

**Topic ID**: 36162
**Date**: 2024-05-15
**URL**: https://discourse.slicer.org/t/retrieve-the-segmentation-and-source-volume-from-segment-editor-segmenteditorwidget/36162

---

## Post #1 by @waromero (2024-05-15 09:37 UTC)

<p>Hello,</p>
<p>I embedded the <code>segmentEditorWidget</code> from the Segment Editor module into my custom-made module. Now I want to retrieve the <code>vtkMRMLScalarVolumeNode</code> from the <code>sourceVolumeNodeSelector</code>; and the <code>vtkMRMLSegmentationNode</code> from <code>segmentationNodeSelector</code> (selection made by the user).</p>
<p>Normally, I have a component of the style: <code>self.ui.inputSegmentationSelector.currentNode()</code> but I can’t find the access to the object in the UI in <code>segmentEditorWidget</code>.</p>
<p>Thank you!</p>

---
