# Resampling an Image

**Topic ID**: 461
**Date**: 2017-06-08
**URL**: https://discourse.slicer.org/t/resampling-an-image/461

---

## Post #1 by @ahoover (2017-06-08 18:24 UTC)

<p>When I resample an image in Slicer using the Resample Image (Brains) module and a transform I made using the Transform module, the image ends up correctly resampled except for its flipped around one axis. I’m assuming this is because of the RAS and LAS coordinate system, but I don’t know how to fix it. What is the best way to go about preventing this flip?</p>
<p>Thank you for your help.</p>

---

## Post #2 by @pieper (2017-06-08 19:00 UTC)

<p>Can you provide the exact steps (ideally demonstrated using the SampleData) and how you are looking at the data when you say it is flipped?</p>

---

## Post #3 by @lassoan (2017-06-08 20:01 UTC)

<aside class="quote no-group" data-username="ahoover" data-post="1" data-topic="461">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/35a633/48.png" class="avatar"> ahoover:</div>
<blockquote>
<p>its flipped around one axis</p>
</blockquote>
</aside>
<p>Is it flipped when displayed in Slicer or when you load it in your own software? When you display an image in your own software, you must always take into account patient orientation and axis directions information that are stored in the image header.</p>
<p>Images are displayed correctly in all commonly used medical image computing software, such as 3D Slicer, ITK-Snap, or MITK. Images are often not displayed correctly in generic scientific visualization software, such as ParaView, 2D/microscopy-oriented software such as ImageJ/Fiji, and in other small custom single-project-use research software (various Matlab or Python scripts that were only tested on a limited set of images).</p>

---

## Post #4 by @ahoover (2017-06-08 20:25 UTC)

<p>I have a mri and nii scan that i want to co-register.</p>
<p>These are the steps I did.<br>
1.Uploaded both images<br>
2. Centered both images<br>
3. Save the centered images<br>
4. Used the transforms module to align the mri with the ct scan<br>
5. Saved the transform<br>
6. Tried to resample them with the resample (brains) module<br>
(the ct scan as the reference, the mri scan as the movable, my transform as the transform, and hit apply)<br>
However when I look at the resampled image in slicer the image is flipped. Specifically, the coronal window is flipped vertically. It’s as if the signs in the right column of my transform matrix were flipped. (I don’t know if this is related but I’ve noticed the signs of the right column of my transform matrix are flipped whenever I upload the transform in slicer however the magnitudes and all the other signs are unchanged)</p>

---

## Post #5 by @ahoover (2017-06-08 20:26 UTC)

<p>It’s flipped in slicer.</p>

---

## Post #6 by @pieper (2017-06-08 21:48 UTC)

<p>Thanks for the info.  In step 6 are you running the brains resample through<br>
slicer or externally?  (Not sure why you need step 5 if you are running<br>
inside slicer).</p>

---

## Post #7 by @ahoover (2017-06-09 02:11 UTC)

<p>Resampling in slicer. I’m doing everything in slicer but i just feel better about saving things as I go along. Do you have any idea why the signs in the right column are flipping?</p>

---

## Post #8 by @lassoan (2017-06-09 04:06 UTC)

<p>I guess you don’t see any image misalignment in Slicer as a result of resampling. Can you confirm?</p>
<p>Input images can have any orientation but outputs are often generated with standardized axis order and direction. As a result, you may see that the output image axes directions are different from the input image. It’s not a problem because voxels in the array are ordered accordingly.</p>

---

## Post #9 by @ahoover (2017-06-09 14:02 UTC)

<p>My problem is that the image still looks flipped over one axis in slicer. It’s the same project that you really helped me on yesterday with how to segment two images in slicer.  When I hit apply for the segmentation in slicer, the segmentation done with the registered scan flips so half of the segmentation is upside down relative to the other half. I thought maybe if I resampled the image I wouldn’t have this problem, but  resampling causes the image to appear flipped in slicer which I need not to be the case so that I can segment them together.</p>

---

## Post #10 by @lassoan (2017-06-09 14:07 UTC)

<p>If the image appears flipped inside Slicer then it is probably a bug but we need to be able to reproduce the problem to be able to fix it. Would you be able to create a screen capture video so that we can see what exact steps did you follow?</p>

---
