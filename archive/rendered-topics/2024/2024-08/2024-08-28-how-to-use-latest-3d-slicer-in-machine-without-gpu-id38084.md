---
topic_id: 38084
title: "How To Use Latest 3D Slicer In Machine Without Gpu"
date: 2024-08-28
url: https://discourse.slicer.org/t/38084
---

# How to use latest 3D Slicer in machine without GPU

**Topic ID**: 38084
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/how-to-use-latest-3d-slicer-in-machine-without-gpu/38084

---

## Post #1 by @xiyue (2024-08-28 12:28 UTC)

<p>Could I use the latest 3D Slicer in a machine without GPU support?  Now I use the old version (v4.8.0) in our machine, the machine has no GPU because of some restriction. But some features are not supported by the old version, so we have to upgrade to a newer version such as v5.0.2 or latest version, but got the error “Renderer does not support required OpenGL capabilities”. I’m wondering if there is configuration to disable the GPU mode and render with CPU like old version?  Because I don’t need 3D view so it’s ok to display the 2D view for me.</p>

---

## Post #2 by @pieper (2024-08-28 12:45 UTC)

<p>I guess you mean Windows, so you probably need to check for Windows-specific workarounds.</p>
<p>But one option would be to use docker so you have the software fallback graphics options with the linux-based guest.</p>

---
