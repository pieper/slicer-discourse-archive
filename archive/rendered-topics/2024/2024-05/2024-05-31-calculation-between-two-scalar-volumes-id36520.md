---
topic_id: 36520
title: "Calculation Between Two Scalar Volumes"
date: 2024-05-31
url: https://discourse.slicer.org/t/36520
---

# Calculation between two scalar volumes

**Topic ID**: 36520
**Date**: 2024-05-31
**URL**: https://discourse.slicer.org/t/calculation-between-two-scalar-volumes/36520

---

## Post #1 by @mssm (2024-05-31 10:42 UTC)

<p>Dear respected experts,</p>
<p>I have two Dicom volumes (Volume A,  Volume B). The positions are exactly same.</p>
<p>I would like to create a new volume by performing calculations on each voxel value.<br>
Specifically, I would like to perform the calculation α*A + (1-α)*B and create a new volume, but what function should I use to do this in 3D Slicer?<br>
I have already tried the “Add Scalar Volume” function, but I couldn’t make it.</p>
<p>I can visualize the image, but I need a dicom volume data for the image.</p>
<p>Thank you in advance.</p>
<p>A neurosurgeon from Japan</p>

---

## Post #2 by @cpinter (2024-05-31 11:29 UTC)

<p>I would use numpy to do this. It is easy to get the numpy array from volumes and then moving the result back to a volume. You can get the idea looking for example at this script in the script repository:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one</a></p>

---

## Post #3 by @mssm (2024-05-31 15:47 UTC)

<p>Thank you for your kind advice. It is a bit difficut for me, but I am going to try the method you taught me. Thanks again.</p>

---

## Post #4 by @mssm (2024-08-14 16:39 UTC)

<p>I was managed to make a script to make a fusion of two volumes. Thanks, cpinter!</p>
<pre data-code-wrap="python"><code class="lang-python">#  name of volume data, BONE and VESSEL
#  alfa-blending of BONE and VESSEL with a certain alfa value.

volumenode_A = slicer.util.getNode("BONE")
array_A = slicer.util.arrayFromVolume(volumenode_A)
volumenode_B = slicer.util.getNode("VESSEL")
array_B = slicer.util.arrayFromVolume(volumenode_B)
alfa = 0.05  # change this value as you like
array_C = array_A * (1 - alfa) + array_B * alfa
volumenode_C = slicer.modules.volumes.logic().CloneVolume(volumenode_A, "Calc")
slicer.util.updateVolumeFromArray(volumenode_C, array_C)
</code></pre>

---
