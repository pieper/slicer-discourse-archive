# Guidance on Intensity Correction for Siemens Multiband EPI Data

**Topic ID**: 46155
**Date**: 2026-02-14
**URL**: https://discourse.slicer.org/t/guidance-on-intensity-correction-for-siemens-multiband-epi-data/46155

---

## Post #1 by @Muhammad_Faizan (2026-02-14 04:24 UTC)

<p>I am working with EPI d</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45bb1bd9b0daf7e4240b7efcdf646caed759c263.jpeg" data-download-href="/uploads/short-url/9WRP6cUpIGnY5etT4hOSDZQigq7.jpeg?dl=1" title="sub-ICC141_chunk000_rep0_comparison" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45bb1bd9b0daf7e4240b7efcdf646caed759c263_2_690x332.jpeg" alt="sub-ICC141_chunk000_rep0_comparison" data-base62-sha1="9WRP6cUpIGnY5etT4hOSDZQigq7" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45bb1bd9b0daf7e4240b7efcdf646caed759c263_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45bb1bd9b0daf7e4240b7efcdf646caed759c263_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45bb1bd9b0daf7e4240b7efcdf646caed759c263_2_1380x664.jpeg 2x" data-dominant-color="848383"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sub-ICC141_chunk000_rep0_comparison</span><span class="informations">1920×924 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>ata acquired on a Siemens 3T scanner. The data is multiband with no in-plane acceleration. I reconstructed the multiband data using the slice GRAPPA technique.</p>
<p>However, I am facing an issue: the reconstructed image intensity fades from anterior to posterior. In contrast, the corresponding Siemens-reconstructed images appear intensity-corrected. I have completed the reconstruction, but I am unsure what additional post-processing steps are required to match Siemens’ reconstruction. Specifically, I am looking for guidance on how to perform intensity correction on reconstructed single-band data to improve image quality.</p>
<p>In each run (.dat) file, there is a prescan (3D acquisition) and a 2D EPI acquisition (which is reconstructed). The prescan has lower resolution:</p>
<p>Prescan resolution: (32, 32, coils, 64) → (partition, phase, coils, readout)</p>
<p>Body prescan: (32, 32, 2, 64)</p>
<p>Head prescan: (32, 32, 38, 64)</p>
<p>The reconstructed EPI has resolution (36, 64, 38, 64) → (slices, phase, coils, readout). I will attach an image comparing my reconstruction with the Siemens reconstruction for clarity regarding intensity differences and post-processing effects.</p>
<p>Currently, my approach is as follows:</p>
<p>Use affine transforms to map voxels from prescan and EPI into scanner XYZ coordinates.</p>
<p>Transform to EPI space and interpolate to match the prescan and EPI dimensions.</p>
<p>Compute the ratio head_prescan / body_prescan to correct the EPI, applying smoothing to the ratio.</p>
<p>Unfortunately, this approach does not produce the expected intensity correction. It is possible that I am not correctly using the geometry transforms in the Siemens header, or that this approach is not optimal.</p>
<p>Any guidance would be greatly appreciated. In particular, I am interested in:</p>
<p>Correct usage of Siemens geometry information for intensity correction or other approaches that work well</p>
<p>Open-source tools or implementations that can reproduce Siemens-like intensity correction</p>
<p>Thank you very much for your time and assistance.</p>

---

## Post #2 by @lassoan (2026-02-14 04:56 UTC)

<p>You can correct this inhomogeneity using <code>N4ITK MRI Bias Correction</code> module.</p>

---
