---
topic_id: 48373
title: "Volume Rendering TDR ERROR CODE 7 issue persists"
date: 2026-10-01
url: https://discourse.slicer.org/t/48373
last_bumped: 2026-10-07T18:42:20.949Z
---

# Volume Rendering TDR ERROR CODE 7 issue persists

**Topic ID**: 48373
**Date**: 2026-10-01
**URL**: https://discourse.slicer.org/t/volume-rendering-tdr-error-code-7-issue-persists/48373

---

## Post #1 by @ThomasVanParys (2026-10-01 14:19 UTC)

<p>Hello,</p>
<p>I have a large mCT volume which I have halved and converted to an .nrrd volume (1.32 GB) which is succesfully imported into 3DSlicer. However, when I attempt to use the volume rendering window and shift the contrast using 8-bit or 16-bit mCT bone modality, it immediately crashes with NVIDIA/graphics TDR Error Code 7.</p>
<p>I am working on a dedicated 3D imaging desktop with 128GB ram and the latest CPU/GPU specs. However, the TDR timeout issue has continued after many resolution attempts:<br>
NVIDIA driver update, desktop restart, with tests Geekbench and Cinebench CPU and GPU is running as they should be.</p>
<p>Any advice is appreciated!<br>
Thank you,<br>
Tom</p>

---

## Post #2 by @muratmaga (2026-10-01 16:16 UTC)

<p>What is your specific GPU model? Can you provide a screenshot of your Volumes module with volume information expanded? I want to see exact dimensions of your dataset and data type.</p>
<p>Quick things to check:</p>
<ol>
<li>Make sure your rendering method if GPURaycasting (not MultiVolume)</li>
<li>Also make sure quality is Normal not adaptive.</li>
</ol>

---

## Post #3 by @ThomasVanParys (2026-10-02 08:55 UTC)

<p>System specs:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439f8b8ebcd4722215811ff28fbf3f98a61cf236.png" data-download-href="/uploads/short-url/9EdOuDdoT4f6jbSimHLgRJKvwWy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/439f8b8ebcd4722215811ff28fbf3f98a61cf236_2_276x375.png" alt="image" data-base62-sha1="9EdOuDdoT4f6jbSimHLgRJKvwWy" width="276" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/439f8b8ebcd4722215811ff28fbf3f98a61cf236_2_276x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/439f8b8ebcd4722215811ff28fbf3f98a61cf236_2_414x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/439f8b8ebcd4722215811ff28fbf3f98a61cf236_2_552x750.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1054×1426 48.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Volumes module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2b69756d1c7d27c9f50d142774e4813fccd136c.jpeg" data-download-href="/uploads/short-url/wlB6HwgdstBMKfprxSN7VGuqs5S.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2b69756d1c7d27c9f50d142774e4813fccd136c_2_444x375.jpeg" alt="image" data-base62-sha1="wlB6HwgdstBMKfprxSN7VGuqs5S" width="444" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2b69756d1c7d27c9f50d142774e4813fccd136c_2_444x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2b69756d1c7d27c9f50d142774e4813fccd136c_2_666x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2b69756d1c7d27c9f50d142774e4813fccd136c_2_888x750.jpeg 2x" data-dominant-color="232221"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1620 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Volume rendering was always set to Normal quality and VTK GPU Ray Casting mode.<br>
Thank you for the help Murat!<br>
Tom</p>

---

## Post #4 by @muratmaga (2026-10-02 17:29 UTC)

<p>This specs are oonly for the computer (CPU + RAM etc), and they are good. But it doesn’t list the GPU. Go to your task manager and switch to gpu and capture the model and specs from there.</p>
<p>Your volume would require a GPU with at least 24GB of texture memory to work.</p>

---

## Post #5 by @ThomasVanParys (2026-10-07 10:56 UTC)

<p>Hi Murat,<br>
Apologies for the delay in responding. The desktop has a NVIDIA Quatro RTX 4000, total GPU memory: 110 GB, Shared GPU memory: 102 GB.<br>
I have spoken with our faculty IT about increasing the TDR delay value in Registry, or use CPU based volume rendering instead. I am at a loss here, because the specs seem fine.<br>
Open to ANY suggestions.<br>
Thank you!</p>

---

## Post #6 by @muratmaga (2026-10-07 15:00 UTC)

<p>That graphics card has only 8GB of dedicated memory. It is surprising, it even tries to show the data. Most often it simply shows an empty box.</p>
<p>Given your scan is a multiple unrelated objects, you best bet is to use the ImageStacks in SlicerMorph, and import one by one as individual volumes using the ROI option. Otherwise your data is too big for that gpu.</p>

---

## Post #7 by @ThomasVanParys (2026-10-07 16:00 UTC)

<p>Thank you Murat - as this machine was setup by our faculty IT for the specific use of 3D imaging and handling mCT datasets, do you recommend upgrading the GPU graphics card to one with more dedicated memory? If so, what minimum GB do you recomment?</p>

---

## Post #8 by @muratmaga (2026-10-07 18:42 UTC)

<p>RTX4000 is the lowest of RTX series. I would suggest something like the newer A5000, or gaming cards like geforce 4090 ro 5090. It is really a function of available power in the system, airflow and the slots.</p>

---
