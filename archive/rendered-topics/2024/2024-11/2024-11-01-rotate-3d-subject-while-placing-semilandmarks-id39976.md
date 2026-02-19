---
topic_id: 39976
title: "Rotate 3D Subject While Placing Semilandmarks"
date: 2024-11-01
url: https://discourse.slicer.org/t/39976
---

# Rotate 3D subject while placing semilandmarks 

**Topic ID**: 39976
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/rotate-3d-subject-while-placing-semilandmarks/39976

---

## Post #1 by @Ruiqi-CUB (2024-11-01 10:46 UTC)

<p>I am using Slicer 5.6.2 on MacOS. I am working on 3D mesh file in stl format.</p>
<p>I can’t see all the surface when placing semi-landmarks of a curve. Is there a way to rotate the subject WHILE placing semilandmarks? Right now, I have to place some semilandmarks near the part I would like to put them, then rotate the subject, then move those semilandmarks to correct positions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8cd9e9ba1d556153af9ba0949346396c3112603.png" data-download-href="/uploads/short-url/sEo1YToz94wSLKVezzIUvV53YlB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8cd9e9ba1d556153af9ba0949346396c3112603.png" alt="image" data-base62-sha1="sEo1YToz94wSLKVezzIUvV53YlB" width="433" height="149"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">433×149 7.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, I found that I need to lock interactions after finishing landmarking a curve before I can rotate the subject, is there a way to rotate without locking interaction? Right now it is quite annoying, as I have to 1. put semilandmarks at nearby surface 2. lock interaction 3. rotate subject. 4. move those points into correct positions. I usually have to do it several times. I am quite new to slicer, is there an easy way to do this?</p>

---

## Post #2 by @lassoan (2024-11-01 10:53 UTC)

<p>You can rotate around the 3D view by using the arrow keys on the keyboard. If you installed SlicerMorph extension them you can activate SlicerMorph customizations in application settings, which makes the <code>p</code> key activate place mode (after you deactivated it with right-click). You can also add keyboard shortcut to activate or deactivate any Slicer function.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> do you have any additional tips for landmarking?</p>

---

## Post #3 by @muratmaga (2024-11-01 18:40 UTC)

<aside class="quote no-group" data-username="Ruiqi-CUB" data-post="1" data-topic="39976">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b38774/48.png" class="avatar"> Ruiqi-CUB:</div>
<blockquote>
<p>I can’t see all the surface when placing semi-landmarks of a curve. Is there a way to rotate the subject WHILE placing semilandmarks?</p>
</blockquote>
</aside>
<p>The answer is yes. You can right click to end the placement, and then rotate your subject to the new orientation, then restart the placement by putting the mouse to the placement mode (the dropdown with the curve icon, in the markups toolbar).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea3e074151ee1a421b8133593f2b368f4beaf5bd.png" alt="image" data-base62-sha1="xqcCDy0qyP2zZuAyhAbKgu1P7kh" width="690" height="79" data-dominant-color="E7E6E7"></p>
<p>This works for everyone. As <a class="mention" href="/u/lassoan">@lassoan</a> indicated, if you are usign SlicerMorph and enabled its customizations, you can use the p shortcut key to place a new control point on the curve after you stop the placement. It will automatically put the point whereever your cursor is on.</p>

---

## Post #4 by @muratmaga (2024-11-01 18:42 UTC)

<aside class="quote no-group" data-username="Ruiqi-CUB" data-post="1" data-topic="39976">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b38774/48.png" class="avatar"> Ruiqi-CUB:</div>
<blockquote>
<p>I found that I need to lock interactions after finishing landmarking a curve before I can rotate the subject, is there a way to rotate without locking interaction?</p>
</blockquote>
</aside>
<p>That doesn’t sound right. Interaction lock and rotation has nothing to do with each other. You might have to provide a screen capture movie of how you are using this (or explain the issue better).</p>

---
