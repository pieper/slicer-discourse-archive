---
topic_id: 15442
title: "How To Transform Fiducial Coordinates Into Image Space"
date: 2021-01-10
url: https://discourse.slicer.org/t/15442
---

# How to transform fiducial coordinates into image space

**Topic ID**: 15442
**Date**: 2021-01-10
**URL**: https://discourse.slicer.org/t/how-to-transform-fiducial-coordinates-into-image-space/15442

---

## Post #1 by @FatihSogukpinar (2021-01-10 22:51 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>One last (and kind of dumb) question : If I want to transform my fiducials points to my image space, (rather than rotating my slice view), can I do that by using this transform matrix ? I have some other models, which I don’t know how to rotate. Therefore I don’t want to rotate my image(s), but just adjust fiducial RAS’s, so that they are not cut through multiple slices. Is this doable ?</p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2021-01-10 22:58 UTC)

<p>You can find complete examples of transforming between world (RAS) and voxel (IJK) coordinates (even if the volume and fiducials are under arbitrary, even warping transforms) in the script repository:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates</a></p>

---

## Post #3 by @FatihSogukpinar (2021-01-11 00:54 UTC)

<p>If I understand correctly, I need the following step to solve my problem (the rest is for mapping from RAS to IJK).  However, when I applied the following code to my fiducials, their coordinates do not change (i.e., point_VolumeRas  = point_Ras) . Why would that be ? Should I change the first argument of GetTransformBetweenNodes from None to something else ?</p>
<pre><code class="lang-python"># If volume node is transformed, apply that transform to get volume's RAS coordinates
transformRasToVolumeRas = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transformRasToVolumeRas)
point_VolumeRas = transformRasToVolumeRas.TransformPoint(point_Ras[0:3])
</code></pre>

---

## Post #4 by @FatihSogukpinar (2021-01-11 01:02 UTC)

<p>If my question is not clear enough, here is what I am doing :</p>
<pre><code class="lang-python">fidList = slicer.util.getNode(nodeName)
numFids = fidList.GetNumberOfFiducials()
markupsNode = getNode(nodeName)
for i in range(numFids):
    ras = [0,0,0]
    fidList.GetNthFiducialPosition(i,ras)
    point_Ras = [ras[0], ras[1], ras[2], 1]
    markupsIndex = i 
    markupsNode.GetNthFiducialWorldCoordinates(markupsIndex, point_Ras)
    transformRasToVolumeRas = vtk.vtkGeneralTransform()
    slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transformRasToVolumeRas)
    point_VolumeRas = transformRasToVolumeRas.TransformPoint(point_Ras[0:3])
</code></pre>
<p>But point_VolumeRas  is the same as point_Ras</p>
<p>Thanks a lot.</p>

---

## Post #5 by @lassoan (2021-01-11 06:13 UTC)

<p><code>point_VolumeRas</code> is expected to be the same as <code>point_Ras</code>, unless the volume is transformed.</p>
<p>If you want to compute voxel coordinates (IJK) then use the complete example code that I linked above.</p>

---
