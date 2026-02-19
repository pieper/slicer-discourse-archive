---
topic_id: 14574
title: "How Can I Get The Hounsfield Units From A Dicom File Acquire"
date: 2020-11-12
url: https://discourse.slicer.org/t/14574
---

# how can I get the Hounsfield Units from a DICOM file acquired by CB. The purpose of knowing this, it this is to analyze the bone density of both jaws for the correct planning of dental implants. Thank you.

**Topic ID**: 14574
**Date**: 2020-11-12
**URL**: https://discourse.slicer.org/t/how-can-i-get-the-hounsfield-units-from-a-dicom-file-acquired-by-cb-the-purpose-of-knowing-this-it-this-is-to-analyze-the-bone-density-of-both-jaws-for-the-correct-planning-of-dental-implants-thank-you/14574

---

## Post #1 by @odonto100 (2020-11-12 20:37 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @manjula (2020-11-12 21:29 UTC)

<p>If you move the mouse pointer to the area of interest, in the data probe you will see the HU unit for the point.</p>
<p>But i guess for your purpose you need to consider a region and average it to have a meaningful value. So go to segmentation and segment the area of interest. For your purpose, I guess a scissor tool would be best (fill inside, circle or rectangle, symmetric 2 mm ) and then use the segment statistic module (scalar volume statistics plugin - mean). This will give the mean HU value of the ROI you segment.</p>

---
