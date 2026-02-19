---
topic_id: 35293
title: "How To Get Aim For Whole Sample"
date: 2024-04-04
url: https://discourse.slicer.org/t/35293
---

# How to get AIM for whole sample?

**Topic ID**: 35293
**Date**: 2024-04-04
**URL**: https://discourse.slicer.org/t/how-to-get-aim-for-whole-sample/35293

---

## Post #1 by @Rufaidah_Othman (2024-04-04 15:51 UTC)

<p>Hi, I am new to this forum.</p>
<p>I would like to know if anyone here has ever encountered the same problem of getting AIM file, specifically on how to get an AIM file of the whole bone instead of just a few slices, or only part of the bone.</p>
<p>I have searched in this forum, but it seems I could not find one related.</p>
<p>I am currently using high-resolution peripheral quantitative CT (XTREME CT II; SCANCO MEDICAL AG).</p>
<p>My sample consists of both femur and tibia. Therefore, I would like to use the AIM file to view both femur and tibia in one image in 3D using 3D Slicer.</p>
<p>However, I usually get an incomplete form of the AIM file. Below are some examples from a few different samples viewed in 3D Slicer:</p>
<ol>
<li>Femur only (picture 1)</li>
<li>Femur &amp; Tibia but in a few slices (picture 2)</li>
<li>Femur in a few slices (picture 3)</li>
<li>Tibia in a few slices (picture 4)</li>
</ol>
<p>I would greatly appreciate any guidance on this matter.</p>
<p>Thank you in advance.</p>
<p>Operating system: Windows 10, 64-bit operating system, 12 GB RAM, AMD Ryzen 7 3750H with Radeon Vega Mobile Gfx, 2.30 GHz</p>
<p>Slicer version: 5.2.1</p>
<p>Expected behavior:</p>
<p>Actual behavior:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f11540a0d7921fe7d600bff718204309736d7f38.png" alt="1 Femur" data-base62-sha1="yoIBq3dgDT7QN6kL2vMXbLvKErK" width="421" height="346"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355a4fb806b11211ec7d6575408c0835c9f18022.png" data-download-href="/uploads/short-url/7BYNqvMjQRUosOm5kMtkUAWKwZI.png?dl=1" title="3 Femur with shaft (slices)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355a4fb806b11211ec7d6575408c0835c9f18022_2_437x500.png" alt="3 Femur with shaft (slices)" data-base62-sha1="7BYNqvMjQRUosOm5kMtkUAWKwZI" width="437" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355a4fb806b11211ec7d6575408c0835c9f18022_2_437x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355a4fb806b11211ec7d6575408c0835c9f18022.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355a4fb806b11211ec7d6575408c0835c9f18022.png 2x" data-dominant-color="8890B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3 Femur with shaft (slices)</span><span class="informations">522×597 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123e93f53e345d52fd3a8773f6446151df12f07f.png" alt="4 Tibia (slices)" data-base62-sha1="2BoFmrYcDeEWCZ067OqZAxbhYgD" width="571" height="480"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5efa290f0e5a06d261494a028009bf6837857f17.png" alt="2 Femur Tibia (slices)" data-base62-sha1="dycQBa4CsdCf3dCdxDLLEQFcvqv" width="392" height="268"></p>

---

## Post #2 by @muratmaga (2024-04-04 16:19 UTC)

<p>AIM is a volumetric file (i.e., raw data from microCT). What you are showing in screenshots are 3D models derived from the volumetric data through segmentation. So it is hard to tell where the missing stuff is coming from. Perhaps incomplete segmentation, cropped original volume?</p>
<p>Loading AIM file is very simple, just drag and drop, and you should immediately see the microCT images populating the slice views. Then you can navigate through the slice views to see if the volume is complete or missing parts of femur.</p>

---
