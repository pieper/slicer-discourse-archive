---
topic_id: 28370
title: "3D Mouse Cursor For Stereoscopic Displays"
date: 2023-03-14
url: https://discourse.slicer.org/t/28370
---

# 3D mouse cursor for stereoscopic displays

**Topic ID**: 28370
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/3d-mouse-cursor-for-stereoscopic-displays/28370

---

## Post #1 by @LucasGandel (2023-03-14 11:18 UTC)

<p>Hello,</p>
<p>We would like have a 3D cursor in the 3D view, similar to the <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/9894" rel="noopener nofollow ugc">new widget</a> that was recently merged in VTK.<br>
This widget replaces the mouse cursor by a 3D point representation that is projected on the surface when an actor is hovered.<br>
This feature is useful in a stereo environment, or when using haptic devices, to better visualize the position of the cursor in the 3D scene.</p>
<p>We noticed that the current crosshair implementation in 3DSlicer offers a similar functionality, but the following requirements are missing:</p>
<ol>
<li>The 2D mouse cursor should be hidden and replaced by the crosshair</li>
<li>The crosshair position should be updated on mouse move events without pressing the shift key</li>
<li>The crosshair position should be updated smoothly using a hardware picker (as opposed to the current volume picker)</li>
</ol>
<p>We are not sure what is the best path forward to make this functionality available in 3DSlicer.<br>
Should we update the current crosshair implementation to add a new mode that fulfills the requirements above?<br>
Or is it preferred to integrate the vtk3DCursorWidget directly?</p>
<p>Many thanks,<br>
Lucas</p>
<p>cc: <a class="mention" href="/u/laurennlam">@LaurennLam</a></p>

---

## Post #2 by @pieper (2023-03-14 14:00 UTC)

<p>That sounds pretty close to the current crosshair behavior and I think you could just make these modes available without adding a whole new mechanism.</p>

---

## Post #3 by @LucasGandel (2023-03-15 08:02 UTC)

<p>Thanks a lot for your insight <a class="mention" href="/u/pieper">@pieper</a> ! Sounds good to me.</p>
<p>Let’s wait for potential feedback from <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jcfr">@jcfr</a> before we go any further.</p>

---

## Post #4 by @LaurennLam (2023-03-24 10:20 UTC)

<p>A PR has been opened to answer the requirements.<br>
It can be found <a href="https://github.com/Slicer/Slicer/pull/6910" rel="noopener nofollow ugc">here</a></p>

---
