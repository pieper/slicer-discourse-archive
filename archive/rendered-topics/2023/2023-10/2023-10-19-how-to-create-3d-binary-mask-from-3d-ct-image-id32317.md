# How to create 3D binary mask from 3D CT image? 

**Topic ID**: 32317
**Date**: 2023-10-19
**URL**: https://discourse.slicer.org/t/how-to-create-3d-binary-mask-from-3d-ct-image/32317

---

## Post #1 by @Debapriya (2023-10-19 01:39 UTC)

<p>Hello,</p>
<p>I am new to 3D Slicer.<br>
I have 3D CT images of the brain in dicom format. I want to segment certain regions of the brain, and create 3D binary masks of those regions. Is there any provision of doing that in 3D Slicer? Please tell me the process.</p>

---

## Post #2 by @lassoan (2023-10-19 01:48 UTC)

<p>You can use the Segment Editor module for manual segmentation of regions as binary masks. <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html">This page</a> is a good starting point for 3D Slicer and you can learn more about image segmentation in Slicer on <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this page</a>.</p>
<p>You can segment the whole brain by a couple of clicks (without any manual effort) as described in <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/">this recipe</a>. Before starting manual segmentation of effort, check out if you can find AI models for fully automatic segmentation of the structures you are interested in; or if there are segmented data sets that you can use to train your own segmentation AI model using <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel extension</a>.</p>

---

## Post #3 by @Debapriya (2023-10-26 13:37 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>. <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" rel="noopener nofollow ugc">This link</a> helped me to segment the brain CT images.</p>
<p>Is there a similar tutorial for MR brain segmentation also? I tried to segment MR images using the same steps described for CT images. However, I am not getting the desired result, probably because I am entering wrong values for <strong>bone intensity range</strong> and <strong>cavity size</strong> of MR.</p>
<p>My goal is to register CT and MR images of the brain using FFD (BSpline) and compute Dice Coefficient and Hausdorff distance, before and after registration.</p>

---

## Post #4 by @lassoan (2023-10-26 13:40 UTC)

<p>Segmenation of the brain in MRI (“skull stripping”) is much easier, because it is a very common task and there are many automated tools for it. For example, you can use the HDBrainExtraction extension in Slicer.</p>
<aside class="quote no-group" data-username="Debapriya" data-post="3" data-topic="32317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/bc79bd/48.png" class="avatar"> Debapriya:</div>
<blockquote>
<p>My goal is to register CT and MR images of the brain using FFD (BSpline)</p>
</blockquote>
</aside>
<p>You don’t need to segment the brain for this. Most registration methods can easily register images of the same patient acquired with different imaging modalities. Both SlicerElastix and SlicerANTs extensions should work well.</p>

---
