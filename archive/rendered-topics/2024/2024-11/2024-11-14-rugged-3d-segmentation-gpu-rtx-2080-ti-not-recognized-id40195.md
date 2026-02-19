---
topic_id: 40195
title: "Rugged 3D Segmentation Gpu Rtx 2080 Ti Not Recognized"
date: 2024-11-14
url: https://discourse.slicer.org/t/40195
---

# Rugged 3D Segmentation - GPU ( RTX 2080 Ti) not recognized

**Topic ID**: 40195
**Date**: 2024-11-14
**URL**: https://discourse.slicer.org/t/rugged-3d-segmentation-gpu-rtx-2080-ti-not-recognized/40195

---

## Post #1 by @bkasmai (2024-11-14 14:23 UTC)

<p>I have an Nvidia GeForce RTX 2080 Ti card with 11.0 GB of dedicated GPU memory and 32 GB of shared GPU memory. The card is recognized by all of my applications except TotalSegmentator. This is not a big issue as I am happy to wait as long as it takes to get a smooth segmentation. My understanding is that if fast mode is not selected, the outcome would be the same with or without GPU utilization. My CT scan has a slice thickness of 1 millimeter, but the 3D segmentation is very rugged. Any advice would be appreciated. CUDA Installation went fine with no problem.</p>

---

## Post #2 by @mau_igna_06 (2024-11-14 20:18 UTC)

<p>Fast mode sets another CT resample resolution before doing the AI segmentation.</p>
<blockquote>
<p><code>--fast</code>: For faster runtime and less memory requirements use this option. It will run a lower resolution model (3mm instead of 1.5mm).</p>
</blockquote>
<p><a href="https://github.com/wasserth/TotalSegmentator/?tab=readme-ov-file#advanced-settings" rel="noopener nofollow ugc">source</a></p>
<p>I would guess this resampling is isotropic so there is 8x difference between fast and normal options</p>

---
