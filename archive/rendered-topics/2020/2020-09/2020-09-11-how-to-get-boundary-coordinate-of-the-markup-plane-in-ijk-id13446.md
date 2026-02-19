---
topic_id: 13446
title: "How To Get Boundary Coordinate Of The Markup Plane In Ijk"
date: 2020-09-11
url: https://discourse.slicer.org/t/13446
---

# How to get boundary coordinate of the markup plane in IJK

**Topic ID**: 13446
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/how-to-get-boundary-coordinate-of-the-markup-plane-in-ijk/13446

---

## Post #1 by @Yusuke (2020-09-11 17:58 UTC)

<p>Hi,</p>
<p>I would like to know how to get coordinates for the boundaries of a markup plane in IJK.<br>
In fiducial point case, my understanding is that we can get the following codes:<br>
world = [0, 0, 0, 0]<br>
fiducialNode.GetNthFiducialWorldCoordinates(index, world)<br>
then something like this<br>
p_Ras = [coord[0], coord[1], coord[2], 1.0]<br>
p_Ijk = RasToIjkMatrix.MultiplyDoublePoint(p_Ras)</p>
<p>but I am wondering  how to get the coordinates of plane nodes. I couldn’t find the function for it in the vtkMRMLMarkupsPlaneNode class.</p>
<p>Thank you for your help!</p>

---

## Post #2 by @lassoan (2020-09-11 19:15 UTC)

<p>Markups plane coordinate system is described in the <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsPlaneNode.html#details">documentation</a>: “Origin of plane at 0,0,0, XYZ axis aligned to XYZ unit vectors”. For example, homogeneous coordinate of one of the corners is <code>[planeBounds[0], planeBounds[2], 0, 1]</code>.</p>

---

## Post #3 by @Yusuke (2020-09-14 19:19 UTC)

<p>Thank you so much for your comment!</p>
<p>I was able to get the rectangle points by the following codes.</p>
<pre><code>    planeMarkup = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsPlaneNode")
    vol=slicer.util.getNode('MR*')

    planeBounds = [0, 0, 0, 0, 0, 0]
    planeMarkup.GetPlaneBounds(planeBounds)
    planeToWorldMatrix = vtk.vtkMatrix4x4()
    planeMarkup.GetPlaneToWorldMatrix(planeToWorldMatrix)

    ras_p1 = planeToWorldMatrix.MultiplyPoint([planeBounds[0], planeBounds[2], 0, 1])
    ras_p2 = planeToWorldMatrix.MultiplyPoint([planeBounds[1], planeBounds[3], 0, 1])
    RasToIjkMatrix = vtk.vtkMatrix4x4()
    vol.GetRASToIJKMatrix(RasToIjkMatrix)

    p1 = RasToIjkMatrix.MultiplyDoublePoint(ras_p1)
    p2 = RasToIjkMatrix.MultiplyDoublePoint(ras_p2)
    print('p1:{}'.format(p1))
    print('p2:{}'.format(p2))
</code></pre>
<p>Thanks for your help!</p>

---
