# intensity correction and spatial normalization

**Topic ID**: 33548
**Date**: 2023-12-28
**URL**: https://discourse.slicer.org/t/intensity-correction-and-spatial-normalization/33548

---

## Post #1 by @zhudao176 (2023-12-28 17:00 UTC)

<p>Operating system:windows11<br>
Slicer version:5.5.0<br>
Expected behavior:<br>
I want to use  3D slicer to automatically delineate the striatum from brain PET/MRI data and obtain radiomics data, but preprocessing is required before segmentation（intensity correction and spatial normalization）<br>
Actual behavior:I don’t know how to operate and which extension plugin to use？</p>

---

## Post #2 by @pieper (2023-12-28 18:58 UTC)

<p>It’s not directly integrated with Slicer, but you should be able to use SynthSeg on your data and load the results in Slicer for further analysis.</p>

---
