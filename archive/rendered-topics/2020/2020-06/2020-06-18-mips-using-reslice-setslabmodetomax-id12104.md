# MIPs using reslice.SetSlabModeToMax()

**Topic ID**: 12104
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/mips-using-reslice-setslabmodetomax/12104

---

## Post #1 by @rohan_n (2020-06-18 22:10 UTC)

<p>Can someone please explain how the SetSlabNumberOfSlices feature works for displaying MIPs as shown here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections</a></p>
<p>I tried doing this to have the MIP cover just enough slices for the entire volume:</p>
<pre><code>inputVolume = self.inputSelector.currentNode()
img = inputVolume.GetImageData()
rows,cols,slices = img.GetDimensions()
sliceNodeRed = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
appLogic = slicer.app.applicationLogic()
sliceLogicRed = appLogic.GetSliceLogic(sliceNodeRed)
sliceLayerLogicRed = sliceLogicRed.GetBackgroundLayer()
resliceRed = sliceLayerLogicRed.GetReslice()
resliceRed.SetSlabModeToMax()
resliceRed.SetSlabNumberOfSlices(slices) 
sliceNodeRed.Modified()
</code></pre>
<p>But that doesn’t appear to work as intended and I end up having to use a very large value for slab # of slices, like 600.<br>
If I’m doing something similar for the yellow slice because I want to display sagittal MIPs, how would I set slab # of slices so that there is one sagittal MIP for the left half of the volume and another sagittal MIP for the right half?</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @lassoan (2020-06-20 04:43 UTC)

<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="12104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>But that doesn’t appear to work as intended and I end up having to use a very large value for slab # of slices, like 600.</p>
</blockquote>
</aside>
<p>For a MIP covering an entire volume 600 slices sounds reasonable. If you want to generate MIP in real-time, I would recommend to use Volume Rendering module with Display / Rendering → <code>GPU Ray Casting</code>; and Advanced / Techniques / Technique → <code>Maximum Intensity Projection</code>.</p>

---
