---
topic_id: 20546
title: "After Smoothing And Hole Filling Still Some Holes Arte There"
date: 2021-11-09
url: https://discourse.slicer.org/t/20546
---

# After Smoothing and hole filling Still some holes arte there in 3 D model of nasal cavity

**Topic ID**: 20546
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/after-smoothing-and-hole-filling-still-some-holes-arte-there-in-3-d-model-of-nasal-cavity/20546

---

## Post #1 by @Sliceeeeee (2021-11-09 15:21 UTC)

<p>I am going to do nasal airflow simulation , i am made a 3D model of nasal cavity in 3D slicer , but still there are many holes what to do ? and also after making 3D model is there any other post processing required before exporting it to any simulation software ?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-11-09 16:08 UTC)

<aside class="quote no-group" data-username="Sliceeeeee" data-post="1" data-topic="20546">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sliceeeeee/48/12358_2.png" class="avatar"> Sliceeeeee:</div>
<blockquote>
<p>i am made a 3D model of nasal cavity in 3D slicer , but still there are many holes what to do ?</p>
</blockquote>
</aside>
<p>There are many different approaches to decide what are considered holes and how to fill them. Could you post a few images that illustrate what kind of shapes, level of details, and size and number of holes you encounter?</p>
<aside class="quote no-group" data-username="Sliceeeeee" data-post="1" data-topic="20546">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sliceeeeee/48/12358_2.png" class="avatar"> Sliceeeeee:</div>
<blockquote>
<p>after making 3D model is there any other post processing required before exporting it to any simulation software ?</p>
</blockquote>
</aside>
<p>If your simulation software can create volumetric mesh from surface mesh (ply, vtk, vtp, or obj file) then probably no post-processing is necessary. If your simulation software expects a volumetric mesh (e.g., tetrahedral mesh) then you can use SegmentMesher extension to generate it from the segmentation.</p>

---

## Post #3 by @Sliceeeeee (2021-11-09 18:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84886b6aa309de83b2945c8be568ac098cab204d.jpeg" data-download-href="/uploads/short-url/iUriPyG5NBDnyfsXFXEhHOzPeHj.jpeg?dl=1" title="20211109_221832" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84886b6aa309de83b2945c8be568ac098cab204d_2_666x500.jpeg" alt="20211109_221832" data-base62-sha1="iUriPyG5NBDnyfsXFXEhHOzPeHj" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84886b6aa309de83b2945c8be568ac098cab204d_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84886b6aa309de83b2945c8be568ac098cab204d_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84886b6aa309de83b2945c8be568ac098cab204d_2_1332x1000.jpeg 2x" data-dominant-color="788071"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211109_221832</span><span class="informations">1920×1440 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b79cee0b51e55fd984e10bc493ab852adbb49d62.jpeg" data-download-href="/uploads/short-url/qcjB3ODfSmqlkreNbngh9uRlQc2.jpeg?dl=1" title="20211109_221756" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b79cee0b51e55fd984e10bc493ab852adbb49d62_2_690x435.jpeg" alt="20211109_221756" data-base62-sha1="qcjB3ODfSmqlkreNbngh9uRlQc2" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b79cee0b51e55fd984e10bc493ab852adbb49d62_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b79cee0b51e55fd984e10bc493ab852adbb49d62_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b79cee0b51e55fd984e10bc493ab852adbb49d62_2_1380x870.jpeg 2x" data-dominant-color="93968C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211109_221756</span><span class="informations">1920×1212 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>These types of holes are there …</p>

---

## Post #4 by @lassoan (2021-11-09 18:16 UTC)

<p>For me it is very hard to interpret these screenshots. Could you maybe show a few slice views and use an arrow to point out the issue instead of circling a large area?</p>

---

## Post #5 by @Sliceeeeee (2021-11-09 19:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0c2446664abcf52307d80ebe7f16a133a3a6a06.jpeg" data-download-href="/uploads/short-url/pdGfwghwlGBo6swGbGXCi5GJ3Rc.jpeg?dl=1" title="20211109_221836" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0c2446664abcf52307d80ebe7f16a133a3a6a06_2_690x212.jpeg" alt="20211109_221836" data-base62-sha1="pdGfwghwlGBo6swGbGXCi5GJ3Rc" width="690" height="212" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0c2446664abcf52307d80ebe7f16a133a3a6a06_2_690x212.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0c2446664abcf52307d80ebe7f16a133a3a6a06_2_1035x318.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0c2446664abcf52307d80ebe7f16a133a3a6a06_2_1380x424.jpeg 2x" data-dominant-color="7E8377"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211109_221836</span><span class="informations">1920×592 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Please Check This one , while doing smoothing for higher size hole other anatomy also merged (which should not be actually)</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2021-11-09 20:03 UTC)

<p>If the holes only appear where the surface is very thin then it may be due to surface smoothing (that is applied when the binary labelmap representation is converted to a closed surface representation). You can address this by increasing the resolution (reducing the spacing of the segmentation) or reduce the smoothing factor.</p>

---
