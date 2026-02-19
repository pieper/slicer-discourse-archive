---
topic_id: 2498
title: "Simple Region Splitting"
date: 2018-04-03
url: https://discourse.slicer.org/t/2498
---

# Simple Region Splitting

**Topic ID**: 2498
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/simple-region-splitting/2498

---

## Post #1 by @Steve_W (2018-04-03 04:03 UTC)

<p>Hello Slicer Forum!</p>
<p>I sort out a number of 3d Prints for orthopaedics and plastics in my hospital.<br>
Following tutorials I have been sucessful in making a number of models now using slicer 3d,  however I need some help in working out a quick way to split region a and b,  where after thresholding they are joined.</p>
<p>I have been using islands and whilst the “keep largest” is great, I struggle to find a grow option thats usable in 3d,   or a seeding that works ONLY on threasholds already created.</p>
<p>A price example of what I want to do is in the tutorial for Plevis / Femur splitting.   If there was a way to paint region A (eg the pelvis) and then region B (the femur) then click split, it would be much quicker.<br>
Also in the example once the Femur has been removed, there isn’t a way to “Island grow” to select all joined parts.</p>
<p>If there is a simple way of doing this please let me know!  Aside from that, Great program and so far has helped me out!</p>

---

## Post #2 by @lassoan (2018-04-04 06:09 UTC)

<p>Have you experimented with masking options in the Segment editor? If you select an effect and scroll to the bottom then in Masking section you can choose to operate only in already segmented regions or in specific segments.</p>
<aside class="quote no-group" data-username="Steve_W" data-post="1" data-topic="2498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba9def/48.png" class="avatar"> Steve_W:</div>
<blockquote>
<p>A price example of what I want to do is in the tutorial for Plevis / Femur splitting.</p>
</blockquote>
</aside>
<p>Yes, that’s tricky, since there may be no intensity difference between the two and they touch each other. However, luckily the femur head is quite spherical, so you can get a nice initial separation by using sphere paint. See how it is done in this femur segmentation video tutorial:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="0at15gjk-Ns" data-video-title="Creating femur model from CT volume using 3D Slicer" data-video-start-time="2m37s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=0at15gjk-Ns&amp;t=2m37s" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/0at15gjk-Ns/maxresdefault.jpg" title="Creating femur model from CT volume using 3D Slicer" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="Steve_W" data-post="1" data-topic="2498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba9def/48.png" class="avatar"> Steve_W:</div>
<blockquote>
<p>Also in the example once the Femur has been removed, there isn’t a way to “Island grow” to select all joined parts.</p>
</blockquote>
</aside>
<p>You can add islands to an existing segment by Islands effect / Add selected island, then clicking on the islands that you would like to add.</p>

---

## Post #3 by @Steve_W (2018-04-13 04:47 UTC)

<p>I used the femur splitting example to make my last model, but there are times when a automatic split, even for “touching segments” would be useful.</p>
<p>the paiting/seeding is a good function, but is there a way to use it for only threshold’d items?</p>

---
