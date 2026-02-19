---
topic_id: 38187
title: "Transform For X Y Z Involving Hu"
date: 2024-09-03
url: https://discourse.slicer.org/t/38187
---

# Transform for x,y,z involving HU

**Topic ID**: 38187
**Date**: 2024-09-03
**URL**: https://discourse.slicer.org/t/transform-for-x-y-z-involving-hu/38187

---

## Post #1 by @francois (2024-09-03 17:25 UTC)

<p>Dear qll<br>
Thank you for all you do for this community. I`m new here<br>
My project is to extract all or segmented spatial and HU data (4 columns) from a bone dataset, perform a mathematical transform of the x,y,z coordinates of each voxel based on HU values. I saw that this was possible. But the tricky part is then to import the values back into a viewer and create a new picture based on the transformed x,y,z,HU coordinates. The picture will be distorted compared with the original but also some spatial values may be projected outside the field of view and some voxels may end up at the same location. So we would need to add a filter to exclude voxels that are too far away and another filter to transform stacked voxels into something else like retain just one voxel but multiplie the HU value.<br>
I would be very grateful if you could help me understand what would be the steps to reach this goal.<br>
Thanks !!!</p>

---
