# CT image registration

**Topic ID**: 14430
**Date**: 2020-11-04
**URL**: https://discourse.slicer.org/t/ct-image-registration/14430

---

## Post #1 by @sahithi (2020-11-04 13:52 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.10.2<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/481087b6127f6022f28e502904d50e5487e76992.jpeg" data-download-href="/uploads/short-url/ahvNcc8RiBQj8SxxGefItHvZ12G.jpeg?dl=1" title="output" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/481087b6127f6022f28e502904d50e5487e76992_2_690x466.jpeg" alt="output" data-base62-sha1="ahvNcc8RiBQj8SxxGefItHvZ12G" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/481087b6127f6022f28e502904d50e5487e76992_2_690x466.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/481087b6127f6022f28e502904d50e5487e76992_2_1035x699.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/481087b6127f6022f28e502904d50e5487e76992.jpeg 2x" data-dominant-color="222121"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">output</span><span class="informations">1329×899 69.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hello Everyone,</p>
<p>while i was trying to register two CT abdomen  scans using general registration(brains) - geometry align, in the output image i am getting lines at the corners( attached the output image).</p>
<p>I really appreciate it if somebody can tell me where it is going wrong.<br>
Looking forward for the response.</p>
<p>Thank you,</p>

---

## Post #2 by @mikebind (2020-11-05 18:49 UTC)

<p>Hello, that is occurring because the registered output has areas which are outside the original volume, and those areas are having their voxels filled with 0’s.  On CT this means they look like water.  You can fix this by changing the “Advanced Output Settings” parameter “Background Fill Value” to -1000 instead of 0.  That way any filled areas will look like air instead of water.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/376f5358403c16d3cdd2299105302ba3fd3ab092.png" alt="image" data-base62-sha1="7UoM2kaeCeO5dwg1GFJKsxnQOcO" width="598" height="320"></p>

---
