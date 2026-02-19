---
topic_id: 42424
title: "Cant Access Installed Extension Surfacesolidify 6006814 In 3"
date: 2025-04-03
url: https://discourse.slicer.org/t/42424
---

# Can't access installed extension SurfaceSolidify 6006814 in 3D slicer 5.8.1

**Topic ID**: 42424
**Date**: 2025-04-03
**URL**: https://discourse.slicer.org/t/cant-access-installed-extension-surfacesolidify-6006814-in-3d-slicer-5-8-1/42424

---

## Post #1 by @SBM2025 (2025-04-03 13:01 UTC)

<p>I am approaching you guys from New Zealand regarding a challenge I have with enabling SurfaceSolidify extension in 3D slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I am completely new to 3D slicer, so please be gentle on me…hahaha.</p>
<p>Here’s my humble question / issue:  I have installed the segment editor extension SurfaceWrapSolidify Version 6006814 in my 3D slicer version 5.8.1. After installation I restarted 3D slicer, and I could see the extension installed and enabled in the extension manager window.</p>
<p>However I can now not see the new extension in the module list. I have tried using the search term “Solidify” as well and it still doesn’t show up. What went wrong? Is this a version incompatibility issue?</p>
<p>I have also tried to run the extension on teh older 3D slicer version 5.6.2 and SurfaceSolidify still doesn’t show up although I have restarted after installation and the extension is enabled.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb04029b9f447167944992d0963dda362cb0fb61.png" data-download-href="/uploads/short-url/sXXw8ioR9n0bpMXaQyTe4xh4ARH.png?dl=1" title="SurfaceSolidify_extension" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb04029b9f447167944992d0963dda362cb0fb61_2_669x500.png" alt="SurfaceSolidify_extension" data-base62-sha1="sXXw8ioR9n0bpMXaQyTe4xh4ARH" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb04029b9f447167944992d0963dda362cb0fb61_2_669x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb04029b9f447167944992d0963dda362cb0fb61_2_1003x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb04029b9f447167944992d0963dda362cb0fb61_2_1338x1000.png 2x" data-dominant-color="CDCBD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SurfaceSolidify_extension</span><span class="informations">2353×1756 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any hints on how to enable the extension would be much appreciated!!</p>
<p>FYI: I am trying to use the extension to convert an intricate CAD surface model into a solid 3D-printable mesh!</p>

---

## Post #2 by @lassoan (2025-04-03 13:03 UTC)

<p>The extension adds a new effect to Segment Editor module. The extension’s documentation includes a tutorial that tou may find helpful: <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify?tab=readme-ov-file#how-to-use">https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify?tab=readme-ov-file#how-to-use</a></p>

---

## Post #3 by @SBM2025 (2025-04-06 04:45 UTC)

<p>Thanks very much Andras for your reply - much appreciated. I managed to get access to the effects feature. Now I reckon, I will have to spend more time with the documentation. Still not sure whether your extension is actually suitable for my complex technical CAD source model design and to create a solid, watertight mesh with defined minimum wall thickness? Still struggling to generate a useful result and tweaking the settings for my use case. Maybe it was not created for my situation :))</p>

---

## Post #4 by @lassoan (2025-04-07 04:08 UTC)

<p>Can you attach a screenshot of the model you are working with?<br>
This method will shrinkwrap the model (e.g., you put the object in a plastic bag and suck out the air - the method will provide you the shape of the plastic bag).</p>

---

## Post #5 by @SBM2025 (2025-04-07 05:46 UTC)

<p>Hi Andras, this is exactly the effect I’d like to achieve…and ideally the shrink-wrapped plastic bag volume is completely solid within!! :))</p>
<p>Here’s a link to the model file…maybe this will clarify my challenge for you.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1dVtrxNxHcm3jyEf1vWjYm17K-FTPvCwg/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1dVtrxNxHcm3jyEf1vWjYm17K-FTPvCwg/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1dVtrxNxHcm3jyEf1vWjYm17K-FTPvCwg/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1dVtrxNxHcm3jyEf1vWjYm17K-FTPvCwg/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">boiler_room_scale_1to30_vers2_extract_1Mio.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I did not manage to achieve this effect for my CAD model design…but it’s probably just me not trying hard enough or not fully grasping the UI &amp; parameters?</p>
<p>Any views?</p>
<p>Thanks and best regards</p>

---
