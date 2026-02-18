# Combing curves and point lists

**Topic ID**: 35256
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/combing-curves-and-point-lists/35256

---

## Post #1 by @jmhuie (2024-04-03 14:42 UTC)

<p>Mostly a question for <a class="mention" href="/u/muratmaga">@muratmaga</a> or <a class="mention" href="/u/smrolfe">@smrolfe</a> and the SlicerMorph team. Is there a tool or best practice for combing a curve with a point list, where the ends of a curve are fixed landmarks in the list? Here’s a mock up, where there’s a point list and a curve that connects LM-25 and LM-35. I want to export all of the landmarks as a single file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e84eaa764f9f60a46a5cc2d8328758e60372ed31.jpeg" data-download-href="/uploads/short-url/x95jsYh6kH3PoG1KcS7cLhUU17r.jpeg?dl=1" title="Screenshot 2024-04-03 at 10.37.13 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e84eaa764f9f60a46a5cc2d8328758e60372ed31_2_690x400.jpeg" alt="Screenshot 2024-04-03 at 10.37.13 AM" data-base62-sha1="x95jsYh6kH3PoG1KcS7cLhUU17r" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e84eaa764f9f60a46a5cc2d8328758e60372ed31_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e84eaa764f9f60a46a5cc2d8328758e60372ed31_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e84eaa764f9f60a46a5cc2d8328758e60372ed31_2_1380x800.jpeg 2x" data-dominant-color="757545"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-03 at 10.37.13 AM</span><span class="informations">1920×1114 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I could copy and paste the curve points to the point lists, but I have to be careful not to also copy the duplicated points. If I have a lot of curves that could be cumbersome. Is there anything similar to the MergeMarkups module but for combining different markup node types?</p>

---

## Post #2 by @muratmaga (2024-04-03 15:20 UTC)

<p>There is a mergeMarkup module in SlicerMorph that does some of what you want. For example, if you have multiple resampled curves, such that the last point of the one curve is the first point of the other, you can use the module to create a single curve without redundant points.</p>
<p>See the tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MergeMarkups">Tutorials/MergeMarkups at main · SlicerMorph/Tutorials (github.com)</a></p>

---
