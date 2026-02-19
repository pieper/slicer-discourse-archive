---
topic_id: 21804
title: "Is There A Way To Adjust The Painting Area"
date: 2022-02-04
url: https://discourse.slicer.org/t/21804
---

# Is there a way to adjust the painting area?

**Topic ID**: 21804
**Date**: 2022-02-04
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-adjust-the-painting-area/21804

---

## Post #1 by @Jolly_thoughts (2022-02-04 16:58 UTC)

<p>Hi <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I just got to study about 3D slicer, I have a question that I couldn’t solve through googling.<br>
I’m currently doing a pulmonary segmentation right now, and I’m working with artery and veins. But the coronal and sagittal slides won’t paint as accurate as I want it to be, however small I make the paint brush, there’ll be a larger pixel and it’ll keep paint even the outside of the vessels. Is this because the slides’ resolution is to low? How do I fix this?</p>

---

## Post #2 by @Juicy (2022-02-08 06:59 UTC)

<p>Yes, It is probably because the original images were axial and the coronal and saggital slices have lower resolution because of the larger slice thickness. You can resample your volume to be of higher resolution using the “crop volume” module. To do this, place and ROI on the volume, then select isotropic spacing in the crop volume module to make the voxels into cube shapes and change the scaling if you want to make the voxel size smaller or larger. You can also edit the resolution of the segment itself in the segment editor. See further instructions <a href="https://discourse.slicer.org/t/fetal-lung-volume-calculation/578/5">here</a></p>

---
