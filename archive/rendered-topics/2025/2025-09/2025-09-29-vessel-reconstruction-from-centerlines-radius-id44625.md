---
topic_id: 44625
title: "Vessel Reconstruction From Centerlines Radius"
date: 2025-09-29
url: https://discourse.slicer.org/t/44625
---

# Vessel reconstruction from centerlines/radius

**Topic ID**: 44625
**Date**: 2025-09-29
**URL**: https://discourse.slicer.org/t/vessel-reconstruction-from-centerlines-radius/44625

---

## Post #1 by @gred (2025-09-29 17:27 UTC)

<p>Hello everyone,</p>
<p>I am working on segmenting small cerebral arteries for future CFD studies.</p>
<p>After segmenting the small arteries that interest me, I am looking for a way to reconstruct an ideal (cylindrical) geometry from the average radius obtained for each segment/centerline with a smoothed intersection (blending type).</p>
<p>I have tried to create cylinders around each centerline with VTK librairy, but the intersections between cylinders are bad.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8d8552c733ded3c7e85e663655291c91a889cc5.png" data-download-href="/uploads/short-url/qndlp9Y2cBYc2RhbCCretksqSpL.png?dl=1" title="topic_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d8552c733ded3c7e85e663655291c91a889cc5_2_690x407.png" alt="topic_1" data-base62-sha1="qndlp9Y2cBYc2RhbCCretksqSpL" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d8552c733ded3c7e85e663655291c91a889cc5_2_690x407.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d8552c733ded3c7e85e663655291c91a889cc5_2_1035x610.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8d8552c733ded3c7e85e663655291c91a889cc5.png 2x" data-dominant-color="64645C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">topic_1</span><span class="informations">1140×674 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a method already implemented in 3D Slicer that could address this?</p>
<p>Thank you very much.</p>
<p>Gred</p>

---

## Post #2 by @pieper (2025-09-29 17:40 UTC)

<p>I’d suggest making a distance transform from the centerlines and then thresholding that to make the surface.</p>

---

## Post #3 by @mau_igna_06 (2025-09-30 14:58 UTC)

<p>Hi, there is a vtk filter that should help a bit in this situation:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://vtk.org/doc/nightly/html/classvtkTubeBender.html#details">
  <header class="source">
      <img src="https://vtk.org/doc/nightly/html/vtk_favicon.png" class="site-icon" alt="" width="16" height="16">

      <a href="https://vtk.org/doc/nightly/html/classvtkTubeBender.html#details" target="_blank" rel="noopener nofollow ugc">vtk.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://vtk.org/doc/nightly/html/classvtkTubeBender.html#details" target="_blank" rel="noopener nofollow ugc">VTK: vtkTubeBender Class Reference</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @gred (2025-09-30 15:36 UTC)

<p>Hi Pieper, by making a distance transform from the centerlines, do you mean somethink like polyball modelling along the centerlines and get the isosurface?</p>

---

## Post #5 by @pieper (2025-09-30 17:56 UTC)

<p>I’ve never used the polyball feature of vmtk, but maybe it would work.  I was thinking you can just fill a volume with the distance to the closest vessel segment and threshold that.  There are probably many ways of doing this depending on how efficient you need it to be.</p>

---

## Post #6 by @eNable_Polska (2025-10-02 18:04 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="44625">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>thresholding</p>
</blockquote>
</aside>
<p>Could you describe in more detail what you mean by “thresholding”? Perhaps a use case? I don’t quite understand what you mean, and I have a similar problem to the thread’s creator.</p>

---

## Post #7 by @pieper (2025-10-02 18:45 UTC)

<p>I mean using the threshold tool in the segment editor.  Or for creating a mesh from a distance transform you could use the GrayscaleModelMaker directly.  Just set a threshold for the isosurface distance you want.</p>

---

## Post #8 by @gred (2025-10-02 20:46 UTC)

<p>I’m still stuck on 3D reconstruction with smoothing and physiological connections. I’ll take a look at greyscalemodel.</p>
<p>If you have any other ideas, please feel free to share them.</p>
<p>Thank you very much for your feedback.</p>

---

## Post #9 by @gred (2025-10-13 14:23 UTC)

<p>Hello there,</p>
<p>I have finaly managed to obtain what I wanted by doing the following:</p>
<ol>
<li>creating cylinders around each centerline curve with a mean radius taken from the centerline quantification table</li>
<li>converting to segment node and fill holes</li>
<li>Finally converting it to model.</li>
</ol>
<p>It is not the best and most obvious way to do it but the result is great.</p>

---
