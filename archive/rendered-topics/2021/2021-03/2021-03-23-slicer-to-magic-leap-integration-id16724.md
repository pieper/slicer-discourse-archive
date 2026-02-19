---
topic_id: 16724
title: "Slicer To Magic Leap Integration"
date: 2021-03-23
url: https://discourse.slicer.org/t/16724
---

# Slicer to Magic Leap Integration

**Topic ID**: 16724
**Date**: 2021-03-23
**URL**: https://discourse.slicer.org/t/slicer-to-magic-leap-integration/16724

---

## Post #1 by @cshreyas (2021-03-23 17:20 UTC)

<p>Hello,<br>
I am exploring ways to integrate Slicer 3D.</p>
<p>I am looking to use SlicerVirtualReality. Can someone help me with file format that gets IN and Out of SlicerVirtualReality? This will be helpful to explore its compatibility with Magic leap.</p>
<p>Thanks</p>

---

## Post #2 by @adamrankin (2021-03-23 17:47 UTC)

<p>As the MagicLeap is not an OpenVR supported device, it cannot be used currently with Slicer Virtual Reality. We are exploring the possibility of moving to OpenXR, but are looking for help in this area.</p>

---

## Post #3 by @cshreyas (2021-03-23 19:34 UTC)

<p>Thank <a class="mention" href="/u/adamrankin">@adamrankin</a> . I am looking to use this integration for my research. I am open for collaboration. Please let me know if we can work together on exploring this.</p>

---

## Post #4 by @cshreyas (2021-03-23 19:41 UTC)

<p><a class="mention" href="/u/adamrankin">@adamrankin</a> , can you let me know the file format that goes IN and Out of SlicerVirtualReality? Is it a video stream?</p>

---

## Post #5 by @adamrankin (2021-03-23 19:43 UTC)

<p>I’m not quite sure I follow. VR just shows you your current 3D scene in a VR environment. Anything you have in your 3D view on your desktop, you’ll see in VR.</p>

---

## Post #6 by @cshreyas (2021-03-23 19:46 UTC)

<p>yes, but there is communication between slicer and VR environment through SlicerVirtualReality plugin. Thats the reason the 3D scene in slicer (desktop), shows up in VR. I am trying to understand what kind of communication is that?</p>

---

## Post #7 by @cpinter (2021-03-24 13:28 UTC)

<p><a class="mention" href="/u/cshreyas">@cshreyas</a> VTKRenderingOpenVR has a special VTK render window that renders two scenes that are transferred by OpenVR to the headset.</p>
<p><a class="mention" href="/u/adamrankin">@adamrankin</a> We are waiting for the result of a grant in which we included OpenXR integration. We should get word within a few weeks (they promised by the end of March but who knows).</p>

---

## Post #8 by @lassoan (2021-03-24 15:53 UTC)

<p>VTK developers had plans for working on OpenXR integration, too. It may worth asking on the <a href="https://discourse.vtk.org">VTK forum</a> for latest updates.</p>

---

## Post #9 by @cshreyas (2021-03-31 18:34 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/cpinter">@cpinter</a>  . Of what I heard from Magic Leap support, they have no plans to support OpenXR in near future.</p>
<p>I am trying to use OpenIGTLink as a bridge between Slicer and Magic Leap. This would have to do be done using OpenCV most likely and publish the point cloud data to a streaming server.</p>
<p>Do you have any pointers on where to get started from the slicer code base? Where are the images getting published in Slicer?</p>

---

## Post #10 by @lassoan (2021-04-03 01:46 UTC)

<aside class="quote no-group" data-username="cshreyas" data-post="9" data-topic="16724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e56c9b/48.png" class="avatar"> cshreyas:</div>
<blockquote>
<p>Of what I heard from Magic Leap support, they have no plans to support OpenXR in near future.</p>
</blockquote>
</aside>
<p>You may consider moving to a device that has more certain future and supports OpenXR, such as Microsoft Hololens.</p>
<aside class="quote no-group" data-username="cshreyas" data-post="9" data-topic="16724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e56c9b/48.png" class="avatar"> cshreyas:</div>
<blockquote>
<p>I am trying to use OpenIGTLink as a bridge between Slicer and Magic Leap.</p>
</blockquote>
</aside>
<p>What data do you plan to send between Slicer and Magic Leap?</p>
<aside class="quote no-group" data-username="cshreyas" data-post="9" data-topic="16724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e56c9b/48.png" class="avatar"> cshreyas:</div>
<blockquote>
<p>This would have to do be done using OpenCV most likely and publish the point cloud data to a streaming server.</p>
</blockquote>
</aside>
<p>Could you clarify? What is the role of OpenCV? What data you would like to get from/send to Magic Leap?</p>
<aside class="quote no-group" data-username="cshreyas" data-post="9" data-topic="16724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e56c9b/48.png" class="avatar"> cshreyas:</div>
<blockquote>
<p>Do you have any pointers on where to get started from the slicer code base? Where are the images getting published in Slicer?</p>
</blockquote>
</aside>
<p>All incoming data (images, transform, surface meshes, etc.) appear as MRML nodes. If you set a MRML node as outgoing node then any changes in that node are automatically sent via OpenIGTLink.</p>

---

## Post #11 by @cshreyas (2021-05-13 13:24 UTC)

<p>Thank you for the clarification.</p>

---

## Post #12 by @cshreyas (2021-10-11 22:43 UTC)

<p><em>What data do you plan to send between Slicer and Magic Leap?</em><br>
I am exploring two options.</p>
<ol>
<li>Send the image Voxel from Slicer through OpenIGTL to client. The client uses some volume rendering algorithm like Marching Cube and render this in OpenGL on the the device.</li>
<li>Or simply send live steam compressed video from Slicer to device and the device just un-compresses the video stream and display. (I have already a working version of the Marching cube algorithm)</li>
</ol>
<p>Option 1 has 3 stages and could not much performant.<br>
Option 2 looks ok except that the client could just be publishing the video.</p>
<p>Can you please suggest the best option?</p>
<p>I am also open for other approaches.<br>
Thanks</p>

---

## Post #13 by @lassoan (2021-10-13 12:42 UTC)

<p>If rendering capabilities of the Magic Leap are limited (slow CPU/GPU, no sophisticated visualization toolkit, such as VTK) then I would render remotely (in Slicer) and just stream the rendered 2D images. This is also beneficial because you don’t k ow when Magic Leap has been on the brink of bankruptcy for a while now, so it is better to minimize the time you spend getting to know it and develop code that runs on it.</p>
<p>If you render using Slicer then there is no need to use marching cubes, because you can get much higher quality images with more details, colors, depth perception at magnitudes faster rendering speed using volume renderering module (raycasting).</p>

---

## Post #14 by @cshreyas (2021-10-13 16:18 UTC)

<p>Thanks Andras,<br>
That make sense. I agree with you, we can just render in Slicer and pass the image Stream to Magic Leap.</p>
<p>I would like to stream all three planes. Should I use 2D images of 3 planes separately or should this be a 3D volume (UseStreamingVolume)?</p>
<p>Should I scream as image data or video data?</p>

---

## Post #15 by @lassoan (2021-10-13 18:30 UTC)

<p>If you send rendered images then you don’t send individual slices but just the fully rendered left and right images, probably as a single image, in a side-by-side or over-under configuration.</p>

---

## Post #16 by @cshreyas (2021-10-13 18:33 UTC)

<p>Thank you, will try it out. Will get back when if I get struck.</p>

---

## Post #17 by @Valerii (2024-01-06 19:01 UTC)

<p>Now that Magic Leap 2 is released packing a proper Ryzen APU, maybe, the perspective has changed?</p>

---
