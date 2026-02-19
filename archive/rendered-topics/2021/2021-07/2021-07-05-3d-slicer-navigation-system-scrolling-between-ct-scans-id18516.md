---
topic_id: 18516
title: "3D Slicer Navigation System Scrolling Between Ct Scans"
date: 2021-07-05
url: https://discourse.slicer.org/t/18516
---

# 3D slicer navigation system: scrolling between CT scans

**Topic ID**: 18516
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/3d-slicer-navigation-system-scrolling-between-ct-scans/18516

---

## Post #1 by @Matteo_Boles (2021-07-05 14:08 UTC)

<p>Hello,<br>
I was able to make polaris vicra navigation system work with 3D slicer, because I wanted to take into account the position of the tip of an instrumented while navigating inside a 3D printed vertebral body.<br>
What I would like now to do is to be able to scroll between the different slices of the CT scans while i am moving the tip of the tracked instrument.<br>
The problem is that the scans move with the tip but I want only to change the level of the slice not the position, so sometimes I cannot see the CT scans.<br>
I attach two videos to show you better what I actually get and what I would like to get.</p>
<p>What happens in my scene:<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7267bba7616b6028b7520f7fd69fda7dad402fff.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7267bba7616b6028b7520f7fd69fda7dad402fff.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7267bba7616b6028b7520f7fd69fda7dad402fff.mp4</a>
    </source></video>
  </div><p></p>
<p>This is instead what I would like to get:<br>
<a href="https://www.youtube.com/watch?v=lpnvMrpqjxs" rel="noopener nofollow ugc">(1) Optical tracking using 3D Slicer + IGT - YouTube</a></p>
<p>Hope anybody can help!</p>

---

## Post #2 by @lassoan (2021-07-09 05:04 UTC)

<p>I don’t think there is a built-in reslicing mode like that, but it is very easy to add a short Python script to implement this behavior. You need to add an observer to the transform node and in the callback function, retrieve the position (4th column of the transformation matrix) and use that position to update the SliceToRAS matrix of the slice node. You can find many relevant examples for this in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>

---
