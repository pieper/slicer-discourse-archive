# SlicerMorph: about values in sliders for PCA deformation

**Topic ID**: 19858
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/slicermorph-about-values-in-sliders-for-pca-deformation/19858

---

## Post #1 by @Ale (2021-09-26 02:32 UTC)

<p>Dear Slicer community. I’m playing with GPA module, specially deforming the mean shape along principal axes.  My question is if the values in the slider represent the position in percentage of the target shape? I guess that 100 and -100 are the extremes of selected component?<br>
Thanks in advance.</p>
<p>Ale</p>

---

## Post #2 by @muratmaga (2021-09-26 04:57 UTC)

<p>-100, +100 are the negative and positive extremes of selected PC. They are not necessarily percentages, but an arbitrary scale factor.</p>

---
