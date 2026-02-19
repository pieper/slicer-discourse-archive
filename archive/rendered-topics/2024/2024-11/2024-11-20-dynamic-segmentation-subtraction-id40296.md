---
topic_id: 40296
title: "Dynamic Segmentation Subtraction"
date: 2024-11-20
url: https://discourse.slicer.org/t/40296
---

# Dynamic segmentation subtraction

**Topic ID**: 40296
**Date**: 2024-11-20
**URL**: https://discourse.slicer.org/t/dynamic-segmentation-subtraction/40296

---

## Post #1 by @ava23 (2024-11-20 21:00 UTC)

<p>I have a Volume A (a PET scan) with two segmentations: <strong>Seg1</strong> and <strong>Seg2</strong>.</p>
<p>A user is making adjustments to <strong>Seg2</strong> (adding and removing voxels).</p>
<p>I would like to dynamically display all voxels that are in <strong>Seg1</strong> but not in <strong>Seg2</strong> in a 3D volume (using a 3D Volume of the PET). This will help the user with their adjustments.</p>
<p>I understand that this can be achieved using <strong>Segment Editor &gt; Logical Operators &gt; Subtract</strong>, but this method is not dynamic.</p>
<p>Is there any way to achieve this dynamically?</p>
<p>I am also interested in an automated or Python-based solution</p>

---

## Post #2 by @lassoan (2024-11-20 21:01 UTC)

<p>You can make it dynamic using Python scripting. See many examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>

---
