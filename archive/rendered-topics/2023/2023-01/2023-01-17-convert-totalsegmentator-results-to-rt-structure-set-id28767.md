---
topic_id: 28767
title: "Convert Totalsegmentator Results To Rt Structure Set"
date: 2023-01-17
url: https://discourse.slicer.org/t/28767
---

# Convert TotalSegmentator results to RT structure set

**Topic ID**: 28767
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/convert-totalsegmentator-results-to-rt-structure-set/28767

---

## Post #1 by @LipTeck_Chew (2023-01-17 07:47 UTC)

<p>Hi Lassoan,</p>
<p>After the segmentation by the totalsegmentator is completed, how do we convert it to dicom RT structure set for a dicom rt send to another computer? FYI, we have tested a dicom send and it is working.</p>
<p>Thank you.</p>
<p>regards,<br>
LipTeck</p>

---

## Post #2 by @lassoan (2023-01-17 18:47 UTC)

<p>After you install SlicerRT extension you get the option of <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#dicom-data">exporting the segmentation to DICOM</a> as DICOM RT Structure Set.</p>

---

## Post #3 by @LipTeck_Chew (2023-01-18 02:20 UTC)

<p>Hi Lasso</p>
<p>I have tested on 100 slice of 2.5 mm CT with either 3.0 mm or 1.5 mm segmentation using totalsegmentator and Gaussian smooth to 1mm. After export to dicom, there was only 22 slices of AutoSS file. There should be 100.</p>
<p>Any workaround?</p>
<p>Regards<br>
Lip Teck</p>

---
