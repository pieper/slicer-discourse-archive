# The spline function for spline curve in Markups

**Topic ID**: 29381
**Date**: 2023-05-09
**URL**: https://discourse.slicer.org/t/the-spline-function-for-spline-curve-in-markups/29381

---

## Post #1 by @Chuan (2023-05-09 15:54 UTC)

<p>Hi,<br>
Does anyone how in 3D slicer, which kind of spline curve function is used in markups?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ec09652033ecae0331a28713aa8d4aea311e847.png" data-download-href="/uploads/short-url/26viE1HPrEcHO4xpOcrcP696A1p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ec09652033ecae0331a28713aa8d4aea311e847_2_434x500.png" alt="image" data-base62-sha1="26viE1HPrEcHO4xpOcrcP696A1p" width="434" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ec09652033ecae0331a28713aa8d4aea311e847_2_434x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ec09652033ecae0331a28713aa8d4aea311e847.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ec09652033ecae0331a28713aa8d4aea311e847.png 2x" data-dominant-color="F2F2F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">632×727 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I can only see the curve type is spline, but have not found out which kind of function is used for this Spline type.</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #2 by @lassoan (2023-05-10 02:02 UTC)

<p>Cardinal or Kochanek spline is used. You can find details in the source code <a href="https://github.com/Slicer/vtkAddon/blob/main/vtkCurveGenerator.cxx">here</a>.</p>

---
