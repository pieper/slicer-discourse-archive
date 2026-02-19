---
topic_id: 8070
title: "Dwi Convert Nifti To Nrrd Gives Extremely Small File Size Un"
date: 2019-08-17
url: https://discourse.slicer.org/t/8070
---

# DWI Convert: .Nifti to .nrrd gives extremely small file size, unable to run in UKF Tractography

**Topic ID**: 8070
**Date**: 2019-08-17
**URL**: https://discourse.slicer.org/t/dwi-convert-nifti-to-nrrd-gives-extremely-small-file-size-unable-to-run-in-ukf-tractography/8070

---

## Post #1 by @Bex (2019-08-17 19:26 UTC)

<p>Operating system: iMac<br>
Slicer version: 4.10.2<br>
Expected behavior: DWI Nifti file with 54 different diffusion-sensitizing gradient directions would convert to .nrrd and generate a file size similar to the sample data online (42 directions, 85MB) and run smoothly in UKF Tractography like the sample dataset.<br>
Actual behavior: DWI Nifti file with 54 different diffusion-sensitizing gradient directions generates a .nrrd file of 4.5MB and gives error when run in UKF Tractography (error:  libc++abi.dylib: terminating). Strangely, my converted .nifti to .nrrd file of 4.5MB runs smoothly in other tractography modules, but not the UKF module.</p>
<p>Is it normal to have such a small .nrrd file size or could it be losing info during convert to .nrrd?</p>

---

## Post #2 by @ljod (2019-08-17 19:49 UTC)

<p>If you have DICOM please use the dcm2nii module instead to get nrrd.</p>
<p>What other error text appeared before that last error?</p>

---
