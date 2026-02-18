# Surface registration/multi volume

**Topic ID**: 4325
**Date**: 2018-10-09
**URL**: https://discourse.slicer.org/t/surface-registration-multi-volume/4325

---

## Post #1 by @Melanie (2018-10-09 11:18 UTC)

<p>Is there a function of surface registration in extensions that can be applicable to multi volume sequences, without having to segment structures separately. Thank you</p>

---

## Post #2 by @lassoan (2018-10-09 15:00 UTC)

<p>Sequence registration extension can compute displacement fields directly from volume sequences. You then need to segment only a single volume. You can get segmentation for any other volume by applying the appropriate displacement field to the segmentation. Use “fixed frame to moving frames” as transform direction in Sequence Registration module; and segment the volume that you selected by “fixed frame index”.</p>

---

## Post #3 by @Melanie (2018-10-10 14:43 UTC)

<p>Thank you very much Prof Lasso</p>

---
