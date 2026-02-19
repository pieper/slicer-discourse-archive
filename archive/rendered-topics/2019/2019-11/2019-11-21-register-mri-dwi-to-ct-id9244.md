---
topic_id: 9244
title: "Register Mri Dwi To Ct"
date: 2019-11-21
url: https://discourse.slicer.org/t/9244
---

# Register MRI-DWI to CT

**Topic ID**: 9244
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/register-mri-dwi-to-ct/9244

---

## Post #1 by @E.M.Lam (2019-11-21 12:39 UTC)

<p>Hello! I want to register a DWI to a CT image but I cannot select the DWI for general registration because it’s in the wrong node. Is there a possibility to use general registration anyhow?</p>

---

## Post #2 by @pieper (2019-11-21 13:24 UTC)

<p>Hi - you are right, the registration needs a scalar volume, so if you start with a DWI you can use SlicerDMRI extension to estimate the tensor and you will also get a baseline scalar volume.  If the baseline doesn’t lead to good registration you could try other tensor-derived scalars.</p>

---

## Post #3 by @E.M.Lam (2019-11-21 13:32 UTC)

<p>Thanks a lot, that works out perfectly!</p>

---

## Post #4 by @E.M.Lam (2019-11-21 14:26 UTC)

<p>Maybe I answered too quick … Unfortunately it doesn’t work as I expected. I can select the Output Baseline Volume in General Registration but Slicer cannot use or save it.<br>
“That file doesn’t exist.”<br>
Is there anything I have to do with the Volume to make it “exist”?</p>

---

## Post #5 by @pieper (2019-11-21 14:58 UTC)

<p>Hmm, where does that message appear?  Can you paste a screenshot of describe the steps you used?</p>

---

## Post #6 by @E.M.Lam (2019-11-21 15:17 UTC)

<p>The message appears as error when using the General Registration.<br>
After trying it again several times I noticed, that Diffusion Tensor Estimation finished with errors but there are no errors described in the box. So maybe the file doesn’t exist actually.<br>
I first converted the data with Diffusion-weighted DICOM Import (DWIConvert) to nrrd.<br>
I could imagine that Diffusion Tensor Estimation doesn’t work because it’s no diffusion weighted data, but Slicer loaded it this way.</p>

---

## Post #7 by @pieper (2019-11-21 15:19 UTC)

<p>Ah, yes, I think I see what happened.  I’ve noticed that if you have SlicerDMRI installed it is sometimes overzealous at trying to import dicom as DWI even if it’s actually scalar data.  In the Advanced mode of the DICOM module you can turn off the Diffusion Plugin (or just select the scalar option in the list when importing).</p>

---

## Post #8 by @E.M.Lam (2019-11-21 15:29 UTC)

<p>Ok, I could fix that. Thank you for helping me out!</p>

---
