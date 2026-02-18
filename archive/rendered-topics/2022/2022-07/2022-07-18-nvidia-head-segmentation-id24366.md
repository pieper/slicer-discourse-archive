# NVIDIA head segmentation

**Topic ID**: 24366
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/nvidia-head-segmentation/24366

---

## Post #1 by @ggrrll (2022-07-18 13:01 UTC)

<p>Hi,</p>
<p>is is possible to have a head segmentation with NVIDIA AIAA from a brain MRI</p>
<p>something like<br>
<img src="https://raw.githubusercontent.com/NVIDIA/ai-assisted-annotation-client/master/slicer-plugin/snapshot.jpg" alt="" width="690" height="427"></p>
<p>for head</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2022-07-18 13:05 UTC)

<p>What do you mean by “head segmentation”? Segmenting the skin surface, skull, brain,…?</p>
<p>Since there is no such thing as a perfect segmentation, you always need to specify what is the purpose of the segmentation. Is your end goal surgical planning, surgical simulation, 3D printing a souvenir keychain,…?</p>

---

## Post #3 by @ggrrll (2022-07-18 16:47 UTC)

<p>Hi,</p>
<p>yes, the basic segmentation including, skull, white/gray matter,  …</p>
<p>the goal is to build a 3D model (.stl file) of the heed</p>
<p>thanks</p>

---

## Post #4 by @ggrrll (2022-07-18 16:54 UTC)

<p>I guess my Q is basically</p><aside class="quote quote-modified" data-post="1" data-topic="17778">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miglius_mikalauskas/48/11046_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/anatomical-brain-segmentation/17778">Anatomical brain segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi. Is there a way to automatically segment human brain in mri by anatomical structures? 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffd1c82cd89d67b40536d73046d4fe3e514dd577.jpeg" data-download-href="/uploads/short-url/Av5d3SlgIKm9tK6Cmqf9n5Zqu9N.jpeg?dl=1" title="smegenu anatomija" rel="noopener nofollow ugc">[smegenu anatomija]</a> 
So that i could automatically see the human brain segmented by either lobes (frontal, temporal etc) or by gyri? 
The photo is from a video in youtube.
  </blockquote>
</aside>

<p>so, would you suggest the same <a class="mention" href="/u/lassoan">@lassoan</a> ?</p>
<p>although, I am still curious to know if we could retrain a similar model to get something like that picture in the AIAA repo, for the brain</p>

---

## Post #5 by @lassoan (2022-07-18 22:54 UTC)

<aside class="quote no-group" data-username="ggrrll" data-post="4" data-topic="24366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ggrrll/48/15987_2.png" class="avatar"> ggrrll:</div>
<blockquote>
<p>so, would you suggest the same <a class="mention" href="/u/lassoan">@lassoan</a> ?</p>
</blockquote>
</aside>
<p>Yes, the recommendations in that topic are still valid.</p>
<aside class="quote no-group" data-username="ggrrll" data-post="4" data-topic="24366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ggrrll/48/15987_2.png" class="avatar"> ggrrll:</div>
<blockquote>
<p>although, I am still curious to know if we could retrain a similar model to get something like that picture in the AIAA repo, for the brain</p>
</blockquote>
</aside>
<p>Those recommended methods provide similar models.</p>

---
