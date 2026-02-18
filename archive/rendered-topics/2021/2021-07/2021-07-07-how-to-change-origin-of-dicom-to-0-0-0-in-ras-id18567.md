# How to change origin of dicom to 0,0,0 in RAS?

**Topic ID**: 18567
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/how-to-change-origin-of-dicom-to-0-0-0-in-ras/18567

---

## Post #1 by @akshay_pillai (2021-07-07 15:38 UTC)

<p>Operating system: windows 10</p>
<p>I want to use a set of dicoms as input for image processing using deep learning models and in order for me to feed these images I want them all to have the same orientation. All my dicom files have different origin coordinates. Is there any way I can set them all to 0,0,0 as origin in the RAS coordinate system. If so what is the way to do it? Also, will this change or distort the dicom in any way? If anyone has done this or knows how to please let me know. Any help is appreciated. Thanks.</p>

---

## Post #2 by @pieper (2021-07-07 16:34 UTC)

<p>We generally discourage people from changing the geometry of images because it means they would no longer match other images that are in the same frame of reference.</p>
<p>Deep learning models usually take numpy arrays as input, so you can just ignore the dicom origin info when passing in the data.</p>

---

## Post #3 by @akshay_pillai (2021-07-07 16:35 UTC)

<p>ok, I’ll try that out.</p>

---

## Post #4 by @akshay_pillai (2021-07-07 16:56 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> do you think the Image  dimensions of the dicom file matters? I have dicom files that are 200 , 220  and 120 in dimensions do you think they need to be isotropic atleast?</p>

---

## Post #5 by @lassoan (2021-07-09 05:51 UTC)

<p>This is up to you to decide: you can train your network to deal with different image geometries or you normalize the input image before you feed it into the network.</p>

---
