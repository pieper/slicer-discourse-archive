# Problem uploading MRI image

**Topic ID**: 11269
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/problem-uploading-mri-image/11269

---

## Post #1 by @youssef (2020-04-23 16:19 UTC)

<p>Operating system: WINDOWS 10<br>
Slicer version: 4.10.2<br>
I have a problem when I load the file (MRI DICOM) as you see below<br>
I used the DICOM module and I followed tips in the DICOM FAQ, but  i have the same problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/640d1cf2caf9aa7888e8d8f26e83c1bd07f4823d.png" data-download-href="/uploads/short-url/eh5QbrYeqQU2mf6Ae1D9CcqNMVn.png?dl=1" title="frira halima" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/640d1cf2caf9aa7888e8d8f26e83c1bd07f4823d_2_628x499.png" alt="frira halima" data-base62-sha1="eh5QbrYeqQU2mf6Ae1D9CcqNMVn" width="628" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/640d1cf2caf9aa7888e8d8f26e83c1bd07f4823d_2_628x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/640d1cf2caf9aa7888e8d8f26e83c1bd07f4823d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/640d1cf2caf9aa7888e8d8f26e83c1bd07f4823d.png 2x" data-dominant-color="393945"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">frira halima</span><span class="informations">764×608 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-04-23 18:36 UTC)

<p>What is the problem?  That looks like a spine MRI.  Did you expect there is more in the scan that’s not displayed?</p>

---

## Post #3 by @youssef (2020-04-23 19:06 UTC)

<p>exactly I expect full images in the green and red areas like the yellow area</p>

---

## Post #4 by @pieper (2020-04-23 19:59 UTC)

<p>You said you checked the FAQ (thank you for that! it helps when people read that before posting).  Can you summarize what you tried and what you learned.  That is, are there any clues besides not seeing all the images?</p>

---

## Post #5 by @youssef (2020-04-24 15:40 UTC)

<p>My objectif  is segmentation the entire spine when I import the DICOM file i wait the full images of spine on the 3 slices.<br>
so i don’t know what is the problem. is it the DICOM file or another problem?</p>

---

## Post #6 by @pieper (2020-04-24 15:52 UTC)

<p>Hard to say for sure without more information.  If you can’t share the data for others to inspect, then you’ll need to check the logs yourself and maybe we can answer any questions that come up.</p>

---

## Post #7 by @lassoan (2020-04-24 16:19 UTC)

<p>Due to the shape of the spine, a 3D image will never fill square-shaped views in all three axis directions, but it is expected to appear as a tall rectangle in two views.</p>
<p>The image in the screenshot indeed looks to be cropped a bit narrow along left-right axis, but it may have been acquired like this. Have you seen larger image area when looking at the images with the image viewer supplied on the DICOM DVD?</p>

---

## Post #8 by @youssef (2020-04-25 15:48 UTC)

<p>No, I didn’t see it.</p>

---

## Post #9 by @lassoan (2020-04-25 16:37 UTC)

<p>If all other DICOM viewers show this region only then most likely your image is acquired just like that. It is quite common for spine MRI images to only contain a few have high resolution sagittal slices.</p>
<p>Of course, it is always the best to ask the clinicians who you work with - they know exactly what they imaged and why.</p>

---

## Post #10 by @youssef (2020-04-25 16:43 UTC)

<p>I see. Thank you sir</p>

---
