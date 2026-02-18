# How to overlay pre- and post-operative dental DICOM files to measure bone gain ?

**Topic ID**: 46099
**Date**: 2026-02-09
**URL**: https://discourse.slicer.org/t/how-to-overlay-pre-and-post-operative-dental-dicom-files-to-measure-bone-gain/46099

---

## Post #1 by @Sont (2026-02-09 15:01 UTC)

<p>Hello,</p>
<p>I would like to overlay two dental DICOM files (pre-operative and post-operative) following a bone graft in order to measure the volumetric bone gain (in mm and/or %). To perform these measurements, I would need to be able to distinguish between the two datasets, for example by assigning a different color to one of the DICOM files.</p>
<p>I have not been able to find any tutorial or explanation on how to do this.<br>
Would you know how to proceed?</p>
<p>Thank you for your help !</p>

---

## Post #2 by @cpinter (2026-02-09 15:08 UTC)

<p>If you already have the registration (correct overlap of the two images), then you can choose a different color table for each of them in the Volumes module. For example one with Green the other one with Red.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ed529d7b0d314fa9ffea4656241511ed83fdc2c.png" data-download-href="/uploads/short-url/dwVA8i2SlIWlSBqnIhiu5rsMLuc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ed529d7b0d314fa9ffea4656241511ed83fdc2c.png" alt="image" data-base62-sha1="dwVA8i2SlIWlSBqnIhiu5rsMLuc" width="459" height="436"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">459×436 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then you can make the forground volume 50% opaque, and you’ll see the differences.</p>
<p>You can also use modules like the one that creates a checkerboard, but I don’t remember its name.</p>

---

## Post #3 by @Sont (2026-02-09 19:15 UTC)

<p><strong>Thank you for your response!</strong><br>
I tried this approach, but once the CBCTs are registered, the result is a <strong>single file</strong>, so I can only assign <strong>one color</strong> to it. Changing the colors of the two original CBCTs does not affect the final superimposed volume.<br>
I performed the registration using <strong>Elastix</strong>.</p>
<p><strong>Did I miss a step?</strong></p>

---

## Post #4 by @cpinter (2026-02-10 12:50 UTC)

<p>You can only register two images, in which one is the fixed and the other is the moving image, which will get the resulting transform applied. Set one color table to the fixed image and the other to the moving one.</p>
<p>If you still have problems, please elaborate more on what is actually wrong (what you did exactly and what you expected differently) and add screenshots. That way we can reduce the number of iterations. Thanks</p>

---
