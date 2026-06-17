---
topic_id: 21347
title: "Nvidia AIAA on default server, I dont have \"annotation_mri_brain_tumors_t1ce_tc\" model under Segment from Boundary points (DExtr3D). I just have three models brain mri, lung ct covid and spleen annotation. How to get that model?"
date: 2022-01-06
url: https://discourse.slicer.org/t/21347
last_bumped: 2026-06-16T07:37:59.776Z
---

# Nvidia AIAA on default server, I dont have "annotation_mri_brain_tumors_t1ce_tc" model under Segment from Boundary points (DExtr3D). I just have three models brain mri, lung ct covid and spleen annotation. How to get that model?

**Topic ID**: 21347
**Date**: 2022-01-06
**URL**: https://discourse.slicer.org/t/nvidia-aiaa-on-default-server-i-dont-have-annotation-mri-brain-tumors-t1ce-tc-model-under-segment-from-boundary-points-dextr3d-i-just-have-three-models-brain-mri-lung-ct-covid-and-spleen-annotation-how-to-get-that-model/21347

---

## Post #1 by @Akhil_Ratan_Mishra (2022-01-06 17:07 UTC)

<p>Operating system: Windows 11<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @bruce2647 (2026-06-16 07:37 UTC)

<p>It sounds like the full Brain MRI segmentation model package may not be installed in your current setup. The “annotation_mri_brain_tumors_t1ce_tc” model is typically part of the brain tumor annotation workflow used with DExtr3D rather than the default sample models.</p>
<p>You may need to:</p>
<p>• Download the complete Brain MRI segmentation or BraTS model bundle<br>
• Check whether your MONAI Label or annotation server version supports that model<br>
• Verify that the app configuration includes the tumor annotation model in the inference section<br>
• Restart the server after adding the new model files</p>
<p>In many medical imaging workflows, only basic demo models like brain MRI, spleen annotation, or lung CT COVID are included during the initial setup, while tumor-specific segmentation models require separate installation.</p>
<p>Advanced AI-based Brain MRI segmentation workflows often depend on additional pretrained tumor models for accurate neuroimaging and tumor boundary annotation. You can also check the official documentation or GitHub releases to confirm whether that specific model requires a separate download package.</p>

---
