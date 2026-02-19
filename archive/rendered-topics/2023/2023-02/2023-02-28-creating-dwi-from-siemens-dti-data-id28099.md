---
topic_id: 28099
title: "Creating Dwi From Siemens Dti Data"
date: 2023-02-28
url: https://discourse.slicer.org/t/28099
---

# Creating DWI from siemens DTI data

**Topic ID**: 28099
**Date**: 2023-02-28
**URL**: https://discourse.slicer.org/t/creating-dwi-from-siemens-dti-data/28099

---

## Post #1 by @Shabnam_R (2023-02-28 17:15 UTC)

<p>Operating system: Windows 10, Core™ i7<br>
Slicer version: 4.13<br>
Expected behavior: I want to create the DWI from the DTI that I have from siemens scanner, But the files that I have is different from the one that I can find in tutorial. Shall I convert these DICOM file first?</p>
<p>Actual behavior:</p>

---

## Post #2 by @pieper (2023-02-28 19:12 UTC)

<p>Most cases are handled by the <a href="https://github.com/SlicerDMRI/SlicerDcm2nii">SlicerDcm2nii</a>, but if not you should try referring to the <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Introduction">dcm2niix</a> page for more info and maybe you can run it manually.</p>

---

## Post #3 by @ebrahim (2023-03-01 14:38 UTC)

<p>You mean create DTI from DWI?<br>
Look for the “diffusion tensor estimation” module in the SlicerDMRI extension.</p>

---

## Post #4 by @Shabnam_R (2023-03-01 14:40 UTC)

<p>Yes, I convert them to nii, now I can create dwi from them. thank you!</p>

---

## Post #5 by @Shabnam_R (2023-03-01 14:42 UTC)

<p>I am using this module, but I am not sure whether it is correct or not? because I am trying to create the tractography for muscles and this module mostly designed for brain.</p>

---

## Post #6 by @ebrahim (2023-03-01 15:14 UTC)

<p>For just DTI estimation it should not matter if it’s brain or something else</p>
<p>For other things, like tractography, it depends. They can be designed for brain only (e.g. using priors or defining stopping conditions based on brain imaging concepts), or they can be more general. I am not sure about SlicerDMRI tools specifically, maybe someone can comment who knows about that.</p>

---

## Post #7 by @Shabnam_R (2023-03-01 16:21 UTC)

<p>Thank you! I just started to tractography and I am a bit new.</p>

---
