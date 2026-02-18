# cbct distortion

**Topic ID**: 45493
**Date**: 2025-12-15
**URL**: https://discourse.slicer.org/t/cbct-distortion/45493

---

## Post #1 by @seda_ozdemir (2025-12-15 11:18 UTC)

<p>In 3D Slicer version 5.10.0, when we load a CBCT with a 24 × 19 mm FOV, distortion occurs in the sagittal and coronal slice views. How can we resolve this issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02a01c876ce039e83dd830d7ea1bb24e7977ab22.jpeg" data-download-href="/uploads/short-url/ndZvItftxtaurqe6PrVJLWxpOG.jpeg?dl=1" title="Ekran Alıntısı.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a01c876ce039e83dd830d7ea1bb24e7977ab22_2_690x373.jpeg" alt="Ekran Alıntısı.PNG" data-base62-sha1="ndZvItftxtaurqe6PrVJLWxpOG" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a01c876ce039e83dd830d7ea1bb24e7977ab22_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a01c876ce039e83dd830d7ea1bb24e7977ab22_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a01c876ce039e83dd830d7ea1bb24e7977ab22_2_1380x746.jpeg 2x" data-dominant-color="79787F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Alıntısı.PNG</span><span class="informations">1920×1040 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-12-15 13:36 UTC)

<p>You’ll need to fix the anterior-superior image spacing in the Volume Information part of the Volumes module.  Normally this would be automatic if the data were in valid DICOM format, but probably you have the data in some non-standard format.  You’ll need to provide more details if you want specific help.</p>

---
