---
topic_id: 45377
title: "How To Correctly Warp A Cct Rtstruct Target Volume To 4Dct A"
date: 2025-12-05
url: https://discourse.slicer.org/t/45377
---

# How to correctly warp a CCT RTSTRUCT target volume to 4DCT after CCT→4DCT registration?

**Topic ID**: 45377
**Date**: 2025-12-05
**URL**: https://discourse.slicer.org/t/how-to-correctly-warp-a-cct-rtstruct-target-volume-to-4dct-after-cct-4dct-registration/45377

---

## Post #1 by @Huoqin_Zhou (2025-12-05 15:17 UTC)

<p>(Original post deleted upon author’s request to protect private information. -staff)</p>

---

## Post #2 by @cpinter (2025-12-09 10:00 UTC)

<p>It seems to me that your workflow should work.</p>
<p>First I’d verify that the resulting registration is what you want. It seems that your registration was a 6 DOF rigid one, so there is no vector field, but you can still visualize the vectors in the Transform module’s Display section. Also you can place landmarks on the border of the CCT, apply the transform on the fiducial markup node, and see how the markups changed (whether they appear in the expected locations on the 4DCT).</p>
<p>If the registration is not correct, obviously you need to work on that part. If it is, it might be a visualization issue but let’s go step by step.</p>

---
