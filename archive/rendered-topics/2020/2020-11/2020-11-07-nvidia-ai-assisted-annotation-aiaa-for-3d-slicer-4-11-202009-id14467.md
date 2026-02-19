---
topic_id: 14467
title: "Nvidia Ai Assisted Annotation Aiaa For 3D Slicer 4 11 202009"
date: 2020-11-07
url: https://discourse.slicer.org/t/14467
---

# Nvidia AI-assisted annotation (AIAA) for 3D Slicer (4.11.20200930)

**Topic ID**: 14467
**Date**: 2020-11-07
**URL**: https://discourse.slicer.org/t/nvidia-ai-assisted-annotation-aiaa-for-3d-slicer-4-11-20200930/14467

---

## Post #1 by @scorey1983 (2020-11-07 02:36 UTC)

<p>Operating system: WIN 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: Today, when I opened the slicer, I found that the module could not be started. The program prompts no response.</p>

---

## Post #2 by @lassoan (2020-11-07 05:50 UTC)

<p>The default NVidia AIAA server that we set up for helping Slicer users is open for everyone. As a result, it is time-to-time overwhelmed with amount of requests. As of now, it is up and running.</p>
<p>If you find that anytime the server does not respond then wait some time (few ten minutes or few hours) and try again, or set up your own server (as described in the link provided in the <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#nvidia-ai-assisted-annotation-aiaa-for-3d-slicer">documentation</a>).</p>

---

## Post #3 by @scorey1983 (2020-11-08 10:23 UTC)

<p>After reporting the problem, the module recovered for a short time. But since yesterday, I can’t connect to the server again.</p>

---

## Post #4 by @lassoan (2020-11-08 15:12 UTC)

<p>The service is under constant monitoring, so we receive notifications about all outages. When the server is knocked off so hard that it cannot recover by itself then it has to be physically reset by someone, which takes more time because most of us are working from home now.</p>
<p>We’ll reset the server today and soon update to the latest version of the server, which might work more robustly and have a few more features (unfortunately, it may also have a bit smaller number of available trained demo models). If the upgrade does not help with the overloads then we could check if NVidia could implement some throttling mechanism, which would allow us to prevent a user from sending unreasonably large amount of requests.</p>
<p>The server will remain available for free, without any quality of service guarantee. If you want to have a more reliable service then you need to set it up on your own hardware (the software and trained models are freely available) or look for a paid service.  The hardware requirements listed in NVidia AIAA documentation are for model training, if you just want to use pre-trained models then the GPU memory requirement is about half or less.</p>

---

## Post #5 by @Laode_Muhammadin_Mat (2022-04-10 12:24 UTC)

<p>hi, I’m new to using this application program,<br>
can we do Nvidia Clara training via 3D slicer?</p>
<p>For example, I am currently collecting MSCT of congenital heart disease and segmenting each part of the heart and existing congenital abnormalities.<br>
Can Nvidia Clara training be done from the segmentation model that I have in 3d slicer so that an AIAA model can be generated which can later make automatic segmentation?</p>

---

## Post #6 by @lassoan (2022-04-10 17:57 UTC)

<p>Developers of NVIDIA-AIAA have changed their focus on working on MONAILabel instead. You can do both training and inference using the <a href="https://github.com/Project-MONAI/MONAILabel/#monai-label">MONAILabel extension of Slicer</a>.</p>

---

## Post #7 by @scorey1983 (2022-05-18 02:09 UTC)

<p>Is the Nvidia AIAA module in the Segment Editor not available now?</p>

---

## Post #8 by @scorey1983 (2022-05-18 04:23 UTC)

<p>The new MONAI Label also does not have a model for lung nodule segmentation</p>

---

## Post #9 by @lassoan (2022-05-25 12:18 UTC)

<p>The NVIDIA AI-assisted annotation extension is available now for both the Slicer Stable Release and Slicer Preview Release.</p>

---

## Post #10 by @Laode_Muhammadin_Mat (2022-06-18 11:27 UTC)

<p>if i want to use nvidia clara, should i use quadro series like RTX A5000, or is it the same as using geforce series like rtx 3080 ti? and for the minimum recommended VRAM?</p>

---

## Post #11 by @lassoan (2022-06-18 12:47 UTC)

<p>GeForce RTX works well. Probably 16GB is sufficient for most models, but 24GB may be better - just to be safe and a bit more future-proof.</p>
<p>Note that there may be legal/licensing limitations in using a GeForce GPU in a server shared via network.</p>

---
