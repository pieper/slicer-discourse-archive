---
topic_id: 23977
title: "Nasal Endoscopy Error Navigating Through Inside The 3D Rende"
date: 2022-06-21
url: https://discourse.slicer.org/t/23977
---

# Nasal Endoscopy Error (Navigating through/inside the 3D rendering) :(

**Topic ID**: 23977
**Date**: 2022-06-21
**URL**: https://discourse.slicer.org/t/nasal-endoscopy-error-navigating-through-inside-the-3d-rendering/23977

---

## Post #1 by @harukam_122 (2022-06-21 04:20 UTC)

<p>Hello! I am trying to use the 3D render in 3DSlicer to be able to navigate inside the bodies that I’ve rendered from DICOM data. I was not able to navigate through, for example, the nasal passage just via my mouse and zooming, so I’m trying to do it via the endoscopy module. But When I create a new curve through the nasal passage and click ‘create path’ with the input fiducials selected (the curve I created), I get this error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9011b2ad01f716a4816cba6ba61292f67fb23869.png" data-download-href="/uploads/short-url/kyuFKFT1zdR5xr2DcGebRFEGO7v.png?dl=1" title="Screen Shot 2022-06-21 at 1.10.58 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9011b2ad01f716a4816cba6ba61292f67fb23869_2_690x146.png" alt="Screen Shot 2022-06-21 at 1.10.58 PM" data-base62-sha1="kyuFKFT1zdR5xr2DcGebRFEGO7v" width="690" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9011b2ad01f716a4816cba6ba61292f67fb23869_2_690x146.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9011b2ad01f716a4816cba6ba61292f67fb23869_2_1035x219.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9011b2ad01f716a4816cba6ba61292f67fb23869_2_1380x292.png 2x" data-dominant-color="FAECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-06-21 at 1.10.58 PM</span><span class="informations">1746×370 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone know what I may be doing wrong? Thank you so so much!</p>

---

## Post #2 by @gaoyi.cn (2022-06-21 08:51 UTC)

<p>that may be caused by a bug. please try download the newest version of slicer and try again.</p>

---

## Post #3 by @harukam_122 (2022-06-22 00:35 UTC)

<p>I will try that, thank you!</p>

---

## Post #4 by @lassoan (2022-06-22 01:28 UTC)

<p>Yes, this is a regression in Slicer-5.0.2 until a new patch release becomes available. You can use Slicer-5.1.x version instead.</p>

---

## Post #5 by @harukam_122 (2022-06-23 02:29 UTC)

<p>Hi <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> and <a class="mention" href="/u/lassoan">@lassoan</a> , thank you so much for your help! The newer version did work!<br>
I just have a follow-up regarding the endoscopy module––is it possible to navigate inside the 3D image without the “play/stop” of the flythrough? By that, I mean is it possible to just navigate inside freely with for example the zooming motion on the mouse but still staying on the path of the point list?<br>
(please let me know if that didn’t make sense:))</p>

---

## Post #6 by @lassoan (2022-06-24 15:07 UTC)

<p>You can zoom in/out using the <code>View angle</code> slider. You can move along the trajectory using the <code>Frame slider</code>.</p>
<p>If you want to slightly deviate from the trajectory - “look around” - you can:</p>
<ul>
<li>rotate the camera in the 3D view by left-click-and-drag as usual</li>
<li>set up a mouse gesture for moving the camera focal forward/backward - just <a href="https://discourse.slicer.org/t/move-3d-focal-point-using-mouse-or-keyboard/15468/2">copy-paste the code snippet in this post to the Python console</a> and you can move forward/backward using Ctrl+MouseWheel. This custom gesture is needed because the usual MouseWheel gesture just moves the camera towards or away from the camera’s focal point, which is not what you want in endoscopy when you are so close to the focal point (because you cannot ever go beyond the focal point).</li>
</ul>

---
