---
topic_id: 19956
title: "How To Complete A Segmentation Where There Is No Image To Se"
date: 2021-10-01
url: https://discourse.slicer.org/t/19956
---

# How to complete a segmentation where there is no image to segment?

**Topic ID**: 19956
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/how-to-complete-a-segmentation-where-there-is-no-image-to-segment/19956

---

## Post #1 by @Matheus (2021-10-01 15:20 UTC)

<p>Hey guys,</p>
<p>I segmented some DICOM files but I can’t complete the subcutaneous fat segmentation because my images are incomplete (as shown in the image: <a href="/uploads/short-url/sGvSMfmM7VM6FBGmIrgNEbYF7lM.jpeg">knee segmentation</a>). Is there any way I can complete the segmentation?</p>
<p>I know how thick and shaped the subcutaneous fat should be in this empty region. If there is some way to add empty images to the DICOM file for example, this would probably work.</p>
<p>Does anyone know any way to help me?</p>
<p>Thanks!!</p>

---

## Post #2 by @lassoan (2021-10-01 17:52 UTC)

<p>You can use “Crop volume” module to enlarge a volume. If you already have a segmentation then you then need to modify the segmentation’s geometry using “Specify geometry” button. See details in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">Segment Editor module’s documentation</a>.</p>

---
