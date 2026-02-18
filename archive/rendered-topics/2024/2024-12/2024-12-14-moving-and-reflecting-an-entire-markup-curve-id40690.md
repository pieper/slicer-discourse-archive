# moving and reflecting an entire markup curve

**Topic ID**: 40690
**Date**: 2024-12-14
**URL**: https://discourse.slicer.org/t/moving-and-reflecting-an-entire-markup-curve/40690

---

## Post #1 by @Elizabeth_Miller (2024-12-14 02:36 UTC)

<p>Hello:</p>
<p>I have a case where the left tooth is broken but the right tooth is not. We want to approximate a landmark on the tip of the left tooth by making a curve on the unbroken tooth, cloning it and moving it to where the broken tooth would be. I have my curve, however I can’t figure out how to move the entire curve to the other side (and then mirror its direction).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/649ab4ff7fd323a86fbc027da941f1fe383bcf90.jpeg" data-download-href="/uploads/short-url/elZcJe9oh7zrk2CTuKkHuARGsUg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649ab4ff7fd323a86fbc027da941f1fe383bcf90_2_690x388.jpeg" alt="image" data-base62-sha1="elZcJe9oh7zrk2CTuKkHuARGsUg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649ab4ff7fd323a86fbc027da941f1fe383bcf90_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649ab4ff7fd323a86fbc027da941f1fe383bcf90_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649ab4ff7fd323a86fbc027da941f1fe383bcf90_2_1380x776.jpeg 2x" data-dominant-color="8D8E9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2024-12-14 07:55 UTC)

<p>If you invert the sign of the ‘R’ coordinate values, the curve should mirror by geometry. Then with ‘Shift + left click’ or ‘middle click’, you can move the curve to the broken tooth.</p>

---

## Post #3 by @muratmaga (2024-12-15 02:30 UTC)

<p>To simplify what <a class="mention" href="/u/chir.set">@chir.set</a> suggested, you can create a linear transform and edit the first diagonal as -1, create a clone of your curve and put it under that transform.</p>
<p>That’s equivalent to multiplying “R” coordinate with -1 for all your control points (instead of doing one by one).</p>

---
