---
topic_id: 36626
title: "How To Export Reconstructed Volume And Position Data"
date: 2024-06-06
url: https://discourse.slicer.org/t/36626
---

# How to Export Reconstructed Volume and Position Data

**Topic ID**: 36626
**Date**: 2024-06-06
**URL**: https://discourse.slicer.org/t/how-to-export-reconstructed-volume-and-position-data/36626

---

## Post #1 by @valerie (2024-06-06 17:27 UTC)

<p>Hi,<br>
I made a previous post about live reconstruction of the kidney using Telemed and NDI Aurora, which was somewhat successful (I still have to troubleshoot some things).</p><aside class="quote quote-modified" data-post="1" data-topic="36578">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/ccd318/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/live-volume-reconstruction-using-telemed-and-ndi-aurora/36578">Live volume reconstruction using Telemed and NDI Aurora</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Windows 10 
Slicer version: 4.11.20200930 
Plus version: 2.9.0.20240320-Telemed-Win64 
Expected behavior: Image slice from Telemed moves as tracked by the NDI Aurora. Scout scan projects movement and live reconstruction creates volume. 
Actual behavior: Image slice from Telemed is not moving based on NDI Aurora tracker. Scout scan is not working, and live reconstruction does not work due to scout scan. 
Hi, I am trying to perform live reconstruction of the kidney using Telemed …
  </blockquote>
</aside>
<p>
My next question is how I can export the reconstructed volume data and the associated position data. The goal of my project is to be able to display the ultrasound image based on the assigned position. Is 3D slicer able to export the volume and position data? So far, I’ve seen different file formats for volume or image export but nothing for position.</p>

---

## Post #2 by @ungi (2024-06-06 23:04 UTC)

<p>Hi,</p>
<p>If you need the position of each 2D ultrasound image, you need to save the ultrasound images and their transform nodes in two separate sequences in the same sequence browser. While OpenIGTLink and most of Slicer supports transformed images (one node), you can only save untransformed images in sequences.</p>
<p>There is no widely accepted standard format to save a time-sequence of tracking data. I recommend saving the Slicer scene as an mrb file, which will contain all the data you have recorded.</p>
<p>The reconstructed volume does not contain tracking data, so you will lose ultrasound positions if you only save the reconstructed volume.</p>
<p>I hope this helps clarify.</p>

---
