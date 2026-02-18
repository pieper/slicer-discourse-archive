# Resampling a label map

**Topic ID**: 32404
**Date**: 2023-10-24
**URL**: https://discourse.slicer.org/t/resampling-a-label-map/32404

---

## Post #1 by @Windy (2023-10-24 23:14 UTC)

<p>I know we can resample a volume using “Resample Scalar Volume” module. If I want to resample a LabelMap, is it correct to use the same module?</p>

---

## Post #2 by @muratmaga (2023-10-25 00:06 UTC)

<p>You can, however make sure you use the nearestneighbor interpolation when resampling labelmaps.</p>

---
