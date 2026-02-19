---
topic_id: 44487
title: "Measuring An Irregular 3D Image Surface Area"
date: 2025-09-15
url: https://discourse.slicer.org/t/44487
---

# Measuring an irregular 3D image surface area

**Topic ID**: 44487
**Date**: 2025-09-15
**URL**: https://discourse.slicer.org/t/measuring-an-irregular-3d-image-surface-area/44487

---

## Post #1 by @highlook (2025-09-15 21:30 UTC)

<p>Hello everyone. After segmenting brain tumors from contrast-enhanced brain MRI images using the BrainLab application, I can export the resulting 3D tumor image as a DICOM file. My goal is to calculate the surface area of ​​this non-geometric 3D object contained in the DICOM file. Could you help me with this? Thank you in advance.</p>

---

## Post #2 by @pieper (2025-09-15 22:45 UTC)

<p>Yes, you can get all that with the SegmentStatistics module.</p>

---

## Post #3 by @highlook (2025-09-16 08:29 UTC)

<p>Thanks for prompt response. However, segmentstatistics can’t recognize that dicom file. How can i import it into the module?</p>

---

## Post #4 by @pieper (2025-09-16 12:11 UTC)

<p>You would need to install the Quantitative Reporting extension and import the DICOM SEG as a Segmentation in Slicer and then you can use the Segment Statistics module.</p>

---
