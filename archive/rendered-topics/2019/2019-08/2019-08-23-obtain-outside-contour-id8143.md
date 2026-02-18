# Obtain outside contour

**Topic ID**: 8143
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/obtain-outside-contour/8143

---

## Post #1 by @mikecsu (2019-08-23 07:27 UTC)

<p>Operating system: win10<br>
Slicer version: slicer 4.10.0 /4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,there . I would like know if i can segment the skin of a head CT images  with the help of “Segmenteditor module”, i want the outside contour of the head,  and there are many tools i<br>
can use, but  i don’t know which one can perfectly do this work ?( i know i can simply use<br>
pure manual segmentation method,s like draw、paint… but it is time-consuming)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1f25cddf5983c0ab50bba57206d5ce61d0eb4dc.jpeg" data-download-href="/uploads/short-url/n6E8dzSQ88VzMk1LgUlqg5Mf7k0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f25cddf5983c0ab50bba57206d5ce61d0eb4dc_2_690x397.jpeg" alt="image" data-base62-sha1="n6E8dzSQ88VzMk1LgUlqg5Mf7k0" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f25cddf5983c0ab50bba57206d5ce61d0eb4dc_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f25cddf5983c0ab50bba57206d5ce61d0eb4dc_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1f25cddf5983c0ab50bba57206d5ce61d0eb4dc_2_1380x794.jpeg 2x" data-dominant-color="969AB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2354×1355 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be appreciated.</p>

---

## Post #2 by @JanWitowski (2019-08-23 13:20 UTC)

<p>I think a good starting point would be to threshold whole head:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76bb3b7c2ea86e70408d871d340710cfa1d102a3.png" data-download-href="/uploads/short-url/gWlu4lyouGtidDxsu28XEEJhSsX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76bb3b7c2ea86e70408d871d340710cfa1d102a3_2_690x372.png" alt="image" data-base62-sha1="gWlu4lyouGtidDxsu28XEEJhSsX" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76bb3b7c2ea86e70408d871d340710cfa1d102a3_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76bb3b7c2ea86e70408d871d340710cfa1d102a3_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76bb3b7c2ea86e70408d871d340710cfa1d102a3_2_1380x744.png 2x" data-dominant-color="869490"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2544×1374 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And then use Hollow to get the outer layer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da7c33debb90c86f46873d57dc4c65ea9fd1369b.jpeg" data-download-href="/uploads/short-url/vaObRT7Od4XoOuIXQsGcdEJURuP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da7c33debb90c86f46873d57dc4c65ea9fd1369b_2_690x374.jpeg" alt="image" data-base62-sha1="vaObRT7Od4XoOuIXQsGcdEJURuP" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da7c33debb90c86f46873d57dc4c65ea9fd1369b_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da7c33debb90c86f46873d57dc4c65ea9fd1369b_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da7c33debb90c86f46873d57dc4c65ea9fd1369b_2_1380x748.jpeg 2x" data-dominant-color="686B6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1390 439 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This requires minor manual processing but should get you a satisfying result within a few minutes:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/012463558b34e15c578ded44191df1db9f00f9ab.jpeg" data-download-href="/uploads/short-url/a6rbpu9WNXh14CfaD2YcUtp7Ht.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/012463558b34e15c578ded44191df1db9f00f9ab_2_690x233.jpeg" alt="image" data-base62-sha1="a6rbpu9WNXh14CfaD2YcUtp7Ht" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/012463558b34e15c578ded44191df1db9f00f9ab_2_690x233.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/012463558b34e15c578ded44191df1db9f00f9ab_2_1035x349.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/012463558b34e15c578ded44191df1db9f00f9ab_2_1380x466.jpeg 2x" data-dominant-color="4E575A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1907×644 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2019-08-23 16:39 UTC)

<p>This segmentation recipe may also help: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface/" rel="nofollow noopener">https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface/</a></p>
<p>Also, a new “surface solidify” extension will be added to Slicer very soon, which may further automate the process (see status <a href="https://github.com/Slicer/ExtensionsIndex/pull/1655" rel="nofollow noopener">here</a>).</p>

---

## Post #4 by @mikecsu (2019-08-26 03:18 UTC)

<p>It  did work. Thank you .</p>

---
