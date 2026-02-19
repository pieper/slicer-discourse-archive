---
topic_id: 15459
title: "Nasal Airways Simulation"
date: 2021-01-11
url: https://discourse.slicer.org/t/15459
---

# Nasal airways simulation

**Topic ID**: 15459
**Date**: 2021-01-11
**URL**: https://discourse.slicer.org/t/nasal-airways-simulation/15459

---

## Post #1 by @Polyynom (2021-01-11 18:11 UTC)

<p>Dear 3D Slicer users,</p>
<p>I need to make model of nasal airways. like on the picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/845d79718692eaa68e703c405ad3ee5d24a0f196.jpeg" data-download-href="/uploads/short-url/iSXiel4xmT2MAdlaFxrXOJzTqdM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/845d79718692eaa68e703c405ad3ee5d24a0f196_2_517x294.jpeg" alt="image" data-base62-sha1="iSXiel4xmT2MAdlaFxrXOJzTqdM" width="517" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/845d79718692eaa68e703c405ad3ee5d24a0f196_2_517x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/845d79718692eaa68e703c405ad3ee5d24a0f196_2_775x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/845d79718692eaa68e703c405ad3ee5d24a0f196_2_1034x588.jpeg 2x" data-dominant-color="D7CAC0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1136×648 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I have some problem with this owing I’m new user.<br>
To solve I’ve use Segment Editor where choose Threshold range and obtained the model. But There is not correct sectors I’d like to change. I think to decide the problem I need to segregate space to segments and for each segment choose each threshold range. Next step is add all segments to one body.<br>
If you help me to decide the task or suggest another decision I will be very glade.</p>
<p>Thank you very much for your attention! If necessary to add more information to the Topic to make the question more understandable please write.</p>

---

## Post #2 by @lassoan (2021-01-13 21:25 UTC)

<p>I would recommend to use Grow from seeds effect in Segment Editor module, using masking. See detailed recipe here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>
<p>If you find it difficult to segment thin structures (as they get thinner than 1-2 voxels) or the input image voxels are not cubic (pixel spacing is highly anisotropic) then I would recommend to crop and resample the input volume before segmentation using Crop volumes module (with Isotropic spacing enabled, Scaling factor set to something between 0.2 to 0.6, cropped to minimum necessary size).</p>

---

## Post #3 by @Polyynom (2021-01-14 14:29 UTC)

<p>Thank you a lot for your answer!</p>

---
