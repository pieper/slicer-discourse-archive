# Apply filters to a CT scan to deal with high-contrast elements

**Topic ID**: 45560
**Date**: 2025-12-19
**URL**: https://discourse.slicer.org/t/apply-filters-to-a-ct-scan-to-deal-with-high-contrast-elements/45560

---

## Post #1 by @Francesca_Parrotta (2025-12-19 12:49 UTC)

<p>Good morning everyone,</p>
<p>I am workin with CT scans as the one attached (I am attaching just one slice of the CT). My objective is to recognize and segment all the different layers in the scanned structure. As you can see, the lower part is a very high-contrast region, and this is covering elements in the mid-lower part of my structure. Moreover, due to this high-contrast element, the grey levels of the other layers apper very similar to each other.</p>
<p>I was wondering whether I could be able to filter out this white part, in order to increase the contrast between the other layers. To do so, I tried to use some 3D Slicer filtering, specifically “Threshold scalar volume”. Do you have any suggesion on this regard?</p>
<p>Best,</p>
<p>Francesca</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d35f4d7c91120e1cc6174e79bc9b5bde4f0b039.jpeg" data-download-href="/uploads/short-url/fA7E0NSeQRy0Z3ORx2VYevHSs8V.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d35f4d7c91120e1cc6174e79bc9b5bde4f0b039_2_690x374.jpeg" alt="image" data-base62-sha1="fA7E0NSeQRy0Z3ORx2VYevHSs8V" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d35f4d7c91120e1cc6174e79bc9b5bde4f0b039_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d35f4d7c91120e1cc6174e79bc9b5bde4f0b039.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d35f4d7c91120e1cc6174e79bc9b5bde4f0b039.jpeg 2x" data-dominant-color="474747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">773×420 42.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
