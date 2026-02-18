# How to provide global coordinate system after crop volume segment?

**Topic ID**: 1199
**Date**: 2017-10-09
**URL**: https://discourse.slicer.org/t/how-to-provide-global-coordinate-system-after-crop-volume-segment/1199

---

## Post #1 by @deepmech (2017-10-09 10:47 UTC)

<p>After segmenting any bone or ligament, is there any provision to change the coordinates of the part?<br>
because when we import this file to any other finite element package it reads the global coordinate system .</p>

---

## Post #2 by @lassoan (2017-10-09 14:05 UTC)

<p>Export segments to model nodes (using Segmentations module, Export/import section) and apply transform to a model (using Transforms module) to move it around. Either use sliders to change the transform or enable Interaction/Visible in 3D view to move it interactively in 3D.</p>
<p>If you see that first two axes of the exported model are inverted the apply a diag(-1,-1,1,1) transformation matrix on the models before you export.</p>

---

## Post #3 by @lassoan (2017-10-09 16:15 UTC)

<p>Note that while cropping affects voxel coordinates, physical coordinates are always preserved in Slicer in any editing operation. Make sure that the external software you use works in physical coordinates, too (use image origin, spacing, and axis directions to scale and position the volume).</p>

---

## Post #4 by @deepmech (2017-10-09 16:27 UTC)

<p>thankyou sir<br>
i am trying it to convert but the matrix mention there is only linear transformation not rotational matrix.  when i rotated only LR  by 90 degree it also translate, that i want to know why?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa9bba28a22eeee0812b9526c8f8903c975aa8c1.png" data-download-href="/uploads/short-url/zKZ0IrySoPrhHJ2Fz8HCkPen9o5.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9bba28a22eeee0812b9526c8f8903c975aa8c1_2_690x349.png" alt="Capture" data-base62-sha1="zKZ0IrySoPrhHJ2Fz8HCkPen9o5" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9bba28a22eeee0812b9526c8f8903c975aa8c1_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9bba28a22eeee0812b9526c8f8903c975aa8c1_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9bba28a22eeee0812b9526c8f8903c975aa8c1_2_1380x698.png 2x" data-dominant-color="C4C5E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1383×701 56.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2017-10-09 17:04 UTC)

<p>This looks like RAS/LPS mismatch. See solution in this post:</p>
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
