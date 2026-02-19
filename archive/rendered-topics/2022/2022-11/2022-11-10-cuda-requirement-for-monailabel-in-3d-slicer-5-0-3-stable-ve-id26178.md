---
topic_id: 26178
title: "Cuda Requirement For Monailabel In 3D Slicer 5 0 3 Stable Ve"
date: 2022-11-10
url: https://discourse.slicer.org/t/26178
---

# CUDA requirement for MONAILabel in 3D Slicer 5.0.3 stable version

**Topic ID**: 26178
**Date**: 2022-11-10
**URL**: https://discourse.slicer.org/t/cuda-requirement-for-monailabel-in-3d-slicer-5-0-3-stable-version/26178

---

## Post #1 by @platanus (2022-11-10 06:43 UTC)

<p>Dear 3D-Slicer members</p>
<p>Let me know version information by CUDA, CUDNN and tensorflow_gpu that recommended in 3D-Slicer 5.0.3 stable version for modeling segmentation of monai label</p>
<p>System information of my laptop  is as following.</p>
<p>[display]<br>
Operating System: Windows 10 Home, 64-bit<br>
DirectX Version: 12.0<br>
GPU Processor: NVIDIA GeForce RTX 3070 Laptop GPU<br>
Driver Version: 471.51<br>
Driver Type: DCH<br>
Direct3D feature level: 12_1<br>
CUDA Core: 5120<br>
Resizable BAR Yes<br>
Max-Q technology 3rd generation<br>
Dynamic Boost 2.0 Yes<br>
WhisperMode 2.0 Yes<br>
Advanced Optimus No<br>
Maximum graphics performance 100 W<br>
Core clock: 1290 MHz<br>
Memory data rate: 12.00 Gbps<br>
Memory interface: 256-bit<br>
Memory bandwidth: 384.06 GB/s<br>
Total available graphics memory: 16079 MB<br>
Dedicated video memory: 8192 MB GDDR6<br>
System video memory: 0 MB<br>
Shared system memory: 7887 MB<br>
Video BIOS Version: 94.04.4F.00.19<br>
IRQ: Not used<br>
Bus: PCI Express x8 Gen3<br>
Device Id: 10DE 249D 20141A58<br>
Part number: 4735 0010</p>
<p>Please let me know version information by CUDA, CUDNN and tensorflow_gpu that recommended in 3D-Slicer 5.0.3 stable version for modeling segmentation of monai label.</p>

---

## Post #2 by @rbumm (2022-11-10 12:22 UTC)

<p>You can check the CUDA version within Slicer 5.0.3 as follows:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c76d613072e4238f5a552022d4751fb0e69b965.png" alt="image" data-base62-sha1="hL3OktOjAxmmUYRQjXWKQ6tOXwV" width="309" height="118"></p>
<p>So on my laptop, the CUDA version is 11.3.</p>

---

## Post #3 by @platanus (2022-11-14 09:44 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Thank you for answering my question.</p>
<p>For working 3D-Slicer 5.0.3 stable version based on windows 11 64bit OS , I installed in (my laptop) pc as following.<br>
Python 3.9<br>
monailabel 0.5.2<br>
monai 1.0.1<br>
torch 1.1.3<br>
tensorflow-gpu 2.1.0<br>
CUDA 11.3<br>
CUDNN 8.6</p>
<p>And then using PyPi, I conducted command that is ‘python -c "import torch; print(torch.cuda.is_available())’.<br>
The result shows ‘False’.</p>
<p>I think that it can’t conduct torch (with cuda) using gpu.</p>
<p>What should I do for showing ‘False’ into ‘True’ in result of ‘python -c "import torch; print(torch.cuda.is_available())’?</p>
<p>Please, let me know solution of above problem.</p>

---

## Post #4 by @rbumm (2022-11-14 10:31 UTC)

<p>Your laptop with an RTX 3070 GPU should definitely be ready to enable CUDA and use MONIALabel in GPU mode. We have set up a MONAILabel segmentation project during the last 3D Slicer Project week:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/" target="_blank" rel="noopener">NA-MIC Project Weeks</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>On that page is a link <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">How To Setup MONAILabel in Windows 11</a> that should help you with installation. Please follow this step by step, we’ll assist if something does not work.</p>

---

## Post #5 by @platanus (2022-11-14 10:40 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>I solved this problem</p>
<p>when I installed ‘python –m torch-1.7.1-cp39-cp39-win_amd64.whl’, the result of ‘python -c "import torch; print(torch.cuda.is_available())’ shows ‘True’.</p>
<p>Thank you for helping me.</p>

---
