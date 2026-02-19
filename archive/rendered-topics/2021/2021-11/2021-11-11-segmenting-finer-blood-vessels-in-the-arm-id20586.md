---
topic_id: 20586
title: "Segmenting Finer Blood Vessels In The Arm"
date: 2021-11-11
url: https://discourse.slicer.org/t/20586
---

# Segmenting Finer Blood Vessels in the Arm

**Topic ID**: 20586
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/segmenting-finer-blood-vessels-in-the-arm/20586

---

## Post #1 by @DPMM3D (2021-11-11 18:55 UTC)

<p>Hello!</p>
<p>I am working with angiogram data of the arm and need to be able to segment the finer blood vessels throughout the forearm. It is not high contrast imaging, making it very difficult to see in the slices, (hopefully the next scan will be), and I have downloaded the VMTK extension, hoping to find a feature that would be able to help, but it is still difficult to navigate. It seems that many of the features are optimized for much larger vessels, such as aortic ones, but wondering if anyone has any tips or tricks besides manually segmenting and painting where I’m guessing they are located throughout the slices?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-11-12 06:05 UTC)

<p>In general, if you have hard time seeing the vessels then segmentation will have to be mostly manual.</p>
<p>Vesselness filtering module might help with somewhat increasing the contrast of vessels. You can also try anisotropic filtering in Simple Filters module to improve visibility. If you have contrast-free acquisition then you can do DSA - by subtracting the contrast-free image from the opacified image.</p>
<p>If visibility is very bad (basically not visible, you only see slight hints on some slices and you know that those pieces must be connected) then probably the best is to just use the “Draw tube” effect (provided by SegmentEditorExtraEffects extension) to manually draw each vessel segment. This is of course tedious, but if you have only a few dozen of images then it may be still much faster than developing some custom processing methods.</p>
<p>Is the image quality comparable to the “CTACardio” Slicer sample data set? Can you attach a few screenshots of your image?</p>

---

## Post #3 by @DPMM3D (2021-11-17 22:46 UTC)

<p>Andras,</p>
<p>Thank you so much for getting back to me. I’ve attempted vesselness filtering, and it is somewhat helping for larger blood vessels. However, I’m unable to adjust some of the parameters such as vessel contrast and I’m not sure why, seems like increasing the contrast would be very helpful in this situation where it’s difficult to see.</p>
<p>I’ve attached a screenshot to show you the quality of the scan, it is relatively similar to the sample data “CTA Cardio”, but focused more on the left side of the body and arm. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9368e7c897be80a78facb7567080a6a4223d1350.jpeg" data-download-href="/uploads/short-url/l22WI4nZiLfCbxMjEpMh0DMWmli.jpeg?dl=1" title="slicer.test" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9368e7c897be80a78facb7567080a6a4223d1350_2_690x378.jpeg" alt="slicer.test" data-base62-sha1="l22WI4nZiLfCbxMjEpMh0DMWmli" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9368e7c897be80a78facb7567080a6a4223d1350_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9368e7c897be80a78facb7567080a6a4223d1350_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9368e7c897be80a78facb7567080a6a4223d1350_2_1380x756.jpeg 2x" data-dominant-color="A4A5A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer.test</span><span class="informations">1856×1017 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
My main focus is to detect the finer blood vessels, such as the one I’m pointing to in the screenshot, but even with the vesselness filtering it is proving difficult.</p>
<p>I’ve also tried the anisotropic filtering methods like you suggested, however I am getting error messages for both of these as well saying “sitk::ERROR: Pixel type: 16-bit signed integer is not supported in 3D by class itk::simple::CurvatureAnisotropicDiffusionImageFilter.”.</p>
<p>My current method that I’ve been using for my last few scans has been the draw tube method as you’ve suggested, and it works well for larger vessels that are easier to see, but is definitely tedious and does not help as I get closer to the wrist where the finer ones of interest are located.</p>
<p>If you have any input for better utilizing vesselness fiiltering or to address the error for the anisotropic filters I’d really appreciate it! Thanks in advance.</p>

---

## Post #4 by @chir.set (2021-11-18 07:07 UTC)

<p>Can you provide a sample anonymized volume as an NRRD file ?</p>

---
