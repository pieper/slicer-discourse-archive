---
topic_id: 17185
title: "How To Get A High Resolution Of Modified 3D Models"
date: 2021-04-19
url: https://discourse.slicer.org/t/17185
---

# how to get a high resolution of modified 3d models?

**Topic ID**: 17185
**Date**: 2021-04-19
**URL**: https://discourse.slicer.org/t/how-to-get-a-high-resolution-of-modified-3d-models/17185

---

## Post #1 by @Michele_Atzori (2021-04-19 20:11 UTC)

<p>Goodmorning everyone. I recently discovered this beautiful 3d slicer software. I wanted to ask why the images I drag onto the 3d screen are much more defined than those obtained from the thresold-show 3d editor; they are more defined but unfortunately I can’t change them. How is it possible?I would like to make segmentation more realistic without that “lava flow” effect.</p>

---

## Post #2 by @pieper (2021-04-19 20:21 UTC)

<p>Hi, welcome -</p>
<p>There’s been a lot of prior discussion around these topics, so you might find insight by searching for a few keywords on this forum.  In a nutshell, segmentation happens at the pixel level which is either on or off while the volume rendering shows the full dynamic range of the scan (maybe 12 bits).  So one option is to supersample the segmentation with respect to the source image data.  There are other tricks too, like smoothing.</p>
<p>If you post screenshots of what you are seeing we might be more help.</p>

---
