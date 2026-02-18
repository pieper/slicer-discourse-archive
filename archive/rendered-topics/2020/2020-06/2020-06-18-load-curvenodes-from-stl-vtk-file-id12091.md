# Load curvenodes from stl/vtk file

**Topic ID**: 12091
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/load-curvenodes-from-stl-vtk-file/12091

---

## Post #1 by @Neda (2020-06-18 11:23 UTC)

<p>Hi,<br>
I am using 3D slicer 4.11.0 for analyzing dental CT. I need a bunch of points around mandible curve to compute a panoramic X-ray from a cone-beam dental CT (<a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" rel="nofollow noopener">https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07</a>). I have segmented this curve using “segment editor” -&gt; “draw tube” (to generate the curve from points) -&gt; with fiducial markups (points). This segment can be saved in .vtk or .stl format. From this saved files (vtk or stl) how can I get the points coordinates in python interactor to proceed with my 3D to 2D projection?<br>
Slicer crashes and exists by running this line:<br>
curve = vtk.vtkPolyData(‘path_to/mandible_bow.vtk’)</p>
<p>Do I need to forget about this segmentation (curve in stl/vtk) and save the points in CSV file? If so how should I load points coordinates from it in slicer python interactor?</p>
<p>Any suggestion is appreciated!<br>
Thank you</p>

---

## Post #2 by @lassoan (2020-06-18 21:16 UTC)

<p>You can reverse-engineer the curve-shaped segment into a curve using VMTK extension’s brand new “Extract centerline” module - to be released tomorrow for Slicer Preview Release. Give it a try tomorrow and write here if you need help figuring out how to use it.</p>

---

## Post #3 by @lassoan (2020-06-19 16:46 UTC)

<p>See announcement of the new module here: <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117" class="inline-onebox">New module: Extract Centerline (in SlicerVMTK extension)</a></p>

---
