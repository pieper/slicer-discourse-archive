---
topic_id: 46065
title: "Surface Model Turns Black Under Transformation"
date: 2026-02-05
url: https://discourse.slicer.org/t/46065
---

# Surface model turns black under transformation

**Topic ID**: 46065
**Date**: 2026-02-05
**URL**: https://discourse.slicer.org/t/surface-model-turns-black-under-transformation/46065

---

## Post #1 by @mikebind (2026-02-05 18:09 UTC)

<p>When I reflect a model node using a linear transform node that has a reflection, the visualization of it in 3D unexpectedly turns black.  I gather from other posts and LLM consultation that this is because a transform with negative determinant turns the model “inside-out”.  The surface normals are properly reflected, but the clockwise/counterclockwise sense of which side of a surface facet is the “front” is reversed by the reflection. Thus when the renderer is trying to figure out how to light a facet, the surface normal for the “front” actually points out the “back” of the facet, and this results in no color or light at that facet, it’s just black (note that this is somehow different than just flipping the normal vectors, in which case you would see the backface color lighting rather than black). The proper way to address this is to apply a vtkReverseSense() filter, which flips the facet orientation back the other way around. My suggestion is that Slicer should do this sense reversal under transformation with negative determinant automatically.  I think that even relatively sophisticated users used to applying all sorts of transformations to all sorts of MRML nodes will find the current behavior surprising and undesirable.  Is there any use case where a user would actually want their transform to make their surface unlightable in this way?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa8d6665f17510bfdc76f02ccabee7bedf0f993.jpeg" data-download-href="/uploads/short-url/AtFueu2biS0RAhZSJ13f51XWCiv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffa8d6665f17510bfdc76f02ccabee7bedf0f993_2_660x500.jpeg" alt="image" data-base62-sha1="AtFueu2biS0RAhZSJ13f51XWCiv" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffa8d6665f17510bfdc76f02ccabee7bedf0f993_2_660x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa8d6665f17510bfdc76f02ccabee7bedf0f993.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa8d6665f17510bfdc76f02ccabee7bedf0f993.jpeg 2x" data-dominant-color="7C83A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">887×671 61.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Background context: I am constructing a heatmap of a brain structure in a standardized coordinate system for something like a probabilistic atlas of its location.  Since there is bilateral symmetry in the brain, I am reflecting all of the left side structures to the right to make a combined map with a “lateral” coordinate rather than a R/L coordinate. I was surprised and confused when some of the models turned black and were impervious to lighting changes. I realized that it was all of the reflected versions that were like this and I spent a lot of time trying to figure out what was different before coming across the explanation above. The typical experience of applying transforms to nodes in Slicer is that they “just work”, but in this case it felt like it broke the models in a way that was not easy to understand.</p>

---

## Post #2 by @pieper (2026-02-05 18:27 UTC)

<p>Yes, I can see how this is unexpected and could be automatically detected and fixed.  It would mean that in the models displayable manager we’d check the transform and add the reverse sense filter as you suggest.  I know people worked on mirroring applications in the past but I don’t recall if anything ever made it as an extension; something that simplified the whole process using landmarks and planes and also handled the visualization would probably be easiest if people are doing this a lot.</p>
<p>In case it helps, there’a Flip Normals option in the Surface Toolbox that can do this.  Also a mirror, which might do what you need.</p>

---

## Post #3 by @mikebind (2026-02-05 18:41 UTC)

<p>Thanks for the response!  Surface Toolbox does indeed handle this properly in the “Mirror” function, and internally, all it does is detect whether the transformation has negative determinant, and if so, applies vtkReverseSense().  Now that I know what the issue is, it is straightforward to correct; I just had trouble figuring it out, and it would be nice (and seems like it would be appropriate) if this were handled in the model’s displayable manager, as you suggest. Is there a good place I can suggest this change (e.g. github issue)?</p>

---

## Post #4 by @pieper (2026-02-05 18:44 UTC)

<p>Yes, a github issue make sense.  We could also move this to the Feature Requests category so people could vote in support of the idea (just did that).</p>

---

## Post #5 by @mikebind (2026-02-05 19:01 UTC)

<p>Thanks!  I added a github issue as well referencing this discussion: <a href="https://github.com/Slicer/Slicer/issues/9018" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/9018</a></p>

---
