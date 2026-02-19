---
topic_id: 21174
title: "Unexpected Voxel Values At Boundary When Using Cpr Curved Pl"
date: 2021-12-22
url: https://discourse.slicer.org/t/21174
---

# Unexpected voxel values at boundary when using CPR (curved planer reformat) to straighten label volume

**Topic ID**: 21174
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/unexpected-voxel-values-at-boundary-when-using-cpr-curved-planer-reformat-to-straighten-label-volume/21174

---

## Post #1 by @Kane_Daizah (2021-12-22 02:52 UTC)

<p>Hi, when I used the centerline extraction and CPR to straighten the true and false lumen labels of the aorta, I found that some of the true lumen labels of the aorta will be mixed with the false lumen labels after straightening. I don’t think there should be such a problem according to the principle of straightening.<br>
I have no idea why it . Do you have any suggestions?</p>
<p>Before straightening<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44ef6831cafd72175ba1f275630f81b0a80de8a4.png" alt="WeChat Image_20211222102449" data-base62-sha1="9PPouVJyM26OjOxZKGDe4HiBH1y" width="315" height="295"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c6576b1b328e20f5f0b38a797a167b29901c457.png" alt="WeChat Image_20211222102444" data-base62-sha1="hKsAEzLyvUm873yte82Q0ZakByD" width="325" height="298"></p>
<p>After straightening<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3cbce71f753a07ccf83081ef81cfb53fbc62b09.png" alt="WeChat Image_20211222102455" data-base62-sha1="wvb2q5XsErTavUsT42fV5rlobkl" width="302" height="285"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8120dd8c3668b3632b4bcae3147a4868796fbce9.png" alt="WeChat Image_20211222102728" data-base62-sha1="iqk0sVUHECpqh08Oo1NqOjuKNHH" width="294" height="297"></p>

---

## Post #2 by @lassoan (2021-12-22 03:15 UTC)

<p>You need to turn off interpolation (use “nearest neighbor” method) when you harden transforms on labelmap volumes.</p>
<p>Interpolation would create smooth transition from label value to the background value. For example if your segment’s label value is 5 and the background value is 0 then you would have all kinds of voxel values values between 0-5 at the boundary of this segment.</p>
<p>I’ve just noticed that you’ve sent ITK-Snap screenshots. Is there any specific feature in ITK-Snap that you have not found in Slicer?</p>

---

## Post #3 by @Kane_Daizah (2021-12-22 06:58 UTC)

<p>Thank you so much!</p>
<p>I used ITK-snap screenshots because I am a cs student who has new to medical image segmentation and is very lack of medical image knowledge. And I often encounter the orientations are different from images and labels for various reasons.</p>
<p>Images and labels with different orientations in 3D slicer will not automatically overlap. ITK-snap seems to automatically merge and visualize images and labels in different orientations. So I would like to use ITK-snap to visualize the data. But I think 3D slicer can make beginners notice the problem of orientation. In fact, I’m ashamed to say that after I used 3D slicer, I realized that the poor performance of my deep learning network is due to the inability of images and labels to overlap due to different orientations.</p>
<p>Pictures and labels in different orientation<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/210a1a9554e5daa64b813f6e8e78aad0a576d22a.png" alt="b8650b1786e9cba61b31731bf4ff93d" data-base62-sha1="4Ihp2BLO38nc1ftYRostLbHSpwC" width="620" height="139"></p>
<p>In 3D slicer<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cb2bf395cd9b19d3b68c8891b1f562d7f4af378.png" alt="ac66b23bf2dd6ce9da80f97718d5544" data-base62-sha1="hN8axhZDgBcnAzTZMk4zsJTwyaQ" width="451" height="342"></p>
<p>In ITK-snap<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c790f70d8381d62f605d55323dd44438dbc30ca5.png" alt="c9dcc145cbc5be6289f5a8a82ae6061" data-base62-sha1="strBnbF2XTuOWp0AYvSv6tH4uC9" width="264" height="204"></p>

---

## Post #4 by @lassoan (2021-12-22 14:03 UTC)

<aside class="quote no-group" data-username="Kane_Daizah" data-post="3" data-topic="21174">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kane_daizah/48/13600_2.png" class="avatar"> Kane_Daizah:</div>
<blockquote>
<p>Images and labels with different orientations in 3D slicer will not automatically overlap. ITK-snap seems to automatically merge and visualize images and labels in different orientations.</p>
</blockquote>
</aside>
<p>ITK-Snap cannot operate on images and labels with different geometry (origin, spacing, and axis directions must be the same). ITK-Snap warns you about the geometry mismatch when you load the data but if you proceed then it simply ignores the geometry information, so you will not be able to see the actual misalignment between your data sets.</p>

---

## Post #5 by @giovform (2022-05-02 15:49 UTC)

<p>Hello Andras, how can I set to neareast neighbor when hardening a transform?</p>

---

## Post #6 by @lassoan (2022-05-08 03:30 UTC)

<p>Hardening a transform on a volume always used linear interpolation <a href="https://github.com/Slicer/Slicer/commit/704c46f00ab98a2b59883ecec5444c99176e58ba">until a few days ago</a>. Now in the latest Slicer Preview Release uses nearest neighbor interpolation for labelmap volumes. If you use a different Slicer version then you can convert your labelmap volume to segmentation and harden the transform on that.</p>

---
