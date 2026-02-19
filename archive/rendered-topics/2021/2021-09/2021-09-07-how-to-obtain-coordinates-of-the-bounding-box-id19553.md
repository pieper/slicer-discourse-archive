---
topic_id: 19553
title: "How To Obtain Coordinates Of The Bounding Box"
date: 2021-09-07
url: https://discourse.slicer.org/t/19553
---

# How to obtain Coordinates of the Bounding Box

**Topic ID**: 19553
**Date**: 2021-09-07
**URL**: https://discourse.slicer.org/t/how-to-obtain-coordinates-of-the-bounding-box/19553

---

## Post #1 by @Rituraj_Dutta (2021-09-07 19:39 UTC)

<p>I have generated a bounding box (cuboid) for the liver in 3d Slicer using the ROI tool. How can I get the coordinates of the cuboid ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4681c5c35a45c55f3197abc967a44c03346eb7b.jpeg" data-download-href="/uploads/short-url/uj2hmxpbcYHXzy9eDH40wdjoY79.jpeg?dl=1" title="3d slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4681c5c35a45c55f3197abc967a44c03346eb7b_2_690x371.jpeg" alt="3d slicer" data-base62-sha1="uj2hmxpbcYHXzy9eDH40wdjoY79" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4681c5c35a45c55f3197abc967a44c03346eb7b_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4681c5c35a45c55f3197abc967a44c03346eb7b_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4681c5c35a45c55f3197abc967a44c03346eb7b_2_1380x742.jpeg 2x" data-dominant-color="636374"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d slicer</span><span class="informations">1920×1034 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-09-08 04:15 UTC)

<p>You can use the <code>GetBounds</code> method of the markups ROI (or the legacy annotation ROI) node:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; bounds = np.zeros(6)
&gt;&gt;&gt; getNode('R').GetBounds(bounds)
&gt;&gt;&gt; bounds
array([-30.14435768, 79.05784416,
-20.47541332, 40.95082569,
-54.60110092, 54.60110092])
</code></pre>
<p>The returned values are R min, R max, A min,  A max, S min, S max.</p>

---

## Post #3 by @Rituraj_Dutta (2021-09-08 08:46 UTC)

<p>Thanks for the answer but sorry to say I’m new to 3d slicer so how can I implement this script along with 3d slicer. Like do I need to import some packages or we  can run this code directly on 3d slicer ?</p>

---

## Post #4 by @lassoan (2021-09-08 13:55 UTC)

<p>You can run this code as is, in Slicer’s Python console. To get started with Python scripting in Slicer, check out the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">developer tutorials</a>.</p>

---

## Post #5 by @Rituraj_Dutta (2021-09-08 14:07 UTC)

<p>Also one more thing the no. of coordinates should be 8 equal to the number of edges. But here’s it’s 6.</p>

---

## Post #6 by @lassoan (2021-09-08 14:16 UTC)

<p>The returned values are R min, R max, A min, A max, S min, S max: 3 axes * 2 bounds = 6.</p>

---
