---
topic_id: 10938
title: "Lossy Image Conversion With Fsl Inputs"
date: 2020-03-31
url: https://discourse.slicer.org/t/10938
---

# Lossy image conversion with FSL inputs

**Topic ID**: 10938
**Date**: 2020-03-31
**URL**: https://discourse.slicer.org/t/lossy-image-conversion-with-fsl-inputs/10938

---

## Post #1 by @LearningSlicerYay (2020-03-31 14:36 UTC)

<p>System: Ubuntu 18.04 LTS<br>
Slicer: 4.10.2</p>
<p>Hi everyone,</p>
<p>I previously used the dMRI pipeline to conduct all my diffusion and tractography analyses and everything worked fine. However, I believe I need to use FSL to do some corrections, which outputs to .nii files.</p>
<p>The .nii’s (with 76 volumes) can be opened in Slicer with no issues, but it seems to only recognize the first volume. If I use DWIConvert FSLtoNRRD (with output, and NiftiFSL to NRRD parameters filled and all other areas with the defaults), I get the following error:</p>
<blockquote>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>Error: ReadVolume: Unsupported source pixel type.<br>
Input volume:  float<br>
Output volume: short<br>
The only supported output type is . You may consider using allowLossyConversion option.<br>
However, use this option with caution! Conversion from images of a different type may cause data loss due to rounding or truncation.<br>
terminate called without an active exception</p>
</blockquote>
<p>If I check off “Allow lossy image conversion” it works fine. I’m just wondering what exactly it’s doing to the images - and if there’s any suggestions on how I could perhaps compare the FSL NIFTIs with Slicer’s NRRDs to ensure they’re the same? I’m worried that this may affect the tractography results we get later down the line.</p>
<p>Thanks for your input!</p>

---

## Post #2 by @pieper (2020-03-31 15:35 UTC)

<p>It’s a <a href="https://github.com/BRAINSia/BRAINSTools/blob/a8c0c926a2c183b37786100f0d4d0ceb6725e9b4/DWIConvert/DWIConvertUtils.hxx#L131-L139">data casting issue</a> so if you investigate the types you will be able to tell what data might get lost.</p>
<p>dcm2niix now support nifti/nrrd conversion for dwi data.  You could compare the results.</p>
<p><a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage" class="onebox" target="_blank">https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage</a></p>

---

## Post #3 by @LearningSlicerYay (2020-03-31 16:22 UTC)

<p>Hi Steve,</p>
<p>Thanks for your response. I’ll look into data casting.</p>
<p>Regarding dcm2niix, I don’t think it supports NIFTI-to-NRRD conversion does it? I’m looking to compare the outputs from FSL with the NRRD from dwiconvert, so it’s not the same as using the nifti converted from the raw DICOM data.</p>

---

## Post #4 by @pieper (2020-03-31 19:46 UTC)

<p>Yes, I understand dcm2niix does nifti-nrrd conversion for dwi.  I haven’t used it myself.</p>

---

## Post #5 by @ebrahim (2023-07-11 16:43 UTC)

<p>In case anyone runs into this topic during search as I did:</p>
<p>dcm2niix does not do NIFTI-to-NRRD conversion.</p>
<p>The situation is clarified a bit in <a href="https://discourse.slicer.org/t/nrrd-to-fsl-error-with-dwiconvert/11666/8">this discussion</a>, where it is suggested to use the tools here: <a href="https://github.com/pnlbwh/conversion#introduction" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pnlbwh/conversion: Various mri conversion/modification scripts</a></p>
<p>This is what ended up working for me.</p>

---
