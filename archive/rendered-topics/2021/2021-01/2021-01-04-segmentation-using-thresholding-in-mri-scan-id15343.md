---
topic_id: 15343
title: "Segmentation Using Thresholding In Mri Scan"
date: 2021-01-04
url: https://discourse.slicer.org/t/15343
---

# Segmentation using Thresholding in MRI Scan

**Topic ID**: 15343
**Date**: 2021-01-04
**URL**: https://discourse.slicer.org/t/segmentation-using-thresholding-in-mri-scan/15343

---

## Post #1 by @JacobD (2021-01-04 23:22 UTC)

<p>Hello,</p>
<p>I am attempting to segment bone from a shoulder MRI. Using the threshold feature, I have been able to select the humerus and scapula so that they can be modeled, however, there is other area highlighted that matches the same intensity in the threshold range. I was wondering what the best way to remove the unwanted highlighted area would be, without using the erase tool on each individual slide.</p>
<p>I tried to use the scissors tool, however, it cuts out sections from various points in the scan that I am attempting to keep. For example, an area of soft tissue is highlighted, but it cannot be cut out because when the scan is at a superficial location as opposed to a deep location, there is bone present that should be kept, but would be deleted if the scissors tool is used.</p>
<p>With a CT scan, I have been able to split islands to segments and remove unwanted segments, but with the MRI scan, the program does not seem to detect islands, so other segments are not made.</p>
<p>I am learning this software, so I may not be familiar with the proper techniques to accomplish this goal, but I appreciate any suggestions or information that may be helpful.</p>
<p>Thank you,<br>
Jacob</p>

---

## Post #2 by @pieper (2021-01-04 23:47 UTC)

<p>Yes, MRI is very different from CT and there is no general purpose solution.  Bones from MR is a particularly challenging task because their relatively low water content means less signal.  Grow from seeds is probably your best option.</p>

---
