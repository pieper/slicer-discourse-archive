---
topic_id: 17318
title: "Trying To Create Custom Dti Volume"
date: 2021-04-25
url: https://discourse.slicer.org/t/17318
---

# Trying to create custom DTI volume

**Topic ID**: 17318
**Date**: 2021-04-25
**URL**: https://discourse.slicer.org/t/trying-to-create-custom-dti-volume/17318

---

## Post #1 by @haz_lanz (2021-04-25 23:22 UTC)

<p>Hello,</p>
<p>I am trying to use the diffusion tractography capabilities of 3DSlicer to visualise some data I have collected from my PhD research. It is similar to diffusion weighted MRI but does not produce diffusion weighted images. My data is processed in such a way that I end up with vectors at various coordinates in 3D space (these vectors represent the directions of collagen fibre tracts).</p>
<p>Essentially what I would like to do is jump into the “diffusion mri analysis pipeline” so I start with a custom DTI volume in slicer. i.e. I would like to generate a custom version of slide 42/107 from: <a href="https://spujol.github.io/SlicerDiffusionMRITutorial/SlicerDiffusionMRITutorial_SoniaPujol.pdf" rel="noopener nofollow ugc">here</a> .</p>
<p>My current approach has been to try and create a new volume following the process <a href="https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository#Create_a_new_volume" rel="noopener nofollow ugc">here</a> but I cannot seem to find a way to input a custom tensor field. Does anyone know if this is possible or whether there is a better way of achieving what I’m trying to do?</p>
<p>Thank you, please let me know if anything needs clarifying,</p>
<p>Harry</p>

---

## Post #2 by @pieper (2021-04-26 15:11 UTC)

<p>You need to be sure to make a <code>vtkMRMLDiffusionTensorVolumeNode</code> and manipulate the array as described <a href="https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository#Access_values_in_a_DTI_tensor_volume">here</a>.  You’ll need to determine the best method to estimate tensors from the vectors you have.</p>

---

## Post #3 by @haz_lanz (2021-04-26 16:19 UTC)

<p>Thank you, from a lot of fiddling I have managed to do it by creating a vtkFloatArray and adding it to imageData with the line <code>imageData.GetPointData().SetTensors(tensorarray)</code> and then <code>volumeNode.SetAndObserveImageData(imageData)</code>. With most of the other steps the same as in the documentation you linked.</p>

---

## Post #4 by @lassoan (2021-04-26 23:26 UTC)

<p>You can also visualize vector fields very nicely, without converting them to tensors. All you need to do is to select Description-&gt;Transform in the “Add data” window. You can then use the field using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#display">Transforms display infrastructure</a>. You can also use the vector field to warp any nodes, invert the field, fit b-spline to it, etc.</p>

---
