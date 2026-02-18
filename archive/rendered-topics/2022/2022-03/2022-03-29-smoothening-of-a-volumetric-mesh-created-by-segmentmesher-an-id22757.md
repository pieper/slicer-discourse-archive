# Smoothening of a volumetric mesh created by SegmentMesher and changed by applying DVF

**Topic ID**: 22757
**Date**: 2022-03-29
**URL**: https://discourse.slicer.org/t/smoothening-of-a-volumetric-mesh-created-by-segmentmesher-and-changed-by-applying-dvf/22757

---

## Post #1 by @BraveDistribution (2022-03-29 20:03 UTC)

<p>Hello,</p>
<p>I face a problem that after transforming mesh created by SegmentMesher with transform obtained by elastix registration, mesh is heavily deformed and yielding weird outliers, see following image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a17d165a8a7132337111b20ca97e5c5f8411492.png" data-download-href="/uploads/short-url/60n5aXKADpkvvlFVnRyPtjvrUWK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a17d165a8a7132337111b20ca97e5c5f8411492_2_690x278.png" alt="image" data-base62-sha1="60n5aXKADpkvvlFVnRyPtjvrUWK" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a17d165a8a7132337111b20ca97e5c5f8411492_2_690x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a17d165a8a7132337111b20ca97e5c5f8411492.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a17d165a8a7132337111b20ca97e5c5f8411492.png 2x" data-dominant-color="9899A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">696×281 41.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The registration looks fine. I tried applying DVFs on a segmentation and the output was fine as well.</p>
<p>Atop of that, when loading the points with python I found also an outlier that is not shown on the visualisation itself but is located at following position:<br>
[852.7322, -1861.4615,  5814.2349] (far from the actual volume).</p>
<p>I was thinking that this could be fixed by some smoothing tools. Is there something that slicer can do about that? I found laplacian smoothing in surfacetoolbox but it unfortunately works only for surface volumes, not volumetric volumes.</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2022-03-31 13:17 UTC)

<p>To transform an image, you need the resampling transform (fixed to moving image), while to transform a mesh, you need the modeling transform (moving to fixed image, inverse of the resampling transform). Automatic image intensity based registration always computes the resampling transform. When you apply that to a mesh then Slicer automatically computes the modeling transform by inverting the resampling transform. However, if the resampling transform was very noisy or inconsistent (maps different regions into the same region) then the modeling transform computation is unstable.</p>
<p>Probably the simplest solution is to compute the modeling transform by image registration is to switch up the fixed and moving images. If you need to have a single transform that can be used for both images and meshes then you need to tune the registration parameters to get smooth, consistent transform as a result.</p>

---

## Post #3 by @BraveDistribution (2022-03-31 13:30 UTC)

<p>Dear Andras,</p>
<p>thank you for your help, I appreciate that.</p>
<p>If I am doing everything inside Slicer, the only thing that I need is to switch up the moving and fixed image in Elastix registration right?</p>
<p>What about the application of deformation fields, does the slicer know that we have modelling transform instead of resampling transform?</p>
<p>thanks again.</p>

---

## Post #4 by @lassoan (2022-03-31 14:00 UTC)

<aside class="quote no-group" data-username="BraveDistribution" data-post="3" data-topic="22757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bravedistribution/48/14564_2.png" class="avatar"> BraveDistribution:</div>
<blockquote>
<p>If I am doing everything inside Slicer, the only thing that I need is to switch up the moving and fixed image in Elastix registration right?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="BraveDistribution" data-post="3" data-topic="22757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bravedistribution/48/14564_2.png" class="avatar"> BraveDistribution:</div>
<blockquote>
<p>What about the application of deformation fields, does the slicer know that we have modelling transform instead of resampling transform?</p>
</blockquote>
</aside>
<p>Slicer keeps track of the transform direction: it stores either a <code>ToParent</code> or <code>FromParent</code> transform. You can see that in <code>Transforms</code> module’s <code>Information</code> section.</p>

---
