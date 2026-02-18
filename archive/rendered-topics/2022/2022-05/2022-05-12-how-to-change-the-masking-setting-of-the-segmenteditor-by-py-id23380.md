# How to change the masking setting of the segmenteditor by python?

**Topic ID**: 23380
**Date**: 2022-05-12
**URL**: https://discourse.slicer.org/t/how-to-change-the-masking-setting-of-the-segmenteditor-by-python/23380

---

## Post #1 by @Xing_Lu (2022-05-12 02:03 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ef0aee5bb31956e6d7ec524a0432a704de58ae.png" alt="image" data-base62-sha1="bYvM9vZgpFt1AFK4FowOEfARqeG" width="585" height="134"><br>
trying to change this ‘Overwrite other segmentation’ option programmably. However, I tried the code:</p>
<p>defaultSegmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
defaultSegmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteVisibleSegments)<br>
slicer.mrmlScene.AddDefaultNode(defaultSegmentEditorNode)</p>
<p>But it doesn’t work actually, everytime the default is still shown as ‘Allsegments’.</p>
<p>Any suggestions?</p>
<p>Thanks so much!</p>

---

## Post #2 by @lassoan (2022-05-12 02:08 UTC)

<p>This changes the default. It does not affect the current setting if you have already switched to the Segment Editor before or you loaded a scene that contained a segment editor node.</p>
<p>You can change the masking settings in all the existing segment editor nodes like this:</p>
<pre><code class="lang-python">for segmentEditorNode in slicer.util.getNodesByClass('vtkMRMLSegmentEditorNode'):
  segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteVisibleSegments)

</code></pre>

---

## Post #3 by @Xing_Lu (2022-05-30 23:46 UTC)

<p>That really helps, Andras!</p>
<p>It is solved, thanks! Sorry for my late reply.</p>

---
