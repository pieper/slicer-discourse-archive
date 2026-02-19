---
topic_id: 7176
title: "Limited Fast Marching Range"
date: 2019-06-15
url: https://discourse.slicer.org/t/7176
---

# Limited Fast marching range

**Topic ID**: 7176
**Date**: 2019-06-15
**URL**: https://discourse.slicer.org/t/limited-fast-marching-range/7176

---

## Post #1 by @Amine (2019-06-15 12:20 UTC)

<p>Windows 10<br>
Tried on Slicer 4.10.1 and 4.11</p>
<p>For this particular volume Fastmarching gets limited by an upper and lower limit ( i run it at a high “max volume” to better show its limits).</p>
<p>Already tried:<br>
-Make sure the master volume is correct (there is only one)<br>
-Node contains only one scalar volume<br>
-No segment masking involved</p>
<p>Painting and Thresholding on the other hand cover the whole volume.<br>
Here is a link to the volume:<br>
<a href="https://drive.google.com/open?id=1HWnVEwjbAXzBJxVRid6F8Cg4CYsBHSxJ" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/open?id=1HWnVEwjbAXzBJxVRid6F8Cg4CYsBHSxJ</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a65a1bc62c1faf3f3cd788811c834d0f464bf7dd.png" alt="Capture" data-base62-sha1="nJCjDct5Uq5qC1lYq68uL1YwEwt" width="507" height="328"></p>

---

## Post #2 by @lassoan (2019-06-15 15:01 UTC)

<p>Fast Marching effect requires availability of a 4-voxel neighborhood of segmented voxels, which is not valid at the volume boundary. You can expand the volume using “Crop volume” module and enlarge the clipping ROI box to add a black boundary around the original image.</p>
<p>However, I would recommend to try the much more powerful and flexible “Grow from seeds” effect instead.</p>

---

## Post #3 by @Amine (2019-06-16 00:36 UTC)

<p>Thanks for your reply, very informative.<br>
As to why i still turn back to Fastmarching sometimes, is the possibility to examine the expansion in real time via the “segment volume” slider, while grow from seeds require editing and updating the effect takes longer.</p>

---
