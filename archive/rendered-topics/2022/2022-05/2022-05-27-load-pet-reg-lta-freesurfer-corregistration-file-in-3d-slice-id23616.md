# Load PET.reg.lta freesurfer corregistration file in 3D slicer 4.11

**Topic ID**: 23616
**Date**: 2022-05-27
**URL**: https://discourse.slicer.org/t/load-pet-reg-lta-freesurfer-corregistration-file-in-3d-slicer-4-11/23616

---

## Post #1 by @Gonzalo_Rojas_Costa (2022-05-27 22:14 UTC)

<p>Hi:<br>
I corregistered a PET file to a freesurfer data using mri_coreg command. I imported the freesurfer-generated data to 3D Slicer. How can I import the PET.reg.lta file in 3D Slicer?</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @lassoan (2022-05-28 00:26 UTC)

<p>You should be able to convert the <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/LtaFormat">.reg.lta linear transform</a> to an ITK transform. Slicer can read the ITK transform and you can apply it to the PET image.</p>
<p>It seems that <a href="https://github.com/nipy/nitransforms/">nitransforms</a> can do the lta to ITK transform file conversion.</p>

---

## Post #3 by @Gonzalo_Rojas_Costa (2022-05-31 18:24 UTC)

<p>I couldn’t install the nitransforms. Would there be another software that performs the same conversion (.reg.lta linear transform to ITK)?</p>

---
