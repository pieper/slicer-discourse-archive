# Matching CBCT scans and calculating the volume difference after bone augmentation

**Topic ID**: 26767
**Date**: 2022-12-16
**URL**: https://discourse.slicer.org/t/matching-cbct-scans-and-calculating-the-volume-difference-after-bone-augmentation/26767

---

## Post #1 by @Johanna_Caca (2022-12-16 13:05 UTC)

<p>Hello,</p>
<p>I´m looking for a software which can match cbct scans from before and after bone augmentation of the jaw bone and calculate the volume difference in the region of interest in the jaw bone. Is this possible with 3D Slicer?</p>
<p>Thank you so much for your help!</p>
<p>Johanna</p>

---

## Post #2 by @muratmaga (2022-12-16 19:39 UTC)

<p>You can rigidly register post and pre-op scans, and then segment the difference to calculate the change. All the tools you need should be present in Slicer.</p>

---
