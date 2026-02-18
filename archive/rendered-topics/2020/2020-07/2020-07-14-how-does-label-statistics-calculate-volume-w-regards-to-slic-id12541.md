# How does Label Statistics Calculate Volume w/ regards to Slice Thickness/Spacing

**Topic ID**: 12541
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/how-does-label-statistics-calculate-volume-w-regards-to-slice-thickness-spacing/12541

---

## Post #1 by @ebear (2020-07-14 19:04 UTC)

<p>We used the Editor module to delineate tumor volumes slice-by-slice for an MRI series with slice thickness of 0.5mm and slice spacing of 1mm.</p>
<p>When using Label Statistics to convert these slice-by-slice labels into a Label Map volume, does 3D slicer automatically fill the volume in between slices when calculating. I.e., does it multiply the selected slice pixel area by the distance between the next slice, or does it multiply it by slice thickness?</p>
<p>If it multiplies by slice thickness, would this mean that our label map volume is ~1/2 the actual tumor volume as we missed out on 0.5mm of thickness per slice due to differing slice thickness vs slice spacing?</p>

---

## Post #2 by @pieper (2020-07-14 19:22 UTC)

<p>Good question: Slicer always works in spacing (distance between sample centers within and between slices) and does not explicitly consider thickness.  You can verify you are getting the calculations you need by segmenting single pixel and getting statistics.  If some processing step needed to incorporate thickness into a calculation it would need to pull the information back from the dicom database, but I’m not aware of any code that does this currently.</p>

---

## Post #3 by @lassoan (2020-07-14 19:33 UTC)

<p>Slice thickness just affects appearance of a slice (how much it is blurred). It does not change the image geometry or result of volume calculations.</p>

---
