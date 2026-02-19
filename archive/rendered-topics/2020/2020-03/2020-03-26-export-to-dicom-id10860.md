---
topic_id: 10860
title: "Export To Dicom"
date: 2020-03-26
url: https://discourse.slicer.org/t/10860
---

# Export to DICOM

**Topic ID**: 10860
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/export-to-dicom/10860

---

## Post #1 by @Anonymous (2020-03-26 18:26 UTC)

<p>Hello,<br>
I am wondering what it means when Slicer says 2. Select export type: Scalar Volume (50%, 1 series) (DICOMScalarVolumePlugin) after right clicking my data and selecting Export to DICOM… Could you please explain what the 50% in scalar volume export type means? Also, it seems this is the only export type option.<br>
Thanks,<br>
Emily</p>

---

## Post #2 by @lassoan (2020-03-26 18:55 UTC)

<p>The percentage value quantifies the confidence of the exporter that it can export the series correctly. 50% corresponds “fairly confident” (usually only specialized exporters claim &gt;50% confidence).</p>

---
