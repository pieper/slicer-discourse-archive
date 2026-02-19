---
topic_id: 16284
title: "Issue With Level Tracing"
date: 2021-03-01
url: https://discourse.slicer.org/t/16284
---

# Issue with level tracing

**Topic ID**: 16284
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/issue-with-level-tracing/16284

---

## Post #1 by @mohammed_alshakhas (2021-03-01 12:06 UTC)

<p>i heve the level tracing only showing axial regardless of the view im trying to segment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a26a61f2e95f7bb73a1140857ed1536a8d83b1b.jpeg" data-download-href="/uploads/short-url/jI8H8NoF6B1NHZQJtYV7znWLAgz.jpeg?dl=1" title="Screen Shot 2021-03-01 at 15.04.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a26a61f2e95f7bb73a1140857ed1536a8d83b1b_2_690x388.jpeg" alt="Screen Shot 2021-03-01 at 15.04.20" data-base62-sha1="jI8H8NoF6B1NHZQJtYV7znWLAgz" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a26a61f2e95f7bb73a1140857ed1536a8d83b1b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a26a61f2e95f7bb73a1140857ed1536a8d83b1b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a26a61f2e95f7bb73a1140857ed1536a8d83b1b_2_1380x776.jpeg 2x" data-dominant-color="ABABAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-01 at 15.04.20</span><span class="informations">1920×1080 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
i had this issue for a while , now it is not working properly anymore</p>

---

## Post #2 by @lassoan (2021-03-01 12:52 UTC)

<p>Level tracing only works in non-rotated slices (slice view plane is parallel with a volume plane). Click the warning button to rotate the volume to view plane. If you want to segment in oblique plane then you can resample the volume. See this segmentation recipe for more details: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>

---
