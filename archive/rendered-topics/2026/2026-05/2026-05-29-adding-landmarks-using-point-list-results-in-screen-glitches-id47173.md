---
topic_id: 47173
title: "Adding landmarks using Point List results in screen glitches"
date: 2026-05-29
url: https://discourse.slicer.org/t/47173
last_bumped: 2026-05-29T17:12:37.680Z
---

# Adding landmarks using Point List results in screen glitches

**Topic ID**: 47173
**Date**: 2026-05-29
**URL**: https://discourse.slicer.org/t/adding-landmarks-using-point-list-results-in-screen-glitches/47173

---

## Post #1 by @thelobsternods (2026-05-29 16:51 UTC)

<p>We have been using the same protocol for adding landmarks to 3D models for years, but are suddenly experiencing issues with our established protocol. Specifically, we only have this problem after starting a new “point list” and adding one or more points in the markups module. As shown below, once there are one or more landmarks and they are visible, then the 3D Slicer window will glitch as shown in the photo below. The issue is confined to the 3D slicer window (for instance does not invade the desktop display in the background). We can interact with the slicer window, clicking and moving the model, to get it to look correct again. But then the glitch will keep occurring as the model is rotated and interacted with more.</p>
<p>This is not 3D Slicer crashing–we can still interact with the window, add landmarks, save data, but it will keep glitching with this display issue (artifact?).</p>
<p>This issue started suddenly today (for instance was not happening last week). We have only seen this behavior with 3D slicer (no other software so far).</p>
<p>The behavior seems to be limited to the points list being visible. Hiding the list of points returns 3D slicer to normal behavior. Adding a curve does not reproduce the behavior.</p>
<p>[Edit] We have only been able to “fix” this issue by hiding the Points List or by making a curve first and then making our Points List so that it is not the first node listed in the module.</p>
<p>We have verified that it is none of the following:</p>
<ul>
<li>Not the monitor–happens using any monitor we switch in</li>
<li>Not the specific 3D model–happens on any model now</li>
<li>Not the computer–happens on another computer that has different specs but is 3D slicer compatible and has also worked normally up to this point.</li>
<li>Not this version of 3D Slicer-- happens using v5.10.0 and v5.6.1.</li>
</ul>
<p>Any ideas for how to fix or troubleshoot this issue would be appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f683202b39425af1dbff2ff067ea41fe982f9462.jpeg" data-download-href="/uploads/short-url/zaKonj7LUDw6Btpi3zZRlqu5KXE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f683202b39425af1dbff2ff067ea41fe982f9462.jpeg" alt="image" data-base62-sha1="zaKonj7LUDw6Btpi3zZRlqu5KXE" width="320" height="240"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">320×240 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-05-29 17:12 UTC)

<p>The image too small to tell what’s going on? Can you send a higher resolution picture? From what I can see this might be related to graphics driver issue. Did this computer received a windows update sometime recently?</p>

---
