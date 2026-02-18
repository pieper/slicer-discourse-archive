# Python - Get Node copy to Modify

**Topic ID**: 687
**Date**: 2017-07-14
**URL**: https://discourse.slicer.org/t/python-get-node-copy-to-modify/687

---

## Post #1 by @Filipe_Trocado_Ferre (2017-07-14 12:22 UTC)

<p>I want to modify a copy of the input node and output it. I’m not being able to do that without modifying the input node. How to make a copy?</p>

---

## Post #2 by @pieper (2017-07-14 12:42 UTC)

<p>What kind of node do you want to copy?  What do you mean that the input is modified?</p>
<p>Maybe look at vtkSlicerVolumesLogic::CloneVolume</p>

---

## Post #3 by @Filipe_Trocado_Ferre (2017-07-14 12:50 UTC)

<p>I’m using python. I want to extract a numpy array from a volumeNode (CT Scan) and apply my modifications and then deploy in a different node but with the same characteristics as the input Volume. I’m not being able to ‘clone’ the volume. It always refer to the same data array and it modifies both input and output volume node</p>

---

## Post #4 by @Filipe_Trocado_Ferre (2017-07-14 12:57 UTC)

<p>ok, so using this:</p>
<p><code> outputVolume = slicer.vtkSlicerVolumesLogic().CloneVolume(inputVolume,'out')</code></p>
<p><code>arr = vtk_to_numpy(outputVolume.GetImageData().GetPointData().GetScalars())</code></p>
<p>results in</p>
<blockquote>
<p>:‘NoneType’ object has no attribute ‘GetImageData’</p>
</blockquote>

---

## Post #5 by @lassoan (2017-07-14 13:03 UTC)

<p>CloneVolume only works for scalar volume. Use <a href="http://apidocs.slicer.org/master/classvtkSlicerVolumesLogic.html#af08c6a610b25237da8153f8c6fc005ad">CloneVolumeGeneric()</a> method to clone other types of volumes.</p>

---

## Post #6 by @Filipe_Trocado_Ferre (2017-07-14 13:04 UTC)

<p>This worked:</p>
<p>outputVolume = slicer.vtkSlicerVolumesLogic().CloneVolume(slicer.mrmlScene,inputVolume,‘out’,True)</p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a> . Great job!</p>

---
