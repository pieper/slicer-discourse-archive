# Deformable registration between two CTs

**Topic ID**: 20564
**Date**: 2021-11-10
**URL**: https://discourse.slicer.org/t/deformable-registration-between-two-cts/20564

---

## Post #1 by @alan6690 (2021-11-10 13:57 UTC)

<p>Hello. I am a new user of 3D slicer. I am trying to deformably register a set of CBCT with regular CT. However, the CBCT has a much smaller FOV so that there is a large dark region outside the FOV,  in which regular CT does not have.  And it seems that this incoherent region between the two image sets causes some undesirable deformation during registration.</p>
<p>I am looking for a way to circularly crop the regular CT so that both CT and CBCT have the same FOV. Or is there anyway to define a ROI to be used during registration so that only the anatomy within the ROI would be deformed?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-11-11 03:48 UTC)

<p>To get started, have a look at <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">this documentation section</a>. Align the volumes and crop the volumes to the same anatomical region. Additional mask can be defined to exclude small region, such as screws, implants, fiducial markers, etc.</p>

---

## Post #3 by @alan6690 (2021-11-12 00:14 UTC)

<p>I tried create mask by scissors tool in segment editor module. But it seems that I can only apply the mask directly onto the volume and crop it, instead of applying on the the registration aglorithm. Would you mind give me some lead? Thank you.</p>

---

## Post #4 by @lassoan (2021-11-12 01:35 UTC)

<p>Registration algorithms usually require the mask to be specified as a labelmap volume. You can export the segmentation to labelmap by right-clicking on it in Data module.</p>

---

## Post #5 by @alan6690 (2021-11-13 05:38 UTC)

<p>Thank you so much. Exporting as a labelmap works well for my case.</p>

---

## Post #6 by @alan6690 (2021-11-16 03:16 UTC)

<p>The deformation is performed very well now. However, I don’t know why after every deformation the moving image is shifted longitudinally for a bit (inf-sup direction) and I have to manually adjust the IS transformtion so that two images are matched slice-to-slice. Not a big problem though. I just wonder what causes this transformation. Very much appreciated if you can give some suggestion. Thank you.</p>

---

## Post #7 by @lassoan (2021-11-16 06:22 UTC)

<p>Which module did you end up using for registration?<br>
Can you attach a screenshot that demonstrates the image shift?</p>

---

## Post #8 by @alan6690 (2021-11-16 14:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af775b795c1ac7c3ffaeff2e2ba92524aecd3ee.jpeg" data-download-href="/uploads/short-url/8pDS9R9BcuW7xciTK9UhbSjUxem.jpeg?dl=1" title="CB" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3af775b795c1ac7c3ffaeff2e2ba92524aecd3ee_2_690x388.jpeg" alt="CB" data-base62-sha1="8pDS9R9BcuW7xciTK9UhbSjUxem" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3af775b795c1ac7c3ffaeff2e2ba92524aecd3ee_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3af775b795c1ac7c3ffaeff2e2ba92524aecd3ee_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3af775b795c1ac7c3ffaeff2e2ba92524aecd3ee_2_1380x776.jpeg 2x" data-dominant-color="939696"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CB</span><span class="informations">1920×1080 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3028ae953032c4e3f824a6ebec56f5eb38d79787.jpeg" data-download-href="/uploads/short-url/6S24UMnLEO9Ypb1C7z3PIFvuobt.jpeg?dl=1" title="PL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3028ae953032c4e3f824a6ebec56f5eb38d79787_2_690x388.jpeg" alt="PL" data-base62-sha1="6S24UMnLEO9Ypb1C7z3PIFvuobt" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3028ae953032c4e3f824a6ebec56f5eb38d79787_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3028ae953032c4e3f824a6ebec56f5eb38d79787_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3028ae953032c4e3f824a6ebec56f5eb38d79787_2_1380x776.jpeg 2x" data-dominant-color="939696"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PL</span><span class="informations">1920×1080 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am using the preset of “generic (all)” of general registration (Elastix) to do the deformation. The picture shows the translational error between the fixed image(53_CB_spacing_lung) and already deformed image (53_PL_CB_deformed). The segment in green is what I applied as a labelmap for the deformation, whereas the ROI boxes in two pictures outlines the border of two images respectively.</p>
<p>As both images have the same dimension, I wonder if this translational error would persist if I export the images as DICOM for further usage? Or it only appears when I view the image in the 3D slicer application?</p>
<p>Thank you.</p>

---

## Post #9 by @alan6690 (2021-11-16 15:32 UTC)

<p>The problem seems to come from that the output deformed volume is not automatically centered in the application after the deformation. But it does not affect the exported DICOM image. The visually mismatch in the application can be simply solved by manual centering in the Volume module. I would suggest automatic centering of the output deformed volume to be enabled in the future for convenience. Thank you for you help.</p>

---
