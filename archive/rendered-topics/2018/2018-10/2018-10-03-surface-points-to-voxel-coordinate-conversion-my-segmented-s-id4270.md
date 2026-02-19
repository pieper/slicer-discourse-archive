---
topic_id: 4270
title: "Surface Points To Voxel Coordinate Conversion My Segmented S"
date: 2018-10-03
url: https://discourse.slicer.org/t/4270
---

# Surface points to voxel coordinate conversion (my segmented surface is outside volume)

**Topic ID**: 4270
**Date**: 2018-10-03
**URL**: https://discourse.slicer.org/t/surface-points-to-voxel-coordinate-conversion-my-segmented-surface-is-outside-volume/4270

---

## Post #1 by @tron (2018-10-03 13:42 UTC)

<p>Operating system: Microsoft Windows 7 Professional<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
I load a CT head volume and manually segment the mandibular canal using the following sequence:<br>
Segment Editor, Paint/Draw, Add Segment (give it a name, e.g. test), Models Export, Save data (.vtk format).<br>
Now I would expect that the saved surface data (test.vtk) would contain physical coordinates in mm that are located inside the CT volume space (after converting voxel coordinates to physical coordinates by multiplying by the voxel size).</p>
<p>Actual behavior:<br>
Instead, the saved surface coordinates are representing points far outside of the volume, and even with negative values in the z-direction. (Transformimg by multiplying with -1 one or more of the diagonal of the transformation matrix does not solve the problem.)</p>
<p>Anyone know how to solve this problem?</p>
<p>Tron</p>

---

## Post #2 by @lassoan (2018-10-03 14:39 UTC)

<p>DICOM uses LPS coordinate system, so if you load the exported image into third-party software then you may need to choose this coordinate system for export. Use <a href="https://discourse.slicer.org/t/how-to-export-stl-files/3041">Export to files</a> feature.</p>
<aside class="quote no-group" data-username="tron" data-post="1" data-topic="4270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/3da27b/48.png" class="avatar"> tron:</div>
<blockquote>
<p>Now I would expect that the saved surface data (test.vtk) would contain physical coordinates in mm that are located inside the CT volume space (after converting voxel coordinates to physical coordinates by multiplying by the voxel size).</p>
</blockquote>
</aside>
<p>Image is specified in physical space, so the exported model is defined in physical space, too. There is no need for any further conversion. Note that “converting voxel coordinates to physical coordinates by multiplying by the voxel size” would produce incorrect results: you need to take into account not just image spacing (voxel size) but also image origin and axis directions.</p>
<aside class="quote no-group" data-username="tron" data-post="1" data-topic="4270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/3da27b/48.png" class="avatar"> tron:</div>
<blockquote>
<p>even with negative values in the z-direction</p>
</blockquote>
</aside>
<p>This is completely normal. Origin of LPS coordinate system in DICOM files is often chosen to be near the center of object of interest, so S coordinate value is negative in half of the image.</p>

---
