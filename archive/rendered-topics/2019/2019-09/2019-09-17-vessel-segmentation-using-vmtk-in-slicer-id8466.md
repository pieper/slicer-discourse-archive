# Vessel Segmentation using VMTK in Slicer

**Topic ID**: 8466
**Date**: 2019-09-17
**URL**: https://discourse.slicer.org/t/vessel-segmentation-using-vmtk-in-slicer/8466

---

## Post #1 by @Pooja_Virkar (2019-09-17 10:57 UTC)

<p>Hello,</p>
<p>I need to do liver vessel segmentation.<br>
I installed VMTK from extension Manager in Slicer. I am using Slicer version 4.10.1</p>
<p>When I try to use vesselness filtering or Level set segmentation from VMTK module in Slicer,<br>
I am getting the following error -</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/552cfdb88e713a112446951bf1b2b931d2a0a394.png" alt="Screenshot_1" data-base62-sha1="c9uYDjyR79TNZpGCNpwQ2NJPxLm" width="528" height="338"></p>
<p>Also I would like to know how to set the parameters in Vesselness filtering? I tried using different values but still not getting any good vessel output.<br>
Please help me.</p>

---

## Post #2 by @lassoan (2019-09-17 13:34 UTC)

<p>You have run out of memory. You can crop and/or resample your input volume (using Crop volume module), increase virtual memory size in your system settings, or add more physical memory to your computer. Also, update to latest stable release (currently 4.10.2).</p>

---
