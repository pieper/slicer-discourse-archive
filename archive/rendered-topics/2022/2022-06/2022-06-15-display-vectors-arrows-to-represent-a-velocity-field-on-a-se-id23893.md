---
topic_id: 23893
title: "Display Vectors Arrows To Represent A Velocity Field On A Se"
date: 2022-06-15
url: https://discourse.slicer.org/t/23893
---

# Display vectors (arrows) to represent a velocity field on a section plane using python

**Topic ID**: 23893
**Date**: 2022-06-15
**URL**: https://discourse.slicer.org/t/display-vectors-arrows-to-represent-a-velocity-field-on-a-section-plane-using-python/23893

---

## Post #1 by @l.geronzi (2022-06-15 16:21 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.0.2<br>
Expected behavior: Display of a set of vectors<br>
Actual behavior: None</p>
<p>Hello,<br>
I would be interested in showing vectors reporting the velocity on a cutting plane of a blood vessel. In particular, let’s suppose I have 100 points p=[p_1,…p_i,…,p_100] and on each point a vector v_i=[v_i_x,v_i_y,v_i_z]. How can I display those vectors in Slicer?</p>
<p>Thank you.</p>
<p>Leonardo</p>

---

## Post #2 by @mau_igna_06 (2022-06-15 18:43 UTC)

<p>You need to use an arrow filter and a glyph filter</p>
<p>Hope it helps</p>

---

## Post #3 by @l.geronzi (2022-06-16 08:07 UTC)

<p>Hello Mauro,<br>
thanks for your answer.<br>
How to define the orientation of the arrows? That’s not clear to me.</p>
<p>Leonardo</p>

---

## Post #4 by @mau_igna_06 (2022-06-16 10:33 UTC)

<p>I think some of the available glyph filters let’s ypu do that. Please check on the vtk code class brief</p>

---

## Post #5 by @lassoan (2022-06-17 19:45 UTC)

<p>You can visualize vector fields using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualization-modes">Transforms module</a>. The visualization feature is mostly used for transforms, but you can use it for visualization of any kind of vector fields.</p>
<p><img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/module_transforms_glyph_arrow_2d.png" alt="" width="378" height="323"> <img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/module_transforms_glyph_arrow_3d_slice.png" alt="" width="378" height="323"></p>
<p>No programming is needed. You can load your vector field from a .nrrd file as a transform by choosing “Description” → “Transform” when you add the data file for loading.</p>

---
