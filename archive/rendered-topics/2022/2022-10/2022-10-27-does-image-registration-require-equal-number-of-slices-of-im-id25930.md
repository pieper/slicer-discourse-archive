---
topic_id: 25930
title: "Does Image Registration Require Equal Number Of Slices Of Im"
date: 2022-10-27
url: https://discourse.slicer.org/t/25930
---

# Does image registration require equal number of slices of images?

**Topic ID**: 25930
**Date**: 2022-10-27
**URL**: https://discourse.slicer.org/t/does-image-registration-require-equal-number-of-slices-of-images/25930

---

## Post #1 by @gaurav_patel (2022-10-27 12:26 UTC)

<p>How is registration hadled in multimodal case wherein there are unequal number of slice eg. whole body CT with partial MR like abdomen</p>
<p>Operating system:Windows 7<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2022-10-27 12:34 UTC)

<p>Image geometry (origin, spacing, axis directions) is constantly being changed during registration, so it does not matter at all if the original geometry was the same or not. Image value at any position is computed usign interpolation.</p>
<p>Most registration algorithms require the images to be fairly well aligned (less than 10mm translation, 10 degrees rotation) and their physical extents not differ by more than 10%. If the input images are not like this originally then you can use transform initializers to prealign them. For some reason image cropping is usually not included in automatic registration initialization implementations, so if one image is much larger than the other then you may need to crop it manually.</p>

---

## Post #3 by @gaurav_patel (2022-10-27 13:03 UTC)

<p>Thank you for such quick reply.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Most registration algorithms require the images to be fairly well aligned (less than 10mm translation, 10 degrees rotation)</p>
</blockquote>
</aside>
<p>Does this mean that fully automatic registration without user intervention is not possible.</p>
<p>My problem is that I have larger CT scan and partial MRI scan since they are not in synchronization. I was wondering if there was some way by which I can atleast align the volume and then perform registration slice by slice.</p>

---

## Post #4 by @lassoan (2022-10-27 17:07 UTC)

<p>It is certainly possible, you just need to choose pre-alignment method (it depends on the imaging modalities, anatomy, etc. what method works bes). After approximate alignment, cropping is trivial.</p>
<p>Depending on how strict your imaging protocols are, pre-alignment may be trivial, too. For example, if image origin is set consistently by the imaging technologist in all images then images may be already sufficiently aligned. If you accept random images from anywhere in the world then you can use a generic segmentation tool, such as <a href="https://totalsegmentator.com/">Total Segmentator</a> (you can use it directly in Slicer) to figure out what is where and pre-align images based on that.</p>

---

## Post #5 by @gaurav_patel (2022-10-28 05:06 UTC)

<p>Thank you very much.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is certainly possible, you just need to choose pre-alignment method (it depends on the imaging modalities, anatomy, etc. what method works bes). After approximate alignment, cropping is trivial.</p>
</blockquote>
</aside>
<p>I will tryout these approaches and look deeper into pre-alignment step.</p>
<p>Thanks again.</p>

---

## Post #7 by @lassoan (2022-11-03 12:33 UTC)

<p>Reconstructing a 3D Cartesian image from a DICOM series is a very complex operation. You get a number of slices, each with its position, orientation, size in 3D space, but DICOM does not tell how to interpret these independent slices. The slices can be arbitrarily ordered, spaced, rotated, they may overlap each other. They may contain images of the same region over time, so you may need to group them and reconstruct multiple 3D volumes from them. Slicer can handle almost all combinations of all these variations.</p>
<p>If you are sure that all the image series you need to work with:</p>
<ul>
<li>contain slices with equal size and pixel spacing</li>
<li>slices are parallel</li>
<li>not skewed (slice normal is parallel with the vector that connects the slice origin point to the previous/next slice origin)</li>
<li>distance between each neighbor slice is the same</li>
<li>contain only a single time point</li>
</ul>
<p>then you can reconstruct a volume by putting the slices into a volume after sorting (no interpolation or grouping is needed). You must determine image origin, spacing, axis directions, and order of slices by inspecting the “image position patient” and “orientation patient” tags.</p>

---
