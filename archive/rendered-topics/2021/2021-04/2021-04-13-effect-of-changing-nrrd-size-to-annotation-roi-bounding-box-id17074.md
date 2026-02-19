---
topic_id: 17074
title: "Effect Of Changing Nrrd Size To Annotation Roi Bounding Box"
date: 2021-04-13
url: https://discourse.slicer.org/t/17074
---

# Effect of changing ".nrrd" size to annotation (ROI bounding box)

**Topic ID**: 17074
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/effect-of-changing-nrrd-size-to-annotation-roi-bounding-box/17074

---

## Post #1 by @Dhruba (2021-04-13 21:33 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11</p>
<p>I used 3D slicer to annotate (Using ROI) some DICOM images and saved them as “.nrrd” file and annotation as “.acsv”. I have attached an image below. The “.nrrd” has a size of 512x512x158 and the bounding box (annotation) has the following parameters “point|12.8546|219.402|128.809|1|1 (center of the box); point|7.72059|5.88235|4.0311|1|1 (length of each axis)”.<br>
If I change the size of “.nrrd” to 128x128x128 before training them in the neural network, should I change the annotation parametrs too? What effect does changing the “.nrrd” size has on the annotation (bounding box parameters)?<br>
My goal is to make a detection algorithm (to find the region of interest in the neuroimage).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9273cd4541909d4f268467a691afd59e55236c4a.png" data-download-href="/uploads/short-url/kTzOwMnq7X1q5INXBKwf0Ohk8mC.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9273cd4541909d4f268467a691afd59e55236c4a_2_690x355.png" alt="1" data-base62-sha1="kTzOwMnq7X1q5INXBKwf0Ohk8mC" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9273cd4541909d4f268467a691afd59e55236c4a_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9273cd4541909d4f268467a691afd59e55236c4a_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9273cd4541909d4f268467a691afd59e55236c4a_2_1380x710.png 2x" data-dominant-color="A8A9AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">3719×1914 1.21 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-04-13 21:37 UTC)

<p>Slicer coordinates are in patient space, so if you resize the image you need to take that into account in your code.  This page describes the matrices involved.</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @Dhruba (2021-04-13 21:43 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> . The problem is that I am using data from two different scanner. One produces 158 slices, and the other produces 190 slices. So half of my “.nrrd” has a size of 512x512x158 and the rest has 512x512x190. Do you think I should resize them to a common size and change the annotation accordingly or is there some easier way?</p>

---

## Post #4 by @pieper (2021-04-13 21:47 UTC)

<p>They will probably all have slightly different pixel sizes or at least slice spacings so if you need them all to be in the same pixel grid then you need to resample them to you are sure to take that into account (or the anatomy will get distorted).  The Resample Scalar/Vector/DWI module lets you resample one image into the space of another, optionally through a transform.</p>

---

## Post #5 by @Dhruba (2021-04-13 21:52 UTC)

<p>Great! Let’s say, I want to rescale them to a common spacing of 0.40x0.40x0.40 mm^3. Then crop them to 128x128x128 pixels before feeding them into the neural network. Is this a valid way?</p>

---

## Post #6 by @pieper (2021-04-13 21:59 UTC)

<p>That sound generally reasonable yes.  You might need to do some level of registration so that they are roughly aligned and you might also want to look at SlicerTorchIO to generate augmentation data.</p>

---
