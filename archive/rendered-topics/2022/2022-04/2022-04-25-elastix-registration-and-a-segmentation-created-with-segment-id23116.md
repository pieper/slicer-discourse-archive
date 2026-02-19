---
topic_id: 23116
title: "Elastix Registration And A Segmentation Created With Segment"
date: 2022-04-25
url: https://discourse.slicer.org/t/23116
---

# Elastix registration and a segmentation created with Segment Editor

**Topic ID**: 23116
**Date**: 2022-04-25
**URL**: https://discourse.slicer.org/t/elastix-registration-and-a-segmentation-created-with-segment-editor/23116

---

## Post #1 by @Gonzalo_Rojas_Costa (2022-04-25 16:52 UTC)

<p>Hi:</p>
<p>I co-registered between two FLAIR MRIs of the same patient using “General Registration (elastix)”. I want to apply the obtained transformation to a segmentation made with the Segment Editor based on one of the two images. How can I do that?</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @lassoan (2022-04-25 19:27 UTC)

<p>You can apply the transform to a node as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">here</a>. If you want to persistently modify the segmentation then you need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the applied transform</a> on the node.</p>

---
