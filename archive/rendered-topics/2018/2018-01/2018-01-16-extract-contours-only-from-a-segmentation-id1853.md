# Extract contours only from a segmentation

**Topic ID**: 1853
**Date**: 2018-01-16
**URL**: https://discourse.slicer.org/t/extract-contours-only-from-a-segmentation/1853

---

## Post #1 by @giuseppe.cardone (2018-01-16 12:03 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.8.1</p>
<p>Hi, I am a new users of 3D Slicers. I have to use it to extract a geometry from a CT-Angiography. This geometry has to be as simple as possible because I should modify it on a CAD software (Solidworks).<br>
My idea was to extract only the contour of each slice (like polylines) with the segmentation tool of 3D Slicer. However, with this tool I can only export mesh objects that are more difficult to modify in Solidworks. There is a way to extract only the contours of the segmentation like an .iges file for example?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2018-01-16 13:42 UTC)

<p>In general, you cannot edit arbitrary shapes in generic CAD software. Tools that import surface meshes into solid objects in CAD software are usually intended for reconstructing relatively simple shapes.</p>
<p>One of the main reasons we developed Slicer’s Segment Editor module was to allow editing of arbitrary anatomical shapes (in accordance with the original image data) and combine them with CAD models. There are some nice <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">tutorials</a> on how to do this and we are happy to help with any specific questions that you may have.</p>

---

## Post #3 by @giuseppe.cardone (2018-01-16 13:54 UTC)

<p>Thank you Andras.<br>
I extracted a 3D model of the system subclavian vein-superior vena cava-right atrium and I want to modifiy it through a CAD software in order to have a smoother and more regular geometry.</p>
<p>Thank you for you answer.</p>

---

## Post #4 by @lassoan (2018-01-16 14:03 UTC)

<p>You can use Smoothing effect in Segment editor module (and experiment with different methods and parameters in it) to make the geometry more regular. You can also further smooth the mesh and reduce number of polygons when you create the 3D closed surface representation (by adjusting parameters in Segmentations module, Representations section, Closed surface row, Update button).</p>
<p>You can also generate tetrahedral mesh of the vasculature directly from the segmentation, using Segment Mesher extension (that uses Cleaver2 or TetGen internally).</p>
<p>What is your end goal? Finite-element analysis, direct 3D printing, 3D printing of mold, …?</p>

---

## Post #5 by @giuseppe.cardone (2018-01-16 16:31 UTC)

<p>My final goal is the 3D printing of the vein but smoother and more regular (not a lot of variation of the lumen)</p>

---

## Post #6 by @cpinter (2018-01-16 18:35 UTC)

<p>This video tutorial may help:</p><aside class="quote quote-modified" data-post="1" data-topic="700">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-video-tutorial-for-segment-editor-lumbar-spine-segmentation-for-3d-printing/700">New video tutorial for Segment editor - lumbar spine segmentation for 3D printing</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is the first part of a video tutorial series that teaches how to use Segment editor. This tutorial explains how to create a 3D-printable lumbar spine segment that can be used for lumbar puncture training: 

The video tutorial was created by Hilary Lia (PerkLab, Queen’s University), with help from <a class="mention" href="/u/cpinter">@cpinter</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/ungi">@ungi</a>. 
Please post your comments here about how useful this tutorial format is, what did you like/what to improve, what topics/techniques/anatomical structures you would be int…
  </blockquote>
</aside>

<p>The Smoothing effect in Segment Editor (see at 5:00 in video) can make your model more suitable for 3D printing.</p>

---

## Post #7 by @lassoan (2018-01-16 19:30 UTC)

<aside class="quote no-group" data-username="giuseppe.cardone" data-post="5" data-topic="1853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/a88e57/48.png" class="avatar"> giuseppe.cardone:</div>
<blockquote>
<p>not a lot of variation of the lumen</p>
</blockquote>
</aside>
<p>Smoothing should fix that. You can also use VMTK extension’s level set segmentation to get a nicely smoothed vessel wall.</p>
<p>If you want to print a shell (so that you can try placement of intravascular devices) then you can create that easily in Segment Editor:</p>
<ul>
<li>Go to Logical operators effect, set Overwrite other segments = None in Masking section (to allow segments to overlap)</li>
<li>Create a new segment and copy the existing vessel lumen segment into it</li>
<li>Grow the new segment using Margin effect, by as much as shell thickness you would like to have</li>
<li>Subtract the original vessel lumen segment from the enlarged segment using Logical operators effect</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8405f57a90dfa8eaccc0e38def2a4ccfe9ad9bc7.jpeg" data-download-href="/uploads/short-url/iPVNaeWUNj19A7Ruzz9gyX8PAd9.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8405f57a90dfa8eaccc0e38def2a4ccfe9ad9bc7_2_690x373.jpg" alt="image" data-base62-sha1="iPVNaeWUNj19A7Ruzz9gyX8PAd9" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8405f57a90dfa8eaccc0e38def2a4ccfe9ad9bc7_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8405f57a90dfa8eaccc0e38def2a4ccfe9ad9bc7_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8405f57a90dfa8eaccc0e38def2a4ccfe9ad9bc7_2_1380x746.jpg 2x" data-dominant-color="808086"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 379 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc346556c9f910909258adf83dcb8859433201bc.png" alt="image" data-base62-sha1="qQW1mKsP6vAQ3itI7o0ztLwP3e4" width="679" height="446"></p>

---

## Post #8 by @giuseppe.cardone (2018-01-16 20:18 UTC)

<p>Thank you!<br>
This will be very useful!</p>

---

## Post #9 by @giuseppe.cardone (2018-01-16 20:19 UTC)

<p>Thank you! I will try!</p>

---
