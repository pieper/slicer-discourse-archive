---
topic_id: 33031
title: "Why Do Horizontal Lines Appear After Using Fill Between Slic"
date: 2023-11-26
url: https://discourse.slicer.org/t/33031
---

# Why do horizontal lines appear after using Fill Between Slices in 3D Slicer?

**Topic ID**: 33031
**Date**: 2023-11-26
**URL**: https://discourse.slicer.org/t/why-do-horizontal-lines-appear-after-using-fill-between-slices-in-3d-slicer/33031

---

## Post #1 by @tuwenqing (2023-11-26 03:49 UTC)

<p>Operating system:windows<br>
Slicer version:5.4.0<br>
Expected behavior:there’s no horizontal lines<br>
Actual behavior:there’s horizontal lines appear after using Fill Between Slices in 3D Slicer<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6990fd5dec37bece619354139363d9824bea9b70.png" alt="截屏2023-11-26 11.39.49" data-base62-sha1="f3SLX3s0pSDPF9xJugPCALAu5os" width="486" height="408"></p>

---

## Post #2 by @lassoan (2023-11-27 07:04 UTC)

<p>Fill between slices effect operates on along axes parallel with the axes of the segmentation’s internal labelmap representation. You can snap back the slice views axes to the segmentation axes; or if you want to see oblique slices then you can resample the volume. See some more explanation and step-by-step instructions here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments</a></p>

---
