---
topic_id: 21309
title: "Models Always Shaded Flat Regardless Of Interpolation"
date: 2022-01-02
url: https://discourse.slicer.org/t/21309
---

# Models always shaded flat regardless of interpolation

**Topic ID**: 21309
**Date**: 2022-01-02
**URL**: https://discourse.slicer.org/t/models-always-shaded-flat-regardless-of-interpolation/21309

---

## Post #1 by @hherhold (2022-01-02 14:01 UTC)

<p>This is quite possibly a misunderstanding on my part. It looks like models are always shaded with flat polygons, and the interpolation setting has no effect. Regardless of the setting (Flat, Phong, Gouraud), all polygons are flat (see image below). This is using the “Lights” module, set to Default lighting. Shouldn’t Phong or Gouraud interpolation result in a less “faceted” appearance or am I mis-remembering how these work?</p>
<p>Thanks!!!</p>
<p>-Hollister</p>
<p>Preview 2021-12-19, MacOS, MBP 16" AMD Radeon Pro 5500M 8 GB.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b95f6b50fe7810b3a489a7a35e5141fc0337cc04.jpeg" data-download-href="/uploads/short-url/qrSLxkGHPAsXev13jwtVOnT706U.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b95f6b50fe7810b3a489a7a35e5141fc0337cc04_2_572x499.jpeg" alt="image" data-base62-sha1="qrSLxkGHPAsXev13jwtVOnT706U" width="572" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b95f6b50fe7810b3a489a7a35e5141fc0337cc04_2_572x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b95f6b50fe7810b3a489a7a35e5141fc0337cc04_2_858x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b95f6b50fe7810b3a489a7a35e5141fc0337cc04_2_1144x998.jpeg 2x" data-dominant-color="A39007"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1292×1128 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-01-02 14:44 UTC)

<p>Sharing requires surface normals. They can be computed in Surface Toolbox module.</p>
<p>Moat mesh file formats allow storage of surface normals. What file format are you reading your model from? What software has created the file?</p>

---

## Post #3 by @hherhold (2022-01-02 15:39 UTC)

<p>It’s a segment converted to a model in Slicer. I computed surface normals in Surface Toolbox and it shades smoothly now - thanks!</p>
<p>I was a little confused because Gouraud shading doesn’t require normals (but Phong does). Anyway, thanks for the help!!</p>
<p>-Hollister</p>

---

## Post #4 by @pieper (2022-01-02 16:20 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="21309">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Gouraud shading doesn’t require normals (but Phong does).</p>
</blockquote>
</aside>
<p>To clarify, Gouraud shading uses normals at the vertices to calculate lighting and then interpolates the colors across the triangle, Phong shading interpolates the normals and recalculates the lighting per-fragment across the triangle.  So both require vertex normals.  STL format, for example, does not save normals, so they need to be re-calculated for smooth rendeing.</p>

---

## Post #5 by @lassoan (2022-01-02 16:21 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="21309">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>It’s a segment converted to a model in Slicer</p>
</blockquote>
</aside>
<p>In current Slicer versions, surface normal computation is enabled by default, but you can enable/disable it by adjusting segmentation representation conversion parameters:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d7c357a41044479d2832d03995ff8cdb32c126a.png" data-download-href="/uploads/short-url/mtb4UqetJeMLobRfWVNvWkRslSi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7c357a41044479d2832d03995ff8cdb32c126a_2_574x500.png" alt="image" data-base62-sha1="mtb4UqetJeMLobRfWVNvWkRslSi" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7c357a41044479d2832d03995ff8cdb32c126a_2_574x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7c357a41044479d2832d03995ff8cdb32c126a_2_861x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d7c357a41044479d2832d03995ff8cdb32c126a_2_1148x1000.png 2x" data-dominant-color="ECEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1601×1394 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @hherhold (2022-01-02 16:22 UTC)

<p>Got it, ok. I thought Gouraud interpolated vertex colors across the polygon and didn’t use normals.</p>
<p>My undergrad computer graphics class was an embarrassingly long time ago.</p>

---

## Post #7 by @hherhold (2022-01-02 16:23 UTC)

<p>Ah, okay - Thanks, Andras!</p>

---

## Post #8 by @hherhold (2022-02-27 20:49 UTC)

<p>Hi Andras <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Quick follow-up to this. It seems whenever I save models as PLY, even if I’ve computed surface normals before saving, when I reload the model files, the normals have been lost. Does Slicer save surface normals in PLY files?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #9 by @lassoan (2022-02-27 23:41 UTC)

<p>VTK’s PLY reader reads point normals, but VTK’s PLY file <em>writer</em> does not write them.</p>
<p>I’ve submitted a merge request to VTK to add this feature:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8940">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8940" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" width="146" height="146">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8940" target="_blank" rel="noopener">Make vtkPLYWriter able to write point normals (!8940) · Merge requests · VTK...</a></h3>

  <p>For complex surfaces it is not always trivial to compute the surface normals, so it is useful to store the normals in the mesh. PLY file format can...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Probably it can get into VTK in a couple of days, but I’m not sure when we’ll update Slicer’s VTK to include this update. If it is urgent then we can cherry-pick this feature (and then it’ll be available in the Slicer Preview Release the next day), otherwise it’ll be available in Slicer in a few months.</p>

---

## Post #10 by @hherhold (2022-02-28 03:01 UTC)

<p>Hey Andras,</p>
<p>Thanks! No, not urgent at all. Just wanted to make sure it wasn’t something I was doing wrong.</p>
<p>-Hollister</p>

---

## Post #11 by @hherhold (2022-03-13 14:57 UTC)

<p>Hi Andras <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>If I wanted to do a local build that would incorporate the VTK version with this change, how do I go about that? I tried changing _git_tag in External_VTK.cmake to the latest SHA but I get the following error (Windows):</p>
<pre><code class="lang-auto">  Performing update step for 'VTK'
  fatal: reference is not a tree: 21f9d5e14a695d9fc387aee86b28c36bbe19fdb5
  CMake Error at D:/S/S4D/VTK-prefix/tmp/VTK-gitupdate.cmake:175 (execute_process):
    execute_process failed command indexes:
</code></pre>

---

## Post #12 by @lassoan (2022-03-13 15:59 UTC)

<p>The latest master VTK version does not contain some of the fixes that Slicer needs, so you need to backport the PBR fix into Slicer’s VTK. I’ll try to do this for the official Slicer release today or tomorrow.</p>

---

## Post #13 by @hherhold (2022-03-13 16:03 UTC)

<p>If it’s too much trouble, this is not a critical need - I can work around by using Surface Toolbox to recompute normals when I reload PLY models.</p>

---

## Post #14 by @lassoan (2022-03-14 02:33 UTC)

<p>I’ve just checked and latest Slicer Preview Release already includes the fix for writing of PLY normals.</p>

---

## Post #15 by @hherhold (2022-03-14 11:04 UTC)

<p>Oh, great! Thanks!</p>
<p>This is what I get for being a few weeks behind in preview releases…</p>

---
