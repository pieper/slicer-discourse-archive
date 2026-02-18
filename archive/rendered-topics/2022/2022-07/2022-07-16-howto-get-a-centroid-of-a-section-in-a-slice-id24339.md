# Howto get a centroid of a section in a slice?

**Topic ID**: 24339
**Date**: 2022-07-16
**URL**: https://discourse.slicer.org/t/howto-get-a-centroid-of-a-section-in-a-slice/24339

---

## Post #1 by @jumbojing (2022-07-16 08:59 UTC)

<p>I want to get each centroid of the pedicle sections in green slice(as shown below) by code.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc3cff604f4a2432f8724d21bb379abcea0ae357.jpeg" data-download-href="/uploads/short-url/t8M5Cs1IOhMyxE51QLEFdcv1G2b.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3cff604f4a2432f8724d21bb379abcea0ae357_2_690x440.jpeg" alt="image" data-base62-sha1="t8M5Cs1IOhMyxE51QLEFdcv1G2b" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3cff604f4a2432f8724d21bb379abcea0ae357_2_690x440.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3cff604f4a2432f8724d21bb379abcea0ae357_2_1035x660.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3cff604f4a2432f8724d21bb379abcea0ae357_2_1380x880.jpeg 2x" data-dominant-color="9D9D86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1389×887 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jumbojing (2022-07-17 04:11 UTC)

<blockquote>
<p><a href="https://discourse.slicer.org/t/place-fiducial-at-centroid-of-current-slice/22169">Place fiducial at centroid of current slice - Support - 3D Slicer Community</a><br>
<a href="https://discourse.slicer.org/t/get-centroid-from-script/13191">Get Centroid from Script</a><br>
<a href="https://discourse.slicer.org/t/centroid-determination/3541">Centroid determination</a><br>
<a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>@ jmhuie <a class="mention" href="/u/manjula">@manjula</a> <a class="mention" href="/u/szhang">@szhang</a></p>
</blockquote>

---

## Post #3 by @lassoan (2022-07-17 06:36 UTC)

<p>You can get the current slice image from the slice logic of the slice widget at shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume">this example</a>.</p>
<p>However, probably you can get the ideal pedicle screw axis position and orientation directly in 3D by segmenting a pedicle. It can be as simple as Paint a sphere with “Editable intensity range” set to bone. You could further improve result by applying Island effect → Extract largest island. To fill the internal holes in the segment you can use Wrap Solidify effect. You can get the axis position and direction of this bone segment using Segment Statistics module. You can get the centerline curve of the pedicle using VMTK extension’s Extract centerline module.</p>

---

## Post #4 by @jumbojing (2022-07-17 07:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="24339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can get the current slice image from the slice logic of the slice widget at shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume" rel="noopener nofollow ugc">this example</a>.</p>
</blockquote>
</aside>
<p>我没有看懂这个例子</p>
<blockquote>
<p>I didn’t understand <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume" rel="noopener nofollow ugc">this example</a>. <img src="https://emoji.discourse-cdn.com/twitter/cold_sweat.png?v=12" title=":cold_sweat:" class="emoji" alt=":cold_sweat:" loading="lazy" width="20" height="20"></p>
</blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="24339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, probably you can get the ideal pedicle screw axis position and orientation directly in 3D by segmenting a pedicle. It can be as simple as Paint a sphere with “Editable intensity range” set to bone. You could further improve result by applying Island effect → Extract largest island. To fill the internal holes in the segment you can use Wrap Solidify effect.</p>
</blockquote>
</aside>
<p>由于一些骨质疏松等的特殊病例，segmenting椎弓根with script总是不理想。</p>
<blockquote>
<p>Due to some special cases such as osteoporosis, segmenting a pedicle with script is not always ideal.</p>
</blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="24339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can get the axis position and direction of this bone segment using Segment Statistics module. You can get the centerline curve of the pedicle using VMTK extension’s Extract centerline module.</p>
</blockquote>
</aside>
<p>我一直在探索影像学意义上的理想的椎弓根的轴，利用Slicer以及像VMTK这样的插件。。。可是因为上面提到的原因，没成功 <img src="https://emoji.discourse-cdn.com/twitter/cold_sweat.png?v=12" title=":cold_sweat:" class="emoji" alt=":cold_sweat:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/imp.png?v=12" title=":imp:" class="emoji" alt=":imp:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>I’ve been exploring the ideal pedicle axis in the imaging sense, using Slicer and plugins like VMTK.  .  .  However, for the reasons mentioned above, it was unsuccessful.</p>
</blockquote>

---

## Post #5 by @jumbojing (2022-07-18 13:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="3541">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/centroid-determination/3541/7">Centroid determination</a></div>
<blockquote>
<pre><code class="lang-auto">import numpy as np
print(np.average(array('ModelX'), axis=0))
</code></pre>
</blockquote>
</aside>
<p>老师您的意思👆🏻是说，多边形各顶点坐标的`np.average()'就是这个多边形的质心吗？</p>
<blockquote>
<p>Teacher, do you mean <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> that the `np.average()’ of the coordinates of each vertex of the polygon is the centroid of the polygon?</p>
</blockquote>

---

## Post #6 by @jumbojing (2022-07-18 14:02 UTC)

<p>well,现在的问题就转化成了如何提取当前界面某个多边形的顶点坐标。。。</p>
<blockquote>
<p>Well, the current question now becomes how to extract the vertex coordinates of a polygon of the current section.  .  .</p>
</blockquote>

---

## Post #7 by @lassoan (2022-07-19 07:23 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="4" data-topic="24339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p>Due to some special cases such as osteoporosis, segmenting a pedicle with script is not always ideal.</p>
</blockquote>
</aside>
<p>Yes, I know that segmentation of the pedicle is often not trivial, but there are many Segment Editor tools that can help with this. You could also train a neural network using MONAILabel extension to segment the pedicles fully automatically.</p>

---

## Post #8 by @jumbojing (2022-07-20 05:14 UTC)

<aside class="quote no-group quote-modified" data-username="jumbojing" data-post="3" data-topic="24380" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-extract-the-vertex-coordinates-of-a-polygon-of-a-model-in-the-current-section/24380/3">How to extract the vertex coordinates of a polygon of a model in the current section?</a></div>
<blockquote>
<p>Lassoan教授，好吧。。。我想出来个笨拙的解决方案：</p>
<blockquote>
<p>Prof.Lassoan, okay. . . I came up with a clumsy solution:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458.jpeg" data-download-href="/uploads/short-url/bjm1QYDHqJB7R8EHp6wlWpFiAc0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_454x500.jpeg" alt="image" data-base62-sha1="bjm1QYDHqJB7R8EHp6wlWpFiAc0" width="454" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_454x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_681x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_908x1000.jpeg 2x" data-dominant-color="8C858E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">994×1094 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p>不过这个解决方案有个问题：就是提取的点和点之间的距离不均匀。。。谁有好办法呢？</p>
<blockquote>
<p>However, there is a problem with this solution: the distance between the extracted points is not uniform. . . Who has a better solution?</p>
</blockquote>
<p>Such As Weighted when calculating the average?</p>
</blockquote>
</aside>
<blockquote>
<p>I want to weight the centroid obtained above by the reciprocal of voxel (CT value), how to do it?</p>
</blockquote>

---

## Post #9 by @jumbojing (2022-07-24 00:23 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">这个不完美<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b759b1b677f1693cf638d6b44d4e532ff6f39193.png" data-download-href="/uploads/short-url/q9ZxQRf8iFqBc18CP6nunXAgR6H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b759b1b677f1693cf638d6b44d4e532ff6f39193_2_690x412.png" alt="image" data-base62-sha1="q9ZxQRf8iFqBc18CP6nunXAgR6H" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b759b1b677f1693cf638d6b44d4e532ff6f39193_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b759b1b677f1693cf638d6b44d4e532ff6f39193.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b759b1b677f1693cf638d6b44d4e532ff6f39193.png 2x" data-dominant-color="989AD0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1025×613 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>完美截出轮廓，找到质心。。。</p>
<p>from<a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/699c9970f163a14c7289dd8c8a7aa8b7346969d3/BoneReconstructionPlanner/BRPLib/helperFunctions.py" rel="noopener nofollow ugc">helperFunctions.py</a></p>

---
