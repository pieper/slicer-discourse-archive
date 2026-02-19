---
topic_id: 5560
title: "Isosurface Hangs Or Crashes"
date: 2019-01-29
url: https://discourse.slicer.org/t/5560
---

# isosurface - hangs or crashes

**Topic ID**: 5560
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/isosurface-hangs-or-crashes/5560

---

## Post #1 by @njeffery (2019-01-29 14:34 UTC)

<p>Hi All,<br>
I am looking to create an isosurface to help with the selection of fiducials. However, when I try to create a surface  (segment editor&gt;show 3D or  grayscale model maker [no smoothing, and permutations of 0 to 0.5 decimation]) slicer just hangs (I left it for 67minutes in one instance) or crashes. The CT dataset is large (3GB), but I can load and create isosurfaces in Seg3D in about 90 secs (markup function in seg3d is pretty poor).</p>
<p>Using the latest version 4.10.1</p>
<p>Any suggestions?</p>

---

## Post #2 by @lassoan (2019-01-30 01:28 UTC)

<p>Everything indicates that you run out of memory. You can do one or more of these:</p>
<ul>
<li>crop (to the region of interest) and resample (to make the number of voxels about 300 along each axis) the volume before you do anything</li>
<li>increase the virtual memory size (computation time will still remain long)</li>
<li>smooth the segmentation (using Smoothing effect) before you click “Show 3D”</li>
<li>disable model smoothing (drop-down menu of Show 3D) - it may make generation faster by a factor of 10-50x.</li>
</ul>
<p>But maybe the simplest is to just use volume rendering for surface extraction. Choose a preset and use the offset slider to choose isosurface value. You may need to crop&amp;resample input volume to fit into GPU memory.</p>

---

## Post #3 by @njeffery (2019-01-30 08:28 UTC)

<p>many thanks Andras,<br>
I would be surprised if it were a memory problem - I have 96GB ram (I use the same machine for computational modelling). Unless there is some setup in slicer I have missed which means it is not using the memory correctly? I will check out the volume rendering options, though I have struggled with the landmarking of surfaces with volume rendering in the past - landmarks tend to sink through the surface.<br>
best and thanks</p>

---
