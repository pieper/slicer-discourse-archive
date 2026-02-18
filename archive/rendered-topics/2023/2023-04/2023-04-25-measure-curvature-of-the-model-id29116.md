# Measure curvature of the model

**Topic ID**: 29116
**Date**: 2023-04-25
**URL**: https://discourse.slicer.org/t/measure-curvature-of-the-model/29116

---

## Post #1 by @sridhar (2023-04-25 12:00 UTC)

<p>Hello,<br>
I was hoping I could get some help/ideas on how I can get a measure of the curvature of the model (curvature of insect cornea to be exact). In my project, I am interested in quantifying the curvature of the cornea (i.e. how curved or flat the cornea is) across different species which can affect several properties of the vision (please see the attached image). The image depicted here is the surface cut (after placing the closed curve) from the whole insect head. Is there any way I can do this in Slicer? I have &gt;400 such models from which I would get a measure of the curvature of the eye.<br>
Apologies if I missed any relevant posts.<br>
Thank you very much for your help!<br>
Sridhar</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff74761d464296691ca17b92e45aa5aff45c0e88.png" data-download-href="/uploads/short-url/ArRgSPIpNfeqSbVRbayRx1ayOr6.png?dl=1" title="Eye surface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff74761d464296691ca17b92e45aa5aff45c0e88_2_690x444.png" alt="Eye surface" data-base62-sha1="ArRgSPIpNfeqSbVRbayRx1ayOr6" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff74761d464296691ca17b92e45aa5aff45c0e88_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff74761d464296691ca17b92e45aa5aff45c0e88_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff74761d464296691ca17b92e45aa5aff45c0e88_2_1380x888.png 2x" data-dominant-color="9A98CB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Eye surface</span><span class="informations">3608×2322 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @RafaelPalomar (2023-04-25 13:12 UTC)

<p>There’s probably more than one way to go about this.</p>
<p>Assuming that you have your data-set of cut surfaces already (i.e., a folder with the models), you could make a 3D Slicer scripted module that batch processes (loads, process, unload) all the models and get you the curvature statistics as a .csv file. Sometime ago I followed this approach to do bulk labelmap statistics on entire datasets (<a href="https://github.com/RafaelPalomar/BulkLabelStatistics" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RafaelPalomar/BulkLabelStatistics: Module to compute labelmap statistics in bulk</a>) maybe you can use it as inspiration.</p>
<p>When it comes to curvature estimation, you can use the class <code>vtkCurvatures</code>, which can give you Gaussian, Mean, Max and min curvature (<a href="https://vtk.org/doc/nightly/html/classvtkCurvatures.html" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkCurvatures.html</a>). This should be exposed in Slicer as part of VTK.</p>

---

## Post #3 by @lassoan (2023-04-25 14:06 UTC)

<p>vtkCurvatures can compute local curvature at each point, but probably in this case a description of the overall shape is needed. That could be achieved by fitting a sphere, ellipsoid, or some other shape model to the model points.</p>

---

## Post #4 by @sridhar (2023-04-25 14:23 UTC)

<p>Hi Rafael and Andras,<br>
Thank you very much for your quick replies. I am a complete newbie in Python and I was hoping you could demonstrate how these measures could be obtained, for example in Slicer, for just one model. But I am assuming (based on Andras’s reply) I do not necessarily need Slicer for measuring the curvature of the model.<br>
Thank you,<br>
Sridhar</p>

---

## Post #5 by @lassoan (2023-04-26 03:10 UTC)

<p>First of all, you need to decide what kind of curvature you want to compute. Local surface curvature is good for quantifying surface roughness or other small localized variations in the surface. Global curvature can characterize the overall shape. If your assumption is that a sphere is a good enough approximation of the eye shape then you can fit a sphere or ellipsoid to the surface points and get the curvature value from the radii. However, most likely you would get a more accurate and informative characterization of the eye shape if you fit a more sophisticated shape model. Check out SlicerMorph and SlicerSalt shape analysis extensions for more details.</p>

---

## Post #6 by @sridhar (2023-04-26 07:54 UTC)

<p>Thank you, Andras! I am interested in quantifying the global curvature of the eye (across multiple individuals and species). I thought, for starters, this could give me a rough idea about the extent of eye curvature across species (I do hope to analyze shape variation using landmarks in the future). I believe an ellipsoid would be a good approximation of the eye shape/curvature. I had a look at what is available in SlicerMorph. The PseudoLmGenerator module in SlicerMorph does allow fitting a spheroid or an ellipsoid but I do not get any measure of curvature (I hope I am not missing something obvious). I believe this is more for acquiring landmarks. <a class="mention" href="/u/muratmaga">@muratmaga</a> do you have any suggestions?</p>

---

## Post #7 by @lassoan (2023-05-02 19:37 UTC)

<p>Curvature is 1/radius, so if you know the radius then you know the curvature.</p>

---

## Post #8 by @sridhar (2023-05-04 06:39 UTC)

<p>Thank you, I’ll explore some options!</p>

---

## Post #9 by @sridhar (2023-05-04 12:25 UTC)

<p>It seems like the Segment Statistics module computes several metrics (Feret diameter, roundness, flatness, elongation) and these are exactly the measurements I am looking for. But I converted my model back to segmentation for the Segment Statistics module to work. I also noticed that the surface area of this segmentation is overestimated compared to the surface area of the model. Do you know why is this the case and if I can use this pipeline to get some basic estimates of the shape? Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db823d4380de1937a8c5cee4e821864662016881.png" data-download-href="/uploads/short-url/vjRBlStCKzHMwc0gGk3PtRaHwDD.png?dl=1" title="eye_segment_stats" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db823d4380de1937a8c5cee4e821864662016881_2_690x488.png" alt="eye_segment_stats" data-base62-sha1="vjRBlStCKzHMwc0gGk3PtRaHwDD" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db823d4380de1937a8c5cee4e821864662016881_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db823d4380de1937a8c5cee4e821864662016881_2_1035x732.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db823d4380de1937a8c5cee4e821864662016881_2_1380x976.png 2x" data-dominant-color="4D4D4D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">eye_segment_stats</span><span class="informations">3090×2188 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @Slogish (2024-03-31 16:37 UTC)

<p>Hello!Lasso.<br>
Curvature is 1/radius.I would like to konw what is the radius of the Osculating circle in 3dSlicer.1mm or the distance of two control points?</p>

---

## Post #11 by @lassoan (2024-03-31 19:32 UTC)

<aside class="quote no-group" data-username="sridhar" data-post="9" data-topic="29116">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9fc29f/48.png" class="avatar"> sridhar:</div>
<blockquote>
<p>I also noticed that the surface area of this segmentation is overestimated compared to the surface area of the model</p>
</blockquote>
</aside>
<p>The surface measurement is not overestimated, but you get larger surface area value for the segmentation because it is a different mesh. Segmentation is always a closed surface, so when you import an open surface into a segmentation then a surface patch is added that closes the surface.</p>
<aside class="quote no-group" data-username="Slogish" data-post="10" data-topic="29116">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slogish/48/69830_2.png" class="avatar"> Slogish:</div>
<blockquote>
<p>Curvature is 1/radius.I would like to konw what is the radius of the Osculating circle in 3dSlicer.1mm or the distance of two control points?</p>
</blockquote>
</aside>
<p>This question is not related to models. Models have no control points and in general curvature of a 3D surface cannot be defined by a 2D circle. Please post your question in a new topic.</p>

---
