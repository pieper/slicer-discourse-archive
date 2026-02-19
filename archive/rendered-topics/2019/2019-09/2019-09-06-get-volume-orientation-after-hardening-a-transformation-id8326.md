---
topic_id: 8326
title: "Get Volume Orientation After Hardening A Transformation"
date: 2019-09-06
url: https://discourse.slicer.org/t/8326
---

# Get volume orientation after hardening a transformation

**Topic ID**: 8326
**Date**: 2019-09-06
**URL**: https://discourse.slicer.org/t/get-volume-orientation-after-hardening-a-transformation/8326

---

## Post #1 by @giovform (2019-09-06 17:23 UTC)

<p>Hi, I just would like the get the volume orientation after hardening a transformation. Is it possible?</p>
<p>Thank you in advance, excellent software.</p>

---

## Post #2 by @lassoan (2019-09-06 17:26 UTC)

<p>You can get IJK axis directions in RAS coordinate system by calling <a href="https://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#aecba65818d6210c412b5c4f319e7cb6e" rel="nofollow noopener">GetIJKToRASDirections()</a> or <a href="https://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#ac219b18e05335a172a2128d615153ddf" rel="nofollow noopener">GetIJKToRASMatrix()</a> method of the volume node.</p>

---

## Post #3 by @giovform (2019-09-06 19:36 UTC)

<p>Thank you Andras. Solved my problem.</p>

---

## Post #4 by @Saima (2019-10-29 04:07 UTC)

<p>Hi andras,<br>
I used the following on volume node n.<br>
mRAS=vtk.vtkMatrix4x4();<br>
n.GetIJKToRASMatrix(mRAS)</p>
<p>I need to get the data of image in world coordinates. How can I do that.</p>
<p>Also, is it possible to align fiducials along the vtk model automatically.</p>
<p>Or if I have fiducials in ijk coordinates how can I convert them into RAS coordinates</p>

---

## Post #5 by @lassoan (2019-10-29 12:06 UTC)

<p>Conversion between voxel (IJK) and world (RAS) are described in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates">script repository</a>.</p>
<p>Markup fiducial points are placed on visible surfaces and when you drag-and-drop them they remain on surfaces.</p>
<p>If you want to snap to a particular surface then you need to iterate through the points and modify point coordinates to the closest point on the surface. Within days we expect tonhave this feature added to Markups module (or is currently under review).</p>

---

## Post #6 by @aiden.zhu (2019-12-06 18:00 UTC)

<p>Hi Andras,<br>
I have a silly question for this hardening topic:<br>
Should I have to (or optionally) remove the observers  of  a volume node before I do hardening on this volume-node?  I mean, you say, we do transform on a volume-node which is associated with a transformed node, right? so when we do the volume-node transform-hardening, the transform-node is still connecting to the volume-node or it is being stopped after the hardening process?</p>
<p>Thanks a lot.</p>

---

## Post #7 by @lassoan (2019-12-06 19:48 UTC)

<p>There is no need to change any observers when the parent transform of an observed volume node changes (due to hardening a transform or for any other reason).</p>

---
