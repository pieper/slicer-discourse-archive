# Parsing CenterLine File (.vtk)

**Topic ID**: 3384
**Date**: 2018-07-05
**URL**: https://discourse.slicer.org/t/parsing-centerline-file-vtk/3384

---

## Post #1 by @trnhx001 (2018-07-05 12:57 UTC)

<p>Hi everyone,</p>
<p>I am sorry to ask if this is a simple question. I am trying to parse the centerline file using python for data analysis, but I am confused about the coordinates in 3D Slicer.</p>
<p>Is the data in world coordinates(xyz) or voxel coordinates? Are segmentaions and volume files also stored in world coordinates?</p>
<p>Is there anyway to output the data in world coordinates or voxel coordinates using python packages?</p>
<p>Thanks for all of your helps.</p>

---

## Post #2 by @lassoan (2018-07-05 13:26 UTC)

<p>The simplest is to get the model point coordinates as numpy array as shown here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Model_data_as_numpy_array">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Model_data_as_numpy_array</a></p>
<p>The points are in the node’s coordinate system. The node may be transformed in the world coordinate system if you apply a transform but not harden it yet.</p>

---

## Post #3 by @trnhx001 (2018-07-05 14:32 UTC)

<p>Thank you.</p>
<p>Just to verify, is the node’s coordinates you mentioned is RAS coordinates.</p>
<p>I also see this: d=inv(M) *[ R A S 1 ]’ from the link <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a>.</p>
<p>Can you clarify how to get M?</p>

---
