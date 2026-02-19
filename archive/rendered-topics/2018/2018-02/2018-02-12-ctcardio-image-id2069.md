---
topic_id: 2069
title: "Ctcardio Image"
date: 2018-02-12
url: https://discourse.slicer.org/t/2069
---

# CTCardio Image?

**Topic ID**: 2069
**Date**: 2018-02-12
**URL**: https://discourse.slicer.org/t/ctcardio-image/2069

---

## Post #1 by @sladec1 (2018-02-12 13:43 UTC)

<p>Hey all,</p>
<p>I was wondering what the specifications are for the CT Cardio test image within Slicer’s database is?</p>
<p>I am currently trying to segment the spine with CT images that have been given to me through a University Medical Center, but it seems like the images aren’t high enough quality/may have some other kind of issue.  If I knew the exact specifications of the CT Cardio image that would be very helpful.</p>
<p>Thanks,</p>

---

## Post #2 by @pieper (2018-02-12 14:01 UTC)

<p>We don’t have the original dicom data for that (it was anonymized for sharing as a sample).  On general thing about that study is that it’s from an emergency scan after some kind of accident so the patient is pretty young and otherwise healthy.  So the bones will appear much different than in older or less healthy patients.  Also if I’m not mistaken there was a gradient anisotropic diffusion filter applied to the CTACardio scan before it was uploaded.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @sladec1 (2018-02-12 14:13 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="2069">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>gradient anisotropic diffusion filter</p>
</blockquote>
</aside>
<p>Great information! Do you know how I would go about using this filter for the image I have?</p>

---

## Post #4 by @pieper (2018-02-12 15:14 UTC)

<p>Yes, you can try some of the built-in noise reduction filters:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/GradientAnisotropicDiffusion" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/GradientAnisotropicDiffusion</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/CurvatureAnisotropicDiffusion" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/CurvatureAnisotropicDiffusion</a></p>

---

## Post #5 by @lassoan (2018-02-12 19:10 UTC)

<p>In general, segmentation of spine from CT images is hard. It is especially difficult if you need:</p>
<ul>
<li>each vertebra separated: vertebrae nearly touching each other and have the same density, so unless you have very high resolution (that you rarely have for live patients), there will be no clear boundary</li>
<li>solid models (no holes inside): density inside of bones is often not much higher than soft tissues, therefore simple global thresholding will always leave holes inside the bone.</li>
</ul>
<p>You may partially compensate for these issues by using higher resolution and lower noise acquisitions, but those would increase patient dose. So, in general, you go with the approved imaging protocol and do the best you can by smarter image processing and segmentation.</p>
<p>I would suggest to crop&amp;resample your volume to have isotropic voxel spacing (cubic voxels), using <code>Crop volume</code> module. Then, in <code>Segment editor</code> module try <code>Grow from seeds</code> effect for bone segmentation. You would paint a separate seed segment in each vertebra and you would have an “other” segment for soft tissue. See detailed instructions in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">segmentation tutorials</a>.</p>

---
