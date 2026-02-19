---
topic_id: 9010
title: "Edit Existing Segmentation In 3D"
date: 2019-11-04
url: https://discourse.slicer.org/t/9010
---

# Edit existing segmentation in 3D

**Topic ID**: 9010
**Date**: 2019-11-04
**URL**: https://discourse.slicer.org/t/edit-existing-segmentation-in-3d/9010

---

## Post #1 by @JordinaAviles (2019-11-04 11:58 UTC)

<p>Hi everyone,</p>
<p>I have a doubt regarding the segmentation in 3D Slicer.</p>
<p>I am opening a CT (mha) and it’s segmentation for the heart (.nrrd) and I want to edit the segmentation but the only way I can do it is painting slice for slice.</p>
<p>Is there any way to edit an existing segmentation in a similar way as the region growing does (you paint only a slice and the program makes corrections in whole 3D volume)?</p>
<p>If I need to fix every slice in the image it seems very tedious to me.</p>
<p>Thanks,</p>
<p>Jordina</p>

---

## Post #2 by @lassoan (2019-11-04 12:12 UTC)

<p>You have many options for 3D editing, such as:</p>
<ul>
<li>paint effect with sphere brush option enabled, smudge option enabled for automatic segment selection)</li>
<li>Scissors effect</li>
<li>Smoothing effect with joint smoothing method</li>
<li>Shrink segments to small seeds using Margin effect then grow them using Grow from seeds</li>
</ul>
<p>However, as you have already noticed, “fixing” a segmentation usually takes much longer time than creating a new segmentation from scratch and paying more attention or using better tools.</p>

---
