---
topic_id: 18084
title: "Problems With Volume Rendering"
date: 2021-06-11
url: https://discourse.slicer.org/t/18084
---

# Problems with volume rendering

**Topic ID**: 18084
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/problems-with-volume-rendering/18084

---

## Post #1 by @Leo_Pacheco (2021-06-11 18:38 UTC)

<p>Hello, I’ve been having problems with the volume rendering option of the program for my 910 dcom files. I followed all the basic steps for loading and creating the volume rendering but I simply can’t visualize the model even though I click on the eye icon.<br>
the version of the program is 4.11.2021026<br>
It’s not a GPU problem is it is barely working<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57c2a6cb4f3895ffa77551261b05e7c9ee79298e.jpeg" data-download-href="/uploads/short-url/cwmzTp8Lac0iqR7QFD8WCvz84AS.jpeg?dl=1" title="captura 3d slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57c2a6cb4f3895ffa77551261b05e7c9ee79298e_2_690x370.jpeg" alt="captura 3d slicer" data-base62-sha1="cwmzTp8Lac0iqR7QFD8WCvz84AS" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57c2a6cb4f3895ffa77551261b05e7c9ee79298e_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57c2a6cb4f3895ffa77551261b05e7c9ee79298e_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57c2a6cb4f3895ffa77551261b05e7c9ee79298e_2_1380x740.jpeg 2x" data-dominant-color="46464E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">captura 3d slicer</span><span class="informations">1917×1029 412 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-06-11 18:44 UTC)

<p>What happens when you switch to CPU Raycasting (instead of GPU)? Please be patient as it might be slow.<br>
If you don’t seen anything with CPU rendering, then please provide a screen capture of the volume information tab.</p>

---

## Post #3 by @lassoan (2021-06-11 18:57 UTC)

<p>The problem may be as simple as not centering the 3D view. Hit the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">“Reset field of view” button</a> to ensure that you look at where the volume is.</p>
<p>For volume rendering 910 slices, especially if they are high resolution, you will need some serious GPU. Integrated graphics on a laptop or a discrete GPU in a 5-year-old laptop may not be enough. To make sure that your GPU can handle this volume, you can use “Crop volume” module to downsample it (e.g., setting “Spacing scale” to 2.0) and/or crop it to the region that you are interested in, and render this cropped/resampled volume.</p>

---

## Post #4 by @Leo_Pacheco (2021-07-02 17:46 UTC)

<p>Thank you very much, the problem was the GPU, it could barely process the TIF files so it would have never been able to process the DCOM files.</p>

---
