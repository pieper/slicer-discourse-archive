---
topic_id: 14363
title: "Set Center Of Rotation For Transform In 3D View"
date: 2020-11-01
url: https://discourse.slicer.org/t/14363
---

# Set center of rotation for transform in 3D view

**Topic ID**: 14363
**Date**: 2020-11-01
**URL**: https://discourse.slicer.org/t/set-center-of-rotation-for-transform-in-3d-view/14363

---

## Post #1 by @manjula (2020-11-01 13:12 UTC)

<p>Even though it is possible to rotate the object in 3D view interactively whenever the rotation transformation is applied it is working as origin in the world origin ( I guess. )<br>
3D interactor is very difficult to precisely adjust and i don’t know if it is possible to constrain the 3D interactor to rotate around only one axis if needed.<br>
Is it possible to add a feature to change the object origin to the center of the geometry from GUI?  (and if possible other centers of origin as well )</p>
<p>(i am aware any center of origin can be defined from the fiducial point using the script)</p>

---

## Post #2 by @lassoan (2020-11-01 19:55 UTC)

<p>Similar questions come up quite often but so far in most cases it turned out that manual rotation in 3D view had not been a good solution anyway, so we did not end up investing a lot of time into improving the transform widget. It is true then if you could set the center of rotation and axes directions more easily then it would make accurate orientation somewhat more feasible (we have an <a href="https://github.com/Slicer/Slicer/issues/2579">open issue</a> for this). But there are always much better solutions than free translation/rotation in 3D, because that is inherently a very tedious, iterative process.</p>
<p>If you describe what task you are trying to solve then we can give advice what tools you may consider.</p>

---

## Post #3 by @manjula (2020-11-01 20:19 UTC)

<p>It is that often that we need to orient an  ROI box in relation to structures.  For example we here we want to make the ROI box parallel to the bone surface.  Right now we achieved this with the script placing a fiducial in the centroid and rotating it around that.<br>
But if there is an automated function to set the object origin to the center of geometry/segment then it would be easily rotated from the transform module</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18615690a176c8e2e04007d055d95869f9b1e401.jpeg" alt="Screenshot from 2020-11-01 21-13-11" data-base62-sha1="3tG0knVL2YpNZGyZp4nnBcXlIVX" width="561" height="375"></p>

---

## Post #4 by @lassoan (2020-11-01 20:30 UTC)

<p>We’ll implement ROI rotation in the new Markups ROI node. It should be available in a few months.</p>
<p>Note that you can create optimal oriented bounding box fully automatically, using 10-15 lines of code (see <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203" class="inline-onebox">New Segment Statistics: Oriented Bounding Box, Diameter and More</a>). The script could be slightly modified to create ROI from automatically rotate the ROI to have one side parallel to a specified line.</p>
<p>If you don’t want to do any programming, then you can rotate the volume so that the cut axes are parallel to R/A/S axis and then you don’t need to rotate the ROI.</p>

---

## Post #5 by @manjula (2020-11-01 20:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="14363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We’ll implement ROI rotation in the new Markups ROI node. It should be available in a few months.</p>
</blockquote>
</aside>
<p>It would be great and thank you very much for that. Which will simplify many things.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="14363">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that you can create optimal oriented bounding box fully automatically</p>
</blockquote>
</aside>
<p>This is the way we currently using…</p>

---

## Post #6 by @Sunderlandkyl (2020-11-02 15:52 UTC)

<p>I’ve started the implementation of the Markups ROI here: <a href="https://github.com/Sunderlandkyl/Slicer/tree/wip_roi" rel="noopener nofollow ugc">https://github.com/Sunderlandkyl/Slicer/tree/wip_roi</a></p>
<p>There are a lot of issues with it currently, but I plan to to have it completed by the end of November.</p>

---

## Post #7 by @manjula (2020-11-02 16:39 UTC)

<p>Thank you very much for the great effort! <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=9" title=":clap:" class="emoji" alt=":clap:"></p>

---
