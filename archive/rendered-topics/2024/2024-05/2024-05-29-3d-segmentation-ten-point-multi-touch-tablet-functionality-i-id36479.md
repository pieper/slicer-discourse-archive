---
topic_id: 36479
title: "3D Segmentation Ten Point Multi Touch Tablet Functionality I"
date: 2024-05-29
url: https://discourse.slicer.org/t/36479
---

# 3D segmentation: ten-point multi-touch tablet functionality (in linux ubuntu)?

**Topic ID**: 36479
**Date**: 2024-05-29
**URL**: https://discourse.slicer.org/t/3d-segmentation-ten-point-multi-touch-tablet-functionality-in-linux-ubuntu/36479

---

## Post #1 by @hari_seldon (2024-05-29 22:32 UTC)

<p>Hello, first post. I am attempting to 3D segment CT scan data from ancient carbonized scrolls. I am hoping to test out a touchscreen tablet to manipulate the data (cubes, 512x512x512), in such a way that I can freely rotate and zoom the cubes with my left hand, and segment with the pen in my right hand. Is this functionality possible with any setup? Is it possible specifically on Ubuntu 22.04?</p>
<p>Thank you kindly for your time</p>

---

## Post #2 by @lassoan (2024-05-29 22:50 UTC)

<p>Multi-touch screen and touchpad works great in Windows, macOS only has multitouch touchpad but that works well, too. We don’t have much information on what multitouch features works in which Linux distro, driver, window manager, etc. but Slicer uses Qt-5.15 and any multitouch features that your Linux configuration supports with this Qt version will work with Slicer.</p>

---
