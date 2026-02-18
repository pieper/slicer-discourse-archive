# Voxel extraction , Calculation of GLSZM Failed

**Topic ID**: 14225
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/voxel-extraction-calculation-of-glszm-failed/14225

---

## Post #1 by @Alessio_Romita (2020-10-24 17:43 UTC)

<p>Hi everyone ,<br>
I’m trying to calculate the value of Glszm feature using voxel based extraction.<br>
But I got this erro :IndexError: Calculation of GLSZM Failed.<br>
The setting used are :<br>
voxelSetting:<br>
kernelRadius: 2<br>
maskedKernel: true<br>
initValue: nan<br>
voxelBatch: 10000<br>
This just occurred me with glszm feature, instead with glcm the extraction works.<br>
Thanks to anyone who will help me .</p>

---

## Post #2 by @JoostJM (2020-11-18 18:52 UTC)

<p>Sorry for the late reply. This was a known issue and has since been <a href="https://github.com/Radiomics/pyradiomics/pull/594">fixed</a> in the latest PyRadiomics release (3.0.1). Did you try with the latest version?</p>

---

## Post #3 by @Alessio_Romita (2020-11-20 16:32 UTC)

<p>Hi Joost,<br>
right now I’m just using the glcm features in voxel based extraction. I remembered that I tried to upload it but was the newest version, and the problem still occurred. I will let you know when I will try again with glszm features.</p>

---
