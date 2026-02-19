---
topic_id: 776
title: "Rotate Views Without Rotating Image"
date: 2017-07-27
url: https://discourse.slicer.org/t/776
---

# Rotate Views Without Rotating Image

**Topic ID**: 776
**Date**: 2017-07-27
**URL**: https://discourse.slicer.org/t/rotate-views-without-rotating-image/776

---

## Post #1 by @_jmichael (2017-07-27 14:52 UTC)

<p>Hi all,<br>
I currently have a micro-CT of a phantom that, when loaded into Slicer, appears upside down (there are some file conversions going on before I get to Slicer, so this behaviour is probably correct from a software perspective). Is there a way to rotate my view of the image (e.g. rotate my view of the red slice 180 degrees) without moving the image itself? (e.g. by using the transforms module)</p>
<p>I’ll eventually be segmenting certain structures and performing a surface based registration to other CT images, so while using the transforms module would work, it would mean another transform/coordinate system to keep track of. My problem is really only with visualization so I’d like to avoid that if possible.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2017-07-27 15:05 UTC)

<p>You can use Reformat module to set arbitrary orientation of slice views.</p>

---

## Post #3 by @_jmichael (2017-07-27 15:09 UTC)

<p>Perfect. Just tried and that’s exactly what I was looking for.</p>
<p>Thanks!</p>

---

## Post #4 by @Nicolas_Tempier (2023-08-16 10:17 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> ,<br>
would there be a python script equivalence to this Reformat change please ?</p>
<p>Respectfully,</p>
<p>Nicolas</p>

---

## Post #5 by @lassoan (2023-08-16 10:32 UTC)

<p>In recent Slicer-5.3 versions (and in the soon-to-be-released Slicer-5.4 stable version) you can rotate slices easily like this:</p>
<pre><code class="lang-python">slicer.vtkSlicerReformatLogic.RotateSlice(getNode('vtkMRMLSliceNodeRed'), 0, 180)
</code></pre>
<p>First argument is the slice node, second is the rotation axis index (0, 1, or 2 = horizontal axis, vertical axis, slice normal), third is the rotation angle (180 for flip, 90 for rotation).</p>

---

## Post #6 by @Nicolas_Tempier (2023-08-16 12:02 UTC)

<p>Thank you very much !</p>

---

## Post #7 by @baderstine (2025-02-04 23:03 UTC)

<p>In Slicer 5.6.2, I noticed that when i toggle on/off a vtkMRMLScalarVolumeNode in the Data module, any rotation that i’ve applied gets reset to the default.</p>
<p>Is there a way to set a default value with rotation applied?</p>
<p>I tried this:</p>
<pre><code class="lang-auto">slicer.vtkSlicerReformatLogic.RotateSlice(slicer.util.getNode('vtkMRMLSliceNodeRed'), 2, -90)
orientation = slicer.app.layoutManager().sliceWidget("Red").sliceLogic().GetSliceNode().GetOrientation()
slicer.app.layoutManager().sliceWidget("Red").setSliceOrientation(orientation)
</code></pre>
<p>which returns the following error:</p>
<blockquote>
<p>[VTK] GetSliceOrientationPreset: invalid orientation preset name: Reformat</p>
</blockquote>
<p>since orientation = “Reformat” a string that is not ‘Axial’, ‘Sagittal’, ‘Coronal’, etc.</p>

---
