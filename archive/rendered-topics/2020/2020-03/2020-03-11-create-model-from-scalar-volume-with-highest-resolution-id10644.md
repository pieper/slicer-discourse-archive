# Create Model from Scalar Volume with highest resolution

**Topic ID**: 10644
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/create-model-from-scalar-volume-with-highest-resolution/10644

---

## Post #1 by @siaeleni (2020-03-11 14:34 UTC)

<p>Hi,<br>
I have a ScalarVolume with only two intensities (0,1) and I would like to convert it into a vtkMRMLModelNode. The steps that I follow are the following:</p>
<ol>
<li>In Editor (I convert it into a Label Map)</li>
<li>In Model Creator (I convert the Label Map into a Model Node)<br>
My question is, how can I create the model with highest resolution(mabye the best triangulation)?</li>
</ol>
<p>(I would like to give more information regarding my aim in case that I do extra work without needed.<br>
I want to apply sitk filters to my initial model and the steps that I follow are the following:<br>
vtkModel-&gt;vtkSegmentationNode-&gt;LabelMap-&gt;ScalarVolume-&gt;filter-&gt;ScalarVolume-&gt;LabelMap-&gt;Model – Does this process is what do you recommend or there is different workflow that I should follow? Because I have realized that at the end the model has poor resolution if I am not mistaken.)</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-03-11 16:26 UTC)

<p>I would recommend this pipeline:<br>
vtkMRMLModelNode -&gt; vtkMRMLSegmentationNode -&gt; vtkMRMLLabelMapVolumeNode -&gt; SimpleITK filter -&gt; vtkMRMLLabelMapVolumeNode -&gt; vtkMRMLSegmentationNode -&gt; vtkMRMLModelNode</p>
<p>See a complete example (from segmentation node to segmentation node) in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py">Watershed segment editor effect</a>.</p>

---
