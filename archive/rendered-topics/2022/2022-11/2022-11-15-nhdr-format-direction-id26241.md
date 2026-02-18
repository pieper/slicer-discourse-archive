# NHDR Format direction

**Topic ID**: 26241
**Date**: 2022-11-15
**URL**: https://discourse.slicer.org/t/nhdr-format-direction/26241

---

## Post #1 by @seyang (2022-11-15 06:36 UTC)

<p>Someone can help me to set the direction for NHDR Format?<br>
This is a micro CT image (360 degrees). when I import the NGDR format after making it, it displayed the wrong position.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c09aa588d56c368270200021642cdef055466e84.png" data-download-href="/uploads/short-url/rtR0cdOsqc1aVmRbrKk6HNAq8m0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c09aa588d56c368270200021642cdef055466e84_2_690x164.png" alt="image" data-base62-sha1="rtR0cdOsqc1aVmRbrKk6HNAq8m0" width="690" height="164" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c09aa588d56c368270200021642cdef055466e84_2_690x164.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c09aa588d56c368270200021642cdef055466e84_2_1035x246.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c09aa588d56c368270200021642cdef055466e84.png 2x" data-dominant-color="62615F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×329 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b154823f3c9da61c3b32d75769b5d7e7c80bbe.png" data-download-href="/uploads/short-url/c5e2cA7dv0GR9oF3udQn7esARQO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b154823f3c9da61c3b32d75769b5d7e7c80bbe_2_690x164.png" alt="image" data-base62-sha1="c5e2cA7dv0GR9oF3udQn7esARQO" width="690" height="164" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b154823f3c9da61c3b32d75769b5d7e7c80bbe_2_690x164.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b154823f3c9da61c3b32d75769b5d7e7c80bbe_2_1035x246.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b154823f3c9da61c3b32d75769b5d7e7c80bbe_2_1380x328.png 2x" data-dominant-color="676765"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1380×328 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to crop x-y-z like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dee03aed7a31a95ea06b620642aeae41128ec9d.jpeg" data-download-href="/uploads/short-url/4gLMZcq2zHhcnDmmPkT9TAZHQiV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dee03aed7a31a95ea06b620642aeae41128ec9d_2_690x138.jpeg" alt="image" data-base62-sha1="4gLMZcq2zHhcnDmmPkT9TAZHQiV" width="690" height="138" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dee03aed7a31a95ea06b620642aeae41128ec9d_2_690x138.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dee03aed7a31a95ea06b620642aeae41128ec9d_2_1035x207.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dee03aed7a31a95ea06b620642aeae41128ec9d_2_1380x276.jpeg 2x" data-dominant-color="3F3F3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1622×326 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcc92523b31ef8b1c76e9e15f6db7afeefefa9be.jpeg" data-download-href="/uploads/short-url/qW4InsWaeCeuwG9xTHeu74GvYwC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcc92523b31ef8b1c76e9e15f6db7afeefefa9be_2_690x164.jpeg" alt="image" data-base62-sha1="qW4InsWaeCeuwG9xTHeu74GvYwC" width="690" height="164" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcc92523b31ef8b1c76e9e15f6db7afeefefa9be_2_690x164.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcc92523b31ef8b1c76e9e15f6db7afeefefa9be_2_1035x246.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcc92523b31ef8b1c76e9e15f6db7afeefefa9be.jpeg 2x" data-dominant-color="201F1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×326 58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>NRRD0004<br>
type: unsigned short<br>
dimension: 3<br>
space: LPS<br>
sizes: 2000 1718 361<br>
space directions: (0.027,0,0) (0,0.027,0) (0,0,0.027)<br>
endian: little<br>
encoding: raw<br>
datafile: projection%04d.raw 0 360 1</p>
<p>Is it any require additional item?<br>
Thanks to the 3d slicer development team, I am using this program well.</p>

---

## Post #2 by @muratmaga (2022-11-15 06:41 UTC)

<p>What you have in the first set of pictures (white background) are the shadow (projection) images. Those are X-rays collected in the scanner by changing the samples orientation by small rotations. By themselves they are not useful for anything. From them, cross-sectional slices of the object are “reconstructed” using an algorithm (typically Feldcamp backprojection).</p>
<p>It is these cross-sectional slices (second set of pictures with dark background) that is usable by Slicer. You can virtually reconstruct the 3D object using visualization techniques. Or segment parts of it.</p>
<p>You can’t do any of that on projection images.</p>

---

## Post #3 by @seyang (2022-11-15 07:10 UTC)

<p>Ok got it. Currently, it can’t use in the 3d slicer software.<br>
Thanks a lot.</p>

---

## Post #4 by @lassoan (2022-11-15 12:07 UTC)

<p>You should be able to reconstruct a 3D Cartesian volume in your scanner software (or reconstruct yourself using <a href="https://www.openrtk.org/">RTK</a>) and that image will be usable in Slicer.</p>

---
