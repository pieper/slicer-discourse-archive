---
topic_id: 32949
title: "Failed Centerline Extraction With Extractcenterline Tree"
date: 2023-11-22
url: https://discourse.slicer.org/t/32949
---

# Failed Centerline Extraction with ExtractCenterline Tree

**Topic ID**: 32949
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/failed-centerline-extraction-with-extractcenterline-tree/32949

---

## Post #1 by @SANTIAGO_PENDON_MING (2023-11-22 11:16 UTC)

<p>Hi to everyone, today my post is quite simple. Extracting centerline curves with ExtractCenterline module using Trees fails a lot (joins with straight lines bifurcations with endpoint or something like that…). To be clear enough, the Network centerlines are not as well-made as we need so the only option are Tree centerlines.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfe5c75522208365968a7e0efb46a2c67f1ab454.jpeg" data-download-href="/uploads/short-url/vWGM0IShkVNRqiippmJW6zrYP6A.jpeg?dl=1" title="Captura de pantalla 2023-11-22 121029" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfe5c75522208365968a7e0efb46a2c67f1ab454_2_690x383.jpeg" alt="Captura de pantalla 2023-11-22 121029" data-base62-sha1="vWGM0IShkVNRqiippmJW6zrYP6A" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfe5c75522208365968a7e0efb46a2c67f1ab454_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfe5c75522208365968a7e0efb46a2c67f1ab454_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfe5c75522208365968a7e0efb46a2c67f1ab454_2_1380x766.jpeg 2x" data-dominant-color="414158"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-11-22 121029</span><span class="informations">1797×1000 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This type of bugged centerlines are obtained using segmentations, smoothed segmentation, models and smoothed models.</p>
<p>We also moved a little bit the endpoints to other positions and the results are equally bad.</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> .</p>

---

## Post #2 by @bserrano (2023-11-24 08:00 UTC)

<p>I’m experiencing the same issue. I attempted to resolve it by using version 4.2, and it eventually worked after the program crashed three times. Any suggestions for a permanent solution?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
