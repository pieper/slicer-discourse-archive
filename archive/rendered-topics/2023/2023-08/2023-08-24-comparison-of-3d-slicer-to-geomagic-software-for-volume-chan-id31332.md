# Comparison of 3D slicer to geomagic software for volume change

**Topic ID**: 31332
**Date**: 2023-08-24
**URL**: https://discourse.slicer.org/t/comparison-of-3d-slicer-to-geomagic-software-for-volume-change/31332

---

## Post #1 by @aljarkow (2023-08-24 10:39 UTC)

<p>Hello all,<br>
Does anyone have insight into whether 3D slicer is as accurate as Geomagic software for calculating small changes in volume between 2 STL files (at the micron level)?<br>
I have not been able to find sources comparing the spacial resolution accuracy and voxel sizes for my research purposes.<br>
Thanks in advance!</p>

---

## Post #2 by @muratmaga (2023-08-24 16:08 UTC)

<p>It should be comparable, because it is really the 3D model is providing the geometry. I am not sure how you are calculating <strong>small changes in volume</strong> in geomagic. Are you subtracting one from the other?</p>
<p>If so, ideally you should get same answer in both software (within precision limits). But that’s a fairly simple test for you to do. If you describe what you want to do, we can probably tell you how to do that in Slicer.</p>

---

## Post #3 by @aljarkow (2023-08-24 19:40 UTC)

<p>Hi, thanks for the reply. I am calculating changes in volume on Invisalign attachments, which are already very small to begin with (1-4mm height or width, some even 1mm) so changes would be very small. I am not sure which software would be easier to use and accurate for this purpose between the 2 I have available</p>

---
