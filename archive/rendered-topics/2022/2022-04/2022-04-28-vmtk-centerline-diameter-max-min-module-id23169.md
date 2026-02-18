# VMTK centerline diameter max min module

**Topic ID**: 23169
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/vmtk-centerline-diameter-max-min-module/23169

---

## Post #1 by @Jacktat (2022-04-28 13:36 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/vmtk-centreline-and-metrics/12203">VMTK centreline and metrics</a>:</p>
<p>I actually precisely need this functionality, I have succesfully created a segmentation and a centerline. Now, I want to do a complete characterisation of the vessel’s diameter along the path. Meaning, I want to know the max, min, mean diameter of the vessel perpendicular to the centerline (exactly as indicated for 1 slice in the original post I linked). I was wondering if this module was ever made? I cannot find the function in the slicer.<br>
Thanks so much!</p>
<p>Cheers,<br>
Jack</p>

---

## Post #2 by @chir.set (2022-04-29 08:17 UTC)

<ol>
<li>
<p>Former modules ‘Centerline metrics’ and ‘Cross-section analysis’ have been merged in one single module ‘Cross-section analysis’, included in <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerVMTK extension</a>. You can install this extension with the '‘Extensions manager’ in Slicer. It is quite well <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md" rel="noopener nofollow ugc">documented</a>, though not completely up-to-date.</p>
</li>
<li>
<p>Line measurement in a single slice for minimum and maximum diameter has not been implemented. I don’t know in what field you require this data. In vascular surgery, this kind of measurement is meaningless. Lumen shapes are highly variable in diseased arteries, and not necessarily nicely drawn as in the picture. Instead, cross-section area determination and the circular equivalent diameter have been implemented in this module. This is more relevant to clinical reasoning. Line measurement in a single slice can theoretically be done though, from a pure technical point of view.</p>
</li>
<li>
<p>Avoid private messages for this kind of discussion. Your initial post was a few days ago, and replies on public forums can be delayed for many reasons.</p>
</li>
</ol>
<p>.</p>

---

## Post #3 by @chendong9416 (2022-11-26 05:49 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="23169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>In vascular surgery, this kind of measurement is meaningless.</p>
</blockquote>
</aside>
<p>Although this answer is posted a long-time age, i have to say that in vascular surgery, maximal diameter is of paramount important. In most cases, the indication for surgery is relay on the maximal diameter. Automatic calculation of the maximal diameter along the centerline could give us an exact value and avoid the lower reproductivity by manual measurement. Only in this way can we precisely select patients to treat,</p>

---

## Post #4 by @chir.set (2022-11-26 11:02 UTC)

<aside class="quote no-group" data-username="chendong9416" data-post="3" data-topic="23169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chendong9416:</div>
<blockquote>
<p>maximal diameter is of paramount important</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/chendong9416">@chendong9416</a> ,</p>
<p>I think the confusion lies on a single word : <em>along</em> a centerline, and <em>around</em> a centerline point.</p>
<aside class="quote no-group" data-username="chendong9416" data-post="3" data-topic="23169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chendong9416:</div>
<blockquote>
<p>calculation of the maximal diameter along the centerline</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Jacktat" data-post="1" data-topic="23169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a9a28c/48.png" class="avatar"> Jacktat:</div>
<blockquote>
<p>exactly as indicated for 1 slice</p>
</blockquote>
</aside>
<p>The original post <a href="/uploads/short-url/pCslRrDIxk77M7n2jzpW10ij03I.png">pictures</a> diameter variation on a single slice, that’s what <a class="mention" href="/u/jacktat">@Jacktat</a> specified as quoted above.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c191e2dcf37c61df22d968fc4014b50810fd155f.png" alt="single_slice" data-base62-sha1="rCoI71o36VjDhpfjPsXDLfK3WCr" width="498" height="500"></p>
<p>You can measure an infinite number of diameters on any single slice, and they will differ 1 mm further.</p>
<p>As per your quoted post, you seem to refer to diameters along the centerline. It’s obviously of paramount importance clinically.</p>
<p>If you meant on a single slice, the surface area of the lumen, and the derived circular equivalent diameter, sum up the diameter variation on each slice. This distribution is available with the ‘Cross-section analysis’ module.</p>
<p>As for exposing the diameter distribution around a centerline point, I don’t see it’s daily use. Moreover, it may not be feasible, as below :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c63da12a45207b51d3e8ba6cf81e65b75aea915.png" alt="irregular_stenosis" data-base62-sha1="k1WMcy5nuCGh4U4ReegC89I4xkV" width="474" height="500"></p>

---

## Post #5 by @chendong9416 (2022-11-27 03:47 UTC)

<p>Yes, i agree with you.</p>
<p>In clinical practice, the maximal diameter of the aorta is important, and we measure it from outer wall to outer wall.</p>
<p>I noticed that in cross-sectional analysis, we could get MIS or CE diameter, these two parameters are less useful in clinical practice or medical research.</p>
<p>Hope we could get the maximal diameter on each slice.</p>

---

## Post #6 by @chir.set (2022-11-27 08:51 UTC)

<p>Yes, measurement from wall to wall is important.</p>
<p>Caveat : the wall itself is not visible on CT scans, except in places where you have concentric calcifications.</p>
<p>A work is underway to allow <em>drawing</em> the arterial wall at best estimate. Emphasis : <em>drawing</em>, <em>estimate</em>. The observer draws the wall of the artery on reformatted slices, perpendicular to his estimate of the axis on multiple reformatted slices. He gets a <em>regular</em> tube of varying diameter. ‘<em>Regular</em>’ implies that this process is not suitable for aneurysms, barring very rarely seen short regular aneurysms.</p>
<p>It depends on these works :</p>
<ul>
<li>
<a href="https://github.com/chir-set/SlicerExtraMarkups" rel="noopener nofollow ugc">SlicerExtraMarkups</a> : in the process of being merged in the ‘<a href="https://github.com/Slicer/ExtensionsIndex" rel="noopener nofollow ugc">Extensions index</a>’ repository. It’s highly probable that it will be soon accepted.</li>
<li>Integrating the Shape markups node provided by SlicerExtraMarkups, as a Tube, with Cross-section analysis module : <a href="https://github.com/chir-set/SlicerExtension-VMTK/tree/WithWallSurface" rel="noopener nofollow ugc">this</a> work can only be proposed in SlicerVMTK when SlicerExtraMarkups would be generally available in the extensions index.</li>
</ul>
<p>You may still estimate the wall’s position at selected places using the Line markups node, also an observer dependent interaction.</p>

---
