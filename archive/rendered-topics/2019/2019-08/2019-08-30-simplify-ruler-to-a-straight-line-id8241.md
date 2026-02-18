# Simplify ruler to a straight line

**Topic ID**: 8241
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/simplify-ruler-to-a-straight-line/8241

---

## Post #1 by @rprueckl (2019-08-30 18:07 UTC)

<p>Hi,<br>
I want to use the ruler as a generic line for different purposes. I can simplify it to a degree where it nearly fits my requirements. Only the start and end markers (see picture, marked with yellow arrows) are still there and I cannot find where they are implemented. Can someone direct me to the code that is the basis for those noses?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b941809829895e3612b35fee8c2fb53234cac43.png" data-download-href="/uploads/short-url/jULENJvtgaoX6vWildDWcGx5NED.png?dl=1" title="Bild%201" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b941809829895e3612b35fee8c2fb53234cac43_2_346x500.png" alt="Bild%201" data-base62-sha1="jULENJvtgaoX6vWildDWcGx5NED" width="346" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b941809829895e3612b35fee8c2fb53234cac43_2_346x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b941809829895e3612b35fee8c2fb53234cac43_2_519x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b941809829895e3612b35fee8c2fb53234cac43.png 2x" data-dominant-color="130F10"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bild%201</span><span class="informations">526×759 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As an alternative I also tried with vtkLineSource, however, I cannot set a thickness there and it is not rendered in the slice views (only in 3d views). vtkCylinderSource is also not optimal as the radius would have to be dependent on the camera position and the projection onto the slice views always results in a rectangle.</p>

---

## Post #2 by @lassoan (2019-08-30 18:57 UTC)

<p>You can use markups line in recent preview releases.</p>

---

## Post #3 by @jcfr (2019-09-03 13:42 UTC)

<p><a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a> This may be useful</p>

---

## Post #4 by @rprueckl (2019-09-04 19:11 UTC)

<p>I will keep that in mind, however I have to work with a stable version for now. Thanks.</p>

---
