---
topic_id: 18733
title: "Segmentation Mask Not Overlayed On Top Of The Original Data"
date: 2021-07-14
url: https://discourse.slicer.org/t/18733
---

# Segmentation Mask not overlayed on top of the original data

**Topic ID**: 18733
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/segmentation-mask-not-overlayed-on-top-of-the-original-data/18733

---

## Post #1 by @ZakiaKhatun (2021-07-14 16:09 UTC)

<p>Hello everyone,<br>
I have a CT scan of the knee and an STL file (as segmentation mask) separately. When I load the STL file, it does not overlay on top of my CT data. From the image below, you can see that the 3D object in yellow color (knee segmentation) is not on top of the CT.<br>
Could you kindly tell me how to see the segmentation on top of the original CT data (somewhat similar shown in the attached expected image)? Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3b1bf675f6183fcd45c6989f8f7576298687a4d.png" data-download-href="/uploads/short-url/nm6EjNB9z1EjycnuzGWVDacaSJv.png?dl=1" title="Knee_MRI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b1bf675f6183fcd45c6989f8f7576298687a4d_2_281x500.png" alt="Knee_MRI" data-base62-sha1="nm6EjNB9z1EjycnuzGWVDacaSJv" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b1bf675f6183fcd45c6989f8f7576298687a4d_2_281x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3b1bf675f6183fcd45c6989f8f7576298687a4d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3b1bf675f6183fcd45c6989f8f7576298687a4d.png 2x" data-dominant-color="9B9AD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Knee_MRI</span><span class="informations">325×578 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22d1676a23c1c715c8acb765e879e2580b01807f.jpeg" data-download-href="/uploads/short-url/4Y0SyoZ7nztoFtUnnNg0puM263Z.jpeg?dl=1" title="Expectation.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22d1676a23c1c715c8acb765e879e2580b01807f_2_517x332.jpeg" alt="Expectation.PNG" data-base62-sha1="4Y0SyoZ7nztoFtUnnNg0puM263Z" width="517" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22d1676a23c1c715c8acb765e879e2580b01807f_2_517x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22d1676a23c1c715c8acb765e879e2580b01807f_2_775x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22d1676a23c1c715c8acb765e879e2580b01807f.jpeg 2x" data-dominant-color="35353B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Expectation.PNG</span><span class="informations">956×615 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ZakiaKhatun (2021-07-15 07:59 UTC)

<p>Additional Info: If it helps you to know, the first image (showing the STL file not aligned with the original data), this STL file was generated using other software (probably using the ‘Materialise Mimics’).<br>
In the 3D slicer, when I load it, the STL file does not overlap with the CT data. Any idea?</p>

---

## Post #3 by @pieper (2021-07-15 12:39 UTC)

<p>As discussed many times on this forum, the STL format has many shortcomings that lead to exactly this kind of ambiguity (it doesn’t encode the units or reference coordinate system in the file for example).  That leaves you with the task of tracking down exactly which software was used to create the files and what assumptions were made.  If that’s not convenient or possible your other option is to make guesses and change transform parameters until the data appears to line up as you expect.</p>

---

## Post #4 by @lassoan (2021-07-15 16:55 UTC)

<p>One possibility is RAS/LPS coordinate system difference. You can try to load the STL file with setting coordinate system to RAS and LPS to see if that fixes the issue:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbb2ffa0641e5d4885f97d26096586d2e4c63dec.png" data-download-href="/uploads/short-url/zUDlyvSfAnLioy5b2TPDvtSJHnm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb2ffa0641e5d4885f97d26096586d2e4c63dec_2_690x396.png" alt="image" data-base62-sha1="zUDlyvSfAnLioy5b2TPDvtSJHnm" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb2ffa0641e5d4885f97d26096586d2e4c63dec_2_690x396.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb2ffa0641e5d4885f97d26096586d2e4c63dec_2_1035x594.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb2ffa0641e5d4885f97d26096586d2e4c63dec_2_1380x792.png 2x" data-dominant-color="FCFCFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1485×854 27.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ZakiaKhatun (2021-07-15 18:15 UTC)

<p>Thank you very much for your answer. Yes, manual transformation is a choice I can think of.</p>

---

## Post #6 by @ZakiaKhatun (2021-07-15 18:18 UTC)

<p>Dear Andras Lasso,<br>
Thank you very much for responding. I have tried both but did not resolve my case. The STL file I am using was generated using “Materialise Mimics” software. But thanks!</p>

---

## Post #7 by @lassoan (2021-07-15 18:22 UTC)

<p>Did you load the original DICOM image into Slicer or the one that you processed in Mimics?<br>
In Mimics you may have centered/reoriented the volume so the image is not aligned with the original image anymore. Probably the best is if you save the image again in Mimics and load that into Slicer.</p>

---

## Post #8 by @ZakiaKhatun (2021-07-15 18:25 UTC)

<p>Yes. At first I loaded my original DICOM data, then I chose “Add data” to add the STL file and it appears exactly like the first image I attached to my post.</p>

---

## Post #9 by @lassoan (2021-07-15 19:28 UTC)

<p>Most likely Mimics moved the image (it is not in the original DICOM coordinate system anymore). Therefore, you need to export the image from Mimics (preferably in NRRD, MHA, or maybe DICOM format) and use that along with the exported segmentation.</p>
<p>Note that Slicer has many more and more sophisticated segmentation tools than Mimics, so you may consider doing the segmentation in Slicer. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this page</a> to get started.</p>

---
