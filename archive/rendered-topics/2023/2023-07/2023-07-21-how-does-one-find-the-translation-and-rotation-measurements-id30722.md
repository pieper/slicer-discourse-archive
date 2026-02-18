# How does one find the translation and rotation measurements of one anatomy with respect to another?

**Topic ID**: 30722
**Date**: 2023-07-21
**URL**: https://discourse.slicer.org/t/how-does-one-find-the-translation-and-rotation-measurements-of-one-anatomy-with-respect-to-another/30722

---

## Post #1 by @Firoza_Kothari (2023-07-21 04:29 UTC)

<p>I would like to find the Translation XYZ and Rotation XYZ of one anatomy with respect to another - say if I would like to consider center of the bone to be the origin and would like to find the above measurements of the center of a tumour with respect to the bone, how can I find such measurements?</p>

---

## Post #2 by @lassoan (2023-07-24 16:35 UTC)

<p>First you need to specify coordinate system for each object. An easy way to do it is to place a plane in Markups module that is aligned with the origin and axis directions. You can right-click on a control point and enable Translation and Rotation interactions to make alignment easier.</p>
<p>You can then get the relative transform by copy-pasting this code snippet in the Python console:</p>
<pre><code class="lang-python">planeA = getNode('P')
planeB = getNode('P_1')

# Compute PlaneA to PlaneB transformation matrix 
planeAToWorldMatrix = vtk.vtkMatrix4x4()
planeA.GetObjectToWorldMatrix(planeAToWorldMatrix)
planeBToWorldMatrix = vtk.vtkMatrix4x4()
planeB.GetObjectToWorldMatrix(planeBToWorldMatrix)
worldToPlaneBMatrix = vtk.vtkMatrix4x4()
vtk.vtkMatrix4x4.Invert(planeBToWorldMatrix, worldToPlaneBMatrix)
planeAToPlaneBMatrix = vtk.vtkMatrix4x4()
vtk.vtkMatrix4x4.Multiply4x4(worldToPlaneBMatrix, planeAToWorldMatrix, planeAToPlaneBMatrix)

# Save matrix into transformation node
planeAToPlaneBTransformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", "PlaneA to PlaneB transform")
planeAToPlaneBTransformNode.SetMatrixTransformToParent(planeAToPlaneBMatrix)
</code></pre>
<p>You can then use <a href="https://github.com/PerkLab/SlicerSandbox#characterize-transform-matrix">Characterize transform matrix</a> module (in Sandbox extension) to get some relative position and orientation information from that transformation.</p>

---

## Post #3 by @Firoza_Kothari (2023-10-31 19:25 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> Thank you for your response. I guess the above gives me relative positions to certain points that I choose which can change from dataset to dataset. May be I can rephrase my question.</p>
<p>If I have two STL files - one of the bone and second of tumour, is there a way I can find the center coordinate of bone (so I will consider it as my 0,0,0) and then find the coordinates of translation and rotation of the center of the tumour with respect to the center of the bone? This way I am reducing the dependency on point selection and relative coordinates.</p>
<p>The problem is that when I export the STL files and load it into another viewer (say something like viewstl), it brings all STLs to the center of the viewer and the spatial translations and rotations are lost (sometimes rotations are maintained, so just need translation values in such cases). May be this can help explain the reason I am looking for this solution.</p>

---

## Post #4 by @mikebind (2023-10-31 20:56 UTC)

<p>You need more that a center point to determine a coordinate system in 3D.  <a class="mention" href="/u/lassoan">@lassoan</a> 's suggestion is a simple way to define a coordinate system using a MarkupsPlane.  Once you have defined the coordinate system based on the bone (origin at center, first coordinate axis along the long axis of the bone, second coordinate axis to the patient’s right (for example), third coordinate axis as the cross product of the first two axes (the normal to the plane defined by the first two axes)), only then can you describe the location of something else in this (e.g. a tumor center point) in that coordinate system.</p>
<p>You mention having two STL files.  It is important to note that there is no solution to your problem unless coordinates of both STL files are already reported in a shared coordinate system.  That is, if you load both of them into Slicer, do they appear in the proper 3D spatial relationship to each other?  If for example, they are both centered or both have their coordinate origins at a corner of their bounding boxes, the information which would allow you to understand their spatial relationship to one another has already been lost.</p>

---

## Post #5 by @lassoan (2023-10-31 21:04 UTC)

<p>It sounds like some of the software that you use cannot read or write meshes in STL files. If the meshes get centered after writing&amp;reading then you can try to adjust settings when you read and write the file, use a different file format, or stop using that software.</p>

---

## Post #6 by @Firoza_Kothari (2023-10-31 21:25 UTC)

<p>Thanks <a class="mention" href="/u/mikebind">@mikebind</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for your quick responses. I am not too good with running codes and hence I was looking for solutions to find the co-ordinates with the tools already provided in the interface. I am exporting the STLs from 3D Slicer itself so initially the co-ordinate system is maintained.</p>
<p>I think one solution might work and will need your help with that.</p>
<p>Is there a way to create a bounding box around the part, then create a plane though its exact midplane and get the origin center co-ordinates of that midplane?</p>

---

## Post #7 by @mikebind (2023-10-31 22:18 UTC)

<p>I think it is unlikely that you will be able to extract the information you want using only existing GUI tools, however, the coding/analysis you need to do may be pretty minimal.  Check out the Segment Statistics module.  If you have your bone and your tumor as segments in a segmentation, the Segment Statistics module can help you gather the centroid coordinates for each, as well as principal axes and oriented bounding boxes.  You could consider the centroid or the center of the bounding box as the origin point, and the principal axes of the bone bounding box as the coordinate axis directions.  Then, in your own code (or even by hand if that’s better for you) you can take the centroid coordinates of the tumor and express them in your newly defined bone coordinate system (i.e. subtract the bone center and change the basis vectors).  The result would be a description of the tumor location relative to the bone in a coordinate system centered on the bone and oriented by its principal axes.  If the bone of interest is of reasonably consistent shape from subject to subject, this coordinate system may be reproducible enough to use to compare across subjects (which I am guessing is your ultimate goal?)</p>

---

## Post #8 by @lassoan (2023-11-01 13:46 UTC)

<p>Instead of trying to fix data corruption by manually recording and later restoring some information that is lost; it would be better to prevent data corruption from happening.</p>
<p>Can you describe your data flow - list of what processing steps you do in what software, what inputs are used and outputs are generated in each step? We should be able to give you advice about what to change in your data flow to avoid data corruption.</p>

---
