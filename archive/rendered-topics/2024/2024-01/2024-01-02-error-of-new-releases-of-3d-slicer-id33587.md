---
topic_id: 33587
title: "Error Of New Releases Of 3D Slicer"
date: 2024-01-02
url: https://discourse.slicer.org/t/33587
---

# Error of new releases of 3D slicer

**Topic ID**: 33587
**Date**: 2024-01-02
**URL**: https://discourse.slicer.org/t/error-of-new-releases-of-3d-slicer/33587

---

## Post #1 by @Arakeep90 (2024-01-02 12:13 UTC)

<p>Hey, I always have a problem after installing the latest release of 3D slicer , all features is not working properly. I always need to get back to version 5.2.2 which is working very good on my PC without any problem. Any new release can’t work properly. Please help.</p>

---

## Post #2 by @jamesobutler (2024-01-02 12:19 UTC)

<aside class="quote no-group" data-username="Arakeep90" data-post="1" data-topic="33587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arakeep90/48/15982_2.png" class="avatar"> Arakeep90:</div>
<blockquote>
<p>Any new release can’t work properly.</p>
</blockquote>
</aside>
<p>Please provide a specific example of how you observe it not working properly.</p>
<ul>
<li>What features are you using?</li>
<li>Are you installing any extensions?</li>
<li>What CPU model is your computer?</li>
</ul>

---

## Post #3 by @Arakeep90 (2024-01-03 12:59 UTC)

<p>When I segment the bone in the first segment then I add segment 2 to have another segmentation for the same bone, segment 1 shows nothing. Also, regarding volume rendering sometimes work but sometimes nothing. My CPU is intel i7 11TH Gen.</p>

---

## Post #4 by @jamesobutler (2024-01-03 13:18 UTC)

<aside class="quote no-group" data-username="Arakeep90" data-post="3" data-topic="33587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arakeep90/48/15982_2.png" class="avatar"> Arakeep90:</div>
<blockquote>
<p>When I segment the bone in the first segment then I add segment 2 to have another segmentation for the same bone, segment 1 shows nothing.</p>
</blockquote>
</aside>
<p>I would suggest you check your masking options as it sounds like your segment 2 is overwriting your segment 1. Please read <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#masking-options" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a>.</p>
<aside class="quote no-group" data-username="Arakeep90" data-post="3" data-topic="33587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arakeep90/48/15982_2.png" class="avatar"> Arakeep90:</div>
<blockquote>
<p>, regarding volume rendering sometimes work but sometimes nothing.</p>
</blockquote>
</aside>
<p>Your steps leading up to when it is not working for you would be helpful along with any screenshots. What type of volume is it? I can only think that you may be running into a limitation of using multi-volume rendering with the maximum intensity projection option instead of composite shading. See related post below:</p>
<aside class="quote" data-post="5" data-topic="32313">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/eb9ed0/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/change-order-of-rendering-of-multiple-volumes-with-volume-rendering-module/32313/5">Change 'order' of rendering of multiple volumes with Volume Rendering module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks, yes I was using GPU Ray Casting.  The VTK Multi-Volume option doesn’t work for me (nothing is displayed at all) with the “Maximum Intensity Projection” technique, which I usually need for nuc med images.  It works great with the 'Composite with Shading"  technique though.
  </blockquote>
</aside>


---
