# How to get hepatic vein and portal vein in different color or in different segment?

**Topic ID**: 40868
**Date**: 2024-12-27
**URL**: https://discourse.slicer.org/t/how-to-get-hepatic-vein-and-portal-vein-in-different-color-or-in-different-segment/40868

---

## Post #1 by @hepato (2024-12-27 12:05 UTC)

<p><strong>I use function of</strong> <strong>“</strong> <strong>theshold</strong> <strong>”</strong> <strong>to get the vessel of liver ,including hepatic vein and portal vein.</strong> <strong>And then the color of hepatic vein is same with portal vein in same segment.</strong> <strong>My question is How to get hepatic vein and portal vein in different color ?</strong> <strong>or how to get hepatic vein or portal vein in different segment ?</strong> <strong>Any recommendations ?</strong></p>

---

## Post #2 by @Deep_Learning (2024-12-27 14:00 UTC)

<p>If you have a good segmentation with both (Seg1),  Clone the segmentation  (Seg1 and Seg 2 identical).   Then use the scissors (or another tool) to remove the portal vein from Seg1.  Then Subtract Seg1 from Seg2.  Assign different colors to Seg1 and Seg2.</p>

---

## Post #3 by @hepato (2024-12-29 01:01 UTC)

<p>Thanks  for your answer!</p>

---
