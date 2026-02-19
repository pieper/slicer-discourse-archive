---
topic_id: 31927
title: "Time Average Of Sequence Of Transforms"
date: 2023-09-27
url: https://discourse.slicer.org/t/31927
---

# Time average of sequence of transforms

**Topic ID**: 31927
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/time-average-of-sequence-of-transforms/31927

---

## Post #1 by @Zimogre (2023-09-27 08:58 UTC)

<p>Hi all,</p>
<p>I am recently working with a time series of volumes. First, I obtained a sequence (Sequence module) of volumes and then registered them using the SequenceRegistration module obtaining the corresponding Transforms and displacement fields. I would like to obtain the time-averaged transformation.  Is there a way in Slicer or also in Python to perform the time average operation over the sequence of transformations?</p>
<p>Also, can I apply mathematical operations (such as invention or composition) to these transforms?<br>
Thanks a lot!</p>

---

## Post #2 by @lassoan (2023-09-28 02:46 UTC)

<p>You can write a small Python code snippet that iterates through the sequence for each time point it exports the transform into a displacement field vector volume, and you copy the voxels of the volume into a numpy array. In the end you can concatenate the arrays and use numpy to compute statistics along any axis (e.g., compute mean along time axis).</p>

---

## Post #3 by @Zimogre (2023-09-28 14:30 UTC)

<p>Thanks for the suggestion! Once the time-averaged displacement field is loaded back in Slcier, how can I apply it on a Volume? Can I convert a Displacement Field into a Transform?<br>
P.S. is there any example of a snippet code like the one you mentioned?</p>

---

## Post #4 by @lassoan (2023-09-28 15:39 UTC)

<aside class="quote no-group" data-username="Zimogre" data-post="3" data-topic="31927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zimogre/48/10062_2.png" class="avatar"> Zimogre:</div>
<blockquote>
<p>Can I convert a Displacement Field into a Transform?</p>
</blockquote>
</aside>
<p>You can load a displacement field image file (e.g., in a nrrd file) as a transform. Or you can manually create a grid transform and set the displacement image into it.</p>

---

## Post #5 by @Zimogre (2023-10-02 15:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="31927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>write a small Python code snippet that iterates through the sequence for each time point it exports the transform into a displacement field vector volume, and you copy the voxels of the volume into a numpy array.</p>
</blockquote>
</aside>
<p>I converted all the Transform nodes into Displacement Fields with:<br>
displacement_field_volume =slicer.modules.transforms.logic().CreateDisplacementVolumeFromTransform(transformNode, referenceVolumeNode, False)</p>
<p>Then I tried to extract the corresponding array in this way:<br>
displacement_field_volume_node = slicer.util.getNode(displacement_field_volume.GetID())<br>
array_displacement_field = slicer.util.arrayFromVolume(displacement_field_volume_node)</p>
<p>But slicer gives the error:<br>
File “/opt/Slicer-4.11.20210226-linux-amd64/bin/Python/slicer/util.py”, line 1443, in arrayFromVolume<br>
narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars()).reshape(nshape)<br>
ValueError: cannot reshape array of size 1720320 into shape (28,160,128)</p>
<p>It seems that the arrayFromVolume tries to reshape all the 3 channels of the displacement fields together, do you know how to solve this?</p>

---
