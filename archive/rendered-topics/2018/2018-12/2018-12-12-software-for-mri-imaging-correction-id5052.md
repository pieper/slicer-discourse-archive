---
topic_id: 5052
title: "Software For Mri Imaging Correction"
date: 2018-12-12
url: https://discourse.slicer.org/t/5052
---

# Software for mri imaging correction!

**Topic ID**: 5052
**Date**: 2018-12-12
**URL**: https://discourse.slicer.org/t/software-for-mri-imaging-correction/5052

---

## Post #1 by @thanos (2018-12-12 09:48 UTC)

<p>Operating system:win 64<br>
Slicer version:4.10<br>
I’m new on Slicer !I’ running a project and i need some software to correct flow artifacts on T1 after gd injection ,intencity correction due to distance from isocenter ,and maybe BBB leakage correction!?I think correction is needed before starting any segmentation process and exporting models!Thank you! Ceep the good work!</p>

---

## Post #2 by @pieper (2018-12-12 15:24 UTC)

<p>Hi <a class="mention" href="/u/thanos">@thanos</a> -  I don’t think we have anything for BBB leakage, but you might want to look at using the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/N4ITKBiasFieldCorrection" rel="nofollow noopener">N4 bias correction module</a>.</p>

---
