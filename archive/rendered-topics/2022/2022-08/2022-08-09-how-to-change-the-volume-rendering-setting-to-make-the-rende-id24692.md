# How to change the volume rendering setting to make the rendering effect from picture1 to picture2

**Topic ID**: 24692
**Date**: 2022-08-09
**URL**: https://discourse.slicer.org/t/how-to-change-the-volume-rendering-setting-to-make-the-rendering-effect-from-picture1-to-picture2/24692

---

## Post #1 by @jay1987 (2022-08-09 12:05 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7258e4ecfd2c21b65065759a39ba267afdbffe5.jpeg" alt="image" data-base62-sha1="spJtK884EtcCnOLS7GrJKocrjQp" width="531" height="455"><br>
picture1:obtain the vessel scalar volume node from VMTK,use preset [Vesselness]</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41f6d84e764c47ce6037ac73d4f810a66a1b2dda.jpeg" alt="image" data-base62-sha1="9pxTHBiIEnVG5Iuo6vQnWMU6ppo" width="468" height="379"><br>
picture2:change vessel to segmentation,the rendering segmentation in 3D</p>

---

## Post #2 by @mau_igna_06 (2022-08-09 12:59 UTC)

<p>You could try simpleitk sigmoidfilter (adjusting the parameters). It may help to enhance the vessels for later segmentation if the threshold is selected correctly…<br>
I think that effect you got is because you used islands effect to keep part of the vessels and not all of them</p>

---

## Post #3 by @jay1987 (2022-08-09 13:03 UTC)

<p>thanks<br>
I can change the vessel volume rendering to model rendering and segmentation rendering to avoid this problem , maybe is the vmtk [vesselness] preset cause the opacity rendering , CT and MRI preset is fine</p>

---
