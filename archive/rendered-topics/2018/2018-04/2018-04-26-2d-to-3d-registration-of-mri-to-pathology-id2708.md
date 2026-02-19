---
topic_id: 2708
title: "2D To 3D Registration Of Mri To Pathology"
date: 2018-04-26
url: https://discourse.slicer.org/t/2708
---

# 2d to 3D registration of MRI to pathology

**Topic ID**: 2708
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/2d-to-3d-registration-of-mri-to-pathology/2708

---

## Post #1 by @kayarre (2018-04-26 17:18 UTC)

<p>I am working on that is looking at pathology of resected aneurysms and comparing with an MRI image sequence.<br>
Currently the plan is to analyze each image in 4 quadrants so accuracy doesn’t have be exact, (in the future attempts to do more quantitative analysis may require a little more precision)</p>
<p>They cut out the aneurysm, fill it with glue and thenslice it, apply stains, analyze qualitatively. I believe there are many thin slices ~50 crossections and there might be 2 or 4 slices that would map to one  voxel width in the MRI.</p>
<p>My thought was to do some sort of manual registration to get close and then automate refinement.</p>
<p>For registering two 3D volumes I have had success using the 3D slicer models to start with landmark registration to get close and then follow up with the rigid registration using BrainsFit, therefore a similar workflow would be nice.</p>
<p>Does anyone have guidance and or input they could offer to help which direction to go.</p>

---

## Post #2 by @ihnorton (2018-04-26 19:42 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="2708">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>I believe there are many thin slices ~50 crossections and there might be 2 or 4 slices that would map to one  voxel width in the MRI.</p>
</blockquote>
</aside>
<p>Right, the scale difference is very large, and 2D to 3D registration can be challenging even for similar modalities and scales. The state of the art is papers like <a href="https://www.cv-foundation.org/openaccess/content_cvpr_2016_workshops/w15/papers/Alegro_Multimodal_Whole_Brain_CVPR_2016_paper.pdf">Allegro et al 2016</a> where they do serial blockface imaging along with cryo-sectioning, to provide “as-extracted” registration targets. The blockface images have reasonably similar boundary profiles as the MRI, and crucially, the images are taken before the frequent warping, tearing, and other degradation that accompanies sectioning and staining. Needless to say, that’s probably an intensive pipeline to get started…</p>
<p>Since it sounds like you don’t need that level of accuracy, a simpler approach is to manually stack and align microscopy sections slice-by-slice. There are some tools to do this in FIJI/ImageJ (by Albert Cardona if I recall correctly). Once you have a stacked volume, you could resample to a 3d voxel grid and import to Slicer, then try to manually align the outline of that volume to a segmentation of the aneurysm from MRI.</p>

---
