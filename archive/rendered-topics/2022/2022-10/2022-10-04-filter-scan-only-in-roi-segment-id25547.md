# Filter scan only in ROI / segment

**Topic ID**: 25547
**Date**: 2022-10-04
**URL**: https://discourse.slicer.org/t/filter-scan-only-in-roi-segment/25547

---

## Post #1 by @Niels (2022-10-04 19:06 UTC)

<p>I would like to filter (smoothen/blur) only a region of my scan.</p>
<p>Is that possible?</p>

---

## Post #2 by @pieper (2022-10-04 21:07 UTC)

<p>You could use the Mask effect in the Segment Editor to make two volumes, one inside the mask and one outside setting everything else to zero.  Then you could run the filter on only one and then use Add Scalar Volumes.  You may need to remask the filtered result since it could bleed out into the zeros depending on the filter.</p>

---

## Post #3 by @Niels (2022-10-05 13:46 UTC)

<p>Thank you pieper, that seems too work. but indeed, I need to play around with the correct mask to make the adjusted volume fit the original section without seeing any artefacts… wil play a bit further with it this evening.</p>

---
