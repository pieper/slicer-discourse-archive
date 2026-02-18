# arrayFromVolume issue

**Topic ID**: 9548
**Date**: 2019-12-18
**URL**: https://discourse.slicer.org/t/arrayfromvolume-issue/9548

---

## Post #1 by @fraca (2019-12-18 13:26 UTC)

<p>I’ m trying to obtain the array of this volume, but i obtain some errors. Can you help me?</p>
<blockquote>
<p>labeledImage = self.LabeledVolumeSelector.currentNode().GetImageData()<br>
selectedImage = self.SelectedVolumeSelector.currentNode().GetImageData()</p>
</blockquote>
<p>I tried to use <code>slicer.util.arrayFromVolume</code> but i obtain this error: <code>TypeError: object of type 'vtkCommonDataModelPython.vtkImageData' has no len() </code></p>
<p>This is the code written in 3DSlicer 3.6, it may be helpful:</p>
<blockquote>
<p>labeledImage = self.LabeledVolumeSelector.GetSelected().GetImageData()<br>
selectedImage = self.SelectedVolumeSelector.GetSelected().GetImageData()<br>
labeledArray = labeledImage.ToArray()<br>
selectedArray = selectedImage.ToArray()<br>
labeledSlice = vol[ijk[2],…]<br>
selectedSlice = voll[ijk[2],…]</p>
</blockquote>

---

## Post #2 by @lassoan (2019-12-18 13:30 UTC)

<p><code>arrayFromVolume</code> requires a MRML volume node as input. See examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_value_of_a_volume_at_specific_voxel_coordinates">script repository</a>.</p>

---

## Post #3 by @fraca (2019-12-18 13:40 UTC)

<p>If i want to get an array from the previous image there’s an another way to do that? I have to take necessarily that input, because LabeledVolumeSelector and SelectedVolumeSelector came from <code>qMRMLNodeComboBox</code>. I’m sorry but i’m not very expert</p>

---

## Post #4 by @lassoan (2019-12-18 14:03 UTC)

<p>You can find detailed, step-by-step tutorials here: <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx</a></p>

---
