---
topic_id: 4332
title: "Finding The Corresponding Point To A Specific Displacement F"
date: 2018-10-09
url: https://discourse.slicer.org/t/4332
---

# Finding the corresponding point to a specific displacement field

**Topic ID**: 4332
**Date**: 2018-10-09
**URL**: https://discourse.slicer.org/t/finding-the-corresponding-point-to-a-specific-displacement-field/4332

---

## Post #1 by @aseman (2018-10-09 19:31 UTC)

<p>Slicer version:4.8.1<br>
Hi 3D slicer experts and all users<br>
I have got displacement fields for different points of a particular segment (i.e heart); and with the movement of mouse on each point , the corresponding vector components are displayed in 3 coordinates(RAS) in information section of Transforms module . and inversely ,now I want to find the point which is corresponding  to a specific vector  . on the other words, I want to find that in a volume ,which point has that specific displacement  field ? is it possible to find this point? and can you guide me about this question with an example?<br>
Thanks a lot</p>

---

## Post #2 by @lassoan (2018-10-10 04:24 UTC)

<aside class="quote no-group" data-username="aseman" data-post="1" data-topic="4332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>I want to find that in a volume ,which point has that specific displacement field ?</p>
</blockquote>
</aside>
<p>Thousands of points may have almost exactly the same displacement value in a field. You can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms">Contour visualization mode</a> to highlight regions that have specific displacement magnitude values.</p>
<p>If you were interested in which point was moved to a specific position then you need to invert the transform by clicking on Invert button.</p>

---

## Post #3 by @aseman (2018-10-10 06:58 UTC)

<p>Hi<br>
Thank you very much for your guidelines ; and now, I have another  question !  can I use  also  python to find these points which are correspond to a specific displacement vector or not?<br>
Thanks a lot</p>

---

## Post #4 by @lassoan (2018-10-10 12:56 UTC)

<p>Yes you can. All Slicer APIs are available in Python. If you describe what you would like to do exactly we can give more specific help.</p>

---
