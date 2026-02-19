---
topic_id: 14757
title: "What Is The Difference Between Mask Label And Label Map"
date: 2020-11-24
url: https://discourse.slicer.org/t/14757
---

# What is the difference between mask, label and label map?

**Topic ID**: 14757
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/what-is-the-difference-between-mask-label-and-label-map/14757

---

## Post #1 by @slicer365 (2020-11-24 15:09 UTC)

<p>what is the difference between mask ,label  and label map?</p>

---

## Post #2 by @lassoan (2020-11-24 19:57 UTC)

<p>In general, these terms are used interchangeably (along with segment, segmentation, contour, annotation, etc.).</p>
<p>In Slicer:</p>
<ul>
<li>Labelmap: 3D volume that contains discrete “label” values (instead of continuous scalar values).</li>
<li>Label: used for various things, one of them is referring to a particular voxel value in a labelmap volume.</li>
<li>Mask: Designates an arbitrary shaped region that will be included in the processing operation (what is outside the mask is ignored). It is used for example for image registration (by various image registration modules), or for blanking out parts of a volume (used in Segment Editor’s Mask volume effect). It is most commonly represented as a labelmap volume or segmentation node.</li>
</ul>
<p>You can find more information about segmentation nomenclature in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#basic-concepts">Image Segmentation documentation page</a>.</p>

---
