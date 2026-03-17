---
topic_id: 46472
title: "Does The Resolution Change The Surface Area Values"
date: 2026-03-16
url: https://discourse.slicer.org/t/46472
---

# Does the resolution change the surface area values?

**Topic ID**: 46472
**Date**: 2026-03-16
**URL**: https://discourse.slicer.org/t/does-the-resolution-change-the-surface-area-values/46472

---

## Post #1 by @FabricioFO (2026-03-16 19:52 UTC)

<p>Hello, everyone. I noticed that when we reduce the resolution by half in ImageStack, the spacing value doubles. After finishing the segmentations, will the volume and surface area values be the same as if I had used the original high resolution with the correct spacing?</p>

---

## Post #2 by @muratmaga (2026-03-16 20:29 UTC)

<p>Short answer: It will, but not appreciably.</p>
<p>When you downsample in ImageStacks (or crop volume), you are representing the same distance with fewer voxels. So the spacing increases in the amount you reduced your data (if one voxel was 50 micron, at half resolution it needs to be 100 micron, since it reduces the number of voxels by factor of 2 in each axis). This is still the correct spacing. You simply reduced your dataset to a lower resolution.</p>
<p>To convince yourself, you can run a small experiment. Segment a section at full resolution, calculate the SA, then resample the segment geometry by 0.5 (since in segment geometry it is oversampling, as opposed to downsampling) and then recalculate the SA from that segment one more time.</p>

---
