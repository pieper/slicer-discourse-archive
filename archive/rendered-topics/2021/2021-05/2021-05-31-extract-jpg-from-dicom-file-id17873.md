---
topic_id: 17873
title: "Extract Jpg From Dicom File"
date: 2021-05-31
url: https://discourse.slicer.org/t/17873
---

# Extract .jpg from DICOM file

**Topic ID**: 17873
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/extract-jpg-from-dicom-file/17873

---

## Post #1 by @Manav_Kothari (2021-05-31 00:51 UTC)

<p>I have a DICOM file of the CT scan of an ankle. There are 3 different series in the DICOM file and I wish to extract all the images of one of the series in the required order. Kindly help me understand the steps in the Slicer software to achieve the same.<br>
Thank You</p>

---

## Post #2 by @cpinter (2021-05-31 12:07 UTC)

<p>You should be able to do this conveniently using the Screen Capture module.</p>

---

## Post #3 by @lassoan (2021-05-31 21:39 UTC)

<p>Saving as JPG is good if you want get the image slices so that you can show them in a powerpoint presentation (and then Screen Capture module is a perfect tool).</p>
<p>However, if you are thinking about saving a CT image as JPG for deep learning (because the example/tutorial that you would like to try uses JPG as input) then I would recommend to look a bit further, because you can lose clinically significant information by converting a CT-image to a 8-bit JPG image. See some more information and alternatives in many other similar posts in this forum - for example this one:</p>
<aside class="quote quote-modified" data-post="11" data-topic="17532">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-export-slices-into-system-without-loosing-information/17532/11">How to export slices into system without loosing information</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There is certainly nothing revolutionary about nrrd, it just does what it is designed for - storing 2D/3D/4D images in 3D space with various scalar types and bit depth, with known origin, spacing, and axis directions. 
We try to steer users away from using png and other consumer file formats because they are not designed for storing medical images and they do a very bad job at that: they cannot store 3D information, physical size, position, orientation, only support a few pixel types, etc. 
Have…
  </blockquote>
</aside>


---
