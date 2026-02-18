# Brain SPECT with Tc99m HMPAO problem loading dicom file

**Topic ID**: 42920
**Date**: 2025-05-14
**URL**: https://discourse.slicer.org/t/brain-spect-with-tc99m-hmpao-problem-loading-dicom-file/42920

---

## Post #1 by @Dominic_Velasco_MD_M (2025-05-14 05:24 UTC)

<p>It seems that when I load the Dicom file the volume rendering is distorted. The axial, coronal is the brain spect tomo, and sagittal are not displaying as you would expect it to be.  The dicom file is from Siemen Simbia. 3D slicer version 5.9, windows 11.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcf04f28d995fcccee6ecc308857ee8c40e3e3d1.jpeg" data-download-href="/uploads/short-url/A5BbkcRi9dKQ9XEENmfyJEkkgI9.jpeg?dl=1" title="Screenshot 2025-05-14 064209" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcf04f28d995fcccee6ecc308857ee8c40e3e3d1_2_690x390.jpeg" alt="Screenshot 2025-05-14 064209" data-base62-sha1="A5BbkcRi9dKQ9XEENmfyJEkkgI9" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcf04f28d995fcccee6ecc308857ee8c40e3e3d1_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcf04f28d995fcccee6ecc308857ee8c40e3e3d1_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcf04f28d995fcccee6ecc308857ee8c40e3e3d1_2_1380x780.jpeg 2x" data-dominant-color="30303A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-05-14 064209</span><span class="informations">1920×1087 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-05-14 17:41 UTC)

<p>That appears to be the raw acquisition data and not the 3D reconstruction.</p>

---

## Post #3 by @Dominic_Velasco_MD_M (2025-05-15 00:16 UTC)

<p>Thank you for this reply you are correct I’ve asked them to give me the 3d<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c23c19f2d9cae6dbf9e6165c7b26f449f16683b9.jpeg" data-download-href="/uploads/short-url/rIhoxC06pPoPGsk7pFkFIk2JuDn.jpeg?dl=1" title="AS Surface Scan Inferior" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23c19f2d9cae6dbf9e6165c7b26f449f16683b9_2_644x500.jpeg" alt="AS Surface Scan Inferior" data-base62-sha1="rIhoxC06pPoPGsk7pFkFIk2JuDn" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23c19f2d9cae6dbf9e6165c7b26f449f16683b9_2_644x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23c19f2d9cae6dbf9e6165c7b26f449f16683b9_2_966x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23c19f2d9cae6dbf9e6165c7b26f449f16683b9_2_1288x1000.jpeg 2x" data-dominant-color="575A6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AS Surface Scan Inferior</span><span class="informations">1305×1013 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
reconstruction images and they worked!</p>

---
