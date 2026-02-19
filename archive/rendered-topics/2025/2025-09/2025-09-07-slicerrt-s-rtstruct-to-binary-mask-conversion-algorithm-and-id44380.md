---
topic_id: 44380
title: "Slicerrt S Rtstruct To Binary Mask Conversion Algorithm And"
date: 2025-09-07
url: https://discourse.slicer.org/t/44380
---

# SlicerRT’s RTSTRUCT to Binary Mask Conversion Algorithm and Dice Coefficient Calculation

**Topic ID**: 44380
**Date**: 2025-09-07
**URL**: https://discourse.slicer.org/t/slicerrt-s-rtstruct-to-binary-mask-conversion-algorithm-and-dice-coefficient-calculation/44380

---

## Post #1 by @azam (2025-09-07 16:21 UTC)

<p>Hello everyone,</p>
<p>I need to calculate the Dice coefficient for my organs using Python code, independently from 3D Slicer. I have already written the code for calculating this coefficient and posted it at the following link:</p>
<p>“<a href="https://discourse.itk.org/t/dice-coefficient-calculation-in-python/7628/2%E2%80%9D" rel="noopener nofollow ugc">https://discourse.itk.org/t/dice-coefficient-calculation-in-python/7628/2”</a></p>
<p>under the title “Dice Coefficient Calculation in Python”.</p>
<p>As I mentioned there, the Dice coefficient value calculated by my code is different from the value obtained by  3D Slicer.</p>
<p>Following up on that discussion, I would like to add the following question:</p>
<p>Could you please explain in detail the algorithm that Slicer (or SlicerRT) uses to convert RTSTRUCT contour data into a binary labelmap mask? Specifically, does it perform slice-by-slice 2D polygon filling or true 3D volumetric rasterization? Does it apply any interpolation, hole filling, or other morphological operations? And how does it handle alignment between the contour points and the CT image grid (spacing, orientation, and origin)?</p>
<p>Thanks a lot</p>

---

## Post #2 by @cpinter (2025-09-07 18:18 UTC)

<p>You can find most of this information in the following journal paper and PhD dissertation. There is a paper specifically about planar contours to closed surface conversion that is referenced from these.</p>
<p>Pinter, C., Lasso, A., &amp; Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. <a href="https://doi.org/10.1016/j.cmpb.2019.02.011">https://doi.org/10.1016/j.cmpb.2019.02.011</a></p>
<p>(<a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf">https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf</a>)</p>
<p><a href="https://qspace.library.queensu.ca/handle/1974/26422">https://qspace.library.queensu.ca/handle/1974/26422</a></p>

---
