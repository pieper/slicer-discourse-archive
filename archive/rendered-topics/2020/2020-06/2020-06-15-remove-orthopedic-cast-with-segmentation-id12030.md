# Remove Orthopedic cast with segmentation

**Topic ID**: 12030
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/remove-orthopedic-cast-with-segmentation/12030

---

## Post #1 by @eran_bam (2020-06-15 09:54 UTC)

<p>Hi everyone,<br>
After I try to remove the orthopedic cast from the CT image, I get the image that I attached. <a href="/404" data-orig-href="upload://4WPFtVVztSUFgVo2nrfkG9qYoIP.png">Untitled2222|598x455</a><br>
How can I fill the holes in the image to get the correct image without all these holes?</p>

---

## Post #2 by @timeanddoctor (2020-06-15 10:41 UTC)

<p>You can use the ‘smooth’ in segment module</p>

---

## Post #3 by @eran_bam (2020-06-15 11:32 UTC)

<p>Thank you! it’s work.</p>

---

## Post #4 by @lassoan (2020-06-16 01:23 UTC)

<p>You can also use <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a> if you need to fill larger holes.</p>

---

## Post #5 by @eran_bam (2020-06-16 06:26 UTC)

<p>Thank you, Andras!<br>
I try to fix this problem without changing the bones (to keep realistic)</p>

---
