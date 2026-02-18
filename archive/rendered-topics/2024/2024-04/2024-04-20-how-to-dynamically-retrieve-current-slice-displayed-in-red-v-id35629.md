# How to Dynamically Retrieve Current Slice Displayed in Red View as Independent Volume Node in 3D Slicer?

**Topic ID**: 35629
**Date**: 2024-04-20
**URL**: https://discourse.slicer.org/t/how-to-dynamically-retrieve-current-slice-displayed-in-red-view-as-independent-volume-node-in-3d-slicer/35629

---

## Post #1 by @slicer365 (2024-04-20 00:53 UTC)

<p>I am developing with 3D Slicer. After importing an image as a volume node, which represents the entire volume, how can I dynamically retrieve the currently displayed slice in the red view as an independent volume node?</p>

---

## Post #2 by @pieper (2024-04-20 14:09 UTC)

<p>If you just want to access slices of the volume, just get the array and index them.  If you need the rendered view, you can access the render window of the slice viewer, and use a window to image filter to get a vtk image data and then access the contents of that as a numpy array, then use the slicer utility to add a volume from the array.</p>

---
