# RTStruct viewing anomalies for radiomics

**Topic ID**: 16512
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/rtstruct-viewing-anomalies-for-radiomics/16512

---

## Post #1 by @furMan (2021-03-12 22:15 UTC)

<p>Operating system:Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior:  imported RTStruct mask to show what MRI image regions are masked, and non-masked,  when viewing<br>
Actual behavior: Two problems:(1)  The displayed binary image mask has artifacts (some masked slices are not shown as masked) (2) when I mouse over the mask + image, the ROI does not always show as being masked.</p>
<p>Basically, the masking when using the RTStruct Dicom doesn’t seem reliable when viewing.   This is not a problem when I use a binary mask read in as a Dicom volume.</p>
<p>If this is just a viewing artifact, I’m not concerned.  My concern is whether the RTstruct masks are not reliable for radiomics processing.</p>
<p>Thank you,<br>
Mike</p>

---

## Post #2 by @lassoan (2021-03-13 14:14 UTC)

<p>If you view the closed surface representation in slice views and you have complex segmentation (with holes, etc) then it is indeed just a visualization artifact. You can either switch to binary labelmap representation or switch to a recent Slicer version, where this problem has been already fixed.</p>

---
