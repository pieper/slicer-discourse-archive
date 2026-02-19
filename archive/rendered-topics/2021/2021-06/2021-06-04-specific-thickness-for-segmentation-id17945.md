---
topic_id: 17945
title: "Specific Thickness For Segmentation"
date: 2021-06-04
url: https://discourse.slicer.org/t/17945
---

# Specific thickness for segmentation

**Topic ID**: 17945
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/specific-thickness-for-segmentation/17945

---

## Post #1 by @Aep93 (2021-06-04 04:26 UTC)

<p>Hello all,<br>
Is there possible to set one dimension of a segmentation (such as the thickness of a thin structure) to be a constant value in the slicer?<br>
Thanks</p>

---

## Post #2 by @lassoan (2021-06-04 05:12 UTC)

<p>There are several ways to do this. Can you be a bit more specific, so that I can just describe the options that most likely will work well for you? What would you like to segment?</p>

---

## Post #3 by @Aep93 (2021-06-04 05:29 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I am interested in modeling very thin structures (such as eardrum). In fact, I would like to determine the thickness of my segmentation myself in order to have a more accurate model. I appreciate your help.</p>

---

## Post #4 by @lassoan (2021-06-04 13:16 UTC)

<p>Probably the Baffle Planner module would be well suited for creating the thin model (<a href="https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799" class="inline-onebox">New module: Baffle planner - for designing surface patches</a>).</p>
<p>There are a number of ways to do the thickness measurement. What imaging modality you will use? What is the voxel size? What is the diameter of the eardrum? What is the average thickness of the eardrum? What accuracy do you need for measuring the thickness? What is the goal of determining the thickness (3D printing, surgical planning, quantification, …)?</p>

---

## Post #5 by @Aep93 (2021-06-08 18:52 UTC)

<p>Thank you so much for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I could manage to create my segmentation with the baffle planner extension. However, because of its thickness, I cannot mesh it well with the segmentmesher module. Do you have any suggestions for meshing these thin segmentations?</p>

---

## Post #6 by @lassoan (2021-06-08 19:59 UTC)

<p>It would be nice if we could solve everything by a single segmentation representation, such as binary labelmap, but unfortunately this is not possible. Binary labelmap representations are very simple and robust to edit. However, binary labelmaps are inherently ill-suited for representing thin structures that span a large region: you need small voxel size for representing the thin structures, but since the region to cover is large, you would need to have a lot of these small voxels. If you want to have 0.001mm precision then you can easily end up with a labelmap with a size of hundreds of GB, which would be impractical to work with (would be too slow and/or you would run out of memory).</p>
<p>If you are lucky to have a structure that has a simple shape, such as membrane or tube, then you can generate the volumetric mesh programmatically. For example, the Baffle Planner module creates the warped surface by warping a planar unit disk. If you modify the Python script of Baffle Planner module to warp a volumetric mesh of a thick disk instead of a <a href="https://github.com/SlicerHeart/SlicerHeart/blob/184619867a92379247d1913d6444b5546b1fd2f6/BafflePlanner/BafflePlanner.py#L298">flat disk plate</a> then you’ll get a volumetric mesh as a result.</p>

---
