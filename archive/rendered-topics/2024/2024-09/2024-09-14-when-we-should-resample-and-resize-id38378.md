# When we should resample and resize?

**Topic ID**: 38378
**Date**: 2024-09-14
**URL**: https://discourse.slicer.org/t/when-we-should-resample-and-resize/38378

---

## Post #1 by @sajad_amiri (2024-09-14 13:46 UTC)

<p>I was working with a dataset (<a href="https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/?swpmtx=a4e8067aeba864db9b1451b15a61997c&amp;swpmtxnonce=4475fb572b" rel="noopener nofollow ugc">https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/?swpmtx=a4e8067aeba864db9b1451b15a61997c&amp;swpmtxnonce=4475fb572b</a>), and while annotating with both T2 and DWI, the segmentation was accurate in 3D Slicer. However, the sizes of T2 and DWI images differed. How is this possible? Should I resize the images? After resizing, the segmentation appears incorrect!</p>

---

## Post #2 by @lassoan (2024-09-14 15:49 UTC)

<p>It is normal that various images are properly aligned in physical space but have completely different geometry (different origin, spacing, axis directions). You don’t need to resample the images, unless you use some software or algorithm that operates in voxel space, i.e., ignores image origin, spacing, axis directions.</p>

---

## Post #3 by @sajad_amiri (2024-09-14 16:13 UTC)

<p>I’ve used the code of pyradiomics. Is it okay ? (Like pyradiomic extension )</p>

---

## Post #4 by @sajad_amiri (2024-09-15 19:48 UTC)

<p>Hello dear <a class="mention" href="/u/lassoan">@lassoan</a> I’ve used the code of pyradiomics. Is it okay ? (Like pyradiomic extension )</p>

---

## Post #5 by @lassoan (2024-09-16 01:23 UTC)

<p>Pyradiomics takes the image geometry into account, so it should not be necessary to resample.</p>

---
