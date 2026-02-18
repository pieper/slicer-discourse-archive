# Resetting paint draw etc

**Topic ID**: 39028
**Date**: 2024-09-28
**URL**: https://discourse.slicer.org/t/resetting-paint-draw-etc/39028

---

## Post #1 by @Hannnonk (2024-09-28 15:38 UTC)

<p>3D slicer version 6.6.1 windows</p>
<p>Have increased resolution of CT scan using Crop volume.<br>
However, when using segment editor, paint and draw “thickness” still seems to be the original “thickness” pre - crop volume changes. Any way to match paint thickness etc to new ct scan resolution?</p>
<p>thanks</p>

---

## Post #2 by @muratmaga (2024-09-29 01:17 UTC)

<p>If you generated the segmentation before you used the crop volume on the CT scan, segment editor will inherit the original resolution.</p>
<p>If you haven’t done much, go ahead and start from scratch choosing the new output from the crop volume as the master volume.</p>
<p>or you cna use the Modify Segment Geometry option to increase the resolution of existing segmentation.</p>

---
