---
topic_id: 9304
title: "Different Size Image Registration"
date: 2019-11-26
url: https://discourse.slicer.org/t/9304
---

# Different size image registration

**Topic ID**: 9304
**Date**: 2019-11-26
**URL**: https://discourse.slicer.org/t/different-size-image-registration/9304

---

## Post #1 by @teosava (2019-11-26 16:41 UTC)

<p>Hi all,</p>
<p>I have to register two MRIs that represent the same patient (who is always in the same position). Note that one image is larger than the other as it represents a larger portion of the body.</p>
<p>I roto-translated the larger image in order to obtain an “initial manual registration” and everything is fine until this point.</p>
<p>Then, I applied the General Registration (BRAINS) to refine the initial registration. The results is a cropped image: the larger image is cropped to the same size as the smaller one. This is undesired since I would need the extra portion of the body originally provided by my larger image.</p>
<p>Suggestions?<br>
Thank you!</p>

---

## Post #2 by @pieper (2019-11-26 16:56 UTC)

<p>Can you just swap which one is fixed and moving?</p>
<p>Or you can use brains to calculate the transform and use it instead of the resampled image.</p>
<p>Hope that helps,<br>
-Steve</p>

---

## Post #3 by @lassoan (2019-11-26 18:05 UTC)

<p>I’ve experienced many times that otherwise very stable registration methods (such as Elastix with default bspline parameter set) failed to converge if one image covered a significantly larger portion of the patient than the other. I would recommend to crop the images to cover approximately the same anatomical region. You can still apply the computed transformation to the entire original image.</p>

---

## Post #4 by @teosava (2019-11-27 09:17 UTC)

<p>Thank you very much for your replies.</p>
<p>How can I visualize the computed transform? I cannot find it after applying the registration (BRAIN).  I expect to find a 4x4 matrix.</p>
<p>Moreover, will this transformation matrix refer also to the initial roto-translation (“initial manual alignment” mentioned above)? In other words, shall I apply the transformation matrix to the original volume or to the volume which I obtained after the “initial manual alignment”? If it is the second case, how does the matrix change?</p>

---

## Post #5 by @lassoan (2019-11-27 14:00 UTC)

<aside class="quote no-group" data-username="teosava" data-post="4" data-topic="9304">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/bbce88/48.png" class="avatar"> teosava:</div>
<blockquote>
<p>How can I visualize the computed transform?</p>
</blockquote>
</aside>
<p>You can see all transforms in Transforms module. If you computed a composite transform (e.g., linear+bspline) then you need to open “Information” section. To edit linear component of a composite transform, you need to split it first then choose the linear transform node.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0ddf01fcf9758b9a83cf1133f102376b3b0762d.png" data-download-href="/uploads/short-url/rwbaNSGXiIvEGSefS6AFPLe20B7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ddf01fcf9758b9a83cf1133f102376b3b0762d_2_527x500.png" alt="image" data-base62-sha1="rwbaNSGXiIvEGSefS6AFPLe20B7" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ddf01fcf9758b9a83cf1133f102376b3b0762d_2_527x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0ddf01fcf9758b9a83cf1133f102376b3b0762d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0ddf01fcf9758b9a83cf1133f102376b3b0762d.png 2x" data-dominant-color="F8F7F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×662 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
