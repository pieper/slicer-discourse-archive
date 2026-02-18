# Create 1 model out of 3 volumes with different kernels

**Topic ID**: 10332
**Date**: 2020-02-18
**URL**: https://discourse.slicer.org/t/create-1-model-out-of-3-volumes-with-different-kernels/10332

---

## Post #1 by @zeliair (2020-02-18 13:25 UTC)

<p>Hey!<br>
I want to do threshold segmentation of the cranium.<br>
We found 2 different Kernels, one shows the teeth perfectly, the other one the cranial base.<br>
Now I want to merge the two Kernels into 1 model !<br>
Is this possible?<br>
Thank you!</p>

---

## Post #2 by @lassoan (2020-02-18 13:26 UTC)

<p>Yes, that should be no problem at all. In Segment Editor module, you can switch between master volumes any time. Once you segmented the teeth using one volume, switch to the other volume and segment the cranial base.</p>

---
