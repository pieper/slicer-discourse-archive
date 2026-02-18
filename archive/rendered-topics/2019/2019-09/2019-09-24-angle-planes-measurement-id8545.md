# Angle Planes measurement

**Topic ID**: 8545
**Date**: 2019-09-24
**URL**: https://discourse.slicer.org/t/angle-planes-measurement/8545

---

## Post #1 by @Thom (2019-09-24 12:27 UTC)

<p>Hi!<br>
Im using the angle planes extension to try to measure an angle between the lateral semicircular canal and the vestibular aqueduct. I marked the wanted angle in the picture. The extension shows me 3 angles(pitch,yaw,roll), which one of these angles is the one i wanted and how do i know?<br>
Thanks!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9672aeb68974cde629fc179a7b38f86128508158.png" data-download-href="/uploads/short-url/lsVkfzA84fW8AyeZilFH6P2CqCI.png?dl=1" title="Angle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9672aeb68974cde629fc179a7b38f86128508158_2_690x374.png" alt="Angle" data-base62-sha1="lsVkfzA84fW8AyeZilFH6P2CqCI" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9672aeb68974cde629fc179a7b38f86128508158_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9672aeb68974cde629fc179a7b38f86128508158_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9672aeb68974cde629fc179a7b38f86128508158_2_1380x748.png 2x" data-dominant-color="828395"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Angle</span><span class="informations">2560×1390 472 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-09-24 12:50 UTC)

<p>You can compute angle between planes in several different ways. If you need angle between plane normal vectors then copy-paste this code snippet in the Python interactor: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_slice_planes" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_slice_planes</a></p>

---
