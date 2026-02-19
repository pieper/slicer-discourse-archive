---
topic_id: 20876
title: "Input Models And Markups Into Effects Inside Segment Editor"
date: 2021-12-02
url: https://discourse.slicer.org/t/20876
---

# Input Models and Markups into Effects inside Segment Editor

**Topic ID**: 20876
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/input-models-and-markups-into-effects-inside-segment-editor/20876

---

## Post #1 by @Karthik (2021-12-02 06:12 UTC)

<p>Hi. I am creating an effect inside Segment Editor. I have looked at the code from other effects and saw how a volume selector was being written.<br>
self.inputVolumeSelector = slicer.qMRMLNodeComboBox()<br>
self.inputVolumeSelector.nodeTypes = [“vtkMRMLScalarVolumeNode”]<br>
self.inputVolumeSelector.selectNodeUponCreation = True<br>
self.inputVolumeSelector.addEnabled = True<br>
self.inputVolumeSelector.removeEnabled = True<br>
self.inputVolumeSelector.noneEnabled = True<br>
self.inputVolumeSelector.noneDisplay = “(Master volume)”<br>
self.inputVolumeSelector.showHidden = False<br>
self.inputVolumeSelector.setMRMLScene(slicer.mrmlScene)<br>
self.inputVolumeSelector.setToolTip(“Volume to split. Default is current master volume node.”)<br>
self.inputVolumeSelector.connect(“currentNodeChanged(vtkMRMLNode*)”, self.updateMRMLFromGUI)</p>
<p>This creates a volume selector dropdown from where the user can select an input volume for their logic.</p>
<p>Similarly, I would like to add a inputModelSelector and inputMarkupsSelector. But, when I try it, I am not able to select anything in the dropdown. Also, no other effects have taken input a model or markups, therefore I cannot find any reference for this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949170c544670377d2e8a25d35bde6aba9429e04.jpeg" data-download-href="/uploads/short-url/lcigLJtbPm2fJi8GZ4ErDpTPATG.jpeg?dl=1" title="Screenshot from 2021-12-02 11-38-58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/949170c544670377d2e8a25d35bde6aba9429e04_2_690x86.jpeg" alt="Screenshot from 2021-12-02 11-38-58" data-base62-sha1="lcigLJtbPm2fJi8GZ4ErDpTPATG" width="690" height="86" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/949170c544670377d2e8a25d35bde6aba9429e04_2_690x86.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949170c544670377d2e8a25d35bde6aba9429e04.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949170c544670377d2e8a25d35bde6aba9429e04.jpeg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-12-02 11-38-58</span><span class="informations">842×106 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2021-12-02 15:31 UTC)

<p>The dropdown won’t show anything unless the scene is set:</p>
<blockquote>
<p>self.inputVolumeSelector.setMRMLScene(slicer.mrmlScene)</p>
</blockquote>
<p>There are examples in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" rel="noopener nofollow ugc">SlicerSegmentEditorExtraEffects</a>. For example, ROI nodes are used in the local threshold effect here: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/88673aa16b5c818f8319c7860eef73c361be985b/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L163-L168" class="inline-onebox" rel="noopener nofollow ugc">SlicerSegmentEditorExtraEffects/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py at 88673aa16b5c818f8319c7860eef73c361be985b · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a></p>

---
