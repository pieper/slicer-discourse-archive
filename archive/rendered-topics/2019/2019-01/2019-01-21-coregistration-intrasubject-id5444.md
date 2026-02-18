# Coregistration - intrasubject

**Topic ID**: 5444
**Date**: 2019-01-21
**URL**: https://discourse.slicer.org/t/coregistration-intrasubject/5444

---

## Post #1 by @RadioQuest (2019-01-21 15:54 UTC)

<p>Hi…<br>
Can I coregister T1, T2, post gad and FLAIR scans of the same patient with a brain tumor to get a new single volume?<br>
ABC module works only with normal brains. I want to perform TA  later.<br>
Thanks.<br>
Kind regards,<br>
RQ</p>

---

## Post #2 by @lassoan (2019-01-31 02:00 UTC)

<p>“General registration (BRAINS)” and “General registration (Elastix)” modules should be able to register these images to each other. SlicerElastix extension need to be installed to get the Elastix registration module.</p>

---
