---
topic_id: 20675
title: "How To Change The Gpu Or Cpu"
date: 2021-11-18
url: https://discourse.slicer.org/t/20675
---

# How to change the GPU or CPU？

**Topic ID**: 20675
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/how-to-change-the-gpu-or-cpu/20675

---

## Post #1 by @slicer365 (2021-11-18 03:52 UTC)

<p>About the VolumeRendering module,</p>
<p>when I select GPU as render, no image can appear in 3D view,</p>
<p>but when I select CPU rendering, it can appear,</p>
<p>but when I change other computer, the result is the opposite.</p>

---

## Post #2 by @pieper (2021-11-18 13:34 UTC)

<p>CPU rendering should work anywhere, unless maybe you run out of memory of something - you can check for <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=error%20log#status-bar">error messages</a>.</p>
<p>GPU rendering may not work on some graphics cards due to hardware or driver limitations.  These may or may not result in error messages.</p>

---
