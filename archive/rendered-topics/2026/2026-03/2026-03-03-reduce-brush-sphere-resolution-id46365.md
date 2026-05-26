---
topic_id: 46365
title: "Reduce brush sphere resolution"
date: 2026-03-03
url: https://discourse.slicer.org/t/46365
last_bumped: 2026-03-12T07:29:48.358Z
---

# Reduce brush sphere resolution

**Topic ID**: 46365
**Date**: 2026-03-03
**URL**: https://discourse.slicer.org/t/reduce-brush-sphere-resolution/46365

---

## Post #1 by @SANTIAGO_PENDON_MING (2026-03-03 08:00 UTC)

<p>The goal is to reduce the resolution of the Sphere Brush (i.e., make it more polyhedral).</p>
<p>I assume this can be controlled through one or more parameters in the scripted module, but I have not found any settings related to this.</p>
<p>I would like to do this because when I increase or decrease the brush sphere radius, my PC takes 2–3 seconds to render the updated sphere, which is quite annoying.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36f6a5d1b0487710b46993d793c8dc044b070f3e.jpeg" data-download-href="/uploads/short-url/7QedS1ebn0dzhZ1vds21LuIitWe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f6a5d1b0487710b46993d793c8dc044b070f3e_2_690x406.jpeg" alt="image" data-base62-sha1="7QedS1ebn0dzhZ1vds21LuIitWe" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f6a5d1b0487710b46993d793c8dc044b070f3e_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f6a5d1b0487710b46993d793c8dc044b070f3e_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36f6a5d1b0487710b46993d793c8dc044b070f3e_2_1380x812.jpeg 2x" data-dominant-color="8A696A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1910×1124 385 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @drnoorfatima (2026-03-06 11:03 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="46365">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>The goal is to reduce the resolution of the Sphere Brush (i.e., make it more polyhedral).</p>
<p>I assume this can be controlled through one or more parameters in the scripted module, but I have not found any settings related to this.</p>
<p>I would like to do this because when I increase or decrease the brush sphere radius, my PC takes 2–3 seconds to render the updated sphere, which is quite annoying.</p>
</blockquote>
</aside>
<p>This is controlled by the <code>vtkSphereSource</code> resolution inside the Paint effect pipeline. There is no GUI for it but it is accessible via Python console in one block. The exact attribute path for <code>brushActor</code> can vary slightly between Slicer 5.x versions. If <code>effect.brushActor</code> throws an attribute error, the pipeline needs to be accessed slightly differently depending on your build.</p>
<p>Functionally this changes nothing about how painting works, only how the cursor sphere renders. The 2 to 3 second lag should drop to near zero.</p>
<p>DM me if the attribute path does not resolve on your version, quick fix once I know your exact build.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2026-03-11 07:38 UTC)

<p>Absolutely concise answer, that’s what I need.</p>
<p>Thanks <a class="mention" href="/u/drnoorfatima">@drnoorfatima</a></p>

---

## Post #4 by @cpinter (2026-03-11 10:10 UTC)

<aside class="quote no-group" data-username="drnoorfatima" data-post="2" data-topic="46365">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/drnoorfatima/48/81980_2.png" class="avatar"> drnoorfatima:</div>
<blockquote>
<p>Functionally this changes nothing about how painting works, only how the cursor sphere renders. The 2 to 3 second lag should drop to near zero.</p>
</blockquote>
</aside>
<p>I disagree. I find it very unlikely that rendering a few hundred triangle sphere is what slows down the rendering. Also, the sphere resolution does not depend on its size, so the same number of triangles need to be rendered when it’s large. I find it more likely that painting the changes in the segmentation is what takes longer, and the shape of the brush will not help this issue. What would help this issue is to reduce the resolution of the labelmap in the segmentation.</p>

---

## Post #5 by @SANTIAGO_PENDON_MING (2026-03-11 10:13 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> , in my experience the lag appear when I scroll (shift+mouse wheel) to increase and reduce the ball size, not when I paint.</p>

---

## Post #6 by @cpinter (2026-03-11 10:14 UTC)

<p>I just confirmed that the sphere resolution is fix, see this code in the paint effect</p>
<pre><code class="lang-auto">    this-&gt;BrushSphereSource-&gt;SetRadius(diameterMm / 2.0);
    this-&gt;BrushSphereSource-&gt;SetPhiResolution(32);
    this-&gt;BrushSphereSource-&gt;SetThetaResolution(32);
</code></pre>
<p>At this point I have two suggestions:</p>
<ul>
<li>Use the latest Slicer</li>
<li>Send video if issue persists with new Slicer</li>
</ul>

---

## Post #7 by @SANTIAGO_PENDON_MING (2026-03-12 07:29 UTC)

<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/587a858996b05c856d2a9e97c90f3fce6f8c27fc.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fa9157be221b209122ea8bc8abaa010bcb6970d.jpeg" data-video-base62-sha1="cCIwacqgLt2Od5MM0LrixIInAUk.mp4">
  </div><p></p>
<p>Hi again, I share with you a video explaining the issue. This version is 5.8.1, but my coworkers with 5.10 has the same experience. The video shows that the tool is not used, I am only modifying the radius with shift+mouse wheel</p>

---
