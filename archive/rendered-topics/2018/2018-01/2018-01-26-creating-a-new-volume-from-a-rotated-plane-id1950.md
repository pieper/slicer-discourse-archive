---
topic_id: 1950
title: "Creating A New Volume From A Rotated Plane"
date: 2018-01-26
url: https://discourse.slicer.org/t/1950
---

# Creating a new volume from a rotated plane

**Topic ID**: 1950
**Date**: 2018-01-26
**URL**: https://discourse.slicer.org/t/creating-a-new-volume-from-a-rotated-plane/1950

---

## Post #1 by @Masteling (2018-01-26 20:59 UTC)

<p>Hi everyone,<br>
My main goal is to segment/label map a anatomical feature in a rotated plane.</p>
<p>I’m using MRI and I’m rotating the plane using Reformat to rotate a slice to a given angle. Then I want to segment an anatomical feature in that rotated plane.  If I do it directly there, the plane either changes back to it’s original position or I have the “stair case effect”, with the segmentation spread about different slices.</p>
<p>I would like to know if it is possible to create a new volume of the rotated plane where I can then segment my region of interest.</p>
<p>Many thanks,<br>
Mariana</p>

---

## Post #2 by @lassoan (2018-01-26 22:27 UTC)

<p>If you use Segment Editor module then you can segment in oblique plane but of course at the segment boundaries you’ll see striping artifacts. You can safely ignore the artifacts, as the segmentation is correct in 3D, and the artifacts only appear the boundaries, so if you segment multiple slices they always appear only at the first and last slice.</p>
<p>If the artifacts are too confusing then you can resample your volume with a rotated region of interest, using “Crop Volume” module. To rotate a region of interest, go to Transforms module, create a linear transform, and apply it to the region of interest. If this is something that you would do very often then you can automate this with a short script, which for example creates a region of interest and rotates it to the axis of a selected slice viewer.</p>

---
