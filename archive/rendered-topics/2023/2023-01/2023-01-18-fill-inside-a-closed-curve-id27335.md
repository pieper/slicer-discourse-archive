---
topic_id: 27335
title: "Fill Inside A Closed Curve"
date: 2023-01-18
url: https://discourse.slicer.org/t/27335
---

# Fill inside a closed curve

**Topic ID**: 27335
**Date**: 2023-01-18
**URL**: https://discourse.slicer.org/t/fill-inside-a-closed-curve/27335

---

## Post #1 by @muratmaga (2023-01-18 23:38 UTC)

<p>When creating anatomical teaching materials, it would be nice to highlight different structures with different colors. Obviously this is best done with segmentation, but that’s quite a lot of work; especially when all you want to is highlight an external surface. Closed curve in this situation would work really well, but it needs to also cover the inside of the polygon (but with about 50% opacity), not just the boundary.</p>
<p>Is there a piece of python code to do that? Or better yet, can this be a property of the closed curves?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6aff78172515026a0283708042a95d7f894fb6c.jpeg" data-download-href="/uploads/short-url/q47UdI3UwgqwMsrPlWxxKdZXNGA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6aff78172515026a0283708042a95d7f894fb6c_2_690x395.jpeg" alt="image" data-base62-sha1="q47UdI3UwgqwMsrPlWxxKdZXNGA" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6aff78172515026a0283708042a95d7f894fb6c_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6aff78172515026a0283708042a95d7f894fb6c_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6aff78172515026a0283708042a95d7f894fb6c.jpeg 2x" data-dominant-color="A3A2A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1376×789 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @RafaelPalomar (2023-01-19 06:08 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, maybe you could use the Baffle planner functionality in the Slicer Heart extension: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/BafflePlanner.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerHeart/BafflePlanner.md at master · SlicerHeart/SlicerHeart · GitHub</a>. This would add a new object to the scene rather than modifying the visual properties of the underlying volume.</p>
<p>This is extracted from the documentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c67ca7edc1bf4943c052fd223a994c8efc48d00.jpeg" data-download-href="/uploads/short-url/mjCR6Gz7JnqMTqMxMb6UCmB3nnq.jpeg?dl=1" title="baffleplanner" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c67ca7edc1bf4943c052fd223a994c8efc48d00_2_690x391.jpeg" alt="baffleplanner" data-base62-sha1="mjCR6Gz7JnqMTqMxMb6UCmB3nnq" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c67ca7edc1bf4943c052fd223a994c8efc48d00_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c67ca7edc1bf4943c052fd223a994c8efc48d00_2_1035x586.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c67ca7edc1bf4943c052fd223a994c8efc48d00_2_1380x782.jpeg 2x" data-dominant-color="E4D4D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">baffleplanner</span><span class="informations">3238×1835 362 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @muratmaga (2023-01-19 16:36 UTC)

<p>Thanks <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> that would definitely work for starters.</p>

---
