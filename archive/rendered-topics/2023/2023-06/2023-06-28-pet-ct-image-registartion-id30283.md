# PET/CT image registartion

**Topic ID**: 30283
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/pet-ct-image-registartion/30283

---

## Post #1 by @Sbeta (2023-06-28 14:24 UTC)

<p>Hi, I am a learner. I have a 512x512x74 CT image with 0.3848x0.3848x3 mm voxel size and PET image,135x135x74 with 3x3x3mm voxel size. Please advise me on the PET/CT registration process with different dimensions and voxel sizes. I tried Resample volume but gives an error. Thank you.</p>

---

## Post #2 by @pieper (2023-06-28 20:07 UTC)

<p>If these were from a fairly modern PET/CT scanner, and you loaded via dicom and the headers were correct, then the images should have loaded in the correct patient space, no resampling needed.</p>

---

## Post #3 by @Sbeta (2023-06-29 00:36 UTC)

<p>Thank you ! The original PET images 256x256x74 with voxels size 1.59095x 1.59095 x74 were resized and convolved using Matlab then converted to nrrd format to add in the 3D slicer.</p>

---

## Post #4 by @pieper (2023-06-29 09:32 UTC)

<p>It’s likely that the matlab step lost the geometry information.  You’ll need to trace the calculation and reconstruct the correct origin, spacing, and directions to make the volumes line up again.</p>

---

## Post #5 by @Sbeta (2023-06-29 12:25 UTC)

<p>Thank you. Yes, I have considered origin, direction and voxel size.</p>

---

## Post #6 by @Sbeta (2023-07-16 01:06 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a7bd7c1560a6c6c64d18ab40d4cadc0f9a7a669.png" alt="Screenshot 2023-07-15 174450" data-base62-sha1="cUsiRJNMAxMIwmVS6wyTz62Vopz" width="676" height="435"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3adb707ec4b2df0d00cd297b4115a1ae662fe168.png" data-download-href="/uploads/short-url/8oFQ5mJFMYufvO209yv6lZiIVxC.png?dl=1" title="Screenshot 2023-07-15 174526 (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3adb707ec4b2df0d00cd297b4115a1ae662fe168.png" alt="Screenshot 2023-07-15 174526 (1)" data-base62-sha1="8oFQ5mJFMYufvO209yv6lZiIVxC" width="690" height="440" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-15 174526 (1)</span><span class="informations">701×448 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have these two images to register, I am not sure if I need to change the origin before landmark registration. After registration, I am intending to see the dose (PET unit Gy) in the selected volume using segment editor and quantification. I will greatly appreciate your help! Thank you.</p>

---

## Post #7 by @Sbeta (2023-07-16 04:43 UTC)

<p>I guess I can use Resample scalar/vector/DWI volume module to change the origin through the Manual output parameter.</p>

---
