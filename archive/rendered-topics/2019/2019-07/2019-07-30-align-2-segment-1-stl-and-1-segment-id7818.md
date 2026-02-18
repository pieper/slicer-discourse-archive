# Align 2 segment 1 stl and 1 segment

**Topic ID**: 7818
**Date**: 2019-07-30
**URL**: https://discourse.slicer.org/t/align-2-segment-1-stl-and-1-segment/7818

---

## Post #1 by @Jmarcs (2019-07-30 18:40 UTC)

<p>Is there a solution to align 2 objects (1 STL IMPORT and 1 segment )with a lot of acurate<br>
Maybe an extention.<br>
thanks a lot for your advice<br>
jean-marc<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e75f051595f5164bd9cdce5c05728bf9150f05f5.png" data-download-href="/uploads/short-url/x0NSeG35QJ1kpmhL4XMhn0Yfa17.png?dl=1" title="align" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e75f051595f5164bd9cdce5c05728bf9150f05f5_2_690x411.png" alt="align" data-base62-sha1="x0NSeG35QJ1kpmhL4XMhn0Yfa17" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e75f051595f5164bd9cdce5c05728bf9150f05f5_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e75f051595f5164bd9cdce5c05728bf9150f05f5_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e75f051595f5164bd9cdce5c05728bf9150f05f5.png 2x" data-dominant-color="6D7F74"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">align</span><span class="informations">1164×694 387 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-07-30 20:14 UTC)

<p>You can align two segments using Segment Registration extension or two models using Model registration module in SlicerIGT extension. Both modules require that the segments contain approximately the same content (especially Segment Registration is sensitive to this) and that they are initialized close to the correct position (especially Model registration is sensitive to this).</p>
<p>You can also register based on manually placed anatomical landmarks using Fiducial registration wizard module in SlicerIGT extension.</p>

---

## Post #3 by @Jmarcs (2019-08-01 11:30 UTC)

<p>I try with fiducial registration wizard but sometimes works sometimes not why  ? My goal is to export the the 2 files models stl wich are align like my picture  thanks<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eacc3dddb91715a9c81b53e26ac10f256a9356c4.jpeg" data-download-href="/uploads/short-url/xv7jsndcOWP6z7htUqPVS87VP1i.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eacc3dddb91715a9c81b53e26ac10f256a9356c4_2_690x328.jpeg" alt="1" data-base62-sha1="xv7jsndcOWP6z7htUqPVS87VP1i" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eacc3dddb91715a9c81b53e26ac10f256a9356c4_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eacc3dddb91715a9c81b53e26ac10f256a9356c4_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eacc3dddb91715a9c81b53e26ac10f256a9356c4_2_1380x656.jpeg 2x" data-dominant-color="93909D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1895×902 430 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @rkikinis (2019-08-01 11:47 UTC)

<p>Since you are dealing with rigid objects, you might try the interactive registration: sliders in the transforms module allow you to interactively move one of the two maxillae interactively. Then harden the transform in the data module.</p>

---

## Post #5 by @Jmarcs (2019-08-01 13:01 UTC)

<p>Sorry but what is différence between harden and transform</p>

---

## Post #6 by @rkikinis (2019-08-01 13:55 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms</a></p>
<p>"If a non-linear transform is hardened on a volume then the volume is resampled using the same spacing and axis directions as the original volume (using linear interpolation). Extents are updated to fully contain the transformed volume.”</p>
<p>The transform gets integrated into the model, instead of just being applied.</p>

---

## Post #7 by @Juicy (2019-08-03 02:05 UTC)

<div class="lazyYT" data-youtube-id="hsZrjNsXZbs" data-youtube-title="3K Surface Registration" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>I found this useful for aligning two models.</p>
<p>Also if you double click on those small grid icons (the transform icons which you have circled in red) you can harden them from the pop up menu.</p>
<p>Harden means you fully apply the transformation and the model position is updated.</p>

---
