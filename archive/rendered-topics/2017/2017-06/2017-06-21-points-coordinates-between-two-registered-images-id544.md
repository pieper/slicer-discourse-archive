# Point's coordinates between two registered images

**Topic ID**: 544
**Date**: 2017-06-21
**URL**: https://discourse.slicer.org/t/points-coordinates-between-two-registered-images/544

---

## Post #1 by @sandra (2017-06-21 08:10 UTC)

<p>Hi!</p>
<p>I have two images registered together and I would like to, given the IJK coordinates of a point in the first image, get its IJK coordinates in the second one.<br>
To do so, I did this:</p>
<pre><code> firstVolume-&gt;GetIJKToRASMatrix(ijkToRasMatrix);
 secondVolume-&gt;GetRASToIJKMatrix(rasToIjkMatrix);

 double ijkCoordinates1[3] = {x,y,z};
 double rasCoordinates[3];
 ijkToRasMatrix-&gt;MultiplyPoint(ijkCorrdinates1,rasCoordinates);

 double ijkCoordinates2[3];
 rasToIjkMatrix-&gt;MultiplyPoint(rasCoordinates,ijkCoordinates2);
</code></pre>
<p>But the point I obtain in the second image doesn’t match the point in the first one.<br>
Is this the correct way to do want I want to do ?</p>
<p>Thanks for your help,</p>
<p>Sandra.</p>

---

## Post #2 by @lassoan (2017-06-21 23:37 UTC)

<p>If the two volume nodes have different parent transforms, then you need to take into account the transform between them:</p>
<pre><code>firstVolumeToSecondVolumeTransformMatrix = vtk.vtkMatrix4x4()
slicer.vtkMRMLTransformNode.GetMatrixTransformBetweenNodes(firstVolume.GetParentTransformNode(), secondVolume.GetParentTransformNode(), firstVolumeToSecondVolumeTransformMatrix)</code></pre>

---

## Post #3 by @sandra (2017-06-22 08:39 UTC)

<p>Ok,<br>
but when I do firstVolume.GetParentTransformNode() I get a null node (same thing for the second volume) so the transform matrix between these nodes is identity</p>

---

## Post #4 by @lassoan (2017-06-22 12:06 UTC)

<p>That is good then, they are in the same coordinate system.</p>
<p>However, there is a problem with your coordinates. Homogeneous point coordinates have 4 components, not just 3. The value of the 4th component must be 1.</p>
<p>For example:</p>
<pre><code>double ijkCoordinates1[4] = {x,y,z,1};
double rasCoordinates[4] = {0,0,0,1};</code></pre>

---

## Post #5 by @sandra (2017-06-22 12:40 UTC)

<p>That works perfectly, thank you very much !<br>
I thought I was missing some kind of transformation between the two images and I wouldn’t have thought about this.</p>

---
