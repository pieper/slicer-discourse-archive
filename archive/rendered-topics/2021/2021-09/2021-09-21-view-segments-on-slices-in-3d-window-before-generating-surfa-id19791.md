---
topic_id: 19791
title: "View Segments On Slices In 3D Window Before Generating Surfa"
date: 2021-09-21
url: https://discourse.slicer.org/t/19791
---

# View segments on slices in 3D window before generating surface

**Topic ID**: 19791
**Date**: 2021-09-21
**URL**: https://discourse.slicer.org/t/view-segments-on-slices-in-3d-window-before-generating-surface/19791

---

## Post #1 by @tsehrhardt (2021-09-21 17:23 UTC)

<p>Is there a way to visualize a segment on my 2D slices in the 3D window without actually generating the 3D surface?</p>
<p>I have a bone with a large metal piece but there are also metal particulates and also areas of bone around the larger metal piece that thresholded with the metal, so I want to keep the actual metal particulates in my metal segment and add bright bone areas back into the bone segment.</p>
<p>Any suggestions on filters to reduce the streaks would be helpful too–that itself might help me separate the particulates.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0319084fb7137c49869114ee95a3fc95a6ffa9af.jpeg" data-download-href="/uploads/short-url/rp3YSb7sM9ryXeTVaxnvudGyOb.jpeg?dl=1" title="2021-09-21_11-56-40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0319084fb7137c49869114ee95a3fc95a6ffa9af_2_517x336.jpeg" alt="2021-09-21_11-56-40" data-base62-sha1="rp3YSb7sM9ryXeTVaxnvudGyOb" width="517" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0319084fb7137c49869114ee95a3fc95a6ffa9af_2_517x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0319084fb7137c49869114ee95a3fc95a6ffa9af_2_775x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0319084fb7137c49869114ee95a3fc95a6ffa9af_2_1034x672.jpeg 2x" data-dominant-color="3E423F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-09-21_11-56-40</span><span class="informations">1593×1037 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-09-21 17:59 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="1" data-topic="19791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>Is there a way to visualize a segment on my 2D slices in the 3D window without actually generating the 3D surface?</p>
</blockquote>
</aside>
<p>You can export the segmentation to labelmap volume and show the labelmap volume slice in the 3D view.</p>
<p>The other question (how to separate bone, metal, and metal artifacts) would deserve creating another topic, with a few more screenshots (show how the image looks like and an ideal segmentation, especially in a region where there are streak artifacts and bone and metal).</p>

---

## Post #3 by @tsehrhardt (2021-09-21 18:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can export the segmentation to labelmap volume and show the labelmap volume slice in the 3D view.</p>
</blockquote>
</aside>
<p>Thank you. This is helpful–I did not think about the labelmaps. I will play around more with the metal and maybe post a separate topic on it.</p>

---
