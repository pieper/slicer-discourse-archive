# Bands appear in the painted area when segmenting brain MRI

**Topic ID**: 19320
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/bands-appear-in-the-painted-area-when-segmenting-brain-mri/19320

---

## Post #1 by @H.Khasawneh (2021-08-23 16:04 UTC)

<p>We have been facing some issues when trying to create segmentations on Brain MRI. The draw tool wouldn’t work and when we try to use the paint tool we get lines or band like segmentations instead of the circular shape of the tool. Is there a way around this, or an idea of what the cause of this issue is?<br>
Thank you.</p>

---

## Post #2 by @lassoan (2021-08-23 16:05 UTC)

<p>This is because you segment on oblique slices (slice view is not aligned with image axes). See more information and your options to deal with this <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments">here</a>.</p>

---
