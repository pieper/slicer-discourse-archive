---
topic_id: 24945
title: "Access Volume Rendering Result"
date: 2022-08-27
url: https://discourse.slicer.org/t/24945
---

# Access volume rendering result

**Topic ID**: 24945
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/access-volume-rendering-result/24945

---

## Post #1 by @Muhammed_Fatih_Talu (2022-08-27 14:34 UTC)

<p>Using the volume rendering tool, I can view the brain vascular tree more clearly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02a766eb633c5a642f044bec3416ebbef1bb464b.jpeg" data-download-href="/uploads/short-url/ntBX2LN4GCxERzLgJSJjgmMADF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a766eb633c5a642f044bec3416ebbef1bb464b_2_621x500.jpeg" alt="image" data-base62-sha1="ntBX2LN4GCxERzLgJSJjgmMADF" width="621" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a766eb633c5a642f044bec3416ebbef1bb464b_2_621x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02a766eb633c5a642f044bec3416ebbef1bb464b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02a766eb633c5a642f044bec3416ebbef1bb464b.jpeg 2x" data-dominant-color="FADAD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">862×693 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
However, I want to access this output from within the Python code. Just like a segmentation node. So how can I get the rendering result? Can I transfer to a standalone node?</p>

---

## Post #2 by @lassoan (2022-08-27 22:28 UTC)

<p>You can capture the image rendered in the 3D view as shown in this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#capture-3d-view-into-png-file-with-transparent-background">example in the script repository</a>.</p>

---

## Post #3 by @Muhammed_Fatih_Talu (2022-09-18 14:11 UTC)

<p>Thanks.<br>
But my goal is not to export the rendering result to a 2d image file. I’m trying to get brain vessels in 3d. I think the most convenient way is to use “Scalar Opacity Mapping” under the “Volume Rendering” tool. A wonderful vascular tree information can be extracted. However, I want to assign this manuel rendering result to a 3d variable (or a node variable, 3d dijital matrix variable) and use it within the program.</p>

---
