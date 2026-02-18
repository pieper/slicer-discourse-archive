# Resample Image (BRAIN)

**Topic ID**: 13736
**Date**: 2020-09-28
**URL**: https://discourse.slicer.org/t/resample-image-brain/13736

---

## Post #1 by @zahiraabdala (2020-09-28 16:07 UTC)

<p>Hi everyone, I need to know how Resample Image (BRAIN) module works. I use it and its works very well but I need more information about the functionality. I was looking for more information but I only found this link and it’s not enough <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/BRAINSResample" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.8/Modules/BRAINSResample</a></p>
<p>Im working with PET image and im using ATLAS image like a reference. I choosed float for pixel type and i used Linear Interpolation Mode. Someone know how the algorithm makes the resample?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2020-09-28 18:21 UTC)

<p>The module uses <a href="https://itk.org/Doxygen/html/classitk_1_1ResampleImageFilter.html">ITK ResampleImageFilter</a> under the hood, but it has a few tricks to improve usability, speed, and quality for some special cases (e.g., in-place transformation of composite linear transforms, resampling binary images as distance maps, automatic background value computation, etc.). Its main logic is implemented <a href="https://github.com/BRAINSia/BRAINSTools/blob/master/BRAINSCommonLib/GenericTransformImage.hxx#L30">here</a>.</p>

---

## Post #3 by @zahiraabdala (2020-09-28 22:50 UTC)

<p>Thank you!! I have an other question, does this module take into account any percent error?</p>

---

## Post #4 by @lassoan (2020-09-28 23:51 UTC)

<p>Could you rephrase this question, provide more details, or maybe explain it with a drawing?</p>

---

## Post #5 by @zahiraabdala (2020-09-29 00:19 UTC)

<p>I used Resample Image (BRAIN) module for a PET image by referencing the brain atlas image downloaded from 3D slicer. I chose ‘float’ as pixel type, and when it comes to warping parameters I chose a linear interpolation mode. In the link that you had sent to me, I could see that the algorithms use already established functions such as the itResampleImageFilter.h.  I would like to know  if this function contemplates a certain percentage of error, and if so, what is the calculated percent error?</p>

---

## Post #6 by @lassoan (2020-09-29 13:45 UTC)

<p>I still don’t understand how a function can “contemplate a certain percentage of error” but since this class is implemented in ITK, it is better to ask for details on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---
