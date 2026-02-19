---
topic_id: 26277
title: "Distance From Point To Segment"
date: 2022-11-17
url: https://discourse.slicer.org/t/26277
---

# Distance from point to segment

**Topic ID**: 26277
**Date**: 2022-11-17
**URL**: https://discourse.slicer.org/t/distance-from-point-to-segment/26277

---

## Post #1 by @NILV (2022-11-17 09:09 UTC)

<p>Hello everyone.<br>
I have some problems when using the slicer.<br>
In my project,I want to get the distance from the center of GTV to the lung boundary,which means the distance to the apex of lung in SI direction and the distance to the chest wall in LR,AP direction.<br>
Now the problems is I can not markup the point I want.For example,in this image, I want get the two distances by scripts.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f95f0bc4a81306fef90ba6c1cf44a312f913463.png" data-download-href="/uploads/short-url/mLLa8L7bS5rQ7jcHfX4LlWM9r35.png?dl=1" title="1668676163342" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f95f0bc4a81306fef90ba6c1cf44a312f913463.png" alt="1668676163342" data-base62-sha1="mLLa8L7bS5rQ7jcHfX4LlWM9r35" width="605" height="500" data-dominant-color="3C4239"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1668676163342</span><span class="informations">749×618 71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I checked all the slicer extension but no one can do that.So I wondeing if anyone can help me to solve it!<br>
Thanks a lot!</p>

---

## Post #2 by @lassoan (2022-12-01 07:10 UTC)

<p>You can get the intersection of a line (starting point is the center, endpoint is a point far away in the desired direction) and a mesh (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-representation-of-a-segment">obtained from the segment</a>) and use <code>IntersectWithLine</code> method of a <code>vtkModifiedBSPTree</code> locator to get the intersection point.</p>

---
