# GPU Volume Rendering Issues

**Topic ID**: 1380
**Date**: 2017-11-04
**URL**: https://discourse.slicer.org/t/gpu-volume-rendering-issues/1380

---

## Post #1 by @mrmorgan (2017-11-04 19:13 UTC)

<p>Operating system: win64<br>
Slicer version: 4.8.0</p>
<p>Has anyone else had trouble volume rendering using the GPU raycasting option? I’ve had this problem on two different machines (HP Pavillion 15 touch, intel i7-7700HQ, GTX 1050 GPU and Microsoft Surface Pro Intel i7-7660, intel iris plus 640). When GPU volume rendering is enabled, the window only displays a single slice on the edge of the volume, but will not display the full volume. CPU rendering, however, does just fine.</p>
<p>Any ideas?</p>

---

## Post #2 by @lassoan (2017-11-04 19:23 UTC)

<p>This issue typically occurs with motherboard integrated GPUs (Intel Iris, etc). We used GPU volume rendering on tens of different desktops and laptop models with various Windows versions and it always worked well.</p>
<p>You can make you Pavilion work by configuring Optimus to use NVidia GPU (instead of the integrated graphics card) for Slicer. When you install a new version of Slicer, it is placed in a new directory, so you have to configure it in Optimus again.</p>
<p>For Surface Pro with integrated graphics card, you need to wait for the upcoming version of Slicer, which uses VTK’s new rendering backend. It should be available within a few months.</p>

---
