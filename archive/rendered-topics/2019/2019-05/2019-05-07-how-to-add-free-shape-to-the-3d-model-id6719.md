# How to Add free shape to the 3D model

**Topic ID**: 6719
**Date**: 2019-05-07
**URL**: https://discourse.slicer.org/t/how-to-add-free-shape-to-the-3d-model/6719

---

## Post #1 by @Eloi (2019-05-07 13:37 UTC)

<p>Operating system: Windows 10 64 bit<br>
Slicer version: 4.10</p>
<p>Hello, I want to add a square shape to a 3D model, in oder to compete my form. How to “draw” it or to import a dedicated shape ?<br>
Currently, I use FreeCad to paste a form, but the contours are not smooth enough. We are working on an acoustic biomechanical model. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00013d366c053a3db3c2eabac5acd660928a0408.jpeg" data-download-href="/uploads/short-url/2EAZtHjkLHoD8zf2M5kVEigPu.jpeg?dl=1" title="etapes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00013d366c053a3db3c2eabac5acd660928a0408_2_666x500.jpeg" alt="etapes" data-base62-sha1="2EAZtHjkLHoD8zf2M5kVEigPu" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/00013d366c053a3db3c2eabac5acd660928a0408_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00013d366c053a3db3c2eabac5acd660928a0408.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00013d366c053a3db3c2eabac5acd660928a0408.jpeg 2x" data-dominant-color="8A8C8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">etapes</span><span class="informations">960×720 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> I want to “stick” the square at one end of the canal.<br>
Thanks</p>

---

## Post #2 by @ryanalex (2019-05-07 18:20 UTC)

<p>You can try some of the basic 3D modelling software for this purpose, if you go directly with the advanced software options, it will be very difficult to learn basic stuff. You can refer some top websites for simpler options, try using blender as well.</p>

---

## Post #3 by @lassoan (2019-05-07 22:39 UTC)

<p>You can import models created in Blender, FreeCAD, etc. saved in STL, PLY, OBJ, … format. If you need to represent finer details in your segmentation then <a href="https://discourse.slicer.org/t/segmentation-file-working-slowly/6670/6">adjust your segmentation’s geometry</a> (use oversampling factor &gt; 1.0 and enable isotropic spacing).</p>
<p>You can create simple models (sphere, cylinder, box, etc.) in Slicer using “Create models” module in SlicerIGT extension.</p>
<p>You can also create box or cylinder using Scissors effect in Segment Editor module (choose shape: Circle or Rectangle). If you paint in slice view, then you can paint only behind, in front of, or centered on a slice view.</p>

---

## Post #4 by @samjonas (2019-05-08 09:47 UTC)

<p>Blender would be my preference for this requirement</p>

---

## Post #5 by @lassoan (2019-05-08 12:53 UTC)

<p>You can also define a box with Annotation. ROI and fill it with VolumeClip extension.</p>
<p>You can make free-form blobs (with smooth are sharp edges) using Surface cut effect (appears in Segment Editor if you install SegmentEditorExtraEffects extension).</p>
<p>Blender is great and really powerful but as much I understand the task, Blender would be an overkill for this. By relying on two applications instead of just one, the workflow would become more complicated than necessary (especially if you want to adjust the model size dynamically, based on how it fits into the image).</p>

---
