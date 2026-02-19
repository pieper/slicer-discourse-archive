---
topic_id: 14513
title: "How Does Vmtksurfacecenterlineprojection Work"
date: 2020-11-10
url: https://discourse.slicer.org/t/14513
---

# How does vmtksurfacecenterlineprojection work

**Topic ID**: 14513
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/how-does-vmtksurfacecenterlineprojection-work/14513

---

## Post #1 by @Nadun_19 (2020-11-10 00:02 UTC)

<p>Hi</p>
<p>I was wondering how the vmtksurfacecenterlineprojection function actually carries out the centerline projection to a surface.</p>
<p>Thanks<br>
Nadun</p>

---

## Post #2 by @lantiga (2020-11-13 00:28 UTC)

<p>Hi <a class="mention" href="/u/nadun_19">@Nadun_19</a>,<br>
for each point on the surface, the “closest” location on the centerline is computed and its attributes are set as the attributes of the surface point. Note that the centerline location is typically found in-between centerline points (i.e. looking along each segment), so the attributes might be interpolated accordingly.</p>
<p>The way “closest” is determined is done in two ways:</p>
<ul>
<li>by just using Euclidean distance (<code>-useradius 0</code>)</li>
<li>by determining the location on the surface that is the center of the sphere of radius R whose surface is closest to the surface point (<code>-useradius 1</code>). In other words, thinking about the continuous envelope of spheres along the centerline (the so-called “canal surface”, or “tube”), for each surface point we determine the closest point on the canal surface, and from there the location on the centerline that is a center of the sphere that is tangent to the canal surface in that point.</li>
</ul>
<p>Hope this helps</p>
<p>Luca</p>

---
