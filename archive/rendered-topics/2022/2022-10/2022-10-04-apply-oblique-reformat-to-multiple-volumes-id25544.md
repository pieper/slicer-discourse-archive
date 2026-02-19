---
topic_id: 25544
title: "Apply Oblique Reformat To Multiple Volumes"
date: 2022-10-04
url: https://discourse.slicer.org/t/25544
---

# Apply oblique reformat to multiple volumes

**Topic ID**: 25544
**Date**: 2022-10-04
**URL**: https://discourse.slicer.org/t/apply-oblique-reformat-to-multiple-volumes/25544

---

## Post #1 by @pkenned (2022-10-04 14:00 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello, I have dozens of CT volumes obtained of an implanted device. I wish to make measurements of local changes over time related to the device however this requires me to reformat the slice orientations to obtain the correct orientation for measurement. Is there a way to save the reformat of one series and then apply it to another without having to manually do the reformatting? There is no patient motion throughout the entire run so if I can go to the same slice orientation I could also make a pseudo cine over time .</p>
<p>Thanks for any input.</p>

---

## Post #2 by @pieper (2022-10-04 23:47 UTC)

<p>Maybe you can do this by applying a transform to the volume instead of using the view reformat.  Then you could just put apply the same transform to all the volumes.</p>

---
