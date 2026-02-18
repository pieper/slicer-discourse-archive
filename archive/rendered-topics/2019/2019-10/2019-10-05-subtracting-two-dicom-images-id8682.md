# Subtracting two dicom images

**Topic ID**: 8682
**Date**: 2019-10-05
**URL**: https://discourse.slicer.org/t/subtracting-two-dicom-images/8682

---

## Post #1 by @prencekhan (2019-10-05 12:32 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2<br>
Expected behavior: Subtract two DICOM images<br>
Actual behavior:</p>
<p>I just started using the 3D Slicer. I want to ask if I can subtract two DICOM images from each other using a user-defined equation. Specifically, to subtract the CT number (Hounsfield unit) If yes what and where should I start?</p>
<p>Can you help me, please?</p>

---

## Post #2 by @Amine (2019-10-05 14:06 UTC)

<p>Hi, you can do this via the Subtract Image filter ( Module list&gt;All modules&gt; Simple Filters&gt; SubtractImageFilter),  there is also an AddImageFilter, MultiplyImageFilter , DivideImageFilter(and DivideFloor)</p>

---

## Post #3 by @prencekhan (2019-10-11 09:06 UTC)

<p>Thank you very much Amine Azami.</p>
<p>But still it does not work with my case because I need to use a formula in subtracting not a simple case of subtraction like A-B. What I want is to subtract Ax-Bx where A and B are the HU values and x is a constant value. Hope you can help me again. Thank you</p>

---

## Post #4 by @prencekhan (2019-10-11 09:21 UTC)

<p>Hi Amine Azami,</p>
<p>Can you help me with how can I subtract two Dicom images, specifically to subtract their HU values or CT number? But before subtracting, I need to multiply constant value to the HU value of each image. For image 1 I need to multiply constant x while for image 2 I need to multiply constant y.</p>
<p>Thank you very much.</p>

---

## Post #5 by @Hamburgerfinger (2019-10-11 10:36 UTC)

<p>In the itk Simple Filters module, you could use the ShiftScaleImage filter on each of your images, and the scale factor would be x or y in your case, and shift would be zero. (This multiplies all voxels by constant value). Then you can use the subtract image<br>
filter with the output images.</p>

---

## Post #6 by @lassoan (2019-10-11 11:23 UTC)

<p>You can combine volumes with arbitrary mathematical formula using numpy. See for example this post: <a href="https://discourse.slicer.org/t/is-it-possible-to-view-more-than-two-image-volumes-at-the-same-time-in-slice-viewers/8738/2" class="inline-onebox">Is it possible to view more than two image volumes at the same time in slice viewers?</a></p>

---

## Post #7 by @prencekhan (2019-10-11 12:04 UTC)

<p>Hi!</p>
<p>Thank you very much for your help. I will reply to you as soon as I can execute it.</p>
<p>Until next time. Thanks again.</p>

---
