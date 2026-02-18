# Segmentation leaves empty vertical lines

**Topic ID**: 2319
**Date**: 2018-03-14
**URL**: https://discourse.slicer.org/t/segmentation-leaves-empty-vertical-lines/2319

---

## Post #1 by @alessandronavacchia (2018-03-14 18:23 UTC)

<p>Hi all,</p>
<p>I am having trouble with segmenting an MRI. I am using the ‘draw’ tool in the ‘Segment editor’. I draw the outline you can see in this picture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/595ecbbc2ef0ae8e183a3d0585fb48628f3fdba6.jpeg" data-download-href="/uploads/short-url/cKBAPpOzORvPEV6E2BaHkS6YjcO.jpg?dl=1" title="draw_outline" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/595ecbbc2ef0ae8e183a3d0585fb48628f3fdba6_2_690x374.jpg" alt="draw_outline" data-base62-sha1="cKBAPpOzORvPEV6E2BaHkS6YjcO" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/595ecbbc2ef0ae8e183a3d0585fb48628f3fdba6_2_690x374.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/595ecbbc2ef0ae8e183a3d0585fb48628f3fdba6_2_1035x561.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/595ecbbc2ef0ae8e183a3d0585fb48628f3fdba6_2_1380x748.jpg 2x" data-dominant-color="6A6A69"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">draw_outline</span><span class="informations">2555×1388 552 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And when I press enter, this is what I get:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5e198c09781ea42449ddf7d4c6fb8d59a6bbe26.jpeg" data-download-href="/uploads/short-url/nFs7whjvtYm9HnifR9RhfpHjbIq.jpg?dl=1" title="draw_segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e198c09781ea42449ddf7d4c6fb8d59a6bbe26_2_689x374.jpg" alt="draw_segmentation" data-base62-sha1="nFs7whjvtYm9HnifR9RhfpHjbIq" width="689" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e198c09781ea42449ddf7d4c6fb8d59a6bbe26_2_689x374.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e198c09781ea42449ddf7d4c6fb8d59a6bbe26_2_1033x561.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e198c09781ea42449ddf7d4c6fb8d59a6bbe26_2_1378x748.jpg 2x" data-dominant-color="6B6D6B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">draw_segmentation</span><span class="informations">2558×1390 545 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can see, there are unsegmented vertical lines that should be filled. In addition, some filled vertical lines show up in the next slice. I segmented one slice every three slices and this is what I get in the axial plane (see green lines on the left):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8437f6f438bb3f147a3ca8481ad984c606897d17.jpeg" data-download-href="/uploads/short-url/iREVEiEUe5iwle4aJ23QgkljsPl.jpg?dl=1" title="axial" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8437f6f438bb3f147a3ca8481ad984c606897d17_2_374x500.jpg" alt="axial" data-base62-sha1="iREVEiEUe5iwle4aJ23QgkljsPl" width="374" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8437f6f438bb3f147a3ca8481ad984c606897d17_2_374x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8437f6f438bb3f147a3ca8481ad984c606897d17_2_561x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8437f6f438bb3f147a3ca8481ad984c606897d17_2_748x1000.jpg 2x" data-dominant-color="4F504F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axial</span><span class="informations">850×1136 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My guess is that this error is related to the orientation of the slices or something like that. Can someone help?</p>
<p>Thanks!</p>
<p>Alessandro</p>

---

## Post #2 by @pieper (2018-03-14 19:34 UTC)

<p>Have a look at this topic, it should solve this for you:</p><aside class="quote quote-modified" data-post="1" data-topic="1459">
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

## Post #3 by @alessandronavacchia (2018-03-15 14:22 UTC)

<p>Steve,</p>
<p>that fixed the problem, thanks a lot for your help!</p>
<p>Alessandro</p>

---
