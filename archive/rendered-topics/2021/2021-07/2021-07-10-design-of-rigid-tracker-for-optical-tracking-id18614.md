# Design of rigid tracker for optical tracking

**Topic ID**: 18614
**Date**: 2021-07-10
**URL**: https://discourse.slicer.org/t/design-of-rigid-tracker-for-optical-tracking/18614

---

## Post #1 by @drvarunagarwal (2021-07-10 11:47 UTC)

<p>Hi,</p>
<p>I am trying to setup optitrack duo for optical tracking via slicer IGT.<br>
I am using motive to design tracker as guided in the plustoolkit guide.</p>
<p>My question is regarding pivot point of the tracker.</p>
<p>The reflective spheres are tracked by camera and motive recognizes these and  by default the pivot point is in the centre of geometry.<br>
However the point at which the tracker attaches to tool is somewhat away from this exact centre of geometry.<br>
Motive allows to change the pivot point of the tracker.</p>
<p>Should the pivot point of the geometry be this default centre point? or should it coincide with the point that the geometry attaches to the tool?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3873fc107648e741e3abace9daeabc0b6e00d706.jpeg" data-download-href="/uploads/short-url/83pewuSXRv3Lxsh99EZe9oT3tVI.jpeg?dl=1" title="IMG_3990" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3873fc107648e741e3abace9daeabc0b6e00d706_2_666x500.jpeg" alt="IMG_3990" data-base62-sha1="83pewuSXRv3Lxsh99EZe9oT3tVI" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3873fc107648e741e3abace9daeabc0b6e00d706_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3873fc107648e741e3abace9daeabc0b6e00d706_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3873fc107648e741e3abace9daeabc0b6e00d706_2_1332x1000.jpeg 2x" data-dominant-color="786D66"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_3990</span><span class="informations">4032×3024 1.97 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>which point In the image above, point A, B or C, should be set as pivot point? or it doesn’t matter?</p>
<p>Is this effect taken into account by the tool calibration algorithm? Does this have any effect on accuracy?</p>
<p>I hope I am clear on my question</p>
<p>Please advise.</p>

---

## Post #2 by @lassoan (2021-07-14 03:39 UTC)

<p>It does not matter how Motive chooses origin and axis directions of your marker, because you can get the transformation from the marker to your tooltip using Pivot calibration module of SlicerIGT extension (see <a href="http://www.slicerigt.org/wp/user-tutorial/">U-11 SlicerIGT tutorial</a>).</p>

---

## Post #3 by @drvarunagarwal (2021-07-14 03:56 UTC)

<p>thanks a lot for the guidance</p>

---
