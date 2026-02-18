# DICOM series is split into two

**Topic ID**: 36124
**Date**: 2024-05-13
**URL**: https://discourse.slicer.org/t/dicom-series-is-split-into-two/36124

---

## Post #1 by @Levi (2024-05-13 18:13 UTC)

<p>Hello,</p>
<p>I imported a single folder of 790 DICOM files into 3DSlicer. However, it separates the files into two series, one with 348 files and the other with 442. They both posses the same series name, and are under the same Patient and Study ID. When I render the files, only one is shown. This also goes for when I export said render as an STL file. I have never encountered this issue before. In the past I have imported far more files from the same scanner and never had a problem.</p>
<p>I am curious if anyone knows how to render all the scans at once within 3Dslicer so I can have a complete model of the scan.</p>

---

## Post #2 by @lassoan (2024-05-13 18:15 UTC)

<p>If you click the “Advanced” checkbox in the DICOM module (bottom-right corner in the browser) then you will see why the series has been split into two and you can also choose there to load all the entire series as a single 3D image.</p>

---

## Post #3 by @Levi (2024-05-15 19:25 UTC)

<p>Thanks for the advice, unfortunately however, when I click Examine, it says it runs the MultiVolume plugIn, but doesn’t display any information afterwards.</p>

---
