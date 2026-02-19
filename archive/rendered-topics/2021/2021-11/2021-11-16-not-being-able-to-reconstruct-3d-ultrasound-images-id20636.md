---
topic_id: 20636
title: "Not Being Able To Reconstruct 3D Ultrasound Images"
date: 2021-11-16
url: https://discourse.slicer.org/t/20636
---

# Not being able to reconstruct 3D ultrasound images

**Topic ID**: 20636
**Date**: 2021-11-16
**URL**: https://discourse.slicer.org/t/not-being-able-to-reconstruct-3d-ultrasound-images/20636

---

## Post #1 by @CompSci101 (2021-11-16 06:01 UTC)

<p>Operating system: macOS Big Sur<br>
Slicer version:4.11.20210226<br>
Expected behavior:For the reconstruction of the 3D ultrasound to display a 3D image similar to the tutorial with the dataset of the TorsoCT.<br>
Actual behavior: 2D image being displayed of the ultrasound images as shown in the attachment below.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c739f96b37091325ffe778c9afc72101dcf183f.jpeg" data-download-href="/uploads/short-url/1M9s02oOVfAM2234mYtf6Sxa5Sn.jpeg?dl=1" title="Screenshot 2021-11-16 at 11.22.17 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c739f96b37091325ffe778c9afc72101dcf183f_2_690x431.jpeg" alt="Screenshot 2021-11-16 at 11.22.17 AM" data-base62-sha1="1M9s02oOVfAM2234mYtf6Sxa5Sn" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c739f96b37091325ffe778c9afc72101dcf183f_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c739f96b37091325ffe778c9afc72101dcf183f_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c739f96b37091325ffe778c9afc72101dcf183f_2_1380x862.jpeg 2x" data-dominant-color="A8A6A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-11-16 at 11.22.17 AM</span><span class="informations">1920×1200 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-11-16 06:18 UTC)

<p>This is just a 2D movie of a 3D ultrasound. What you see is not suitable for 3D reconstruction and you won’t be able to 3D print this image sequence.</p>
<p>It might be possible that these sequences contain actual 3D volumetric data in private fields or there are other files on the disk that contain 3D data, but this rarely happens for keepsake ultrasounds. If you want to give it a try anyway then you can follow <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">these instructions</a>.</p>

---
