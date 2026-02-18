# Make viewers dockable and possible to rearrange

**Topic ID**: 32934
**Date**: 2023-11-21
**URL**: https://discourse.slicer.org/t/make-viewers-dockable-and-possible-to-rearrange/32934

---

## Post #1 by @muratmaga (2023-11-21 19:54 UTC)

<p>I occasionally find myself wishing to rearrange the size of the viewer windows independently from each other. Of course this is doable by creating custom layouts and registering with Slicer, and makes sense if someone knows that they routinely will need that exact layout. It does take a while to create the correct XML for the layout.</p>
<p>What I am asking would be a situation rearranging the position and size of the viewers by dragging and dropping them into locations, from which I can create layouts like a 3D viewer that spans the vertical high of windows, a red view that’s same height and green and yellow viewers half height of that. And then being able to drag their corners to adjust their width.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b86105f3b8e58d111f43ad185e11bfc783e34df.png" data-download-href="/uploads/short-url/d3EGbRzMjpC9m76r6J8ELvtM5eT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b86105f3b8e58d111f43ad185e11bfc783e34df_2_345x230.png" alt="image" data-base62-sha1="d3EGbRzMjpC9m76r6J8ELvtM5eT" width="345" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b86105f3b8e58d111f43ad185e11bfc783e34df_2_345x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b86105f3b8e58d111f43ad185e11bfc783e34df_2_517x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b86105f3b8e58d111f43ad185e11bfc783e34df_2_690x460.png 2x" data-dominant-color="BB473D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×639 1.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then for example dragging the yellow viewer on top of red results in this rearrangement automatically:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/033c03bab31870c88da5df33a9f851c649674904.png" data-download-href="/uploads/short-url/sC0O5fQNMKYBtCAWYmrx9y4zEE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/033c03bab31870c88da5df33a9f851c649674904_2_345x230.png" alt="image" data-base62-sha1="sC0O5fQNMKYBtCAWYmrx9y4zEE" width="345" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/033c03bab31870c88da5df33a9f851c649674904_2_345x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/033c03bab31870c88da5df33a9f851c649674904_2_517x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/033c03bab31870c88da5df33a9f851c649674904_2_690x460.png 2x" data-dominant-color="BB4E3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×641 1.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then dragging the 3D viewer (purple) onto green does this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b03224091dd3de7462a5ead120cddbfc41475e65.png" data-download-href="/uploads/short-url/p8HszF9FQmffT44YzufnBZNGuJD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b03224091dd3de7462a5ead120cddbfc41475e65_2_345x230.png" alt="image" data-base62-sha1="p8HszF9FQmffT44YzufnBZNGuJD" width="345" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b03224091dd3de7462a5ead120cddbfc41475e65_2_345x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b03224091dd3de7462a5ead120cddbfc41475e65_2_517x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b03224091dd3de7462a5ead120cddbfc41475e65_2_690x460.png 2x" data-dominant-color="BB622F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×641 1.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2023-11-22 17:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="32934">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b86105f3b8e58d111f43ad185e11bfc783e34df.png" data-download-href="/uploads/short-url/d3EGbRzMjpC9m76r6J8ELvtM5eT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b86105f3b8e58d111f43ad185e11bfc783e34df.png" alt="image" data-base62-sha1="d3EGbRzMjpC9m76r6J8ELvtM5eT" width="690" height="460" data-dominant-color="BB473D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×639 1.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then for example dragging the yellow viewer on top of red results in this rearrangement automatically:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/033c03bab31870c88da5df33a9f851c649674904.png" data-download-href="/uploads/short-url/sC0O5fQNMKYBtCAWYmrx9y4zEE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/033c03bab31870c88da5df33a9f851c649674904.png" alt="image" data-base62-sha1="sC0O5fQNMKYBtCAWYmrx9y4zEE" width="690" height="461" data-dominant-color="BB4E3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×641 1.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
</aside>
<p>Based on your examples does dragging one viewer on top of another swap their positions while becoming the size of the viewer that was previously there? In your first example (quoted above) it appears that the Red slice goes into the yellow slice position, but also changes sizes to be a wide ratio and neither square ratio or tall ratio (original red slice dimension).</p>

---

## Post #3 by @muratmaga (2023-11-22 17:11 UTC)

<p>Yes, when you are swapping them the sizes can change, but the idea all internal edges between viewers should be adjustable (so that you can rearrange the widths/heights in whichever way you want).</p>

---

## Post #4 by @pieper (2023-11-22 17:16 UTC)

<p>Another thing to consider: we traditionally use a tiled layout, but we could offer a mode where views are allowed to overlap (e.g. with <a href="https://doc.qt.io/qt-5/qmdiarea.html#details">QMdiArea</a>.  I’ve seen this used for longitudinal imaging where you get a stack of images you can easily flip through, but I’m not sure how popular it is.</p>
<p>Also, I’ve always wanted the ability to just change the view type in an existing layout.  Like changing the large view in the default layout from a threeDView to a sliceView for example, without changing anything else about the layout.</p>

---

## Post #5 by @jamesobutler (2023-11-22 17:21 UTC)

<p>I think swapping them and it adopting the size of the viewer in the position it is trying to be dropped into would be easier. Dropping some large shape in the middle of say a 4x4 grid could get complicated if to maintain the size of the large shape the other surrounding slice viewers may have to change their size as well even though not directly involved.</p>

---

## Post #6 by @lassoan (2023-11-27 21:07 UTC)

<p>I quite like ParaView’s simple layout editing feature: all it does it allows to split any view horizontally or vertically. You can then specify the view type in the newly opened up space. Would this be sufficient?</p>

---
