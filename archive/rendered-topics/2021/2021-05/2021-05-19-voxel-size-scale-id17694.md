---
topic_id: 17694
title: "Voxel Size Scale"
date: 2021-05-19
url: https://discourse.slicer.org/t/17694
---

# Voxel size scale

**Topic ID**: 17694
**Date**: 2021-05-19
**URL**: https://discourse.slicer.org/t/voxel-size-scale/17694

---

## Post #1 by @granizado (2021-05-19 12:31 UTC)

<p>I completed a segmentation and in the final steps when I added a scale bar I realised that the dimensions are far too big than the real ones which makes a problem with segment statistics as well. I have a voxel resolution of 72 μm so I changed the image spacing accordingly. The problem is that the image has changed but the size of segmentation stays the same. When I change it in „Specify geometry” in Segment Editor it completely lost all shapes. I would be grateful for any tip how to solve it.</p>

---

## Post #2 by @lassoan (2021-05-21 17:41 UTC)

<p>You can transform the segmentation by <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">applying and hardening a transform</a>. You need to put the 3 relative scaling factors in the diagonal of the transformation matrix.</p>

---

## Post #3 by @Philipp_Maintz (2021-07-08 15:35 UTC)

<p>I have the same issue what is the module to do that?</p>

---

## Post #4 by @lassoan (2021-07-08 15:37 UTC)

<p>See the link above, which takes you to the documentation of the <strong>Transforms</strong> module. You can use this module to apply and harden transforms.</p>

---
