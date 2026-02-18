# Why Slicer automatically scales a MultiVolume by a factor

**Topic ID**: 12557
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/why-slicer-automatically-scales-a-multivolume-by-a-factor/12557

---

## Post #1 by @xlucox (2020-07-15 15:06 UTC)

<p>Hi !!!</p>
<p>I have a MRI sequence which consist of a number of images in the time. When I upload it to Slicer the pixel values are scaled with respect to the original values. I plotted the image with matplotlib in python and the values are different. I would like to upload my image without this scaling, is there ant way?</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2020-07-15 15:42 UTC)

<p>What kind of MRI image is this? What did you use to create it? What is the range of values that you see in Slicer and what range would you expect? What DICOM reader did you use when you displayed it using matplotlib?</p>

---

## Post #3 by @xlucox (2020-07-15 16:29 UTC)

<p>This is a look locker sequence for CMR. I used pydicom to extract the matrix of the image. It seems that some times the values in Slicer are scaled by 8 or 16 with respect to the values I get with matplotlib.</p>

---

## Post #4 by @xlucox (2020-07-15 16:31 UTC)

<ul>
<li>I get with pydicom.</li>
</ul>

---

## Post #5 by @lassoan (2020-07-15 16:59 UTC)

<p>For clinical images, Slicer applies the appropriate intensity scaling. Pydicom just provides raw values that you need to rescale yourself.</p>

---

## Post #6 by @xlucox (2020-07-15 17:11 UTC)

<p>Ok. Is there any way to don’t apply this scaling when loading images?</p>

---

## Post #7 by @xlucox (2020-07-15 17:14 UTC)

<p>Or is this scaling value saved in some part of the VolumeNode?</p>

---

## Post #8 by @lassoan (2020-07-15 17:34 UTC)

<p>Scaling is necessary, because this is how DICOM encodes values in byte or word data type. You can reverse engineer it from the appropriate DICOM fields.</p>
<p>In MRML nodes you can only change the displayed window/level (in the volume’s display node).</p>
<p>Why are you interested in the raw values? What are you trying to achieve?</p>

---

## Post #9 by @xlucox (2020-07-15 17:52 UTC)

<p>I’m developing a module which extract the signal from a MRI ROI and fit some functions. The problem is that the fitting is sensitive to the change of value scales and I would like to this module works well in the most general cases. The fact is that different images from the same MR have different order of magnitude because of this auto-scaling.</p>

---

## Post #10 by @lassoan (2020-07-17 21:23 UTC)

<p>That’s exactly why you need to take into account the scaling. You get meaningful/standardized values after you apply the proper scaling.</p>

---
