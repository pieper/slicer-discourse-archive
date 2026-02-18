# Centerline model has duplicate points

**Topic ID**: 27545
**Date**: 2023-01-30
**URL**: https://discourse.slicer.org/t/centerline-model-has-duplicate-points/27545

---

## Post #1 by @chir.set (2023-01-30 21:51 UTC)

<p>Centerline model has duplicate points</p>
<p>Centerline models from ‘Extract centerline’ often, if not always, have duplicate points. I don’t know since when, this is apparent when using ‘Cross-section analysis’. At the duplicate point, the normal is (0, 0, 1) and the slice view always looks upwards. vtkCleanPolyData on the freshly generated centerline polydata in ‘Extract centerline’ does not <em>always</em> fix this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/134fd46ec29ac001688d04d7ae7d8121c92f1da1.png" data-download-href="/uploads/short-url/2KQ6BuJ1PGjopEiewXdtxgf2Dqp.png?dl=1" title="Duplicate_points" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/134fd46ec29ac001688d04d7ae7d8121c92f1da1_2_663x499.png" alt="Duplicate_points" data-base62-sha1="2KQ6BuJ1PGjopEiewXdtxgf2Dqp" width="663" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/134fd46ec29ac001688d04d7ae7d8121c92f1da1_2_663x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/134fd46ec29ac001688d04d7ae7d8121c92f1da1_2_994x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/134fd46ec29ac001688d04d7ae7d8121c92f1da1.png 2x" data-dominant-color="494E4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Duplicate_points</span><span class="informations">1196×901 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The picture above deals with the simplest test situation : draw a segment with ‘Paint’ as a sphere brush, auto-detect end points in ‘Extract centerline’ and generate the centerline model. Then in ‘Cross-section analysis’, use the centerline model with ‘CE diameter’ for the plot. When using a centerline curve, this unexpected output is not observed.</p>
<p>With anatomical surfaces, the same observations can be made.</p>
<p>It’s quite new, don’t know since when. Posting here in the hope of a fix. Using Slicer preview and self-built on Arch Linux.</p>
<p>Regards.</p>

---
