---
topic_id: 18628
title: "Contour Propagation Problems"
date: 2021-07-11
url: https://discourse.slicer.org/t/18628
---

# Contour propagation problems

**Topic ID**: 18628
**Date**: 2021-07-11
**URL**: https://discourse.slicer.org/t/contour-propagation-problems/18628

---

## Post #1 by @labixin (2021-07-11 13:21 UTC)

<p>Hello,</p>
<p>I have a CT image (CT1-moving image) with a manual contour (RT structure-dicom format), and another CT image (CT2-fixed image) with no contour. I have registered CT1 to CT2 using Elastix extension and got the displacement field as a Transform. Now I want to propagate the manual contour from CT1 to CT2.</p>
<p>I did it following these steps:</p>
<ol>
<li>Went to Transforms module’s “Apply transform” section, selected nodes in the “Transformable” node tree and clicked the green arrow buttons. [Through forward transform (Transform from parent)]</li>
<li>Harden transform in the “Transformed” node.</li>
<li>Went to Segmentations module’s “Representations” section and created Binary labelmap. Then update through “Planar contour–&gt;Closed surface–&gt;Binary labelmap” conversion path and changed Reference image geometry (source geometry) to CT2.</li>
</ol>
<p>I want to know if my steps are correct. Besides, I have two questions:</p>
<ol>
<li>It seemed that the contour is a bit different after “Harden transform” operation. Is this correct, and what’s the reason? I wonder how this works.</li>
<li>Is it necessary to change source geometry to CT2 if I want to get the propagated contour in CT2?</li>
</ol>
<p>Thanks in advance. Your help is highly appreciated.</p>
<p>Crayon</p>

---

## Post #2 by @lassoan (2021-07-12 14:35 UTC)

<p>What you did looks reasonable, but you can do it a bit simpler:</p>
<ul>
<li>right-click on transform column in Data module to apply a transform on a node, then right-click again there to harden</li>
<li>you can right-click on the segmentation node to create binary labelmap or closed surface representation (in recent Slicer Preview Releases)</li>
<li>you don’t need to set a reference geometry in advance, you can specify it in “Export to files…”</li>
</ul>
<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="18628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>It seemed that the contour is a bit different after “Harden transform” operation. Is this correct, and what’s the reason? I wonder how this works.</p>
</blockquote>
</aside>
<p>This is normal when you apply a non-linear transform on labelmap representation of a segmentation. When you dynamically apply a transform then the labelmap is resampled at the resolution of your screen. When you harden the transform then the labelmap is resampled at its original resolution, which is typically lower than your display’s resolution.</p>
<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="18628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Is it necessary to change source geometry to CT2 if I want to get the propagated contour in CT2?</p>
</blockquote>
</aside>
<p>If you use “Export to files…” then it is definitely not needed (you can get specify the CT2 in the Advanced options section). If you export to DICOM Segmentation Object then what matter is that the segmentation is in correct physical position (which it is), so you don’t need to change the source geometry before export. DICOM RT structure set is a very old and rigid format, which does store full 3D geometry just slice intersections of the 3D shape with image slices, therefore it requires matching of image slices and contours - but this resampling is probably performed automatically in the DICOM RT exporter.</p>

---
