# Image registration

**Topic ID**: 5512
**Date**: 2019-01-25
**URL**: https://discourse.slicer.org/t/image-registration/5512

---

## Post #1 by @Ash_Alarfaj (2019-01-25 14:12 UTC)

<p>Problem report for Slicer 4.10.0 win-amd64: expected: uniform and aligned slices.<br>
actual behaviour: as MRI Table move through scan the slices registration error happened when the image processed in a computer. Can 3d slicer programme correct and align image slices?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95558d48ce0e6ae854300329e9c23d8ec155a849.jpeg" data-download-href="/uploads/short-url/lj4r6wmnIXY5CEn23gPWI5kLWhr.jpeg?dl=1" title="marlou2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95558d48ce0e6ae854300329e9c23d8ec155a849_2_690x384.jpeg" alt="marlou2" data-base62-sha1="lj4r6wmnIXY5CEn23gPWI5kLWhr" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95558d48ce0e6ae854300329e9c23d8ec155a849_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95558d48ce0e6ae854300329e9c23d8ec155a849_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95558d48ce0e6ae854300329e9c23d8ec155a849_2_1380x768.jpeg 2x" data-dominant-color="7C7E85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">marlou2</span><span class="informations">1940×1080 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-01-25 14:26 UTC)

<p>You could use the CropVolume module to cut the two parts, then put one in a Transform to move it to the right place and then harden it.  Then you probably need to use CropVolume again to make a big enough volume to hold both parts, and then use Add Volumes to make a new volume with the parts in the right places.</p>

---

## Post #3 by @Ash_Alarfaj (2019-01-25 16:34 UTC)

<p>Thank you for your fast response but do you think this will not affect volume measurement? as I intentionally need to measure the volume of elbow muscle.</p>

---

## Post #4 by @pieper (2019-01-25 19:19 UTC)

<p>The data is corrupted by the motion artifact, so yes there will be some error.  Lacking any other information you’ll need to make a manual correction and then estimate how much this increases the possible error of the measurement.</p>

---
