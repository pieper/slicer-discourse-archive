---
topic_id: 24568
title: "Tracking Cursor Movements To Access Voxel Values"
date: 2022-07-29
url: https://discourse.slicer.org/t/24568
---

# Tracking cursor movements to access voxel values

**Topic ID**: 24568
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/tracking-cursor-movements-to-access-voxel-values/24568

---

## Post #1 by @leo (2022-07-29 16:40 UTC)

<p>Hey everyone,<br>
I was trying to write a quick Pyton script to track the mouse movement with ‘Crosshair’ and return the voxel value using the ijk position. I ran the script within Slicer’s Python Interactor and launched Slicer from Command Line in order to be able to see error messages. This is the Script I wrote:</p>
<pre><code class="lang-auto">
def onMouseMoved(observer,eventid):
	crosshair=slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLCrosshairNode")
	crosshair.SetCrosshairBehavior(crosshair.CenteredJumpSlice)
	ras = [0.0, 0.0, 0.0]
	crosshairNode.GetCursorPositionRAS(ras)
	#slicer.vtkMRMLSliceNode.JumpAllSlices(slicer.mrmlScene, *ras, slicer.vtkMRMLSliceNode.CenteredJumpSlice)
	#print(ras)
	transform_ras_to_volume_ras = vtk.vtkGeneralTransform("Crosshair")
	voxel_value_array = slicer.util.arrayFromVolume(transform_ras_to_volume_ras)
	voxel_value = voxel_value_array[ras[2], ras[1],ras[0]]
	ras_to_voxel = vtk.vtkMatrix4x4()
	crosshairNode.GetRASToIJKNatrix(ras_to_voxel)
	voxel_point = [0,0,0,1]
	ras_to_voxel.MultiplyPoint(np.append(voxel_value,1.0),voxel_point)
	voxel_point = [ int(round(c) for c in voxel_point[0:3])	 ]
	print(voxel_point)

crosshairNode = slicer.util.getNode("Crosshair")
id = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)
</code></pre>
<p>The Script did not break upon printing ras and returned coordinate values upon pressing SHIFT.<br>
But when I added the rest of the code to transform ras coordinates to ijk, Slicer started breaking without any errors which before where shown in command line.</p>
<p>Now I hope someone is able to clarify how I am breaking Slicer or whether the approach to the transformation is wrong within itself.</p>
<p>Also it would be helpful to see error outputs on  the command line where I invoked Slicer</p>

---

## Post #2 by @Sunderlandkyl (2022-07-29 17:06 UTC)

<aside class="quote no-group" data-username="leo" data-post="1" data-topic="24568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c2a13f/48.png" class="avatar"> leo:</div>
<blockquote>
<p><code>transform_ras_to_volume_ras = vtk.vtkGeneralTransform("Crosshair")</code></p>
</blockquote>
</aside>
<p>This is the line that is causing the crash. There is no constructor for vtkGeneralTransform that takes a string. I believe the crash is caused because the constructor is trying to interpret it as a hexadecimal memory address.</p>
<p>There are a couple of other issues with your script:</p>
<ul>
<li>The input to slicer.util.arrayFromVolume should be the volume node that you are inspecting, not a vtkGeneralTransform</li>
<li>GetRASToIJKNatrix → GetRASToIJKMatrix</li>
<li>voxel_value_array cannot be accessed using RAS, you should use the IJK coordinates. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></li>
</ul>

---

## Post #3 by @leo (2022-08-03 16:15 UTC)

<p>Hey thankyou very much for you reply!! indeed I see my fallacies there. I am sorry that I haven’t got back to you earlier, but I am only able to access this PC twice a week. May I ask you if there is an alternate way to go from RAS to Volume RAS using Cosshair since right now I have tried this <code>slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, crosshairNode, transform_ras_to_volume_ras)</code>  but my issue is that the transform function cannot be applied to a CrossairNode.</p>

---

## Post #4 by @Sunderlandkyl (2022-08-03 16:25 UTC)

<p>The crosshair node is already in “World” coordinates. If the volume node is not under a transform, then World coordinates == Volume RAS coordinates.</p>
<p>You can get a transform from WorldToVolumeRAS with:</p>
<pre><code class="lang-python">worldToVolumeRAS = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volume.GetParentTransformNode(), worldToVolumeRAS)
</code></pre>

---

## Post #5 by @leo (2022-08-03 17:35 UTC)

<p>If I get you right my next steps should be Volume Ras → IJK by Matrix tranformation and then accessing voxel Value from IJK.</p>
<p>My Matrix generation has thrown errors <code>Volume_RAS_toIJK = vtk.vtkMatrix4x4() 	ijk_node = Volume_RAS_toIJK.GetRASToIJKMatrix(Volume_RAS_toIJK)</code> gets me this error: ‘vtkmodules.vtkCommonMath.vtkMatrix4x4’ object has no attribute ‘GetRASToIJKMatrix’.</p>

---

## Post #6 by @Sunderlandkyl (2022-08-03 18:23 UTC)

<p>Yeah, you’re on the right track.</p>
<aside class="quote no-group" data-username="leo" data-post="5" data-topic="24568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c2a13f/48.png" class="avatar"> leo:</div>
<blockquote>
<p>Volume_RAS_toIJK.GetRASToIJKMatrix(Volume_RAS_toIJK)</p>
</blockquote>
</aside>
<p>It should be volumeNode.GetRASToIJKMatrix(Volume_RAS_toIJK). Where volumeNode is the vtkMRMLVolumeNode that you are trying to inspect.</p>

---

## Post #7 by @siqueirl (2022-08-05 13:53 UTC)

<p>HI Kyle, thank you for helping us on this (I work with Leo).</p>
<p>I’m posting in case other people can benefit from our attempt - I believe we managed to get it working by simply moving the computationally-expensive calls outside the mouse movement loop. The console is now printing reasonable values for voxels at coordinates:</p>
<p>This is our current code:</p>
<pre><code class="lang-auto">import numpy as np

ras = [0, 0, 0]
volumeNode = slicer.util.getNode("MRHead")
# Apply that transform to get volume's RAS coordinates
transform_ras_to_volume_ras = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transform_ras_to_volume_ras)
# Get volume as slicer array
a = arrayFromVolume(volumeNode)

def onMouseMoved(observer,eventid):
    # Get point coordinate in RAS
    ras = [0, 0, 0]
    crosshairNode.GetCursorPositionRAS(ras)
    point_volume_ras = transform_ras_to_volume_ras.TransformPoint(ras[0:3])
    # Get voxel coordinates from physical coordinates
    volume_ras_to_ijk = vtk.vtkMatrix4x4()
    volumeNode.GetRASToIJKMatrix(volume_ras_to_ijk)
    point_ijk = [0, 0, 0, 1]
    volume_ras_to_ijk.MultiplyPoint(np.append(point_volume_ras, 1.0), point_ijk)
    point_ijk = [ int(round(c)) for c in point_ijk[0:3] ]
    # Get markup's position
    x, y, z = point_ijk[0], point_ijk[1], point_ijk[2]
    value = a[z,y,x]
    print(value)

crosshairNode=slicer.util.getNode("Crosshair")
observerId = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)
</code></pre>

---

## Post #8 by @lassoan (2022-08-07 06:42 UTC)

<p>If you need to do relatively expensive computations to display information about the current mouse position then a good technique is “delayed update”: you don’t compute while the mouse is moving but immediately when it stops. Implementation: Instead of calling the computation directly from the mouse event callback, you only trigger a QTimer with a short timeout (e.g., 100ms). If a new mouse event arrives then you restart the timer. When mouse movement stops then the timer elapses, which triggers the computation.</p>

---

## Post #9 by @siqueirl (2022-08-08 14:32 UTC)

<p>Thank you for sharing this tip. I will eventually need to optimize this tracking loop, so it’s good to know about this pattern.</p>

---
