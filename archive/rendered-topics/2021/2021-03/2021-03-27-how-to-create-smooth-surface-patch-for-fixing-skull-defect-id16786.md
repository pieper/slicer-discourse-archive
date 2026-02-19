---
topic_id: 16786
title: "How To Create Smooth Surface Patch For Fixing Skull Defect"
date: 2021-03-27
url: https://discourse.slicer.org/t/16786
---

# How to create smooth surface patch for fixing skull defect?

**Topic ID**: 16786
**Date**: 2021-03-27
**URL**: https://discourse.slicer.org/t/how-to-create-smooth-surface-patch-for-fixing-skull-defect/16786

---

## Post #1 by @slicer365 (2021-03-27 13:12 UTC)

<p>This is a patient with a bilateral skull defect. I want to make a repaired face of the skull, but I don’t want to match it with a new skull because the result is not accurate. I hope to get a new face through the curve. Can this be achieved! I can use the Draw tube function on each layer to get some divisions, but how to use these divisions to generate faces seems difficult. I know that MImics has this kind of curve generation function.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32fcd9259a9f2f764809c0128cd6cf65e2c9a185.jpeg" data-download-href="/uploads/short-url/7h3B65cIOVRHiDSNAqK8e7DfElT.jpeg?dl=1" title="11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32fcd9259a9f2f764809c0128cd6cf65e2c9a185_2_553x500.jpeg" alt="11" data-base62-sha1="7h3B65cIOVRHiDSNAqK8e7DfElT" width="553" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32fcd9259a9f2f764809c0128cd6cf65e2c9a185_2_553x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32fcd9259a9f2f764809c0128cd6cf65e2c9a185.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32fcd9259a9f2f764809c0128cd6cf65e2c9a185.jpeg 2x" data-dominant-color="323332"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11</span><span class="informations">636×575 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-03-27 18:58 UTC)

<p>You can us a warping transform in Fiducial registration wizard module in SlicerIGT extension to accurately match a similar patient’s data set.</p>
<p>If you prefer sculpting, you can use Segment Editor module. Draw tube effect creates thick tubes, so it is hard to create smooth surface. I would recommend using Paint or Draw effects, skipping 5-10 slices between each segmented slice, and then use “Fill between slices” effect to create a full segmentation. You can use Threshold effect and Logical operators to combine the bone flap using Logical operators effect.</p>

---

## Post #3 by @slicer365 (2021-03-28 02:39 UTC)

<p>Thank you very much, Professor Andras Lasso. I have tried both of the two methods you mentioned. In fact, the results of both are not very good. When I use Paint or Draw, it is difficult for me to draw good curves, so I use " “Fill between slices”, the result is rougher. In addition, I use Draw tube, which can help me generate smooth curves. Of course, this is actually a pipe. If you can use paint or draw to construct a smooth curve, it will be perfect.</p>

---

## Post #4 by @lassoan (2021-03-28 16:37 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="3" data-topic="16786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>If you can use paint or draw to construct a smooth curve, it will be perfect.</p>
</blockquote>
</aside>
<p>You already have several options for drawing “smooth curves”, for example Segment editor you can use Surface cut effect (you need to provide at least one point in a different plane) or use Paint effect with a very large diameter sphere brush.</p>
<p>However, we have a much better tool for this now. We have recently released the new Baffle planner module that allows editing of 3D surfaces both in slice views and in 3D. I’ve created a demo video to show how it works for this use case:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="AigTwMYRI1Y" data-video-title="Design surface patches using new Baffle Planner module" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=AigTwMYRI1Y" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/AigTwMYRI1Y/maxresdefault.jpg" title="Design surface patches using new Baffle Planner module" width="" height="">
  </a>
</div>


---

## Post #5 by @slicer365 (2021-03-29 00:23 UTC)

<p>Thank you very much for your patient answers, it has benefited me a lot <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #7 by @lassoan (2021-03-29 04:29 UTC)

<p>It is certainly not limited to cardiac applications, but since its development and maintenance is funded by the SlicerHeart project, it will be kept there for the foreseeable future. We’ll add a documentation section about surface modeling tools to make the module easier to discover.</p>

---

## Post #8 by @Jmarcs (2021-04-07 05:36 UTC)

<p>How can i Install Baffle modle. I ve installed slicerheart extension but impossible to find baffle module . best regards   my version 4.11202</p>

---

## Post #9 by @manjula (2021-04-07 07:25 UTC)

<p>You need the latest preview release 4.13.0</p>

---
