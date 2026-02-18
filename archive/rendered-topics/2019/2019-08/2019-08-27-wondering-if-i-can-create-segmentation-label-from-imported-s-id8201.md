# Wondering if I can create segmentation label from imported STL object?

**Topic ID**: 8201
**Date**: 2019-08-27
**URL**: https://discourse.slicer.org/t/wondering-if-i-can-create-segmentation-label-from-imported-stl-object/8201

---

## Post #1 by @Shangcheng_Wang (2019-08-27 20:57 UTC)

<p>Hi community,</p>
<p>I had a MRI data set and segmented bone models in STL format. Could I create segmentation label from these 3D models?</p>
<p>I also imported a cylindrical pin (create from CAD software) into slicer, and I am wondering I could map the pin into segmentation label. So I can see if the pin would damage tendon or muscle on its path.</p>
<p>Any idea or comment?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-08-27 23:45 UTC)

<p>You can convert a model to segmentation mode by right-clicking on it in Data module then choosing conversion to segmentation.</p>
<p>You can also import models to existing segmentation node using Segmentations module.</p>

---

## Post #3 by @Shangcheng_Wang (2019-08-28 15:05 UTC)

<p>Hi Andras,</p>
<p>I am able to convert model to segment node, but I can not see it in slice and 3D, see picture below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98746bf7ed1f7149c28fd3dbf2d01d1803188039.png" data-download-href="/uploads/short-url/lKG0uBmhUkh7341uUosNC5cQFS1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98746bf7ed1f7149c28fd3dbf2d01d1803188039_2_690x382.png" alt="image" data-base62-sha1="lKG0uBmhUkh7341uUosNC5cQFS1" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98746bf7ed1f7149c28fd3dbf2d01d1803188039_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98746bf7ed1f7149c28fd3dbf2d01d1803188039_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98746bf7ed1f7149c28fd3dbf2d01d1803188039.png 2x" data-dominant-color="8E9191"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×643 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks<br>
Sam</p>

---

## Post #4 by @lassoan (2019-08-28 17:39 UTC)

<p>Probably the STL file is defined in LPS coordinate system. Slicer assumes it is in RAS. Try transforming the model from LPS to RAS coordinate system by applying a transform as described here:</p>
<aside class="quote quote-modified" data-post="7" data-topic="717">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dicom-and-vtk-file-orientation-issue/717/7">DICOM and VTK file orientation Issue</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Most common issue is LPS/RAS coordinate system mismatch. So, may try to convert your data from LPS to RAS coordinate system by transforming it using Transforms module by a matrix that has [-1,-1,1,1] in the diagonal: 
[image]
  </blockquote>
</aside>


---

## Post #5 by @Shangcheng_Wang (2019-08-28 20:18 UTC)

<p>Hi, you are right. That solves my problem. Thanks very much.</p>
<p>Sam</p>

---
