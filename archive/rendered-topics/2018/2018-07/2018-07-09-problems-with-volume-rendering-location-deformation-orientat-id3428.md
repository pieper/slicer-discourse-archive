# Problems with volume rendering (location/deformation/orientation)

**Topic ID**: 3428
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/problems-with-volume-rendering-location-deformation-orientation/3428

---

## Post #1 by @torquil (2018-07-09 13:49 UTC)

<p>Hi! I’m new to Slicer 3d, so hopefully this is not a software problem, but only user error…</p>
<p>When I’m doing 3d segmentation, everything seems to work as expected, but when I try volume redering, the 3d volume seems to end up in the wrong position, deformed, and with incorrect orientation.</p>
<p>If I enable Crop in the volume rendering settings (and the ROI includes all the image areas in the the three projections), the 3d view contains nothing. I have to disable cropping for something to appear in the 3d view. If I show the ROI-cube in the 3d view, it is not located at the same place as the volume.</p>
<p>When I do a 3d segmentation first, and then do the volume rendering, the volume is not located at the same place in the 3d view as the 3d segmentation. I have attached a screenshot of this. The green skull is the segmentation, and the volume is located above, squeezed together, and not oriented in the same way as the segmentation.</p>
<p>I’m using Slider 3d nightly, and with CPU volume rendering. It is the same when using GPU volume rendering.</p>
<p>I also have some DICOM-data from a different CT, and in that case there is still a problem with the placement of the volume, but in that case it is not squeezed together (in that case the voxel size is uniform).</p>
<p>I’m on Windows 10 with a NVIDIA Quadro M2200 graphics card.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3803498cee9f9dd89e4f67d36989154abe41864.jpeg" data-download-href="/uploads/short-url/nkovpoHJt6cGdtxGWzqBD0w4vnS.jpg?dl=1" title="slicer_problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3803498cee9f9dd89e4f67d36989154abe41864_2_690x388.jpg" alt="slicer_problem" data-base62-sha1="nkovpoHJt6cGdtxGWzqBD0w4vnS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3803498cee9f9dd89e4f67d36989154abe41864_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3803498cee9f9dd89e4f67d36989154abe41864_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3803498cee9f9dd89e4f67d36989154abe41864_2_1380x776.jpg 2x" data-dominant-color="9E9FB3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_problem</span><span class="informations">1920×1080 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-07-09 17:25 UTC)

<p>Unfortunately, volume rendering does not support dynamic application of non-linear transforms. If you harden the transform (in Transforms module, click on <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bb418ca6291fd723caaf2e78e3ff0e234ca2e46.png" alt="image" data-base62-sha1="6eCnZlbbKXsBwfxiWlqHUH1Vr1Q" width="69" height="68"> then it will work correctly.</p>

---
