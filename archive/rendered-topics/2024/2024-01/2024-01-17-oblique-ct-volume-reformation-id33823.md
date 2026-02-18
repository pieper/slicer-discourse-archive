# Oblique CT volume reformation

**Topic ID**: 33823
**Date**: 2024-01-17
**URL**: https://discourse.slicer.org/t/oblique-ct-volume-reformation/33823

---

## Post #1 by @Anuta (2024-01-17 13:21 UTC)

<p>Hello! I am new to the Slicer and just starting my project. My main intention is to reslice and save some CT volume in angles (X, Y and Z directions), wich I get from external device, without opening the Slicer itself. I also did some search in documentation, but I am not sure, in which direction should I go now.<br>
Firstly, I would like to know, if oblique reformation of the whole volume is possible in Slicer. I found that with “Reformat” module I can rotate individual slices, but I am not sure, if I can save resliced volume as a whole.<br>
Secondly, I would like to know, how to access this module with a python script to pass the angles to the module without typing them down (the whole “Reformat” module is written on C and I didn’t see any example with Python yet).<br>
Looking forward to your answers!</p>

---

## Post #2 by @mau_igna_06 (2024-01-17 14:16 UTC)

<p>Hi</p>
<p>Please check <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolume.html#use-cases" rel="noopener nofollow ugc">here</a>:</p>
<blockquote>
<p><strong>Definition of new axis directions</strong> for your image: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cropvolume.html#interpolated-cropping-options" rel="noopener nofollow ugc">Interpolated cropping options</a> allows the output volume to have different axis directions that the original volume. The output volume’s axis directions will be aligned with the ROI widget’s axes. ROI widget axes can be rotated using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" rel="noopener nofollow ugc">Transforms</a> module.</p>
</blockquote>
<p>That should answer your <code>oblique reformation</code> question</p>
<p>Hope it helps</p>

---

## Post #3 by @Anuta (2024-01-17 14:50 UTC)

<p>Thank you for your answer! As far as I understand, setting new axis direction and reslicing the volume are two different operation. I think, this module won’t allow me to perform reslicing.</p>

---

## Post #4 by @Anuta (2024-01-23 12:17 UTC)

<p>Ok, so the answer is partially the same, as mentioned in the first comment.<br>
One more step is required after applying transformation. In order to perform reslicing in new orientation “Resample Scalar volume” module is required, though I still didn’t find out how to perform all of this programmatically.</p>

---
