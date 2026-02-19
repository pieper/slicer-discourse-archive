---
topic_id: 25297
title: "Rotate A Node Around A Specified Point Script"
date: 2022-09-16
url: https://discourse.slicer.org/t/25297
---

# Rotate a node around a specified point script

**Topic ID**: 25297
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/rotate-a-node-around-a-specified-point-script/25297

---

## Post #1 by @jegberink (2022-09-16 08:15 UTC)

<p>Hello everyone,</p>
<p>I’ve tried to get the rotate a node around a specified point script to work.<br>
I followed the video as described here:</p><aside class="quote" data-post="11" data-topic="9398">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rotation-around-specific-point/9398/11">Rotation around specific point</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve just tried the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" rel="noopener nofollow ugc">script</a> that I posted earlier and it worked well. I’ve recorded it on a <a href="https://1drv.ms/v/s!Arm_AFxB9yqHucN9pd6edw1a1cgxbg?e=x5SJOd" rel="noopener nofollow ugc">video</a> so that you can see all the steps.
  </blockquote>
</aside>
<p>
Im working in slicer 5.0.3</p>
<p>After applying the script it still rotates around the centerpoint. No errors given.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bbe311ccd3d338c3c4a521c75ec498950e63adf.jpeg" data-download-href="/uploads/short-url/mdLuvw0qrD1NdWHhFjZWGaqH5tZ.jpeg?dl=1" title="rotate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe311ccd3d338c3c4a521c75ec498950e63adf_2_690x374.jpeg" alt="rotate" data-base62-sha1="mdLuvw0qrD1NdWHhFjZWGaqH5tZ" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe311ccd3d338c3c4a521c75ec498950e63adf_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe311ccd3d338c3c4a521c75ec498950e63adf_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe311ccd3d338c3c4a521c75ec498950e63adf_2_1380x748.jpeg 2x" data-dominant-color="D7D7EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rotate</span><span class="informations">1921×1043 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be appreciated</p>

---

## Post #2 by @lassoan (2022-09-16 20:57 UTC)

<p>Have you applied transform_4 to the model and rotated the object using the transform_3 as shown in the video? Could you record a similar video to show what do you do exactly?</p>

---

## Post #3 by @jegberink (2022-09-17 06:05 UTC)

<p>I installed another instance of slicer, and now it seems to be working. Thank you for your time.</p>

---
