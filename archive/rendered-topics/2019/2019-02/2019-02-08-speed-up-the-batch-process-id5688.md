# Speed up the batch process

**Topic ID**: 5688
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/speed-up-the-batch-process/5688

---

## Post #1 by @anandmulay3 (2019-02-08 08:30 UTC)

<p>How can i speed up the slicer process?<br>
in my batch process i’m creating segments form Dicom data and exporting the 3d model output.<br>
For skull, foot or any small body part data takes few minutes (2-5 min) , but for the pelvis data it takes around 30-40 min.<br>
i can understand the pelvis data covers large body part but can we speedup this process anyhow??</p>

---

## Post #2 by @pieper (2019-02-08 12:57 UTC)

<p>You can use print statements or a profiler to identify what is taking the time and see if time is being spent inefficiently (like Instruments in Xcode on the mac, or corresponding tools on other platforms).  Or you can publish a script that demonstrates the slowdown and others can maybe help.  Otherwise there’s not much we can do to help.</p>

---
