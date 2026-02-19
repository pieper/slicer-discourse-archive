---
topic_id: 36301
title: "Calculate Mean Sd"
date: 2024-05-21
url: https://discourse.slicer.org/t/36301
---

# Calculate MEAN, SD

**Topic ID**: 36301
**Date**: 2024-05-21
**URL**: https://discourse.slicer.org/t/calculate-mean-sd/36301

---

## Post #1 by @Vikram (2024-05-21 15:04 UTC)

<p>it is possible to calculate mean and SD and HU to draw ROI BY using 3d slicer.<br>
if it is possible any one can guide me , how i can count</p>

---

## Post #2 by @muratmaga (2024-05-21 17:30 UTC)

<p>If you create a segmentation for your ROI, this example script shows how to extract voxel information for that specific region as a vector. then you can simply use standard mean or sd function to calculate.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-the-values-of-all-voxels-for-a-label-value">Script repository — 3D Slicer documentation</a></p>
<p>You can also use the Segment Statistics to calculate the mean intensity inside the segment, but I am not sure if it does SD.</p>

---
