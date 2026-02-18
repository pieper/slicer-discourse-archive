# Segment statistics; what am I looking at?

**Topic ID**: 44861
**Date**: 2025-10-23
**URL**: https://discourse.slicer.org/t/segment-statistics-what-am-i-looking-at/44861

---

## Post #1 by @valblom (2025-10-23 17:32 UTC)

<p>Operating system:<br>
Slicer version: 3D Slicer 5.6.2</p>
<p>Hi!</p>
<p>I am using Segment Statistics. The input consists of a PET scan and a segmentation. The output creates a table. Min, max, mean, median and standard deviation are provided. When I look at the scalar volume statistics, unit is n/a.</p>
<p>I don’t understand, what this value holds. Could it be mean Bq?</p>
<p>I hope someone can help, I would love to hear!</p>

---

## Post #2 by @pieper (2025-10-24 13:32 UTC)

<p>Depending on how the data is loaded there may be no units attached to a volume, so you need to know what the data represents in order to interpret the statistics.  Typically PET that is loaded through DICOM will indicate if it is corrected or not, or whether is represents SUV calculated by various method.  So you would want to track down the history of the data to know for sure what you have.</p>

---
