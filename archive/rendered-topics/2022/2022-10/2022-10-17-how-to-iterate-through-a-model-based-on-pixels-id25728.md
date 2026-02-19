---
topic_id: 25728
title: "How To Iterate Through A Model Based On Pixels"
date: 2022-10-17
url: https://discourse.slicer.org/t/25728
---

# How to iterate through a model based on pixels?

**Topic ID**: 25728
**Date**: 2022-10-17
**URL**: https://discourse.slicer.org/t/how-to-iterate-through-a-model-based-on-pixels/25728

---

## Post #1 by @jumbojing (2022-10-17 06:47 UTC)

<p>How to iterate through a model (<img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">) based on pixels?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f85d9b9845efb0a91f7af183aa3959a61705d34.png" data-download-href="/uploads/short-url/6Mpdin5ZjfZauZWtfRzeJtmys3q.png?dl=1" title="Screenshot000" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f85d9b9845efb0a91f7af183aa3959a61705d34_2_652x500.png" alt="Screenshot000" data-base62-sha1="6Mpdin5ZjfZauZWtfRzeJtmys3q" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f85d9b9845efb0a91f7af183aa3959a61705d34_2_652x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f85d9b9845efb0a91f7af183aa3959a61705d34_2_978x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f85d9b9845efb0a91f7af183aa3959a61705d34_2_1304x1000.png 2x" data-dominant-color="A8AAB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot000</span><span class="informations">1710×1310 44.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to find the largest inscribed circle based on this. Like <a href="https://www.cnblogs.com/01black-white/p/16289830.html" rel="noopener nofollow ugc">this way</a> or <a href="https://blog.csdn.net/liu_taiting/article/details/104874363" rel="noopener nofollow ugc">this</a> by cv2 .</p>

---

## Post #2 by @lassoan (2022-10-17 15:26 UTC)

<p>You can get model point positions as a numpy array using</p>
<pre><code class="lang-python">pointArray = slicer.util.arrayFromModelPoints(modelNode)
</code></pre>
<p>Note that you cannot implement algorithms in Python that iterate through tens of thousands of points, because it will be extremely slow. You need to work with high-level functions that operate on the entire array.</p>
<p>The first link you described performs an exhaustive search using trial and error. It will be very slow, especially in 3D.</p>
<p>The second method, based on distance transform, should work. There is no need to mess with OpenCV (it is a very big and problematic package), but you can export the segmentation to label volume and use Simple Filters module and use any of the distance map filters to compute the distance map.</p>
<p>You can also use Extract Centerline module in SlicerVMTK extension to get all the minmum inscribed spheres for your shape (along with the radius values). If you need only a single radius value then you can use the maximum radius value (and the corresponding centerline point position). If your object is not spherical (as in your example above) then it might make sense to look at more centerline points (e.g., all local maxima points), because a single sphere may not be a good representation of your object shape.</p>

---

## Post #3 by @jumbojing (2022-10-18 01:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25728">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the minmum inscribed spheres</p>
</blockquote>
</aside>
<p>? but…How to get the maximum inscribed sphere model by code.</p>

---

## Post #4 by @lassoan (2022-10-18 02:19 UTC)

<p>Extract Centerline module gives you a centerline model or curve. You get the computed radii as a numpy array (<code>slicer.util.arrayFromMarkupsCurveData()</code>), get the index of the point that has the largest radius value, and get the position of that point (<code>slicer.util.arrayFromMarkupsCurvePoints()</code>).</p>
<p>It may be even simpler to use the Voronoi diagram that Extract centerline module can also provide you. What you get is model node contains all the centerpoints of the inscribed spheres that can be inscribed in your mesh. You can get the radii values as a numpy array (<code>slicer.util.arrayFromModelPointData()</code>), find the index of the maximum value, and get the position of that point (<code>slicer.util.arrayFromModelPoints()</code>).</p>
<p>Give it a try and let us know if you get stuck at any point.</p>

---
