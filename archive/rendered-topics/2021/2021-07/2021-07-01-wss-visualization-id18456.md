---
topic_id: 18456
title: "Wss Visualization"
date: 2021-07-01
url: https://discourse.slicer.org/t/18456
---

# WSS visualization

**Topic ID**: 18456
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/wss-visualization/18456

---

## Post #1 by @CandeMorello (2021-07-01 13:06 UTC)

<p>Hi everyone good morning.<br>
I have performed several CDF simulations and extracted wall shear stress maps on the surfaces of my models.<br>
The thing is that I can visualize the WSS maps in paraview. What I want to do is to visualize the WSS maps with the DICOM images.<br>
Is it possible to import a .vtk, .ply, or .3mf model and visualize the surface’s color maps ON the DICOM files?. Which format do I have to use to do this?<br>
Thanks!!</p>

---

## Post #2 by @lassoan (2021-07-02 04:25 UTC)

<p>You can go to Models module’s Display / Scalars section to choose which array to display and set colormap, scaling, thresholding, etc. options.</p>

---
