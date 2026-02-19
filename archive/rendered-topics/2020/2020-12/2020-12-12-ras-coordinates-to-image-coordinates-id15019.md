---
topic_id: 15019
title: "Ras Coordinates To Image Coordinates"
date: 2020-12-12
url: https://discourse.slicer.org/t/15019
---

# RAS coordinates to Image coordinates

**Topic ID**: 15019
**Date**: 2020-12-12
**URL**: https://discourse.slicer.org/t/ras-coordinates-to-image-coordinates/15019

---

## Post #1 by @justomont (2020-12-12 17:41 UTC)

<p>Operating system: macOS Big Sur 11.0.1<br>
Slicer version: 4.10.1</p>
<p>Dear Developers and Users,</p>
<p>I have a lot of fiducial markup points in the <strong>RAS Coordinates System</strong>, as can be seen in the screen capture, for example <strong>X’5</strong> <img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> <strong>R</strong>: -33.594  <strong>A</strong>: 15.622  <strong>S</strong>: 16.020</p>
<p>I want to obtain their coordinates in the <strong>Image Space</strong>, and associate them with the labels from the volume called <strong>‘aseg’</strong> in the scene (as can be seen in the Data Probe tab). This volume contains the exact area of the brain where each fiducial markup is located.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76adc510a5ccbfa89a556e983e55ac4a8831dca5.jpeg" data-download-href="/uploads/short-url/gVSDM9Vw3VBmXBSmGcWbuDfdKu1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76adc510a5ccbfa89a556e983e55ac4a8831dca5_2_689x431.jpeg" alt="image" data-base62-sha1="gVSDM9Vw3VBmXBSmGcWbuDfdKu1" width="689" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76adc510a5ccbfa89a556e983e55ac4a8831dca5_2_689x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76adc510a5ccbfa89a556e983e55ac4a8831dca5_2_1033x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76adc510a5ccbfa89a556e983e55ac4a8831dca5_2_1378x862.jpeg 2x" data-dominant-color="A4A3A3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2558×1600 680 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Basically, what I need to do is to <strong>automatically</strong> relate the position of all Fiducial Markups with the information of this ‘aseg’ volume. So, for example, the outcome for this point X’5 should be something like:</p>
<p><strong>X’5:    RAS</strong>:  [-33.594, 15.622, 16.020]  <strong>IMAGE</strong>: [158, 111, 142]   <strong>LABEL</strong>: Left-Putamen</p>
<p>Please guide me, I really need some help.<br>
Best regards.<br>
Justo</p>

---

## Post #2 by @lassoan (2020-12-12 17:43 UTC)

<p>See the code here that takes into account image geometry and all linear/warping transformations applied to the volume and fiducial list: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates</a></p>

---

## Post #3 by @justomont (2020-12-16 10:04 UTC)

<p>Thanks for your response,</p>
<p>I’ve already tried this approach and the output is a single matrix ([203, 128, 161] in my case). But I don’t know what this result means, as according to the documentation this should be the voxel coordinate of a volume corresponding to a markup fiducial point position. As input, I’ve introduced the complete Markup List (containing 38 Markups), shouldn’t the output be a list too?</p>
<p>Sorry if my question is too ignorant, I’m new to Slicer and Image Transformations.<br>
Thanks again for helping me.</p>

---

## Post #4 by @lassoan (2020-12-19 06:53 UTC)

<aside class="quote no-group" data-username="justomont" data-post="3" data-topic="15019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/justomont/48/16814_2.png" class="avatar"> justomont:</div>
<blockquote>
<p>I’ve already tried this approach and the output is a single matrix ([203, 128, 161] in my case). But I don’t know what this result means, as according to the documentation this should be the voxel coordinate of a volume corresponding to a markup fiducial point position.</p>
</blockquote>
</aside>
<p>This is correct.</p>
<aside class="quote no-group" data-username="justomont" data-post="3" data-topic="15019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/justomont/48/16814_2.png" class="avatar"> justomont:</div>
<blockquote>
<p>As input, I’ve introduced the complete Markup List (containing 38 Markups), shouldn’t the output be a list too?</p>
</blockquote>
</aside>
<p>This is the voxel coordinate of a single point. The point index specified in the <code>markupsIndex</code> variable.</p>

---
