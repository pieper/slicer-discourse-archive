# Below/aboverange color show for model scalars

**Topic ID**: 19205
**Date**: 2021-08-16
**URL**: https://discourse.slicer.org/t/below-aboverange-color-show-for-model-scalars/19205

---

## Post #1 by @wabwan25 (2021-08-16 03:20 UTC)

<p>Using python code, I copied a colornode and set below/above-range-colors as I need specific colors for scalar values out of the range. The below/above-range-color show correctly on scalar volume node. However, when applied the colornode to model scalars, it can set the range on  scalars but didn’t show the below/above-range-colors.</p>
<p>cmap = slicer.util.getNode(“vtkMRMLColorTableNodeRainbow”)<br>
cmap.GetScalarsToColors().SetRange(20, 80)<br>
cmap.GetScalarsToColors().UseAboveRangeColorOn()<br>
cmap.GetScalarsToColors().SetAboveRangeColor(0.8, 0,  1,  1)<br>
cmap.GetScalarsToColors().UseBelowRangeColorOn()<br>
cmap.GetScalarsToColors().SetBelowRangeColor(0.82, 0.82, 0.82, 1)</p>
<p>this below/aboveRangeColor works for volume, but didn’t work for model scalars. I need the ranged scalars show for a model in Slicer.  Any suggestions are greatly appreciated.</p>

---

## Post #2 by @lassoan (2021-08-16 05:42 UTC)

<p>Above/below range is not supported and it accidentally works for volumes because we did not explicitly disabled it. Adding proper support for out-of-range values would be probably significant effort (saving into colormap files, propagating to every display pipeline where colors can be used, etc.), but if you implement it then most likely we can integrate it into Slicer core. However, you are probably much better off if you just add one color above and one color below your “valid” color range. Values above/below the colormap’s range use the last/first value of the colormap.</p>

---

## Post #3 by @wabwan25 (2021-08-17 01:01 UTC)

<p>I worry that adding one color below the range will change the mapping slope from scalars to colors which I want to keep. Thank you very much for the answering.</p>

---

## Post #4 by @lassoan (2021-08-17 03:11 UTC)

<p>If you use the same color table and do not specify above/below range values then the color mapping will match.</p>
<p>By default, voxel values are volumes are mapped by via window/level to 0-255 range of the color table. If you use a procedural color map (such as RedGreenBlue or PET-DICOM) then it can simplify things if you bypass this window/level mapping by enable direct color mapping using <code>volumeNode.GetDisplayNode().SetScalarRangeFlag(slicer.vtkMRMLDisplayNode.UseDirectMapping)</code>.</p>

---
