# Exporting segmentation To DicomRT

**Topic ID**: 13377
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/exporting-segmentation-to-dicomrt/13377

---

## Post #1 by @loubna (2020-09-07 15:39 UTC)

<p>Hi;</p>
<p>How much information is lost ( or lack of precision) when converting segmentation  to a series of contours? I think, there is a biais of conversion, I want to know how much this conversion is faithful to the initial segmentation performed in slicer ?</p>
<p>Thank’s in advance.</p>

---

## Post #2 by @lassoan (2020-09-08 01:50 UTC)

<p>It depends on how complex the segment’s shape is. If you want to know what details are lost exactly, export, reimport, then compare it to the original qualitatively and quantitatively (using Segment Comparison and DVH comparison modules).</p>

---
