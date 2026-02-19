---
topic_id: 17066
title: "Registration Mr And Ct Images"
date: 2021-04-13
url: https://discourse.slicer.org/t/17066
---

#  Registration MR and CT images

**Topic ID**: 17066
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/registration-mr-and-ct-images/17066

---

## Post #1 by @berileker (2021-04-13 15:36 UTC)

<p>Operating system:registraiton<br>
Slicer version:4.11.20200930<br>
Expected behavior:Registration MRI and CT images without any trouble<br>
Actual behavior:Since the CT image I have is cut from the lower part of the noise,many structures in the MR image do not correspond to the CT,so the registration process cannot be performed completely. What I should do? What do you suggest?</p>

---

## Post #2 by @lassoan (2021-04-14 04:44 UTC)

<p>In general, you need to crop the two input volumes to approximately the same region before attempting to register. The computed transform can then be applied to the entire non-cropped volume.</p>

---

## Post #3 by @berileker (2021-05-11 22:37 UTC)

<p>So how can I make this clipping process the most simple and convenient?</p>

---

## Post #4 by @lassoan (2021-05-12 00:07 UTC)

<p>For cropping volumes, the easiest is to use Crop volume module.</p>

---
