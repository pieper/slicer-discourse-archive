# 3D volumetric reconstruction from 2D images with 6DOF information offline

**Topic ID**: 23783
**Date**: 2022-06-09
**URL**: https://discourse.slicer.org/t/3d-volumetric-reconstruction-from-2d-images-with-6dof-information-offline/23783

---

## Post #1 by @RealBrandonChen (2022-06-09 06:03 UTC)

<p>Hello, Does anyone know if I can reconstruct a 3D volumetric image with 2D images, of which the world coordinates and the rotation matrix (yaw, pitch, and row) are known? I want to do something like what SlicerIGT does, but I already have the images and 6DOF data and want to process them offline.<br>
Any suggestions would be appreciated!</p>

---

## Post #2 by @RealBrandonChen (2022-06-09 06:39 UTC)

<p>Hello guys,</p>
<p>To better understand, the ultrasound images and the world coordinates are attached for your reference. Thanks! <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> As you might notice, the coordinates are recorded by time series, i.e., 5fps.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c725f7a30710c2152a72e8d555c71f949022f42a.png" alt="US0" data-base62-sha1="spKmoEnspuoPm7YLUY8QkMYxDwm" width="321" height="408"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1db93dc4261c9dd9a33ebb9c001c91e36d229bb.png" data-download-href="/uploads/short-url/pnoXdgxyNQogy0X6Mk38HeuZ1Mv.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db93dc4261c9dd9a33ebb9c001c91e36d229bb_2_690x342.png" alt="1" data-base62-sha1="pnoXdgxyNQogy0X6Mk38HeuZ1Mv" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db93dc4261c9dd9a33ebb9c001c91e36d229bb_2_690x342.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db93dc4261c9dd9a33ebb9c001c91e36d229bb_2_1035x513.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db93dc4261c9dd9a33ebb9c001c91e36d229bb_2_1380x684.png 2x" data-dominant-color="DBDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1490×740 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
