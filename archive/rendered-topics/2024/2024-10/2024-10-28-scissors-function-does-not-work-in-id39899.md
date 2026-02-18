# Scissors function does not work in

**Topic ID**: 39899
**Date**: 2024-10-28
**URL**: https://discourse.slicer.org/t/scissors-function-does-not-work-in/39899

---

## Post #1 by @bkasmai (2024-10-28 20:38 UTC)

<p>I have just upgraded to slicer 5.6.2 from 4.11 and note that scissor function is not working. Has this been reported before?</p>

---

## Post #2 by @mikebind (2024-10-28 21:43 UTC)

<p>I regularly use the scissor function and have not noticed any issues with recent Slicer versions. Do you have any model nodes in your scene? Sometimes, when it looks like scissors isn’t doing anything to edit a segmentation, it is because there is a surface model which is the same as the segment (either by export or import or duplication) and the surface model is not affected by the scissors, only the segmentation.</p>

---

## Post #3 by @cpinter (2024-10-29 09:49 UTC)

<p>Please post a video so that we see how it does not work for you.</p>

---

## Post #4 by @bkasmai (2024-10-29 17:58 UTC)

<p>It seems the problem may be to do with importing data from v 4.11 to 5.6.2. I will see if I can reproduce the problem and then post video. Thanks for offer to help.</p>

---
