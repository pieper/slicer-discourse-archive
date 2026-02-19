---
topic_id: 37590
title: "Hounsfield Units Measurement"
date: 2024-07-28
url: https://discourse.slicer.org/t/37590
---

# Hounsfield units measurement

**Topic ID**: 37590
**Date**: 2024-07-28
**URL**: https://discourse.slicer.org/t/hounsfield-units-measurement/37590

---

## Post #1 by @Hernan (2024-07-28 06:15 UTC)

<p>I’m trying to measure the mean HU in various regions of interest of proximal humerus in coronal and axial slices. I was using radiant before but thing is i’m getting huge HU variations in same patients and between them (example, some of them got around 400-500 HU and the others even -120)…<br>
So I’m trying Slicer.<br>
Is there any tool in this app that might help me get better or more reliable results?<br>
Thanks<br>
By the way, I’m new to Slicer so I don’t relalyt know how to use it yet. Just tried to get a segment of a CT scan but all its measuring is volume in mm3</p>

---

## Post #2 by @pieper (2024-07-30 13:29 UTC)

<p>Look for the Segment Statistics module.</p>
<p>Also be sure your data is loaded correctly (depending on the scanner it might not be generating the correct headers to calibrate HU values - depending on the accuracy you need you may also want to research just how accurate different CT scanners/protocols are at exactly measuring HU).</p>

---

## Post #3 by @CS1 (2025-10-19 01:26 UTC)

<p>Hi Pieper, would you mind elaborating a bit more on what you mean by lading the data correctly? Thank you! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2025-10-19 13:13 UTC)

<p>The values that Slicer reports depend a lot on the source of the data. Cone-beam or microCT values may vary widely depending on the scanner vendor and the file format.  Clinical scanners may report nominal HU and put out valid DICOM, but if you want really accurate measures they need to be well calibrated and perhaps even use a calibration phantom in the scan.  Also the acquisition or reconstruction process may trade off picture quality for absolute accuracy.</p>

---
