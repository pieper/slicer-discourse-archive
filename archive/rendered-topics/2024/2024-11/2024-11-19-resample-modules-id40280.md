# Resample Modules

**Topic ID**: 40280
**Date**: 2024-11-19
**URL**: https://discourse.slicer.org/t/resample-modules/40280

---

## Post #1 by @benedettabottelli (2024-11-19 22:13 UTC)

<p>Which is the difference between the Resample Scalar volume module and the Resample scalar/vector/DWI volume module? when do I use one rather than the other?</p>

---

## Post #2 by @pieper (2024-11-19 22:27 UTC)

<p>Resample Scalar volume should be considered just a simple utility for making the volume smaller or larger for convenience or debugging.  It doesn’t support rotation or translation and <a href="https://discourse.slicer.org/t/new-origin-after-resampling/40157/5">may not give the origin you expect</a>.  Resample scalar/vector/DWI volume is much more sophisticated, as the name chunkily implies, handles more sophisticated volume types.  Generally prefer the latter or if you only have scalar volumes, Resample Image (BRAINS).  The fact that these similar but different modules exist is a historical accident because different groups were addressing similar but slightly different use cases.</p>

---

## Post #3 by @benedettabottelli (2024-11-20 08:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da56860c6a7a6efff2e9a97f949d9341e2a5f0f0.jpeg" data-download-href="/uploads/short-url/v9vsNOUZkAXx7IPYw3mk84YexQ4.jpeg?dl=1" title="Immagine 2024-11-20 090158" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da56860c6a7a6efff2e9a97f949d9341e2a5f0f0_2_690x353.jpeg" alt="Immagine 2024-11-20 090158" data-base62-sha1="v9vsNOUZkAXx7IPYw3mk84YexQ4" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da56860c6a7a6efff2e9a97f949d9341e2a5f0f0_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da56860c6a7a6efff2e9a97f949d9341e2a5f0f0_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da56860c6a7a6efff2e9a97f949d9341e2a5f0f0_2_1380x706.jpeg 2x" data-dominant-color="8F8F94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Immagine 2024-11-20 090158</span><span class="informations">1918×982 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
during the resampling of this DICOM is it necessary changing the directional matrix even if 3D slicer recognize the plane of interest?</p>

---

## Post #4 by @pieper (2024-11-20 12:53 UTC)

<p>Probably not.  It depends what you want to do with it.  Provide more context of your goals and we may be able to help you more.</p>

---
