# Radius Extraction from centerline

**Topic ID**: 34066
**Date**: 2024-01-31
**URL**: https://discourse.slicer.org/t/radius-extraction-from-centerline/34066

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-01-31 13:38 UTC)

<p>Hi to everyone. I’m working with centerlines, which I made with a external python code. From this code I return the centerlines as Markups nodes, and now I would like to extract radius info. For this purpose I use  the Cross Section Analysis. This module works well more of the times but fails in bifurcations, where minimum sphere and cross section methods can’t find the proper area…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a2da0104076ae489089376c5fe7f3409255a31.png" data-download-href="/uploads/short-url/gm7l390sCMpBVkwZ0pXrJ6hkBhf.png?dl=1" title="Captura de pantalla 2024-01-31 142751" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72a2da0104076ae489089376c5fe7f3409255a31_2_367x500.png" alt="Captura de pantalla 2024-01-31 142751" data-base62-sha1="gm7l390sCMpBVkwZ0pXrJ6hkBhf" width="367" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72a2da0104076ae489089376c5fe7f3409255a31_2_367x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72a2da0104076ae489089376c5fe7f3409255a31_2_550x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a2da0104076ae489089376c5fe7f3409255a31.png 2x" data-dominant-color="4C524D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-01-31 142751</span><span class="informations">649×883 314 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I noticed that centerlines made with Extract Centerlines module can give radius data when you use the centerline model (see code). I know that Extract Centerlines workflow is based on Voronoi Diagrams, but the radius extraction is better than Cross Section Analysis?</p>
<pre><code class="lang-auto">&gt;&gt;&gt; c = getNode('Centerline model')
&gt;&gt;&gt; points = slicer.util.arrayFromModelPoints(c)
&gt;&gt;&gt; radii = slicer.util.arrayFromModelPointData(c, 'Radius')
</code></pre>
<p>In that case, could I use my centerlines with the same code?</p>
<p>If there is no solution for this, you have any idea to perform radius extraction in bifurcations ?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @chir.set (2024-01-31 14:05 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="34066">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>bifurcations</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="34066">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>the proper area</p>
</blockquote>
</aside>
<p>Can you draw by hand or with a mouse a bifurcation to illustrate what you mean by ‘proper area’, from which point or circumference to which point or circumference you idealize measurements in a bifurcation?</p>
<p>The minimum sphere radius is more accurate in a bifurcation than the circular-equivalent diameter since the latter is derived from a surface area. This area will include all branches in a bifurcation. You could cut the segment so as to isolate single tubes of interest and regenerate everything.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2024-01-31 14:40 UTC)

<p>Hi Chir.set, thanks for your help. The goals is :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cf4099ae35697a9286e682f0ffc3eb68bebe495.png" alt="Captura de pantalla 2024-01-31 153037" data-base62-sha1="1QAzOmZH9S5YG6kggx4yCO1e2zP" width="137" height="352"></p>
<p>Where clearly both structures are well defined.</p>
<p>At this moment, I’m using the CSA process and then correct the radius for nodes in bifurcation zones using MIS by myself.¡, but this work well. MIS strategy used is:</p>
<p>Create a sphere with radius closer to zero and start increasing the radius until the sphere contains at least 30-40 edges of the segmentation…</p>
<p>Did you see any inconvenience on this procedure?</p>
<p>Is there any other way to attack this problem?</p>

---

## Post #4 by @chir.set (2024-01-31 14:59 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="3" data-topic="34066">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>start increasing the radius until the sphere contains at least 30-40 edges of the segmentation…</p>
<p>Did you see any inconvenience on this procedure?</p>
</blockquote>
</aside>
<p>I can’t really have an authoritative opinion on the matter.</p>
<p>According to the above image: you might process your bifurcated centerline model with the ‘Centerline disassembly’ module in SlicerVMTK. You can thus get a complete centerline model from the first endpoint to each other endpoint, when selecting the ‘Centerlines’ component in the UI.</p>
<p>Each new centerline model will have a ‘Radius array’, which is the MIS radius. This may help you generate the tubes you are pointing to, probably using vtkTubeFilter.</p>

---

## Post #5 by @SANTIAGO_PENDON_MING (2024-01-31 15:10 UTC)

<p>Okay, but MIS would fail when the segment surface is non-smooth or has any stenosis…</p>
<p>Anyway, thanks for your help!</p>

---
