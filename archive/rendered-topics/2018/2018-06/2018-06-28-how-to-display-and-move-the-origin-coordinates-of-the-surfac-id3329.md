---
topic_id: 3329
title: "How To Display And Move The Origin Coordinates Of The Surfac"
date: 2018-06-28
url: https://discourse.slicer.org/t/3329
---

# How to display and move the origin coordinates of the surface model (.STL)

**Topic ID**: 3329
**Date**: 2018-06-28
**URL**: https://discourse.slicer.org/t/how-to-display-and-move-the-origin-coordinates-of-the-surface-model-stl/3329

---

## Post #1 by @Yuta (2018-06-28 14:49 UTC)

<p>Operating system: WINDOWS<br>
Slicer version: 4.8.1</p>
<p>thank you for the outstanding work with 3DSlicer</p>
<p>Expected behavior:<br>
I want to set the origin (0, 0, 0) of the coordinates to an arbitrary position of the segmented bone using the transform modules. Then I want to convert it to STL file in its coordinate system. For example, it is possible to create a skeleton model smoothly by setting the origin coordinates in the femoral head.</p>
<p>Actual behavior:<br>
I do not know how to display the origin of the segmented bone model on the 3D slicer. In addition even if I use the transform module it will not be reflected in the stl file.<br>
segmentation model&gt; transform&gt; Transformed nodes&gt; Right arrow&gt; segmentation&gt; Export model&gt; save segment.stl<br>
Show an image with the STL file created with 3Dslicer opened with another software below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7688495ae6f184a44ff3d367dd0fcfcb02a196e.png" data-download-href="/uploads/short-url/nSXFiGIuL4NJx4WcuWORF3DNcwS.PNG?dl=1" title="femur" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7688495ae6f184a44ff3d367dd0fcfcb02a196e_2_690x278.PNG" alt="femur" data-base62-sha1="nSXFiGIuL4NJx4WcuWORF3DNcwS" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7688495ae6f184a44ff3d367dd0fcfcb02a196e_2_690x278.PNG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7688495ae6f184a44ff3d367dd0fcfcb02a196e_2_1035x417.PNG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7688495ae6f184a44ff3d367dd0fcfcb02a196e.png 2x" data-dominant-color="3D3D78"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">femur</span><span class="informations">1222×493 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
You can see that the origin is far away.</p>
<p>Thank you very much for your help!</p>

---

## Post #2 by @pieper (2018-10-11 19:54 UTC)

<p>By default Slicer will leave the model in <a href="https://www.slicer.org/wiki/Coordinate_systems">patient coordinates</a>.</p>
<p>But if you put the model under a transform you can move it around with the Transforms module and then Harden it using the transform tab of the Data module.  Once hardened you can save it out to STL with the updated vertices.</p>

---
