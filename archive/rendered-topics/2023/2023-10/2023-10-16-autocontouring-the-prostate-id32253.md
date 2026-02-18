# Autocontouring the prostate 

**Topic ID**: 32253
**Date**: 2023-10-16
**URL**: https://discourse.slicer.org/t/autocontouring-the-prostate/32253

---

## Post #1 by @swin (2023-10-16 14:17 UTC)

<p>Hello,</p>
<p>Could anyone recommend an extension to autocontour the prostate on either MRI or CT scan?</p>
<p>Thanks</p>

---

## Post #2 by @Cosmin_Ciausu (2023-10-16 19:19 UTC)

<p>Hi,</p>
<p>Following up on Sarah’s question, I wanted to highlight the current state of automatic prostate delineation/segmentation of the prostate in slicer3d.</p>
<p>So far as my knowledge goes, there is not any active extension that proposes this. However, publicly available AI-based prostate segmentation tools already exist outside of Slicer.</p>
<p>Potential AI-based pre-trained models candidates could be the official nnUNet-based prostate segmentation model, trained on PROMISE12 (Task024_Promise), or newer models, also based on nnUNet framework, such as the <a href="https://github.com/bamf-health/aimi-prostate-mr" rel="noopener nofollow ugc">BAMF prostate segmentation tool</a>, or also MONAI-based (<a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/prostate_mri_anatomy" rel="noopener nofollow ugc">prostate158</a>).<br>
These tools mentioned above were trained on T2W MRI images.</p>
<p>There is also an active effort to integrate dockerized AI-based pre-trained models inside of Slicer, such as the <a href="https://github.com/MHubAI/SlicerMRunner" rel="noopener nofollow ugc">SlicerMRunner</a> extension, from the Medical Hub (mhub) initiative.</p>

---
