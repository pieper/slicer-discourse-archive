---
topic_id: 5163
title: "Can I Get Diffusion Tensor For Every Single Pixel From Dti"
date: 2018-12-21
url: https://discourse.slicer.org/t/5163
---

# can i get diffusion tensor for every single pixel from DTI

**Topic ID**: 5163
**Date**: 2018-12-21
**URL**: https://discourse.slicer.org/t/can-i-get-diffusion-tensor-for-every-single-pixel-from-dti/5163

---

## Post #1 by @Rick (2018-12-21 14:13 UTC)

<p>I wanted to analysis the diffusion coefficient from the DTI<br>
I know that FA map is build up from calculating every pixel’s tensor and get the eigenvalue and eigenvectors and I’m wondering can I get those tensor ? Is it able to show up as a map ?<br>
Rick<br>
sincerely</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2018-12-21 22:12 UTC)

<p>Hi -</p>
<p>If you start from DWI, you can estimate tensors at every voxel, from which you can calculate FA.  See the info at <a href="http://dmri.slicer.org/docs/" rel="nofollow noopener">http://dmri.slicer.org/docs/</a>.</p>
<p>-Steve</p>

---
