# Brain cortical surface reconstruction with blood vessel

**Topic ID**: 4567
**Date**: 2018-10-28
**URL**: https://discourse.slicer.org/t/brain-cortical-surface-reconstruction-with-blood-vessel/4567

---

## Post #1 by @ljc19800331 (2018-10-28 21:30 UTC)

<p>Operating system: Ubuntu 16.04 and Windows 10<br>
Slicer version: 4.9<br>
Expected behavior: Brain 3D reconstruction with blood vessel<br>
Actual behavior:<br>
Hello, I am wondering if there is a better way to generate the brain cortical surface with surface blood vessel after craninotomy in 3D slicer, as shown in the following images. This is for cortical surface registration between intraoperative and preoperative data. I have some questions:</p>
<ol>
<li>For figure 1, is it possible to be generated in 3D Slicer?</li>
<li>For figure 2 and 3, is it possible to be generated in 3D Slicer? If not, what software could generate these figures?<br>
Thanks for the information.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f970fc2328901d1f4a6cce568834bdeaae86dcf.jpeg" alt="3D_reconstruction" data-base62-sha1="icIhLQnFr7AEt1AcIOEXpK0fDzN" width="690" height="445"></li>
</ol>
<p>ref: <a href="https://discourse.slicer.org/t/3d-surface-reconstruction/2665" class="inline-onebox">3D surface reconstruction</a></p>

---

## Post #2 by @lassoan (2018-10-29 16:03 UTC)

<p>Yes you can generate all the figures above using 3D Slicer. You need to have the necessary T1 and MR-angio images and strip the skull and segment vessels as described in the <a href="https://discourse.slicer.org/t/3d-surface-reconstruction/2665/5">post referenced above</a>.</p>

---
