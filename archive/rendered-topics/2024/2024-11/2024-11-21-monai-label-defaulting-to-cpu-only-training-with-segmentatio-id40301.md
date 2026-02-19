---
topic_id: 40301
title: "Monai Label Defaulting To Cpu Only Training With Segmentatio"
date: 2024-11-21
url: https://discourse.slicer.org/t/40301
---

# Monai Label defaulting to CPU only training with segmentation model

**Topic ID**: 40301
**Date**: 2024-11-21
**URL**: https://discourse.slicer.org/t/monai-label-defaulting-to-cpu-only-training-with-segmentation-model/40301

---

## Post #1 by @Saim_ali (2024-11-21 04:07 UTC)

<p>Hi all, novice in programming so I am learning as I go.</p>
<p>I have a set of CT scans with custom labels and I have figured out how to employ Monai Label to customize the segmentation model but I am having some trouble using CUDA for training. I believe I have a capable GPU (RTX 2070 super), I checked nvidia-smi in terminal and it says CUDA 12.7.</p>
<p>I installed PyTorch 2.3.1 w/ Cuda 11.8 in my python environment before installing monai label with Pip but the monai label install uninstalls torch 2.3.1/cuda11.8 and installs 2.5.1 instead.</p>
<p>I am now training the segmentation model with my dataset but it is using cpu and taking quite a long time.</p>
<p>TLDR: I have CT scans + labels but can’t figure out how properly use monai label with cuda</p>

---
