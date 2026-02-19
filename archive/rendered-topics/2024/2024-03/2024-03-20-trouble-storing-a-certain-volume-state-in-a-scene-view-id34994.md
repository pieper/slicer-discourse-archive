---
topic_id: 34994
title: "Trouble Storing A Certain Volume State In A Scene View"
date: 2024-03-20
url: https://discourse.slicer.org/t/34994
---

# Trouble Storing a certain Volume State in a Scene View

**Topic ID**: 34994
**Date**: 2024-03-20
**URL**: https://discourse.slicer.org/t/trouble-storing-a-certain-volume-state-in-a-scene-view/34994

---

## Post #1 by @Adam-Ismaili-92 (2024-03-20 19:45 UTC)

<p><em># Consider having defined “origin” (a 3d array point), “axis1” (a 3d array axis), “alpha” (a float)</em></p>
<p><em># Rotation process</em><br>
<em>transform1 = vtk.vtkTransform()</em></p>
<p><em>transform1.Translate(-origin[0], -origin[1], -origin[2])</em></p>
<p><em>transform1.RotateWXYZ(np.degrees(alpha), axis1[0], axis1[1], axis1[2])</em></p>
<p><em>transform1.Translate(origin[0], origin[1], origin[2])</em></p>
<p><em># Apply the rotation on axis1</em><br>
<em>volumeNode.ApplyTransform(transform1)</em></p>
<p><em># Save a scene view</em><br>
<em>sceneView = slicer.mrmlScene.CreateNodeByClass(‘vtkMRMLSceneViewNode’)</em></p>
<p><em>sceneView.SetScene(slicer.mrmlScene)</em></p>
<p><em>sceneView.SetName(‘View_1’)</em></p>
<p><em>slicer.mrmlScene.AddNode(sceneView)</em></p>
<p><em>sceneView.StoreScene()</em></p>
<p><em># Recover the original volume by applying inverse transformation</em><br>
<em>inverseTransform1 = transform1.GetInverse()</em></p>
<p><em>volumeNode.ApplyTransform(inverseTransform1)</em></p>
<p>With the code snipped above, I have some issues storing my volume at a certain state in a view.</p>
<p>When I try to apply a first transformation, then take a view, and revert the transformation, the view doesn’t save the transformed state, but only the reverted state.</p>
<p>Can someone explain me why and help me find a solution ?</p>

---
