---
topic_id: 12406
title: "Prostate Mri Us Contour Propagation 8 Bits Export"
date: 2020-07-06
url: https://discourse.slicer.org/t/12406
---

# Prostate MRI-US Contour Propagation 8 bits export 

**Topic ID**: 12406
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/prostate-mri-us-contour-propagation-8-bits-export/12406

---

## Post #1 by @michaeleth (2020-07-06 22:20 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>We are tying to import deformed contours done on US image to our planning system. This is after registration has been conducted using “Prostate MRI-US Contour Propagation” module. Unfortunately, the planning system only allows 8 bits US Image and will not accept 16 bit US that has been sent from 3D slicer.</p>
<p>Is there easier way in 3D slicer to down-sample image data set from 16 to 8bits prior to exporting a third party.</p>
<p>Thank you so much,<br>
Michael Ashenafi</p>

---

## Post #2 by @lassoan (2020-07-06 22:33 UTC)

<p>You can use Cast scalar volume module to convert a 16-bit image to 8-bit (unsigned char).</p>

---

## Post #3 by @michaeleth (2020-07-07 18:07 UTC)

<p>Thank you for the prompt reply!! I am still getting 16bits. I have attached the image below to make sure we are referring to the same module and procedure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd3cd52b5018ffc7f0090946bc99e198a121cb4.png" data-download-href="/uploads/short-url/96DRAQeQiUO6MxKWSmIYzhjX7rm.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd3cd52b5018ffc7f0090946bc99e198a121cb4.png" alt="image.png" data-base62-sha1="96DRAQeQiUO6MxKWSmIYzhjX7rm" width="333" height="500" data-dominant-color="F6F8FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">460×689 9.23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-07-07 19:38 UTC)

<p>Probably you would need to write a short Python script if you want to create ultrasound image that your treatment planning system can accept.</p>
<p>Normally MRI-US contour propagation module is used for transforming the MRI and the contours defined on MRI. You can import these into your treatment planning system. The ultrasound is just used as a reference (to define contours of the prostate to drive the warping) - the ultrasound image is not modified and does not have to be imported into the TPS.</p>

---

## Post #5 by @michaeleth (2020-07-07 20:21 UTC)

<p>Thank you so much for your reply and will attempt to import just the deformed structure set to the planning system.</p>
<p>It did look like the US image had been modified inside the 3D slicer because the US data set that was brought in was 8bits. However, what had been exported out of the 3D slicer was 16bits.</p>

---

## Post #6 by @lassoan (2020-07-07 20:27 UTC)

<p>Yes, apparently the DICOM exporter always scales the image to 16 bits. I guess there just has not been any strong need for 8-bit export yet. This MRI-US contour propagation module is used quite widely on clinical data and so nobody has requested deformed US export until now. Even in your case it was probably just a misunderstanding, as you are not interested in how the US image deformed but you want to deform the pre-procedural image and segmentation to the US image space.</p>

---
