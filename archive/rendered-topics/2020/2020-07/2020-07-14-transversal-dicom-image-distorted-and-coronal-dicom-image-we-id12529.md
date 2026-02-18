# transversal DICOM image distorted and coronal DICOM image well

**Topic ID**: 12529
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/transversal-dicom-image-distorted-and-coronal-dicom-image-well/12529

---

## Post #1 by @MarCollado (2020-07-14 13:15 UTC)

<p>Operating system:Windows10<br>
Slicer version:4.10.2<br>
Expected behavior:non distorted images<br>
Actual behavior: distorted transversal image and non-distorted coronal image</p>
<p>Dear Sir or Madame:</p>
<p>I am Mar Collado from the University of Leeds. I am trying to use 3D slicer to analyse MRI images. I have DICOM images, that I have load into the 3D slicer 4.10.2. When I have tried to load the images of interest, the system gives me an error message: "Images are not equally spaced (a difference of -20 vs25 in spacings was detected). If loaded image appears distorted , enable ‘Aquisition geometry regularization’ in Application settings / DICOM / 2 DICOMScalarVolumePlugin. Please use caution. I have followed this instructions but then both images are distorted and so little that I cannot appreciate the organs in the images. Then, I restored the system as it was and the result is the same as the beginning (I am including a picture below so that you can see it). Can you help me, please?<br>
Many thanks in advance<br>
Kind regards<br>
Mar<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bab6d1f22d38a14fd90d71e087ca92ca67b39b0.png" data-download-href="/uploads/short-url/aNp5xrbrk0U0tbrXPjEfA00UGlO.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bab6d1f22d38a14fd90d71e087ca92ca67b39b0_2_690x387.png" alt="imagen" data-base62-sha1="aNp5xrbrk0U0tbrXPjEfA00UGlO" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bab6d1f22d38a14fd90d71e087ca92ca67b39b0_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bab6d1f22d38a14fd90d71e087ca92ca67b39b0_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bab6d1f22d38a14fd90d71e087ca92ca67b39b0.png 2x" data-dominant-color="97979C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1366×768 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-07-14 13:56 UTC)

<p>Please try with latest Slicer Preview Release and let us know if it can load these images correctly.</p>

---

## Post #3 by @MarCollado (2020-07-14 15:04 UTC)

<p>Hi,</p>
<p>Thank you very much for your help. I followed your suggestion but the result is similar to what I obtained with the previous version. I am includding some images.</p>
<p>Kind regards</p>
<p>Mar<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2d76b59d8f3a58979ed825374a3b619c38b6227.png" alt="imagen" data-base62-sha1="u5bNLcj1RgCLC8ZATgGq8dU2Ffh" width="567" height="319"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4262345c85046050d3b4db25953dadebe19dacfc.jpeg" alt="imagen" data-base62-sha1="9tfUKpqZmWSrzlC5vKpT3AiKSrG" width="567" height="319"></p>

---

## Post #4 by @MarCollado (2020-07-15 22:00 UTC)

<p>Hi,<br>
I have just tried to load another DICOM images and no warning message appeared. So, I think that perhaps something happened during the acquisition of the images.<br>
Many thanks for your time and sorry for any inconvenience<br>
Kind regards<br>
Mar</p>

---

## Post #5 by @Juicy (2020-07-15 22:59 UTC)

<p>You could try and go to the Edit menu in the top left corner of the slicer window then choose “Application Settings”, then choose the “DICOM” tab from the list on the left, then under “Acquisition geometry regularization” choose “apply regularization transform”. You will have to close slicer and open it again the apply the settings. Then try and load the DICOM files again and see if that helps. The acquisition regularization can account for some problems like gantry tilt, missing slices, uneven slices etc.</p>
<p>Otherwise look through the images in the stack (with another DICOM viewer such as ImageJ) and see if there are any that are out of place such as a localizer image or maybe an image from another acquisition or something like that. If you find any images that don’t belong in the stack then remove them and try loading the rest of the images again in slicer.</p>
<p>Also if kind of looks like you are trying to load two series at once from the image above? Perhaps only load one series at a time?</p>

---

## Post #6 by @LIE_CAI (2022-04-07 17:42 UTC)

<p>Hi Juicy,</p>
<p>I also came across this problem. I was trying to do segmentation on breast tomosynthesis. But when I loaded images they were distorted in other two planes.<br>
I tried with your advice choose “apply regularization transform”. But still not worked.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dfe2aefcd6ab9d6b231ee128aefc809e639ff1e.png" data-download-href="/uploads/short-url/8QpG0qeYStR2OgtuTmBXwwKS29U.png?dl=1" title="1649352548(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dfe2aefcd6ab9d6b231ee128aefc809e639ff1e.png" alt="1649352548(1)" data-base62-sha1="8QpG0qeYStR2OgtuTmBXwwKS29U" width="690" height="452" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1649352548(1)</span><span class="informations">1010×662 17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a>Uploading: 1649352709(1).png…</a><br>
Then I chekced my images on ImgaeJ, all of the sllices were in correct sequence. I could view the origninal image in ImageJ by importing image sequence.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f570253717fc9674a86d649f4057607ecca4f4c7.png" data-download-href="/uploads/short-url/z1ffxlFGY635vO0c5GflQINWlpB.png?dl=1" title="1649352932(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f570253717fc9674a86d649f4057607ecca4f4c7_2_444x500.png" alt="1649352932(1)" data-base62-sha1="z1ffxlFGY635vO0c5GflQINWlpB" width="444" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f570253717fc9674a86d649f4057607ecca4f4c7_2_444x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f570253717fc9674a86d649f4057607ecca4f4c7_2_666x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f570253717fc9674a86d649f4057607ecca4f4c7.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1649352932(1)</span><span class="informations">719×809 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Can anyone have a solution about this problem now?<br>
Thanks a lot!</p>

---

## Post #7 by @lassoan (2022-04-07 20:03 UTC)

<p>If you provide an anonymized sample DICOM data set, then we can investigate it and fix any issues that may come up.</p>
<p>If you cannot share the data set but provide a detailed description (several screenshots, information on the imaging protocol, values of all <code>Image Position Patient</code> and <code>Image Orientation Patient</code> DICOM tags in the series, etc.) then we may be able to give a few suggestions. However, this requires much more of our and your time, and it is not guaranteed that we can guess correctly what the issue could be, so it would be much better if you could share the DICOM images.</p>

---

## Post #8 by @LIE_CAI (2022-04-07 21:29 UTC)

<p>Hi lassoan,<br>
It’s my pleasure to forward you a anonymized sample.<br>
But how can I attach this file to you? It seems in this forum there’s no such a funtion.</p>
<p>Many thanks to your help!</p>

---

## Post #9 by @lassoan (2022-04-07 22:01 UTC)

<p>You can use any file sharing service (dropbox, onedrive, google drive, etc.) and post the link here. Thank you.</p>

---

## Post #10 by @LIE_CAI (2022-04-07 22:15 UTC)

<p>Please find the link as follows:<br>
<a href="https://drive.google.com/drive/folders/17Ha1m7F5nSNR85CQD7kmjas5BPOJCZQ0?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/17Ha1m7F5nSNR85CQD7kmjas5BPOJCZQ0?usp=sharing</a></p>
<p>Thanks!</p>

---

## Post #11 by @lassoan (2022-04-08 23:51 UTC)

<p>I’ve loaded the data set into the latest Slicer Preview Release and showed a 2D projection image (series 5) and a tomosynthesis volume (series 4) and it all looks good:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e914acc5fc60f1008663c37b5b7b4ba9375e1b.jpeg" data-download-href="/uploads/short-url/pf1pisgWRjutsQlC61XRZpRs5VF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0e914acc5fc60f1008663c37b5b7b4ba9375e1b_2_690x420.jpeg" alt="image" data-base62-sha1="pf1pisgWRjutsQlC61XRZpRs5VF" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0e914acc5fc60f1008663c37b5b7b4ba9375e1b_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0e914acc5fc60f1008663c37b5b7b4ba9375e1b_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0e914acc5fc60f1008663c37b5b7b4ba9375e1b_2_1380x840.jpeg 2x" data-dominant-color="6F6E6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1169 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What distortion did you see? Can you post an image how these images are displayed in the Siemens software?</p>

---

## Post #12 by @LIE_CAI (2022-04-09 06:53 UTC)

<p>Oh, sorry, I updated my slicer version and now it works.<br>
How to show the 3D view without segmentation like this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a635fff838c243aa3183492482b04309795ff454.png" alt="1649487110(1)" data-base62-sha1="nImXam08OyKvGZi1jgV2M2AZmbW" width="429" height="371"><br>
I can only show segmentations it self by clikc “show in 3D”.</p>

---

## Post #13 by @lassoan (2022-04-09 09:57 UTC)

<p>I did not segment the volume, just used volume rendering. Since the image has a very unusual intensity range, none of the presets work as is, but you need to adjust the transfer functions.</p>

---

## Post #14 by @LIE_CAI (2022-04-20 10:03 UTC)

<p>Sorry I’m new to use 3D slicer so I have more questions.<br>
How to check the image’s intensity range?<br>
Does 3D slicer have transfer fucntions to adjust the images’ intenstiy range?<br>
Thanks a lot!</p>

---

## Post #15 by @lassoan (2022-04-20 11:27 UTC)

<aside class="quote no-group" data-username="LIE_CAI" data-post="14" data-topic="12529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lie_cai/48/13293_2.png" class="avatar"> LIE_CAI:</div>
<blockquote>
<p>How to check the image’s intensity range?</p>
</blockquote>
</aside>
<p>It is displayed with numerical values and a histogram in Volumes module. You can see the voxel values at the current mouse cursor position in the Data Probe (window at the lower left corner). But usually when you need to set anything that depends on the intensity values there is visual feedback you can rely on.</p>
<aside class="quote no-group" data-username="LIE_CAI" data-post="14" data-topic="12529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lie_cai/48/13293_2.png" class="avatar"> LIE_CAI:</div>
<blockquote>
<p>Does 3D slicer have transfer fucntions to adjust the images’ intenstiy range?</p>
</blockquote>
</aside>
<p>For slice views, a linear ramp function is used. You can shift the ramp horizontally and change the steepness (adjust window and level, a.k.a. brightness and contrast) numerically in the Volumes module or by setting the mouse mode to Window/Level and left-click and drag in the image. See detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level">here</a>.</p>
<p>For direct volume rendering in 3D views, you have 3 transfer functions to edit (intensity, color, gradient), with more degrees of freedom, in Volume Rendering module.</p>

---
