---
topic_id: 4957
title: "Heart Segmentation"
date: 2018-12-04
url: https://discourse.slicer.org/t/4957
---

# Heart segmentation

**Topic ID**: 4957
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/heart-segmentation/4957

---

## Post #1 by @sarvpriya1985 (2018-12-04 19:16 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.1.10<br>
Expected behavior:<br>
Actual behavior:<br>
how can i prevent merging of hollow shells (F1) like in the image. Also is there away i can reduce size of brush tool below 1% as sometimes i try to erase stuff between two closely placed structures. I am trying to create 3d models of heart but these issues prevent true representation.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b834a6a380f5a858744606dbeb4daa8fbe1a694d.jpeg" data-download-href="/uploads/short-url/qhyEPUj3iBzojMUm1sqTS9nEj3T.jpeg?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b834a6a380f5a858744606dbeb4daa8fbe1a694d_2_656x500.jpeg" alt="Capture1" data-base62-sha1="qhyEPUj3iBzojMUm1sqTS9nEj3T" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b834a6a380f5a858744606dbeb4daa8fbe1a694d_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b834a6a380f5a858744606dbeb4daa8fbe1a694d_2_984x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b834a6a380f5a858744606dbeb4daa8fbe1a694d.jpeg 2x" data-dominant-color="4B5053"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1136×865 84.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2018-12-04 19:23 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="1" data-topic="4957">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>how can i prevent merging of hollow shells (F1) like in the image.</p>
</blockquote>
</aside>
<p>There are two ways to separate falsely connected chambers:</p>
<p>Option A: Separate the touching parts. If you used simple thresholding then you have to go and erase connecting region slice by slice (you’ll have less falsely connected chambers if you use a lower threshold value). If you use grow from seeds then you can place a small seed in between and it will be grown in 3D. I’ve implemented masking in Grow from seeds effect just now (will be available in tomorrow’s nightly version), which should make such separations easier to do.</p>
<p>Option B: Make each chamber a different segment and hollow them one by one. This will create a shell around each chamber, so you need to create openings (using Erase or Scissors effect) where there should be opening (where there is a hole or valve).</p>

---

## Post #3 by @sarvpriya1985 (2018-12-04 20:35 UTC)

<p>Thanks Andrass</p>
<p>I had used threshold method. I am trying to erase slice by slice but as I mentioned since the size of brush doesn’t go less than 1% I end up erasing more than I want to.</p>
<p>Also what is this masking in grow from seeds and how will this work.</p>
<p>Thanks</p>
<p>Sarv</p>

---

## Post #4 by @lassoan (2018-12-04 21:12 UTC)

<p>Brush size is relative to the screen. Zoom in the image more if the smallest brush size is still too large.</p>

---

## Post #5 by @sarvpriya1985 (2018-12-04 21:28 UTC)

<p>Thanks a lot Andras.</p>
<p>Sarv</p>

---
