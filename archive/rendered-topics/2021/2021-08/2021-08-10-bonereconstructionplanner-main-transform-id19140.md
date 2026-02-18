# BoneReconstructionPlanner main transform

**Topic ID**: 19140
**Date**: 2021-08-10
**URL**: https://discourse.slicer.org/t/bonereconstructionplanner-main-transform/19140

---

## Post #1 by @mau_igna_06 (2021-08-10 13:32 UTC)

<p>This post is to explain the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/" rel="noopener nofollow ugc">BoneReconstructionPlanner</a> main transform, that is the mandibleToFibula transform.</p>
<p>The mandibleToFibula transform is used to create the fibulaPlanes from the mandiblePlanes like this:<br>
fibulaPlaneToWorld = mandibleToFibula*mandiblePlaneToWorld</p>
<p>Also the bone pieces of the fibula are transformed to the mandible using the inverse of that transform, the fibulaToMandible transform:<br>
reconstructedFibulaPieceMeshPoints = fibulaToMandible*fibulaPieceMeshPoints</p>
<p>So the mandibleToFibula transform is the most important transform on BoneReconstructionPlanner as Virtual Surgical Planning would be impossible without it.</p>
<p>The mandibleToFibula transform <strong>is a kind of registration transform</strong> and it is not a change of frame transform.</p>
<p>Because the mandibleToFibula transform is not a change of frame transform it cannot be calculated as mandibleToFibula = worldToFibulaFrame*mandibleFrameToWorld</p>
<p>Please look at this example of a registration transform to know more and ask if you have questions:</p>
<pre><code class="lang-auto">#simple registration of two cts of the same patient on Slicer Stable Release

#the second ct will be simulated as a transformed version from the first ct

#first load two equals cts
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
image1 = sampleDataLogic.downloadMRHead()
image1.SetName('image1')
image2 = sampleDataLogic.downloadMRHead()
image2.SetName('image2')

#set up different colors to each scalarVolume
image1DisplayNode = image1.GetDisplayNode()
image1DisplayNode.SetAndObserveColorNodeID("vtkMRMLColorTableNodeGreen")
image2DisplayNode = image2.GetDisplayNode()
image2DisplayNode.SetAndObserveColorNodeID("vtkMRMLColorTableNodeBlue")

image1_points_world = slicer.mrmlScene.CreateNodeByClass("vtkMRMLMarkupsFiducialNode")
image1_points_world.SetName("image1_points_world")
slicer.mrmlScene.AddNode(image1_points_world)
slicer.modules.markups.logic().AddNewDisplayNodeForMarkupsNode(image1_points_world)

image2_points_world = slicer.mrmlScene.CreateNodeByClass("vtkMRMLMarkupsFiducialNode")
image2_points_world.SetName("image2_points_world")
slicer.mrmlScene.AddNode(image2_points_world)
slicer.modules.markups.logic().AddNewDisplayNodeForMarkupsNode(image2_points_world)

pointNose = [-2.324420213699341,	-108.38597106933594,	-14.390022277832031]
pointTipOfTheEar = [83.80633544921875,	33.72900390625,	-15.804760932922363]
pointTipOfTheHead = [-2.6361961364746094,	47.51253890991211,	90.47916412353516]

#You can change this points for any you would like but there has to be 3 points
pointList = [pointNose,pointTipOfTheEar,pointTipOfTheHead]

for i in range(len(pointList)):
  image1_points_world.AddControlPoint(vtk.vtkVector3d(pointList[i]))
  image2_points_world.AddControlPoint(vtk.vtkVector3d(pointList[i]))


#transform image2 and image2_points_world with a randomTransform
randomTransform = vtk.vtkTransform()
randomTransform.PostMultiply()

#angleDegrees, rotationAxis and position can be changed to any you would like
angleDegrees = 49
rotationAxis = [0.27000401,  0.83251236, -0.48375718]
position = [40,50,60]

randomTransform.RotateWXYZ(angleDegrees, rotationAxis)
randomTransform.Translate(position)

randomTransformNode = slicer.vtkMRMLLinearTransformNode()
randomTransformNode.SetName("randomTransform")
slicer.mrmlScene.AddNode(randomTransformNode)

randomTransformNode.SetMatrixTransformToParent(randomTransform.GetMatrix())

#apply and harden the transform
image2.SetAndObserveTransformNodeID(randomTransformNode.GetID())
image2.HardenTransform()
image2_points_world.SetAndObserveTransformNodeID(randomTransformNode.GetID())
image2_points_world.HardenTransform()


#Now we have two cts that need to be registered and we have fiducials marking
# the same anatomical points on them, so we can do a simple registration
#For the registration we need one frame created from each of the markupPointsLists
#To create the frames we will use planes

image1_plane = slicer.mrmlScene.CreateNodeByClass("vtkMRMLMarkupsPlaneNode")
image1_plane.SetName("image1_plane")
slicer.mrmlScene.AddNode(image1_plane)
slicer.modules.markups.logic().AddNewDisplayNodeForMarkupsNode(image1_plane)

image2_plane = slicer.mrmlScene.CreateNodeByClass("vtkMRMLMarkupsPlaneNode")
image2_plane.SetName("image2_plane")
slicer.mrmlScene.AddNode(image2_plane)
slicer.modules.markups.logic().AddNewDisplayNodeForMarkupsNode(image2_plane)

for i in range(image1_points_world.GetNumberOfControlPoints()):
  point = [0,0,0]
  image1_points_world.GetNthControlPointPosition(i,point)
  image1_plane.AddControlPoint(vtk.vtkVector3d(point))

for i in range(image2_points_world.GetNumberOfControlPoints()):
  point = [0,0,0]
  image2_points_world.GetNthControlPointPosition(i,point)
  image2_plane.AddControlPoint(vtk.vtkVector3d(point))


image1FrameToWorldMatrix = vtk.vtkMatrix4x4()
image1_plane.GetPlaneToWorldMatrix(image1FrameToWorldMatrix)

image2FrameToWorldMatrix = vtk.vtkMatrix4x4()
image2_plane.GetPlaneToWorldMatrix(image2FrameToWorldMatrix)

# Now we calculate the transform needed for registration
worldToImage1FrameMatrix = vtk.vtkMatrix4x4()
worldToImage1FrameMatrix.DeepCopy(image1FrameToWorldMatrix)
worldToImage1FrameMatrix.Invert()

registrationTransform = vtk.vtkTransform()
registrationTransform.PostMultiply()
registrationTransform.Concatenate(worldToImage1FrameMatrix)
registrationTransform.Concatenate(image2FrameToWorldMatrix)

registrationTransformNode = slicer.vtkMRMLLinearTransformNode()
registrationTransformNode.SetName("registrationTransform")
slicer.mrmlScene.AddNode(registrationTransformNode)

registrationTransformNode.SetMatrixTransformToParent(registrationTransform.GetMatrix())

#apply the transform to image1 and image1_points_world to see if they overlap with the
# image2 counterparts.
image1.SetAndObserveTransformNodeID(registrationTransformNode.GetID())
image1_points_world.SetAndObserveTransformNodeID(registrationTransformNode.GetID())

#user: view both volumes, one as foreground, the other as background and check that they
# overlap.

#We can confirm that the registrationTransform is indeed correct because it is equal to the
# randomTransform we applied to image1 at the start

#So we know what the registration transform does. So we can call it image1ToImage2Transform 
registrationTransformNode.SetName("image1ToImage2Transform")

#Some interesting detail: the registration transform was not calculated as
# image1FrameToImage2Frame = worldToImage2*image1FrameToWorld
# the main reason for this is that the markup points are in world coordinates, not in
# image1Frame or image2Frame coordinates
</code></pre>

---
