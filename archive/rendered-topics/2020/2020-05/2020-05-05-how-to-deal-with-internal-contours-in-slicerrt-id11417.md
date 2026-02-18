# How to deal with internal contours in SlicerRT

**Topic ID**: 11417
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/how-to-deal-with-internal-contours-in-slicerrt/11417

---

## Post #1 by @loubna (2020-05-05 14:24 UTC)

<p>Hi;</p>
<p>How can I remove the internal contours from planar contours in SlicerRT. I want keep only the extreme outer contours?</p>
<p>Thank’s in advance</p>

---

## Post #2 by @cpinter (2020-05-05 15:33 UTC)

<p>Do you mean structures that has holes in them and are represented as keyholes like in case of the skin or rectum?</p>
<p>If so, then I think your best bet is to use the Wrap Solidify effect in Segment Editor on the segmentation that is created from the planar contours. You can find more information about this in the forum.</p>
<p>What is your overall goal?</p>

---
