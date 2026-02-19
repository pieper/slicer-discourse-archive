---
topic_id: 19046
title: "Draw Effect Sometimes Not Applying"
date: 2021-08-03
url: https://discourse.slicer.org/t/19046
---

# Draw effect sometimes not applying

**Topic ID**: 19046
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/draw-effect-sometimes-not-applying/19046

---

## Post #1 by @jamesobutler (2021-08-03 17:53 UTC)

<p>Does anyone know what might be going on here? I created the new segmentation from an option in the SegmentEditor segmentation node combobox and then the foreground volume (“FusedVolume”) was selected instead of the “Select Master Volume to enable editing”. As shown in the first image, I am able to use the draw effect to apply a segment.  However it appears I can only apply/modify this segment if I’m in the center of a voxel in the foreground volume which is also the original master volume for the segmentation node.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47228e84bc0b14eaf220cfc850e842b42b6ba53d.jpeg" data-download-href="/uploads/short-url/a9hW8Ye7VGUt5dWSV6fHuL1rKK9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47228e84bc0b14eaf220cfc850e842b42b6ba53d_2_690x370.jpeg" alt="image" data-base62-sha1="a9hW8Ye7VGUt5dWSV6fHuL1rKK9" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47228e84bc0b14eaf220cfc850e842b42b6ba53d_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47228e84bc0b14eaf220cfc850e842b42b6ba53d_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47228e84bc0b14eaf220cfc850e842b42b6ba53d_2_1380x740.jpeg 2x" data-dominant-color="B1AF9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I scroll to another slice offset (note the background volume is a finer resolution), then I cannot use the draw tool anymore to modify the segment. The yellow draw disappears, but nothing changes about the segment.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f4be85c080ebee5516f371bb9a07d08a3481c33.jpeg" data-download-href="/uploads/short-url/dB1ZrKXiTj8IbMl03iv8S8zm191.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f4be85c080ebee5516f371bb9a07d08a3481c33_2_690x370.jpeg" alt="image" data-base62-sha1="dB1ZrKXiTj8IbMl03iv8S8zm191" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f4be85c080ebee5516f371bb9a07d08a3481c33_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f4be85c080ebee5516f371bb9a07d08a3481c33_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f4be85c080ebee5516f371bb9a07d08a3481c33_2_1380x740.jpeg 2x" data-dominant-color="B1AF9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
What is weird is that I can use the Paint effect to modify the segment at this other offset, but not the draw effect.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c5c9776ec6987f9a92350c93052af12782060d6.jpeg" data-download-href="/uploads/short-url/fsBWuTDdp7ByspNPVb1Tk8ZNvaC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c5c9776ec6987f9a92350c93052af12782060d6_2_690x370.jpeg" alt="image" data-base62-sha1="fsBWuTDdp7ByspNPVb1Tk8ZNvaC" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c5c9776ec6987f9a92350c93052af12782060d6_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c5c9776ec6987f9a92350c93052af12782060d6_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c5c9776ec6987f9a92350c93052af12782060d6_2_1380x740.jpeg 2x" data-dominant-color="B1AFA0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-08-03 18:19 UTC)

<p>Slice thickness is determined by the slice spacing of the view, which comes from the background volume. If the background volume is not the same as the master volume then the effect has to handle this difference correctly. Newly developed effects, such as Paint and Scissors should work well, but Draw effect uses an extremely old code (vtkImageFillROI from Slicer2), which has a number of limitations (for example, it does not work at all with non-axis-aligned views).</p>
<p>We should retire the Draw effect and improve Scissors effect to have the “delayed apply” mode (drawing is not applied immediately when the mouse button is release but on double-click), as described <a href="https://github.com/Slicer/Slicer/issues/5606">here</a>. It would be awesome if you could work on this.</p>

---

## Post #3 by @jamesobutler (2021-08-03 22:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the background volume is not the same as the master volume then the effect has to handle this difference correctly. Newly developed effects, such as Paint and Scissors should work well</p>
</blockquote>
</aside>
<p>When using the Scissors effect as shown below, I’m still observing the same behavior that it doesn’t apply the effect successfully unless I’m in the middle of the voxel of the foreground volume which is my master volume for the segmentation. For slice cut “0 means that only the current slice is included.” I would expect this to work regardless of the volume’s slice thickness. It appears that it will fill only if I set the slice thickness to a value so that it will cross over the middle position of the voxel. This is because the required minimum slice thickness to fill increases the farther I’m away from the voxel center.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf8d196c00afc41fcdd81ba9a9884e8edc7cad11.jpeg" data-download-href="/uploads/short-url/rkxv2LO9S47OfufKgmZeHlcwJep.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf8d196c00afc41fcdd81ba9a9884e8edc7cad11_2_690x373.jpeg" alt="image" data-base62-sha1="rkxv2LO9S47OfufKgmZeHlcwJep" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf8d196c00afc41fcdd81ba9a9884e8edc7cad11_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf8d196c00afc41fcdd81ba9a9884e8edc7cad11_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf8d196c00afc41fcdd81ba9a9884e8edc7cad11_2_1380x746.jpeg 2x" data-dominant-color="B1B5AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I scroll to another slice offset (note the background volume is a finer resolution), then I cannot use the scissors tool anymore to modify the segment. The yellow scissors free-form disappears, but nothing changes about the segment.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11ee13d6cdb293659dfad92f0e0d104dc2bcc8f9.jpeg" data-download-href="/uploads/short-url/2yCc8cj5as8dxqUXBtP40pIeZjX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11ee13d6cdb293659dfad92f0e0d104dc2bcc8f9_2_690x372.jpeg" alt="image" data-base62-sha1="2yCc8cj5as8dxqUXBtP40pIeZjX" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11ee13d6cdb293659dfad92f0e0d104dc2bcc8f9_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11ee13d6cdb293659dfad92f0e0d104dc2bcc8f9_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11ee13d6cdb293659dfad92f0e0d104dc2bcc8f9_2_1380x744.jpeg 2x" data-dominant-color="B1B5AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1036 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2021-08-03 22:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We should retire the Draw effect and improve Scissors effect to have the “delayed apply” mode (drawing is not applied immediately when the mouse button is release but on double-click), as described <a href="https://github.com/Slicer/Slicer/issues/5606">here</a>. It would be awesome if you could work on this.</p>
</blockquote>
</aside>
<p>Draw effect is fairly heavily used in manual segmentations. I am not aware of a mode in scissors which allows me to draw and paint a polygon. While the proposal calls for closed curves from markups for this functionality, will it be as quick and efficient as the polygon tool in draw?</p>

---

## Post #5 by @pieper (2021-08-03 23:47 UTC)

<p>Yes, the fill ROI code is some of the oldest code in Slicer.  I remember that when working on the Editor in Slicer3 I looked through vtk and itk but didn’t find a good replacement so I kept the old code.</p>

---

## Post #6 by @lassoan (2021-08-04 02:27 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="19046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Draw effect is fairly heavily used in manual segmentations. I am not aware of a mode in scissors which allows me to draw and paint a polygon.</p>
</blockquote>
</aside>
<p>That’s why we still have both effects. If the Scissors effect would not apply the drawing immediately when the mouse button is released then you could draw polygons the same way as in the current Draw effect.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="19046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>While the proposal calls for closed curves from markups for this functionality, will it be as quick and efficient as the polygon tool in draw?</p>
</blockquote>
</aside>
<p>It may be faster and more efficient than that very very old single-threaded image rasterizing code and it will allow drawing thick slices, erasing, application to all segments, work on arbitrary slice orientations, etc. There is really no reason to maintain a completely separate, very limited Draw effect if the only unique feature is the delayed apply (polygon drawing).</p>
<p>In Scissors effect we will also be able to implement spline drawing, not just polyline (using a temporary curve node, similarly to Draw tube effect).</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="19046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>When I scroll to another slice offset (note the background volume is a finer resolution), then I cannot use the scissors tool anymore to modify the segment.</p>
</blockquote>
</aside>
<p>What you describe is the intended behavior. Only those voxels are filled which have their center inside the 3D closed surface that is generated by extruding the drawn contour by half of the current slice spacing in both directions. This image demonstrates the rationale for this (and why can you have empty regions when the drawing brush thickness is comparable or smaller than the slice thickness, with some more information <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">here</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b9a59c82675871d1ebd0b4b1644be81600c0021.png" data-download-href="/uploads/short-url/6dJe18c2bhUahMknDOzRLZNd0Vb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b9a59c82675871d1ebd0b4b1644be81600c0021.png" alt="image" data-base62-sha1="6dJe18c2bhUahMknDOzRLZNd0Vb" width="475" height="500" data-dominant-color="4D4C54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1166×1225 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You could try to implement some kind of “nearest neighbor” behavior for cases when the slice plane is aligned to the labelmap axis directions, but you would need to develop some kind of a generalized Bresenham algorithm for drawing planes in 3D binary images in arbitrary orientation with arbitrary thickness.</p>
<p>We don’t have such algorithm and I’m not sure if such algorithm exists at all (especially implemented in C++, open-source, with non-restrictive license), so if you really must work with such image and segmentation geometries then I would recommend to either set thick manual slice spacing (that’s what is used when you set slice cut thickness to 0) or set a larger slice cut thickness.</p>

---
