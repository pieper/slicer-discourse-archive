---
topic_id: 44099
title: "Segmentation Export To Dicom Rt"
date: 2025-08-15
url: https://discourse.slicer.org/t/44099
---

# Segmentation export to DICOM-RT

**Topic ID**: 44099
**Date**: 2025-08-15
**URL**: https://discourse.slicer.org/t/segmentation-export-to-dicom-rt/44099

---

## Post #1 by @CSalt (2025-08-15 22:42 UTC)

<p>Hello,</p>
<p>I have segmentations from PET dicom source images that I would like to export as DICOM-RT files. I have the extension SlicerRT. Is this possible?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b472579d2901a121a68ed577deeb3404bd336989.png" data-download-href="/uploads/short-url/pKiV9pJkAwqKLj2fUicUPgLlHMR.png?dl=1" title="Screenshot 2025-08-15 at 6.31.01 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b472579d2901a121a68ed577deeb3404bd336989_2_690x165.png" alt="Screenshot 2025-08-15 at 6.31.01 PM" data-base62-sha1="pKiV9pJkAwqKLj2fUicUPgLlHMR" width="690" height="165" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b472579d2901a121a68ed577deeb3404bd336989_2_690x165.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b472579d2901a121a68ed577deeb3404bd336989.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b472579d2901a121a68ed577deeb3404bd336989.png 2x" data-dominant-color="F5EDEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-08-15 at 6.31.01 PM</span><span class="informations">916×220 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Shmarvinoid (2025-08-17 17:34 UTC)

<p>Have you found a solution?</p>

---

## Post #3 by @cpinter (2025-08-18 10:04 UTC)

<p>I very recently <a href="https://github.com/Slicer/Slicer/pull/8538">added</a> PET export to the CreateDicomSeries module, and I think that would fix this issue. Please download the latest preview version and try with that.</p>

---
