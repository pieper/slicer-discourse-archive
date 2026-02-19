---
topic_id: 15322
title: "Help With Pedicle Screw Planning Module"
date: 2021-01-03
url: https://discourse.slicer.org/t/15322
---

# Help with pedicle screw planning module

**Topic ID**: 15322
**Date**: 2021-01-03
**URL**: https://discourse.slicer.org/t/help-with-pedicle-screw-planning-module/15322

---

## Post #1 by @drvarunagarwal (2021-01-03 15:41 UTC)

<p>Hi,</p>
<p>I am trying to develop a pedicle screw planning extension based on pedicle screw simulator.</p>
<p>attached is a video of what we have been able to achieve.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="gcJ8p43PiS8" data-video-title="pedicle screw planning extension slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=gcJ8p43PiS8" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/gcJ8p43PiS8/maxresdefault.jpg" title="pedicle screw planning extension slicer" width="" height="">
  </a>
</div>

<p>As you can see from the above we have made sliders to change orientation of screw.<br>
and there is a large fiducial that can be dragged out.</p>
<p>My queries:</p>
<ol>
<li>How can we do in such a way that instead of only the fiducial the screw can be dragged from anywhere?</li>
<li>How to make the screw can rotated like in the video below. can these arrows for rotations etc be placed alongside the screw like in the video.</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="aJzVry0bww0" data-video-title="ExcelsiusGPS Spine11 TLIF" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=aJzVry0bww0" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/aJzVry0bww0/maxresdefault.jpg" title="ExcelsiusGPS Spine11 TLIF" width="" height="">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="skL79NupiPc" data-video-title="Understand how the Mazor X Stealth Edition ™ is transforming spinal workflow with an expert surgeon." data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=skL79NupiPc" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/skL79NupiPc/hqdefault.jpg" title="Understand how the Mazor X Stealth Edition ™ is transforming spinal workflow with an expert surgeon." width="" height="">
  </a>
</div>

<p>Please guide and advise</p>
<p>many thanks</p>

---

## Post #2 by @lassoan (2021-01-03 16:49 UTC)

<p>You can create a markups plane widget. Markups can be interactively moved and rotated in slice and 3D views. If you add an observer to the markups node then you can copy its position and orientation to the screw model.</p>

---

## Post #3 by @Prathamesh_Vishnudas (2023-09-21 20:58 UTC)

<p>Hello, I am working on a similar project. Can you explain how to create a markups plane widget, add an observer to the markups node, and copy its position and orientation to the screw model?</p>

---
