# Track head position

**Topic ID**: 7453
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/track-head-position/7453

---

## Post #1 by @Zhao_Su (2019-07-08 01:12 UTC)

<p>I want to add a NDI tool on a tracked stuff , but when I move it , it is not like reality in the computer. How can I do calibration or registration?</p>

---

## Post #2 by @Sunderlandkyl (2019-07-08 13:06 UTC)

<p>Have you tried completing the SlicerIGT tutorials?<br>
<a href="http://www.slicerigt.org/wp/user-tutorial/" class="onebox" target="_blank" rel="nofollow noopener">http://www.slicerigt.org/wp/user-tutorial/</a></p>
<p>Specifically the landmark registration tutorial.</p>

---

## Post #3 by @Zhao_Su (2019-07-09 13:37 UTC)

<p>Thanks a lot for your reply! I had completed that tutorial.But the head has to keep still.If I stick a tool to the head, how can I do the calibration? (Like if the head moves，the head model in the computer moves exactly like in reality.)<br>
My English is not so well. If I understand the tutorial wrong, please forgive me.</p>

---

## Post #4 by @lassoan (2019-07-16 21:26 UTC)

<p>If you follow the landmark registration tutorial then you can move the patient as you want, the registration will remain valid, as you compute the transformation between the image and the patient-attached Reference marker.</p>
<p>You may decide to use the Reference coordinate system as Slicer’s world coordinate system (then the head will not move on screen if you physically move it) or use the Tracker coordinate system as world coordinate system (then the head will move on screen if you move it physically). Either way, registration will still remain valid.</p>

---
