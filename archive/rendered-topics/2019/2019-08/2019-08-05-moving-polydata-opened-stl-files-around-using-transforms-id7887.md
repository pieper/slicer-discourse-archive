---
topic_id: 7887
title: "Moving Polydata Opened Stl Files Around Using Transforms"
date: 2019-08-05
url: https://discourse.slicer.org/t/7887
---

# Moving polydata (opened .stl files) around using transforms

**Topic ID**: 7887
**Date**: 2019-08-05
**URL**: https://discourse.slicer.org/t/moving-polydata-opened-stl-files-around-using-transforms/7887

---

## Post #1 by @Renjie_Zhu (2019-08-05 20:02 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.8.1<br>
Expected behavior: Move an .stl polydata around in the 3d view<br>
Actual behavior:</p>
<p>Hi, I want to create an overlay of a needle both on the 3d view and the 2d slices. I have tried to use fiducials by sending a pointcloud over OpenIGTLink but when the number of fiducials goes up the app becomes significantly laggy. I figured that by using a polydata overlay, I can both see the shape in the 3d view and see an intersection with actual dicom slices in the 2d slices viewer.</p>
<p>The problem I am facing is that I want to move this polydata thing around (changing its position and orientation), preferrably with transforms as I can easily send transforms over from ROS using OpenIGTLink.</p>
<p>Any help will be very much appreciated!</p>

---

## Post #2 by @lassoan (2019-08-05 20:13 UTC)

<p>You can receive transforms via OpenIGTLink and apply it to any node (in Transforms module). Use at least the latest Stable Release of Slicer. See tutorials at <a href="http://www.slicerigt.org" rel="nofollow noopener">www.slicerigt.org</a>.</p>

---

## Post #3 by @Renjie_Zhu (2019-08-05 20:58 UTC)

<p>Thank you for your help! So I just add the model as a transformable, is that correct?</p>
<p>I use 4.8.1 as the OpenIGTLink bridge with ROS has problems communicating correctly. So I was suggested by the author of that module to use an older version. I will test if this works in 4.10.2.</p>
<p>Thank you again.</p>

---
