---
topic_id: 30907
title: "Running Monailabel In The Cloud"
date: 2023-08-01
url: https://discourse.slicer.org/t/30907
---

# Running MONAILabel in the cloud

**Topic ID**: 30907
**Date**: 2023-08-01
**URL**: https://discourse.slicer.org/t/running-monailabel-in-the-cloud/30907

---

## Post #1 by @Celina_Hallal (2023-08-01 14:40 UTC)

<p>I’ve been using NVIDIA Clara AI model to segment liver and liver tumors in my local machine without trouble until very recently (An 8GB M1 Mac). I do it mostly for surgical planning, and is the best  way I found until now. But I know the developers recommended to switch to MONAILabel. Now I am having an issue with loading the server, and I really can’t access a remote workstation all the time. Is there anyway I can run MONAILabel using some cloud like Google colab? Thanks <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @rbumm (2023-08-01 15:28 UTC)

<p>For the January 2023 Project Week, we prepared this document:</p>
<p><a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/HowToSetupAWSEC2Server.html">How-to setup AWS EC2 Windows instances to use MONAILabel, deep learning tools, and 3D Slicer</a></p>
<p>However, this GPU-enabled server (NVIDIA A10G, 24GB video RAM) costs around 1-2 $ per hour to run. I have a ready-to-use system in the cloud, but it is only online if needed. With the instructions above you could configure one for yourself, too. But you would need an institutional AWS account and in the end, you would have to set up an untrained MONAILabel liver segmentation with time pressure on that server.</p>
<p>Have you tried the SlicerLiver extension for your purpose?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2734de631c9b64a47abc260c2d712d0745eb77d4.png" data-download-href="/uploads/short-url/5APTiU1OOKWyTB6Dg2wxshU1OpC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2734de631c9b64a47abc260c2d712d0745eb77d4_2_301x500.png" alt="image" data-base62-sha1="5APTiU1OOKWyTB6Dg2wxshU1OpC" width="301" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/2734de631c9b64a47abc260c2d712d0745eb77d4_2_301x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2734de631c9b64a47abc260c2d712d0745eb77d4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2734de631c9b64a47abc260c2d712d0745eb77d4.png 2x" data-dominant-color="F0EEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">312×517 43.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Have not used it yet, but <a href="https://github.com/ALive-research/Slicer-Liver">instructions are here</a>.</p>

---

## Post #3 by @Thibault_Pelletier (2023-08-02 13:45 UTC)

<p>Hi <a class="mention" href="/u/celina_hallal">@Celina_Hallal</a>,</p>
<p>Although it doesn’t support Liver tumor segmentation, you can also try out the <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" rel="noopener nofollow ugc">Slicer RVX Liver Segmentation Extension</a>.</p>
<p>This extension was originally meant for annotating Liver, Liver Vessels and Tumors for MRI and CT.</p>
<p>After installing the extension and its dependencies, you will have access to a MONAI based Liver Segmentation effect in 3D Slicer’s Segment Editor.</p>
<p>Best,<br>
Thibault</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c298b6df876adf962ab714ef0d8991154f6e602f.jpeg" data-download-href="/uploads/short-url/rLtOJlJ1TDMYvbB9cjnqHWC07Sv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c298b6df876adf962ab714ef0d8991154f6e602f_2_690x370.jpeg" alt="image" data-base62-sha1="rLtOJlJ1TDMYvbB9cjnqHWC07Sv" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c298b6df876adf962ab714ef0d8991154f6e602f_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c298b6df876adf962ab714ef0d8991154f6e602f_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c298b6df876adf962ab714ef0d8991154f6e602f_2_1380x740.jpeg 2x" data-dominant-color="717070"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
