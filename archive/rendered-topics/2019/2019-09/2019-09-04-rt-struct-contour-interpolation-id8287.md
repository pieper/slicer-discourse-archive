---
topic_id: 8287
title: "Rt Struct Contour Interpolation"
date: 2019-09-04
url: https://discourse.slicer.org/t/8287
---

# RT struct contour interpolation

**Topic ID**: 8287
**Date**: 2019-09-04
**URL**: https://discourse.slicer.org/t/rt-struct-contour-interpolation/8287

---

## Post #1 by @labixin (2019-09-04 09:18 UTC)

<p>Hi all,</p>
<p>What I have: original breast CT (0.703×0.703×5, 512×512×65); corresponding RT struct (planar contour, exist in 4 slices); cropped image (isotropic spacing 1.005, 173×104×111).</p>
<p>Want to get: interpolated segment which I could edit in each slice more accurately.</p>
<p>Action: First I converted RT struct to binary labelmap representation. Secondly I exported segment to labelmap (reference volume be cropped image). Then I converted labelmap back to segmentation node in subject hierarchy and finally got interpolated segment.</p>
<p>I have two questions then.</p>
<ol>
<li>
<p>In Picture1 the pink one (slice fill) showing original RT struct (planar contour) and the orange one (slice outline) showing interpolated segment (binary labelmap). It’s obvious that in some slices they were not so consistent (taken into consideration the difference between planar contour and binary labelmap). Is there another way to generate interpolated segment more accurately?</p>
</li>
<li>
<p>After I got interpolated segment my way, I couldn’t make desired edit using segment editor module (The editing operation would be restricted in a small region? Shown in Picture2). I have no idea what’s wrong with my processing.</p>
</li>
</ol>
<p>Hope for some suggestions. Thanks a lot!</p>
<p>Sincerely,<br>
Crayon</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa057baf923d7a2d6e63b49da37270174ea049fc.png" data-download-href="/uploads/short-url/og4UT7IPpGKmY3sY7TK8UvIW2Zu.png?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa057baf923d7a2d6e63b49da37270174ea049fc_2_343x500.png" alt="01" data-base62-sha1="og4UT7IPpGKmY3sY7TK8UvIW2Zu" width="343" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa057baf923d7a2d6e63b49da37270174ea049fc_2_343x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa057baf923d7a2d6e63b49da37270174ea049fc_2_514x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa057baf923d7a2d6e63b49da37270174ea049fc.png 2x" data-dominant-color="1F1D1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">636×927 77.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Picture1</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20a696bfaaa880f9cb83dedd400aa50da78c0c31.png" alt="02" data-base62-sha1="4EQc1UreAoA1gDn40ZUE8pn6J1v" width="654" height="464"><br>
Picture2</p>

---

## Post #2 by @cpinter (2019-09-04 13:39 UTC)

<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="8287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Secondly I exported segment to labelmap (reference volume be cropped image). Then I converted labelmap back to segmentation node in subject hierarchy and finally got interpolated segment.</p>
</blockquote>
</aside>
<p>No need for these steps.</p>
<ol>
<li>
<p>This may be due to two things. The first is all the extra conversions you’re making. The second is the resolution of the CT. To mitigate the first, please just skip those steps <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> For the second, you can go to the Segmentations module, click on Update (or if not created yet, long-click Create) in the row of the Binary labelmap representation, and then click Set geometry. Select your CT, and then you can choose to apply oversampling, which will give you a finer labelmap.</p>
</li>
<li>
<p>Again, the extra steps. By going segmentation → volume → segmentation, you limited the bounding box, of which you cannot go out, unless you specify a different geometry. By the way can you please explain why you took these specific steps? Is there some tutorial or documentation that is outdated or wrong? Please let me know.</p>
</li>
</ol>

---

## Post #3 by @labixin (2019-09-05 07:32 UTC)

<p>Thanks for your prompt reply. I am sorry that I didn’t find the right instructions before (maybe this tutorial? <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Segmentations" rel="nofollow noopener">Create new representation in segmentation (conversion)</a>). So I did all the way as I thought (sorry for making things much more complicated). <img src="https://emoji.discourse-cdn.com/twitter/clown_face.png?v=9" title=":clown_face:" class="emoji" alt=":clown_face:"> Thank you again!</p>
<p>One more question. If I plan to export this segment to labelmap (which can be used as mask in later registration), must the reference volume be chosen to match the fixed (or moving) image? Because if I chose the lower resolution image as reference volume, the previous oversampling and thus finer segment would still change a little? Can I use the finer labelmap for mask (reference volume to be none)?</p>
<p>Your help is highly appreciated!</p>
<p>Crayon</p>

---

## Post #4 by @cpinter (2019-09-05 14:08 UTC)

<p>Thanks! I will review the wiki page and update any outdated (and now confusing) information.</p>
<p>I believe the mask the registration uses will be resampled to the proper geometry anyway, so it doesn’t matter if the segmentation is finer. The point is that it should not be coarser. I would just export it to labelmap in its current grid, and give it to the registration.</p>

---

## Post #5 by @labixin (2019-09-06 01:07 UTC)

<p>Thank you for your time. <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>
<p>Yes it’s critical that the segment should not be coarser. I would just change source geometry to cropped volume (also fixed or moving image) and directly edit on it (without oversampling). Then export it to labelmap reference each fixed or moving image ahead. It may be the same I think.</p>
<p>Thanks for your help!</p>
<p>Crayon</p>

---
