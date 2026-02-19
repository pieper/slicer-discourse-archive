---
topic_id: 8832
title: "Hardware For Slicer"
date: 2019-10-18
url: https://discourse.slicer.org/t/8832
---

# Hardware for slicer

**Topic ID**: 8832
**Date**: 2019-10-18
**URL**: https://discourse.slicer.org/t/hardware-for-slicer/8832

---

## Post #1 by @UNSW_MRI (2019-10-18 14:21 UTC)

<p>Hi,<br>
as I am about some new hardware which will partly be used to render and segment high resolution pre-clinical MRI and CT images (including DTI fibre tracts) with slicer I was wondering if someone can give me a hint.<br>
Currently I have 2 different options:<br>
Either I can get a cheaper CPU, which leaves me with some budget for a dedicated GPU or I get a higher end CPU and use integrated graphics. Here are the specs of both options:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beb45e07a882b43fe89c6623272ec7be5977f45d.png" alt="image" data-base62-sha1="rd39A6emaNQDGooPCl1EP9u10Rf" width="600" height="162"><br>
+some graphics card.<br>
Or alternatively:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c72785476b49d6c1e53b8a549370757933a87755.png" alt="image" data-base62-sha1="spNGJ7YGIIhfjQGmJflVQKDI6a1" width="586" height="154"><br>
without graphics card.<br>
Any opinions abpout the preferred specs for using slicer would be appreciated.<br>
Essentially this is probably a question about the relative impaortance of CPU vs graphics card in general slicer applications.<br>
Thanks for your help.</p>

---

## Post #2 by @Chris_Rorden (2019-10-18 15:04 UTC)

<p>The Ryzen 3900X does not include an integrated GPU. The Intel does have a weak integrated (UHD Graphics 630). The 3900X includes a heat sink (Wraith Prism). Assuming you build the AMD system without the ML360R, that should give you about $140 for a GPU.</p>
<p>I am sure others can comment, but my sense is that Slicer likes a lot of system RAM and having a graphics card with a good amount of dedicated video RAM will help a lot. I would think the 8 core AMD 3700X ($330 with cooler) would give you the budget for a better graphics card. Since the popular diffusion tools Eddy, Topup and Probtrackx support CUDA but not OpenCL, I think you would want an Nvidia GPU rather than AMD and you would want at least 6Gb of video RAM (in my experience, those tools are more constrained by video RAM than GPU cores).</p>
<p>I would also reserve some money for an inexpensive slow spinning hard disk to complement your fast SSD - diffusion data will fill up a 500 Gb SSD very quickly.</p>

---
