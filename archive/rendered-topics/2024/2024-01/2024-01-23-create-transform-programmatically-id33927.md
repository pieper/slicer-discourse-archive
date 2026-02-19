---
topic_id: 33927
title: "Create Transform Programmatically"
date: 2024-01-23
url: https://discourse.slicer.org/t/33927
---

# Create transform programmatically

**Topic ID**: 33927
**Date**: 2024-01-23
**URL**: https://discourse.slicer.org/t/create-transform-programmatically/33927

---

## Post #1 by @Anuta (2024-01-23 13:18 UTC)

<p>Hello!<br>
I am trying to perform multiplanar reformation in slicer (reslice the volume in a different orientation). For this task I use “Transforms” module to alter orientation of the volume and “Resample Scalar Volume” module to reslice the volume.<br>
The issue is, I would like to do this all programmatically (without opening the slicer and using sliders).<br>
I would like to create a transformation matrix myself, create a linear transform with this matrix and apply it to the given volume.<br>
The questions are:</p>
<ul>
<li>How to create a new transformation matrix programmatically? Is it even possible (I’ve seen that all of the classes related to transforms are Widget-based)?</li>
<li>How to set parameters in “Resample Scalar Volume” module programmatically?</li>
</ul>

---

## Post #2 by @pieper (2024-01-23 13:30 UTC)

<p>Yes, all that is possible.  Read through the script repository, especially this section:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#transforms" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#transforms</a></p>

---
