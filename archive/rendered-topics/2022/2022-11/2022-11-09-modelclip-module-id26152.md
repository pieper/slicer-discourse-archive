---
topic_id: 26152
title: "Modelclip Module"
date: 2022-11-09
url: https://discourse.slicer.org/t/26152
---

# ModelClip module

**Topic ID**: 26152
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/modelclip-module/26152

---

## Post #1 by @miniminic (2022-11-09 02:37 UTC)

<p>I clipped a model with ModelClip module, but the volume of the generated models is very different from the original model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a0e435ac2d082fd3acb815eec27a9d05eb4a4aa.jpeg" data-download-href="/uploads/short-url/3IuYjpaA7NtKDINmvIlMuVIaQ8q.jpeg?dl=1" title="屏幕截图 2022-11-09 103701" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a0e435ac2d082fd3acb815eec27a9d05eb4a4aa_2_690x345.jpeg" alt="屏幕截图 2022-11-09 103701" data-base62-sha1="3IuYjpaA7NtKDINmvIlMuVIaQ8q" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a0e435ac2d082fd3acb815eec27a9d05eb4a4aa_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a0e435ac2d082fd3acb815eec27a9d05eb4a4aa.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a0e435ac2d082fd3acb815eec27a9d05eb4a4aa.jpeg 2x" data-dominant-color="393838"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-11-09 103701</span><span class="informations">968×484 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-12-01 07:37 UTC)

<p>Volume of an open surface (cut without closing the surface) is undefined.</p>
<p>Try to use the “Dynamic modeler” module’s Plane cut tool, with “Cap surface” option enabled to see if you get more consistent results.</p>

---

## Post #3 by @miniminic (2022-12-01 07:52 UTC)

<p>Okay, thanks. I’ll try</p>

---
