# Unable to set Logical effect's parameter from another effect

**Topic ID**: 23790
**Date**: 2022-06-09
**URL**: https://discourse.slicer.org/t/unable-to-set-logical-effects-parameter-from-another-effect/23790

---

## Post #1 by @Dwij_Mistry (2022-06-09 09:07 UTC)

<p>use case:<br>
in one of our custom effect we want to perform union operation from logical effect.</p>
<p>problem:<br>
when we are setting</p>
<pre><code class="lang-auto"># selecting UNION OPERATION
slicer.util.getModuleWidget("SegmentationEditor").editor.OptionsGroupBox.EffectsOptionsFrame.Logical_operatorsOptionsFrame.methodSelectorComboBox.setCurrentIndex(1)

# selecting MODIFITER SEGMENT 
slicer.util.getModuleWidget("SegmentationEditor").editor.OptionsGroupBox.EffectsOptionsFrame.Logical_operatorsOptionsFrame.qMRMLSegmentsTableView.setSelectedSegmentIDs(['Segment_1'])

# selecting SELECTED SEGMENT
slicer.util.getModuleWidget("SegmentationEditor").editor.segmentTableGroupBox.Form.SegmentsTableView.setSelectedSegmentIDs(['Segment_2'])

# LOGICAL APPLY BUTTON CLICK (performing operation)
slicer.util.getModuleWidget("SegmentationEditor").editor.OptionsGroupBox.EffectsOptionsFrame.Logical_operatorsOptionsFrame.SegmentEditorLogicalEffectApply.click()

</code></pre>
<p>Modifier segment is selected by the code. but still Apply button is not enabled, so that we are unable to click the Apply button.</p>
<p>Moreover, is there any difference if we are selecting a segment by a code and when we are selecting a segment by mouse click operation?</p>
<p>Thank you very much in advance.</p>

---

## Post #2 by @mau_igna_06 (2022-06-09 22:14 UTC)

<p>Please look at this<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html</a></p>
<p>And the set the parameters correspondingly</p>
<p>Then do:<br>
Effect.self.onApply()</p>
<p>Or something pretty similar</p>
<p>Hope it helps</p>

---

## Post #3 by @lassoan (2022-06-10 14:05 UTC)

<p>Yes, the correct way to change segmentation parameters is by modifying the segment editor node, and to run any processing you can call the methods of the segment editor effect object.</p>
<p>We cannot prevent developers directly manipulating Qt widgets, but then correct behavior cannot be guaranteed. If you just rearrange the layout or hide some buttons. However, simulating button clicks in arbitrary state of the effect will probably not work.</p>

---
