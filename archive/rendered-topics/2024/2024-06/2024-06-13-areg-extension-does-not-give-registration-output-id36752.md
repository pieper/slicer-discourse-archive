---
topic_id: 36752
title: "Areg Extension Does Not Give Registration Output"
date: 2024-06-13
url: https://discourse.slicer.org/t/36752
---

# AReg extension does not give registration output

**Topic ID**: 36752
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/areg-extension-does-not-give-registration-output/36752

---

## Post #1 by @Inka_Saraswati (2024-06-13 10:10 UTC)

<p>Hi, I’ve been trying to use AReg to register maxilla of a unilateral cleft patient to a mirror image of itself. The end goal is to create a model of the alveolar cleft defect by superimposing both skulls, then subtracting the defect from the mirrored normal side.</p>
<p>I’ve tried following the tutorial in 5.6.0 and 5.6.2 Slicer versions, using nrrd, niii.gz, and DICOM files. When I selected the folder for T2 scan, it has error notice “Patient does not have T2 scan” even though there is one in the folder. The orientation feature seems to work, but always leaves the output folder for the registration empty. I wonder if the fact that the two files are from the exact same date is an issue? Is there is a way to get this to work?</p>
<p>Thank you for any help!<br>
(Maybe Prof <a class="mention" href="/u/luciacev">@luciacev</a> can help?)</p>

---

## Post #2 by @Anais_Cavare (2025-03-18 19:25 UTC)

<p>Hi,<br>
I am encountering exactly the same problem! The process seems to stop during segmentation, and the T2 centered and Registered folders remain empty. Have you found a solution since you asked this question? Thanks in advance!</p>

---
