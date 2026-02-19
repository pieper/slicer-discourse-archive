---
topic_id: 29749
title: "Revealing Patient Data"
date: 2023-05-31
url: https://discourse.slicer.org/t/29749
---

# Revealing Patient Data

**Topic ID**: 29749
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/revealing-patient-data/29749

---

## Post #1 by @Brandon_Holt (2023-05-31 17:09 UTC)

<p>Hey guys, this might be a dumb question, but how do I enable patient data so that is shows up in my slice window? I would like to export various slices (Axial, Coronal, and Sagittal) that include all of the patient data that you would normally see when looking at the imaging using something like RadiAnt.</p>

---

## Post #2 by @pieper (2023-05-31 18:00 UTC)

<p>Probably you can get what you need by checking out the options in the DataProbe.  If the volumes were loaded from dicom they should have pretty complete metadata.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dataprobe.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dataprobe.html</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee4e122e218e6408ef7e511971005a5bf5faf2e.jpeg" data-download-href="/uploads/short-url/vNOmXILNm0xfW5Dk5l7QM52HNCe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee4e122e218e6408ef7e511971005a5bf5faf2e_2_690x287.jpeg" alt="image" data-base62-sha1="vNOmXILNm0xfW5Dk5l7QM52HNCe" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee4e122e218e6408ef7e511971005a5bf5faf2e_2_690x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dee4e122e218e6408ef7e511971005a5bf5faf2e_2_1035x430.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dee4e122e218e6408ef7e511971005a5bf5faf2e.jpeg 2x" data-dominant-color="3C3C3B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1377×574 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Brandon_Holt (2023-05-31 18:46 UTC)

<p>Thank you so much, it worked like a charm!</p>

---
