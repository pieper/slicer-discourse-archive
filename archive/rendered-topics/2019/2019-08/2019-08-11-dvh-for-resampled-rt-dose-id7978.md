# DVH for resampled RT Dose

**Topic ID**: 7978
**Date**: 2019-08-11
**URL**: https://discourse.slicer.org/t/dvh-for-resampled-rt-dose/7978

---

## Post #1 by @aseman (2019-08-11 08:48 UTC)

<p>Slicer version:4.10.1<br>
Hi 3D Slicer experts and all<br>
I exported RT Dose(Dimension:62x46x88) from TPS  and I converted it to a volume (Dimension: 256x256x89) using Resample Scalar Volume Module. I want to calculate DVH for this volume with Dose Volume Histogram module.But I can’t enter this volume as a Dose volume in input section. How can I calculate DVH for this volume?can you help me?<br>
Thanks a lot</p>

---

## Post #2 by @cpinter (2019-08-11 13:54 UTC)

<p>You can either</p>
<ol>
<li>Uncheck “Show dose volumes only”, but then it will be an “Intensity volume histogram” (only affects plot title and similar), or</li>
<li>Convert regular volume into a dose volume. See slides 17 and 18 in the latest <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials" rel="nofollow noopener">tutorial</a>
</li>
</ol>

---
