---
topic_id: 5280
title: "Registration Of Two Ct Image"
date: 2019-01-05
url: https://discourse.slicer.org/t/5280
---

# Registration of two CT image

**Topic ID**: 5280
**Date**: 2019-01-05
**URL**: https://discourse.slicer.org/t/registration-of-two-ct-image/5280

---

## Post #1 by @aseman (2019-01-05 08:53 UTC)

<p>Operating system:4.8.1<br>
Hi 3D Slicer experts and all<br>
I want to register two CT images (i.e lung contours) and I used Segment Registration Module. Finally it doesn’t register two images (like below figure), and the message that gives me this is “Resampling fixed volume” (and in Data module for fixed image: Resampled 1 x1x1 mm).  Also, it results PreAlignment Moving 2 Fixed Linear Transform and doesn’t give Deformable Transform. Can you guide me about this problem?<br>
thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4e60f74e529b93a0487cb50fa236b9efc9f26ed.png" alt="picture1" data-base62-sha1="s5Qu9jkTMKcrKlb3Jq9iCcKQdqJ" width="270" height="250"></p>

---

## Post #2 by @lassoan (2019-01-05 14:13 UTC)

<p>Does the two segment come from the same patient? Can you attach a screenshot with 3 orthogonal views?</p>
<p>You get deformable transform if you choose “Deformable” registration at the bottom.</p>
<p>Use latest stable Slicer-4.10 or latest nightly version.</p>

---
