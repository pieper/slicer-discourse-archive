# MRI abdominal fat slice quantification

**Topic ID**: 11029
**Date**: 2020-04-07
**URL**: https://discourse.slicer.org/t/mri-abdominal-fat-slice-quantification/11029

---

## Post #1 by @drobnizs (2020-04-07 14:01 UTC)

<p>Hi All,</p>
<p>Operating system: macOS Catalina Version 10.15.4<br>
Slicer version: Slicer.4.10.2<br>
Expected behavior: I would like quantify fat volume on single slice abdominal MRI image. For some patients the dicom file properly loads, and I can quantify.<br>
Actual behavior: However, for some, the dicom file does not load completely, but i can scroll through the full image (example attached) The same image fully appears in Osirix, therefore i suspect the dicom file itself is not corrupted. The main difference than can occur between the properly loaded and not loaded images is that in some cases, the plane is rotated (see attached image), therefore the axial slice is not a true axial one.<br>
Moreover, if I open the Error log, this is what i can find: “Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 7.62242e-06 mm, tolerance threshold is 0.001 mm).”</p>
<p>Could you please help me out?<br>
Really appreciate it,<br>
Zsofi<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d282fe94aae6dbde70ac47bbc8468707c1b1dd8d.png" data-download-href="/uploads/short-url/u2gVetNdqHS3rq9XXEE4mIwWVTD.png?dl=1" title="Screen Shot 2020-04-06 at 10.14.14 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d282fe94aae6dbde70ac47bbc8468707c1b1dd8d_2_690x373.png" alt="Screen Shot 2020-04-06 at 10.14.14 PM" data-base62-sha1="u2gVetNdqHS3rq9XXEE4mIwWVTD" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d282fe94aae6dbde70ac47bbc8468707c1b1dd8d_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d282fe94aae6dbde70ac47bbc8468707c1b1dd8d_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d282fe94aae6dbde70ac47bbc8468707c1b1dd8d_2_1380x746.png 2x" data-dominant-color="33333C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-06 at 10.14.14 PM</span><span class="informations">1882×1020 57.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35ddaa9c1f5a5ed09ac6e7d891712dfd160a28bc.jpeg" data-download-href="/uploads/short-url/7GwdTrCVQjpu0HbyWHUPXtzCmfy.jpeg?dl=1" title="Screen Shot 2020-04-06 at 10.04.09 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35ddaa9c1f5a5ed09ac6e7d891712dfd160a28bc_2_690x270.jpeg" alt="Screen Shot 2020-04-06 at 10.04.09 PM" data-base62-sha1="7GwdTrCVQjpu0HbyWHUPXtzCmfy" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35ddaa9c1f5a5ed09ac6e7d891712dfd160a28bc_2_690x270.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35ddaa9c1f5a5ed09ac6e7d891712dfd160a28bc_2_1035x405.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35ddaa9c1f5a5ed09ac6e7d891712dfd160a28bc_2_1380x540.jpeg 2x" data-dominant-color="393939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-06 at 10.04.09 PM</span><span class="informations">1746×684 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-04-07 15:36 UTC)

<p>This is an oblique acquisition, so you need to align the view to the data.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e4caf730c7b3f1e772f46284a888259ccb45b1a.png" alt="image" data-base62-sha1="6BAgcdGIJJGP3b2jo75W2qKWoPg" width="643" height="104"></p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<aside class="quote quote-modified" data-post="1" data-topic="8032">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rotate-to-volume-plane/8032">Rotate to volume plane</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Maybe someone has already asked this question before, but I could not find it in one of the topics on this forum. 
I’ve noticed that sometimes when I load a serie of dicom’s that they are not always properly displayed in the viewports. What I mean is that they are rotated more or less, so I have to use the ‘Rotate to volume plane’ function to correct this. I try to make it a routine do check this first before doing anything else, but is there a specific reason why this happens and if yes, is it …
  </blockquote>
</aside>


---

## Post #3 by @drobnizs (2020-04-07 20:02 UTC)

<p>Thank you Steve for your quick reply!!!</p>

---

## Post #4 by @drobnizs (2020-04-14 23:17 UTC)

<p>Steve, another question. I only have one slice, but i get volume results in the Segment Statistics. How can I get only area data? I tried the Segement Statistics - Advanced - Closed Surface Statistics - Surface mm2 this option on, but still i dont get it in the table.</p>
<p>Thank you</p>

---

## Post #5 by @pieper (2020-04-15 13:46 UTC)

<p>We always work in 3D, so one slice is really like a slab.  So you would need to divide the volume by the slice spacing to get the area.</p>
<p>Best,<br>
Steve</p>

---

## Post #6 by @lassoan (2020-04-19 05:37 UTC)

<p>I’ve added a new module yesterday that computes cross-section areas for each slice of a segmentation - see <a href="https://discourse.slicer.org/t/compute-surface-area-in-segment-based-on-hounsfield-units-ct-images/11167/2">here</a>. It is a bit of an overkill for a single slice, but it should work well .</p>
<p>To get it, you need to download Slicer Preview Release revision 28984 (or later) and download Sandbox extension from Examples category.</p>

---

## Post #7 by @drobnizs (2020-04-20 12:32 UTC)

<p>Thank you so much again!</p>

---
