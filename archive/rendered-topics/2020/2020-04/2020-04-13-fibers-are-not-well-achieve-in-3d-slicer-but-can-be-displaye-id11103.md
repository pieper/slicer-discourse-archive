# Fibers are not well achieve in 3D Slicer but can be displayed in DTI Studio

**Topic ID**: 11103
**Date**: 2020-04-13
**URL**: https://discourse.slicer.org/t/fibers-are-not-well-achieve-in-3d-slicer-but-can-be-displayed-in-dti-studio/11103

---

## Post #1 by @researchtomliu (2020-04-13 16:05 UTC)

<p>Dear friends, when I deal with DTI data, I found that the results of 3D slicer were different from using DTI studio. The fibers such as of internal capsule were short and fragmented in 3D slicer and they were complete in DTI studio. Is there someone who has same problem? When I changed the parameter “Y-component” to “X-component” in the “Flip engine vector” in the fiber tracking module of DTI studio, the results would be similar to them in 3D slicer. Does anyone know what’s going on? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ace45aca873144112f2144b3063c67fbb52ce94.jpeg" data-download-href="/uploads/short-url/66FZmVBTQtIOsqtTHeBTfZdrZ08.jpeg?dl=1" title="mayunzhong" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ace45aca873144112f2144b3063c67fbb52ce94_2_690x366.jpeg" alt="mayunzhong" data-base62-sha1="66FZmVBTQtIOsqtTHeBTfZdrZ08" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ace45aca873144112f2144b3063c67fbb52ce94_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ace45aca873144112f2144b3063c67fbb52ce94_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ace45aca873144112f2144b3063c67fbb52ce94_2_1380x732.jpeg 2x" data-dominant-color="E2E3E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mayunzhong</span><span class="informations">2854×1517 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @zhangfanmark (2020-04-13 18:53 UTC)

<p>Hi,</p>
<p>The issue of the problematic tracts should be because the converted data has unexpected image orientation that Slicer needs. Wonder what conversion tool you used, perhaps DWIConvert? One suggestion is to try our new DCM2niixGUI module (available in the current stable release and nightly  via Extensions Manager) to perform DWI data conversion.</p>
<p>Thanks,<br>
Fan</p>

---

## Post #3 by @researchtomliu (2020-04-14 16:27 UTC)

<p>Thank you very much,I’ll try it.</p>

---
