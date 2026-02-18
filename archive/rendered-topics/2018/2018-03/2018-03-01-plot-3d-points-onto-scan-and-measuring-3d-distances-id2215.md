# Plot 3d points onto scan and measuring 3d distances

**Topic ID**: 2215
**Date**: 2018-03-01
**URL**: https://discourse.slicer.org/t/plot-3d-points-onto-scan-and-measuring-3d-distances/2215

---

## Post #1 by @Vinny (2018-03-01 01:01 UTC)

<p>Hi,</p>
<p>I’d like to plot a series of 3d contact points onto a diffusion-weighted image (DWI); these points are in the same coordinate system as the DWI and are stored as an Excel file.  Is there a module that can be used to do this?  I can do this manually by using the Data Probe to probe the coordinates on the scan and match it to the stored coordinates and then setting fiducial points, but was wondering if there was a module or pythonic way of doing this.</p>
<p>Also, how can distances be measured between each of these 3d contact points and VTK object of interests that have been imported into 3d Slicer.</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @Vinny (2018-03-01 01:32 UTC)

<p>Ok I can see that the RAS coordinates can be entered in the fiducials list.</p>
<p>Still help with distance calculations between the fiducials and VTK objects would be greatly appreciated.</p>

---

## Post #3 by @lassoan (2018-03-01 02:20 UTC)

<p>You can save fiducial lists as fcsv files, which are essentially csv files that you can read, edit, and save in Excel.</p>
<p>BreachWarning module in SlicerIGT extension can compute closest point position and point distance from a point (defined by a transform) to a model. Typical use is that you move your tool(represented by a model node) using a transform and you display a line to the closest point to an object of interest and the distance from the tool. In your case, you would probably want to add a small sphere for each 3D contact point (you can create the sphere by Create models module of SlicerIGT extension), put them in the correct position by applying a transform, and add a BreachWarning node for each object of interest that you want to compute the distance to.</p>
<p>You can also use vtkImplicitPolyDataDistance class to get distance between a point and a model. In this case, you need to obtain coordinates and VTK objects from MRML nodes and feed them into the vtkImplicitPolyDataDistance object.</p>

---

## Post #4 by @Vinny (2018-03-01 02:31 UTC)

<p>Thanks Andras!  Will try this out</p>

---
