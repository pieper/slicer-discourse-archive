---
topic_id: 16511
title: "How Do I Erase Colic Air Automatically Segmented By Lung Ct"
date: 2021-03-12
url: https://discourse.slicer.org/t/16511
---

# How do I erase colic air automatically segmented by Lung CT Analyzer?

**Topic ID**: 16511
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/how-do-i-erase-colic-air-automatically-segmented-by-lung-ct-analyzer/16511

---

## Post #1 by @GammaMi (2021-03-12 22:15 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8</p>
<p>Expected behavior:<br>
Actual behavior: sometimes the Lung CT analyzer extension automatically selects colic gas when segmenting lungs. How do I remove it?</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a></p>

---

## Post #2 by @rbumm (2021-03-13 09:42 UTC)

<p>There are actually two ways to do this:</p>
<p>Before pressing “Apply” , you could select “Other” markers and place a few of them into the area of colic gas.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa7627beba8cb49b9ebd09ce69f12e888212ea5c.png" alt="image" data-base62-sha1="zJGvS6PJjxUXzeXai4ronVIr4Ek" width="297" height="71"></p>
<p>With each placement, the preview will update itself and show you a new model. “Other” can be used to mark anything that is not right or left lung.</p>
<p>Secondly (if the misinterpreted area is very big or lung leaking even to the outside of the skin),  you could play with the intensity range slider (slide the right one a bit to the middle and press “Update”. Then  “Apply”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/715e4248f5759ffb6e731471c86ff904f1c656aa.png" alt="image" data-base62-sha1="gaTTZ2Tz23cXuZ72eh3v5sAqQd4" width="518" height="84"></p>

---

## Post #3 by @GammaMi (2021-03-13 10:59 UTC)

<p>Thank you very much indeed for your fast and precise response.<br>
I’ll try as soon as possible.</p>
<p>Have a nice day,<br>
Guido.</p>

---
