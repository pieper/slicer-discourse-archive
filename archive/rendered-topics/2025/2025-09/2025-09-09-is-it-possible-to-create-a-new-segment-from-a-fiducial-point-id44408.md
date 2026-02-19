---
topic_id: 44408
title: "Is It Possible To Create A New Segment From A Fiducial Point"
date: 2025-09-09
url: https://discourse.slicer.org/t/44408
---

# Is it possible to create a new segment from a fiducial point cloud?

**Topic ID**: 44408
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-a-new-segment-from-a-fiducial-point-cloud/44408

---

## Post #1 by @maria_m (2025-09-09 13:15 UTC)

<p>I am using 3D Slicer for my master’s thesis. My project involves working with 4 slices in the axial plane of a brain MRI. In each slice, I use the segmentation tool to select the cerebral cortex, and then with a Python script, I remove the segment from all other slices, leaving only the 4 selected 2D planes. Using another script, I place around 20 fiducial points around each segment to define its perimeter. I export these points as a CSV file and send them to a colleague. My colleague then returns a point cloud, which I need to visualize again in order to show the brain-shift.</p>
<p>So far, this workflow works, but I am not sure if it is the most efficient approach. I may be using tools in ways they were not originally intended, and I wonder if there might be better methods. Segmentation is inherently a 3D tool, but I am using it in a 2D context, and perhaps simpler representation tools—similar to drawing tools—would be more appropriate since I don’t need a full 3D model.</p>
<p>My main question is whether it is possible to create a new segment to represent the brain’s new position based on the updated fiducial point cloud. I am also open to suggestions for simpler ways to achieve this without relying on segmentation.</p>

---

## Post #2 by @cpinter (2025-09-09 13:27 UTC)

<p>Please try the Surface cut effect in the SegmentEditorExtraEffects extension and let us know if it does what you need.</p>

---
