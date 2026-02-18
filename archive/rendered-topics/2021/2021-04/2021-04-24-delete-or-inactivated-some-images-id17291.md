# Delete or inactivated some images

**Topic ID**: 17291
**Date**: 2021-04-24
**URL**: https://discourse.slicer.org/t/delete-or-inactivated-some-images/17291

---

## Post #1 by @Valentina_Mejia_Gall (2021-04-24 03:10 UTC)

<p>Hello!,<br>
i’m working in a project where we have to reconstruct the same bone but we are changing the number or slices we’re using.<br>
Achieving this with a CT scan with about 30000 images, so we want to make the same reconstruction using the 30000 images but also using 2000, 1000 and 500. by suppressing every one, two three images</p>
<p>Is there an efficient way to do it in 3dslicer or do i have to do it by importing the Dicom files manually and apart for every reconstruction even when it is the same patient data.</p>

---

## Post #2 by @lassoan (2021-04-25 14:08 UTC)

<p>You can ceetainly remove slices before DICOM import. Each slice file contains position information so Slicer will know where each slice belongs.</p>
<p>However, it may be a sinpler to import the full-resolution image and resample it with keeping the original spacing for the first two axes and increasing it for the third axis. There are several image resample modules in Slicer and most of them allow anisotropic resampling.</p>

---
