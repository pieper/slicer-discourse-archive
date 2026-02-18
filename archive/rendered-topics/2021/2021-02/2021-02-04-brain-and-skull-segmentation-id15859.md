# Brain and skull segmentation

**Topic ID**: 15859
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/brain-and-skull-segmentation/15859

---

## Post #1 by @Saima (2021-02-04 07:38 UTC)

<p>Hi Andras,<br>
I segmented the brain and removed the skull. I now need to get some extra layer on top of the brain extracted assuming that it is a skull how can I do it. and another layer for the scalp as well on top of skull.</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-02-05 04:10 UTC)

<p>Please describe in more detail what you would like to achieve and include a few annotated screenshots or sketches.</p>

---

## Post #3 by @Saima (2021-02-08 07:30 UTC)

<p>Hi,<br>
I have a single brain segmentation. I now need to get the skull segmentation and scalp segmentation without any gaps between the three segmentations. how can i get this. Can I grow a segmentation and then subtract it from brain segmentation. How can I grow a brain segmentation so it covers the skull and scalp as well.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima safdar</p>

---

## Post #4 by @slicer365 (2021-02-08 08:29 UTC)

<p>Have you used the swiss skull stripper module</p>

---

## Post #5 by @lassoan (2021-02-08 21:12 UTC)

<p>Yes, Swiss Skull Stripper can provide the brain segment. Skin surface extraction is easy (see for example <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">this segmentation recipe</a>). Bone segmentation on general T2 MRI images is hard (bone is essentially not visible), but if you don’t want to have gaps between the 3 segments then you can consider “skull” to be anything that is inside the skin and not brain (and generate it using “Logical operators” effect in Segment Editor).</p>

---
