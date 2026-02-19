---
topic_id: 36380
title: "Combine 2 Dental Cbct Scans Maxilla And Mandible"
date: 2024-05-25
url: https://discourse.slicer.org/t/36380
---

# Combine 2 dental cbct scans (maxilla and mandible)

**Topic ID**: 36380
**Date**: 2024-05-25
**URL**: https://discourse.slicer.org/t/combine-2-dental-cbct-scans-maxilla-and-mandible/36380

---

## Post #1 by @Aram_Terterian (2024-05-25 00:02 UTC)

<p>I have received a maxillary and mandibular scan of the same person and would like to combine the cbct , they are of the same instance and are a continuation of one another but for some reason, the medical center has split them into 2 different images, if anyone knows how to achieve this please let me know<br>
Thanks</p>

---

## Post #2 by @cpinter (2024-05-27 08:52 UTC)

<p>Is it of one acquisition but was manually split, or are they two acquisitions (with slightly different patient position etc.)?</p>
<p>If the first, then you could merge them with a simple script using numpy, in the second case it will be more complicated. I’m not aware of a module that handles this case, but maybe someone else will do.</p>
<p>In any case answering the question above and maybe providing a screenshot will help the issue move forward.</p>

---
