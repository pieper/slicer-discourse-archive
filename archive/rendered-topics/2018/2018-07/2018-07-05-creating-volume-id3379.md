# Creating volume

**Topic ID**: 3379
**Date**: 2018-07-05
**URL**: https://discourse.slicer.org/t/creating-volume/3379

---

## Post #1 by @Egor (2018-07-05 08:46 UTC)

<p>How to create volume without jagged lines and bands?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72805fc1c79da5d04e550bd826593a3e331e1547.png" data-download-href="/uploads/short-url/gkVtft4Gw2z0yETuT6E0L6yOjqv.png?dl=1" title="%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72805fc1c79da5d04e550bd826593a3e331e1547_2_690x358.png" alt="%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9" data-base62-sha1="gkVtft4Gw2z0yETuT6E0L6yOjqv" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72805fc1c79da5d04e550bd826593a3e331e1547_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72805fc1c79da5d04e550bd826593a3e331e1547_2_1035x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72805fc1c79da5d04e550bd826593a3e331e1547.png 2x" data-dominant-color="A3A4B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9</span><span class="informations">1366×710 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2018-07-05 13:42 UTC)

<p>Have a look at this discussion:</p>
<aside class="quote quote-modified" data-post="1" data-topic="1459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ecc23a/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459">Segmentation Editor - How to disable painting on adjacent slices?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I am working on a project where we are segmenting lesions from an MRI using the paint tool from the Segment Editor module. We are using a large brush size along with a threshold so only pixels within a certain range are included in the segmentation. 
My problem is that I want the segmentation to be only in 2d (i.e. just affecting the pixels on the current slice of the volume). For example, if I do a threshold paint on slice 10 of the MRI, I don’t want it to paint any of the pixels on slice 9 or …
  </blockquote>
</aside>


---
