---
topic_id: 24380
title: "How To Extract The Vertex Coordinates Of A Polygon Of A Mode"
date: 2022-07-19
url: https://discourse.slicer.org/t/24380
---

# How to extract the vertex coordinates of a polygon of a model in the current section?

**Topic ID**: 24380
**Date**: 2022-07-19
**URL**: https://discourse.slicer.org/t/how-to-extract-the-vertex-coordinates-of-a-polygon-of-a-model-in-the-current-section/24380

---

## Post #1 by @jumbojing (2022-07-19 01:32 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="6" data-topic="24339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"><a href="https://discourse.slicer.org/t/howto-get-a-centroid-of-a-section-in-a-slice/24339/6">Howto get a centroid of a section in a slice?</a></div>
<blockquote>
<p>the current question now becomes how to extract the vertex coordinates of a polygon of the current section. . .</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f686d7554d6785d2dcfff1c76c2dd5743361c2e3.png" data-download-href="/uploads/short-url/zaSlV3lzIlCcNKfkiz9mNkBcAYr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f686d7554d6785d2dcfff1c76c2dd5743361c2e3_2_609x500.png" alt="image" data-base62-sha1="zaSlV3lzIlCcNKfkiz9mNkBcAYr" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f686d7554d6785d2dcfff1c76c2dd5743361c2e3_2_609x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f686d7554d6785d2dcfff1c76c2dd5743361c2e3_2_913x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f686d7554d6785d2dcfff1c76c2dd5743361c2e3_2_1218x1000.png 2x" data-dominant-color="6F707B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1686×1384 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to extract the vertex coordinates of a polygon of the model (blue) in the current slice…</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@pieper@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @lassoan (2022-07-19 07:18 UTC)

<p>You might be able to get the slice intersection actor from the model slice displayable manager, but most probably you need to use a VTK plane cut filter and set the slice as input cut plane and the model’s polydata as input polydata.</p>
<p>Note that center of gravity of the circumference points is not the same as the center of gravity of the cross-section of the object.</p>

---

## Post #3 by @jumbojing (2022-07-19 16:47 UTC)

<p>Lassoan教授，好吧。。。我想出来个笨拙的解决方案：</p>
<blockquote>
<p>Prof.Lassoan, okay.  .  .  I came up with a clumsy solution:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458.jpeg" data-download-href="/uploads/short-url/bjm1QYDHqJB7R8EHp6wlWpFiAc0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_454x500.jpeg" alt="image" data-base62-sha1="bjm1QYDHqJB7R8EHp6wlWpFiAc0" width="454" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_454x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_681x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f4806076a2457dc66b6bbecbdf3b6bc7445f458_2_908x1000.jpeg 2x" data-dominant-color="8C858E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">994×1094 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p>不过这个解决方案有个问题：就是提取的点和点之间的距离不均匀。。。谁有好办法呢？</p>
<blockquote>
<p>However, there is a problem with this solution: the distance between the extracted points is not uniform.  .  .  Who has a better solution?</p>
</blockquote>
<p>Such As Weighted when calculating the average?</p>

---
