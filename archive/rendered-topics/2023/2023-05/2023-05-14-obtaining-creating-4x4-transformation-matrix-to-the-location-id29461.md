---
topic_id: 29461
title: "Obtaining Creating 4X4 Transformation Matrix To The Location"
date: 2023-05-14
url: https://discourse.slicer.org/t/29461
---

# Obtaining/Creating 4x4 Transformation matrix to the location of a vtkMRMLCameraNode

**Topic ID**: 29461
**Date**: 2023-05-14
**URL**: https://discourse.slicer.org/t/obtaining-creating-4x4-transformation-matrix-to-the-location-of-a-vtkmrmlcameranode/29461

---

## Post #1 by @akumar81 (2023-05-14 13:52 UTC)

<p>I’m currently working on a project where I control the position of a <code>vtkCameraNode</code> in 3D view with a robotic arm. To achieve this, I’ve been placing the camera node on top of a transform like so:</p>
<pre><code class="lang-python">
camera_node.SetNodeReferenceID("transform", transform_for_the_camera.GetID())
</code></pre>
<p>With this method, I can successfully move the camera and retrieve the position of the camera using <code>GetAppliedTransform()</code>. Here is an example of the output:</p>
<pre><code class="lang-python">
print(stereo.camera_node2.GetAppliedTransform())
</code></pre>
<p>Output:</p>
<pre><code class="lang-yaml">
vtkMatrix4x4 (0x564de95445d0)
  Debug: Off
  Modified Time: 2695454
  Reference Count: 2
  Registered Events: (none)
  Elements:
    -0.0177592 0.999842 7.34635e-06 -0.000133888 
    0.00592044 9.78115e-05 0.999982 -36.4499 
    0.999825 0.0177589 -0.00592124 -12.88 
    0 0 0 1 
</code></pre>
<p>However, I have a couple of challenges that I need help with. Can I either? :</p>
<p><strong>1. Is there a way to obtain the transformation to the camera_node before SetNodeReferenceID(“transform”, transform_for_the_camera.GetID()) is used?</strong></p>
<p><strong>OR</strong></p>
<p><strong>2. Is it possible to reconstruct the AppliedTransform using available functions like GetViewUp() and GetPosition()?</strong></p>
<p>To illustrate the second point, here are the outputs of these functions:</p>
<pre><code class="lang-python">
print(stereo.camera_node2.GetViewUp())  # view_up
print(stereo.camera_node2.GetPosition())  # position
print(stereo.camera_node2.GetFocalPoint())  # focal_point
</code></pre>
<p>Output:</p>
<pre><code class="lang-scss">
(7.346345810766298e-06, 0.9999824692637288, -0.005921242373602143)  # view_up
(-0.00013388794915210472, -36.4498973704036, -12.879999999811874)  # position
(-1.2295649116714942, -86.05915036780942, 10.081280602927164)  # focal_point
</code></pre>
<p>In the <strong><code>AppliedTransform</code> 4x4 matrix, the <code>view_up</code> vector matches the third column and <code>position</code> matches the fourth column.</strong> I attempted to reconstruct the first or second column using <code>(focal_point - position)/norm(focal_point - position)</code> <em>but the results do not match the values in the matrix.</em></p>
<p>I would greatly appreciate any guidance or suggestions. Thanks in advance for your time and help!</p>

---

## Post #2 by @lassoan (2023-05-14 13:56 UTC)

<p>I would recommend to use the <a href="https://github.com/SlicerIGT/SlicerIGT#viewpoint">Viewpoint</a> module in SlicerIGT extension for positioning a camera with a transform. It allows you to directly set the relative transform between the driving transform and the camera.</p>

---
