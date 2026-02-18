# Smooth Mesh? Comparison to MATLAB

**Topic ID**: 19616
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/smooth-mesh-comparison-to-matlab/19616

---

## Post #1 by @JoJo (2021-09-10 18:55 UTC)

<p>Hello,<br>
for my bachelor thesis I segmented a bone out CT volume data via MATLAB and exported it with stlwrite. For a comparison I’ve used 3D Slicer too. Now I noticed that the 3D-Slicer mesh is much more smoother than the mesh I’ve created with MATLAB (very pixelized). Now my question: Is there any algorithm in 3D Slicer which causes the smooth surface? Because the original volume data have the same resolution…</p>

---

## Post #2 by @hherhold (2021-09-10 19:02 UTC)

<p>Smoothing may have been enabled in Segment Editor (see pic). You can adjust the amount of smoothing, or turn it off entirely.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfb23129a9a9df2a5bb37f34d7f80ed43f3e8e87.png" data-download-href="/uploads/short-url/tDmBSXBucxu9p1e3XgNe7BcR2dx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfb23129a9a9df2a5bb37f34d7f80ed43f3e8e87_2_690x249.png" alt="image" data-base62-sha1="tDmBSXBucxu9p1e3XgNe7BcR2dx" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfb23129a9a9df2a5bb37f34d7f80ed43f3e8e87_2_690x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfb23129a9a9df2a5bb37f34d7f80ed43f3e8e87.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfb23129a9a9df2a5bb37f34d7f80ed43f3e8e87.png 2x" data-dominant-color="48525A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×290 37.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @hherhold (2021-09-10 19:02 UTC)

<p>Oh yeah, note that the default smoothing is (I think) 0.5.</p>

---
