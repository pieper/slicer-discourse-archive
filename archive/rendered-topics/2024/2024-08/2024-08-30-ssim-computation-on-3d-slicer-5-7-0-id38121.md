# SSIM computation on 3D slicer 5.7.0

**Topic ID**: 38121
**Date**: 2024-08-30
**URL**: https://discourse.slicer.org/t/ssim-computation-on-3d-slicer-5-7-0/38121

---

## Post #1 by @Offormata_Osunkwor (2024-08-30 01:53 UTC)

<p>Is there any module on slicer for computing structural similarity index? or any python code will be much appreciated.</p>

---

## Post #2 by @lassoan (2024-09-01 22:44 UTC)

<p>SSIM is not used commonly in medical image computing and I’m not aware of any Slicer extension computing it. However, many implementations are available in Python that you can install and run in Slicer by a few lines of Python code. What are you planning to use SSIM for?</p>

---

## Post #3 by @Offormata_Osunkwor (2024-09-02 00:27 UTC)

<p>Hi Andras,</p>
<p>Thanks for your response. I wanna use it to compare different phases of phased binned 4DCT.</p>

---

## Post #4 by @lassoan (2024-09-02 02:34 UTC)

<p>Thanks for the clarification. For comparison of CT images, I would recommend using similarity metrics that have been specifically developed for this purpose. Several are available in ITK/SimpleITK (that is bundled with Slicer) - see for example in a <a href="https://discourse.itk.org/t/metric-to-compare-two-images-using-simpleitk/3351/2">topic in the ITK forum</a>.</p>

---
