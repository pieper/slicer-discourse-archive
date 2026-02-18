# Combining Segmentations in Slicer

**Topic ID**: 27634
**Date**: 2023-02-04
**URL**: https://discourse.slicer.org/t/combining-segmentations-in-slicer/27634

---

## Post #1 by @nysfour (2023-02-04 23:32 UTC)

<p>Hello, if I am using the segment editor module and I have multiple segment layers of different portions of an image, is there way to create a new segment layer that will combine all of the portions? For context, I want individual segmentations and then an overall segmentation of the whole structure without overwriting the previous segments or having to manually draw over the previous segmentations?</p>

---

## Post #2 by @lassoan (2023-02-04 23:36 UTC)

<p>You can use “Logical operators” effect to combine segments.</p>
<p>Alternatively, you can use Paint effect with masking. For example, to repaint all visible segments by selecting “Editable area” → “Inside all visible segments”.</p>

---

## Post #3 by @nysfour (2023-02-05 05:39 UTC)

<p>Thank you very much!</p>

---
