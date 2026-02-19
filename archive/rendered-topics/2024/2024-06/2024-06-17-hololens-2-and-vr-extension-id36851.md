---
topic_id: 36851
title: "Hololens 2 And Vr Extension"
date: 2024-06-17
url: https://discourse.slicer.org/t/36851
---

# HoloLens 2 and VR extension

**Topic ID**: 36851
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/hololens-2-and-vr-extension/36851

---

## Post #1 by @LeidyMoraV (2024-06-17 20:55 UTC)

<p>I want to display the view in Hololens 2, I’m using Holographic Remoting Player and writing the IP adress in the VR module in Slicer 5.6.1, however, it always crashes and stops working. In the Hololens I only see the black image with the IP adress.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a8573e6c2df390598525a9756b29583ce6697d8.jpeg" data-download-href="/uploads/short-url/m2Xs033c95iAiLhBDxqzjBjrJOg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8573e6c2df390598525a9756b29583ce6697d8_2_690x373.jpeg" alt="image" data-base62-sha1="m2Xs033c95iAiLhBDxqzjBjrJOg" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8573e6c2df390598525a9756b29583ce6697d8_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8573e6c2df390598525a9756b29583ce6697d8_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8573e6c2df390598525a9756b29583ce6697d8_2_1380x746.jpeg 2x" data-dominant-color="8F8E91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1040 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m following the instructions from <a href="https://github.com/KitwareMedical/SlicerVirtualReality" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a Slicer scene using virtual reality.</a>, however I’ve not been able to correctly Set-Up the Windows Mixed Reality since it doesn’t detect my headset but I’m not sure this is the reason why Slicer crashes.</p>
<p>Any idea of how to solve it?</p>

---

## Post #2 by @lassoan (2024-06-18 01:45 UTC)

<aside class="quote no-group" data-username="LeidyMoraV" data-post="1" data-topic="36851">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leidymorav/48/70144_2.png" class="avatar"> LeidyMoraV:</div>
<blockquote>
<p>I’m using Holographic Remoting Player and writing the IP adress in the VR module in Slicer 5.6.1</p>
</blockquote>
</aside>
<p>You always need to use the latest Slicer release (Slicer-5.6.1 is not the latest one). In the case of virtual reality, there have been some fixes in the Slicer core since the last Slicer Stable Release, so the best is to use the latest Slicer Preview Release.</p>

---

## Post #3 by @LeidyMoraV (2024-06-18 20:18 UTC)

<p>Thank you! It worked with Slicer 5.7.0. In case anyone encounters device issues, I also had to disable my NVIDIA graphics card. Now, I have a few questions:</p>
<ol>
<li>How can I prepare the model for walking around and visualizing it in virtual reality? I see there are 3 available transforms (controller, tracker, HMD), but I’m unclear on their specific uses. (Example: video suplementary material: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382668/" rel="noopener nofollow ugc">Interaction with Volume Rendered 3D Echocardiographic Images in Virtual Reality - PMC (nih.gov)</a>)</li>
<li>When I need to rotate or move the object, should I manually place it under one of these transforms?</li>
<li>After closing 3D Slicer, I encounter the error shown in the picture. Does this affect the functionality or tools of 3D Slicer?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1e6075b3e20514b917716c08e871a9f5242cfff.png" alt="image" data-base62-sha1="yvVU5yI6FeoNlAx0jCPyeGAydT9" width="620" height="448"></li>
</ol>

---
