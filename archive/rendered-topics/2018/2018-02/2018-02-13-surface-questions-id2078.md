---
topic_id: 2078
title: "Surface Questions"
date: 2018-02-13
url: https://discourse.slicer.org/t/2078
---

# Surface questions

**Topic ID**: 2078
**Date**: 2018-02-13
**URL**: https://discourse.slicer.org/t/surface-questions/2078

---

## Post #1 by @brhoom (2018-02-13 13:53 UTC)

<p>Dear All<br>
I have a model (solid) and I would like to do following:</p>
<ul>
<li>Generate a surface from the model. I tried Sobel edges, modifying the model properties, somes extensions but the result are not the same as I get with Blender.</li>
<li>Display the triangulation Mesh as wireframe, where I can only see the edges and vertices.</li>
<li>Is it possible to produce all the triangles in the same size? if yes, how?</li>
</ul>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-02-13 14:17 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="1" data-topic="2078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>I have a model (solid)</p>
</blockquote>
</aside>
<p>Is it a polydata or an unstructured grid mesh?</p>
<aside class="quote no-group" data-username="brhoom" data-post="1" data-topic="2078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Sobel edges</p>
</blockquote>
</aside>
<p>Sobel operator is for image processing. It is not applicable to meshes.</p>
<aside class="quote no-group quote-modified" data-username="brhoom" data-post="1" data-topic="2078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Display the triangulation Mesh, where I can only see the edges and vertices</p>
</blockquote>
</aside>
<p>You can adjust model display options, including wireframe-style display in Models module Display section.</p>
<aside class="quote no-group" data-username="brhoom" data-post="1" data-topic="2078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Is it possible to produce all the triangles in the same size? if yes, how?</p>
</blockquote>
</aside>
<p>If you generate model from image and disable decimation then size of triangles in your mesh should be very similar.</p>

---

## Post #3 by @brhoom (2018-02-13 14:34 UTC)

<blockquote>
<p>Is it a polydata or an unstructured grid mesh?<br>
Sobel operator is for image processing. It is not applicable to meshes.</p>
</blockquote>
<p>I generated the model from a label-map and saved it as stl file I guess it is polydata). I used Sobel Edges on the label map image (sorry for not explaining).</p>
<blockquote>
<p>You can adjust model display options, including wireframe-style display in Models module Display section.</p>
</blockquote>
<p>Thanks for the info. I can display wire-frame now.</p>
<blockquote>
<p>If you generate model from image and disable decimation then size of triangles in your mesh should be very similar.</p>
</blockquote>
<p>I used the default options, so i guess zero means disable:<br>
compute surface normals =1<br>
decimation factor =   0<br>
smoothing factor =1</p>
<p>I also tried different number but I keep getting some triangles that are very large comparing to the others.</p>

---

## Post #4 by @lassoan (2018-02-13 15:15 UTC)

<p>Yes, decimation = 0 disables decimation. You may also try disabling or decreasing smoothing factor. If you still not get what you need then post a screenshot so that we can have a look.</p>

---

## Post #5 by @brhoom (2018-02-13 22:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="2078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>decreasing</p>
</blockquote>
</aside>
<p>Thanks for your concern. I did as you said, here as a sample <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97170c64986c2d43415f5577d112dcbea9314e34.png" data-download-href="/uploads/short-url/lyBtHnSLQqnmX5kPdXCCxzoceVK.png?dl=1" title="Sample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97170c64986c2d43415f5577d112dcbea9314e34.png" alt="Sample" data-base62-sha1="lyBtHnSLQqnmX5kPdXCCxzoceVK" width="690" height="426" data-dominant-color="676768"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sample</span><span class="informations">894×552 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-02-13 23:30 UTC)

<p>This seems to be a very nicely triangulated surface. To make triangles less elongated, you can resample your input volume to have cubic shaped voxels, by checking <code>Isotropic spacing</code> checkbox in <code>Crop volume module</code> when you crop/resample your original volume to prepare it for segmentation.</p>

---

## Post #7 by @brhoom (2018-02-14 07:27 UTC)

<p>Thanks for the feedback. I will try the resampling idea.</p>

---

## Post #8 by @brhoom (2018-02-15 21:02 UTC)

<p>Resampling was a helpful idea, thanks a lot. . I have two more questions:</p>
<ul>
<li>Is it possible to control the number of these equal triangles?</li>
<li>Is the triangulation applied only on the surface or it produces tetrahedrons as well?</li>
</ul>
<p>I found out these tools and they are very useful:</p>
<ul>
<li><a href="https://github.com/wjakob/instant-meshes" rel="nofollow noopener">https://github.com/wjakob/instant-meshes</a></li>
<li><a href="https://github.com/gaoxifeng/robust_hex_dominant_meshing" rel="nofollow noopener">https://github.com/gaoxifeng/robust_hex_dominant_meshing</a></li>
</ul>
<p>If you think they are better than the one in slicer, it would be a good idea to integrate this work in slicer. I am planning to integrate them as a slicer extension in the upcoming weeks (if someone is not done this before).<br>
Best!<br>
Ibraheem</p>

---

## Post #9 by @lassoan (2018-02-15 21:17 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="8" data-topic="2078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Is it possible to control the number of these equal triangles?</p>
</blockquote>
</aside>
<p>Triangle size is determined by the input volume’s resolution. You can decrease the number of triangles in flat regions by replacing them by larger ones by using decimation option (you specify the fraction of points that should be removed, so decimation factor of 0.9 means that you remove 90% of the triangles).</p>
<aside class="quote no-group" data-username="brhoom" data-post="8" data-topic="2078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Is the triangulation applied only on the surface or it produces tetrahedrons as well?</p>
</blockquote>
</aside>
<p>Segmentation generates a surface mesh. To generate volumetric mesh, you can use <a href="https://github.com/lassoan/SlicerSegmentMesher">SegmentMesher extension</a>. SegmentMesher uses Cleaver2 or Tetgen meshers internally, which are well-established algorithms.</p>
<p>instant-meshes and robust_hex_dominant_meshing methods seem to be for remeshing of existing surface mesh to improve mesh quality. I don’t think they are relevant for us, as from images we can always generate high-quality meshes that contains triangles with equal size with a nice aspect ratio.</p>

---

## Post #10 by @brhoom (2018-02-15 21:46 UTC)

<p>Thanks for the feedback. I will try your suggestions.</p>

---
