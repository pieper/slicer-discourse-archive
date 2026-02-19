---
topic_id: 3948
title: "Nii Saving Bit Range"
date: 2018-08-30
url: https://discourse.slicer.org/t/3948
---

# Nii saving (bit range)

**Topic ID**: 3948
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/nii-saving-bit-range/3948

---

## Post #1 by @Heiko_Stark (2018-08-30 13:45 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.8<br>
Expected behavior: smallest bit resolution in nii file<br>
Actual behavior: signed int32</p>
<p>My data are in the range of -2000…7000.<br>
How can I modify it?</p>

---

## Post #2 by @Sam_Horvath (2018-08-30 14:17 UTC)

<p>You can use the Cast Scalar Volume module to change the data to a smaller bit resolution.  It will not auto detect the smallest, you will need to pick what resolution you want to cast it to.</p>

---

## Post #3 by @Heiko_Stark (2018-08-31 13:41 UTC)

<p>Thanks!</p>
<p>I will use unsigned short.</p>

---
