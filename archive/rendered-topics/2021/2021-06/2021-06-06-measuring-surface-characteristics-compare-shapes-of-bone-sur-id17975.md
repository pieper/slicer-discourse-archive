---
topic_id: 17975
title: "Measuring Surface Characteristics Compare Shapes Of Bone Sur"
date: 2021-06-06
url: https://discourse.slicer.org/t/17975
---

# Measuring surface characteristics/compare shapes of bone surfaces

**Topic ID**: 17975
**Date**: 2021-06-06
**URL**: https://discourse.slicer.org/t/measuring-surface-characteristics-compare-shapes-of-bone-surfaces/17975

---

## Post #1 by @OrthopedicsSeb (2021-06-06 18:52 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior: Measure and display the surface of a bone and calculate the mean angle (if its convex or concave shape), compare it to other specimens, size of the area<br>
Actual behavior:</p>

---

## Post #2 by @muratmaga (2021-06-07 17:01 UTC)

<p>Welcome to the community.<br>
I wonder if you submit your post prematurely, as there is no question or an actual issue.<br>
All of what you ask should be doable with Slicer. if you can give specifics, we can be more helpful.</p>

---

## Post #3 by @OrthopedicsSeb (2021-06-10 06:40 UTC)

<p>Thanks for the answer.<br>
I think to give my example is much easier:<br>
I imported the files and generated a 3 D Model of a CT Scan. Now I want to measure the contact surface on the radius at the distal radio-ulnar joint and (thats the more important part) calculate/mathematically demonstrate the shape of this surface. Normally it should we more or less concave, convex or straight. After i would do that for a bunch of scans and compare the characteristics and group them accordingly.</p>
<p>I cant figure out a way to calculate and extract the shape of the surface and thats where i would need you guys help.</p>
<p>Thank you</p>

---

## Post #4 by @muratmaga (2021-06-10 14:36 UTC)

<p>Isolating the articular area is easy, you can use the surface cut feature of the segment editor to cut out the articular surface of the radio-ulnar joint.</p>
<p>Quantifying the surfaces is more or less convex/concave is more challenging. While we have shape analysis tools in SlicerMorph, those are all landmark-based, those won’t work for you. You need an analytic pipeline that measures curvature. This is available for curves, but not sure if there is something ready to be used for the surfaces.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #5 by @pieper (2021-06-10 14:44 UTC)

<p>I don’t think there’s any existing module GUI for this, but with a little scripting you could use <a href="https://vtk.org/doc/nightly/html/classvtkCurvatures.html#details">this filter</a> to get the local curvature (per-vertex of the surface model).</p>

---
