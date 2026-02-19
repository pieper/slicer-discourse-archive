---
topic_id: 12606
title: "Dicom Loading Planes Problems"
date: 2020-07-17
url: https://discourse.slicer.org/t/12606
---

# DICOM Loading Planes Problems 

**Topic ID**: 12606
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/dicom-loading-planes-problems/12606

---

## Post #1 by @chedepablo (2020-07-17 23:23 UTC)

<p>Hello team,</p>
<p>I’m relatively new to 3D Slicer, I have a MRI study with several series description, 19 series to be exact with 1957 instances, however, when I tried to load the images, I don’t get the three planes correctly. I understand that they are different studies, but when I choose a series number, it won’t choose the correct planes. Probably I need to go back to the study and change some settings? I have the brain MR and in the same study I have an Angio Brain MR. To be more specific my main goal is to visualize the three planes and I don’t know where my error is. Is it the radiologist technician? Am I uploading the series incorrectly? A tutorial or somebody that I could talk to I would appreciate it!!!</p>
<p>Thank you!</p>
<p>J.</p>

---

## Post #2 by @lassoan (2020-07-17 23:30 UTC)

<p>Please try with latest Slicer Preview Release. We have made lots of fixes and improvements that might help.</p>
<p>Angio series may be 2D time series, and then it is normal that you see them only in a single plane.<br>
Can you post a few screenshots or explain in detail what you mean by “I don’t get the three planes correctly”?</p>

---
