# Save derived DTI heatmap

**Topic ID**: 3319
**Date**: 2018-06-27
**URL**: https://discourse.slicer.org/t/save-derived-dti-heatmap/3319

---

## Post #1 by @ssyip (2018-06-27 18:03 UTC)

<p>Hello, I have a question.</p>
<p>I was able to save my DTI 3D model as object (by saving it as vtk, obj, stl). In addition to the object file, I also want to save the heatmap. Specifically, I want to as the model and its corresponding heatmap (or colormap) so that I can open it using another program different from Slicer.</p>
<p>Does anyone know how to do that? Thank you!</p>

---

## Post #2 by @ihnorton (2018-06-27 18:38 UTC)

<p>(<a class="mention" href="/u/ssyip">@ssyip</a> I created a new topic)</p>
<aside class="quote no-group" data-username="ssyip" data-post="1" data-topic="3319">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3d9bf3/48.png" class="avatar"> ssyip:</div>
<blockquote>
<p>Specifically, I want to as the model and its corresponding heatmap (or colormap) so that I can open it using another program different from Slicer.</p>
</blockquote>
</aside>
<p>You can assign a scalar to the model in the Tractography Display module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/388b3faf885a8011b642aed84cec03c8018a3536.png" data-download-href="/uploads/short-url/84d4NLJYtfYY8MBnFIEwVbTdfRY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/388b3faf885a8011b642aed84cec03c8018a3536_2_690x459.png" alt="image" data-base62-sha1="84d4NLJYtfYY8MBnFIEwVbTdfRY" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/388b3faf885a8011b642aed84cec03c8018a3536_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/388b3faf885a8011b642aed84cec03c8018a3536.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/388b3faf885a8011b642aed84cec03c8018a3536.png 2x" data-dominant-color="E8EAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×644 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then use the export module discussed below, from the SlicerDMRI extension – it will preserve the assigned colors upon export:</p>
<aside class="quote" data-post="2" data-topic="3191">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/tractography-export-by-color/3191/2">Tractography export by color </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Please try the Export tractography to PLY (mesh) module, available in the SlicerDMRI extension in nightly builds (since early April). 
Note that we use PLY specifically because it supports color. 
Most software with STL import also supports PLY, but if you specifically need OBJ (supports color) or STL (no color) you can <a href="https://github.com/SlicerDMRI/SlicerDMRI/wiki/How-to-export-atlas-or-tractography-for-visualization-in-Blender">convert in MeshLab</a>.
  </blockquote>
</aside>


---
