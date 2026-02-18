# Question for Virtual Reality on Slicer

**Topic ID**: 28474
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/question-for-virtual-reality-on-slicer/28474

---

## Post #1 by @Kai (2023-03-20 13:49 UTC)

<p>Hellow<br>
I would like to ask about a problem with Virtual Reality in Slicer.<br>
I am using Slicer 5.0.2 and download and install the vr plugin. I am using oculus quest 2 for hardware.<br>
The problema is I don’t know which Volume Rendering I should chose(VTK CPU Ray Casting, VTK GPU Ray Casting  and VTK Multi-Volume (experimental) ) . When I chose VTK CPU Ray Casting,I got two volume models on both left and right glasses of oculus quest 2,  it is delayed and very lagged(3090GPU), and there is no controller. When I use VTK GPU Ray Casting or VTK Multi-Volume (experimental), virtual reality runs smoothly. However, I can only found an empty backgroud and controllers but no volume models.<br>
Thank you for your help<br>
Best regards<br>
Kai</p>

---

## Post #2 by @cpinter (2023-03-20 17:25 UTC)

<p>Please use the latest Slicer 5.3.0 preview, major fixes have been made in SlicerVirtualReality but those are not in the stable releases yet.</p>
<p>Note that CPU is the central processor of the computer, while GPU is the graphics card. So when you use CPU for volume rendering it doesn’t matter what GPU you have and it will be much slower. Always use GPU (or MultiVolume, which uses GPU but is an experimental mode).</p>

---

## Post #3 by @francesca_flore (2024-02-29 10:58 UTC)

<p>Hi! I can’t find SlicerVirtualReality extension for the latest versions of 3D Slicer. I saw that it exists for version 5.2. Hasn’t it been updated since then? Does it only work for Oculus Rift?<br>
Thanks</p>

---
