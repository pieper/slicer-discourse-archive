# SVD ModelToModel Registration Idea

**Topic ID**: 20388
**Date**: 2021-10-27
**URL**: https://discourse.slicer.org/t/svd-modeltomodel-registration-idea/20388

---

## Post #1 by @mau_igna_06 (2021-10-27 15:31 UTC)

<p>Hi. I was just thinking on an algorithm to register the same bone with boneModels of different time-points (that means segmented from different CTs).<br>
A frame for each bone can be created using the eigenVectors of the SVD (rotation part) and the meanOfPoints (translation part).<br>
The outputs of the SVD may not respect the right-hand rule, so that needs to be checked. And there are a little bit more technical details regarding this.<br>
Then the registrationTransformFromFrame0ToFrame1 is Frame1ToWorld*WorldToFrame0.<br>
With that transform you can register one bone0 to bone1.</p>
<p>The algorithm uses statistic metrics so it should work well with a little bit noisy inputs.</p>
<p>Do you think this algorithm would be useful? I think it would take maximum=15seconds to execute considering some technical details. The advantage is that it needs no user inputs.<br>
Is this an overkill for something that can be done with point2point registration?</p>
<p>I could develop it if the community shows interest</p>
<p>Mauro</p>

---

## Post #2 by @pieper (2021-10-27 16:28 UTC)

<p>Yes, I think that would be useful.  Note that some of the image registration methods have an option for initializing the optimization based on the moments so that might be similar to what you propose (you may want to investigate).</p>
<p>If computing time is a concern you could probably just take a random sample of the model points and still get a good estimate.</p>

---

## Post #3 by @mau_igna_06 (2021-10-28 15:08 UTC)

<p>Hi. Here is the script, you just need to change your input models and the numberOfSampledPoints to make the registration:</p>
<pre><code class="lang-auto">import numpy as np

#SVD Registration

boneModel0 = getNode('fibula')
boneModel1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode',"fibulaMoved")
boneModel1.CreateDefaultDisplayNodes()
boneModel1.CopyContent(boneModel0)
boneModel1DisplayNode = boneModel1.GetDisplayNode()
color = boneModel0.GetDisplayNode().GetColor()
boneModel1DisplayNode.SetColor(color[2],color[0],color[1])

#Create random transformation matrix
import numpy as np
import random
axisOfRotation = np.zeros(3)
angleOfRotation = 0
for i in range(len(axisOfRotation)):
  axisOfRotation[i] = random.random()

axisOfRotation = axisOfRotation/np.linalg.norm(axisOfRotation)

angleOfRotation = random.uniform(45, 315)

origin = np.zeros(3)
for i in range(len(origin)):
  origin[i] = random.uniform(50, 150)

randomTransform = vtk.vtkTransform()
randomTransform.PostMultiply()
randomTransform.RotateWXYZ(angleOfRotation,axisOfRotation)
randomTransform.Translate(origin)

#apply to boneModel1
transformer = vtk.vtkTransformFilter()
transformer.SetInputData(boneModel1.GetPolyData())
transformer.SetTransform(randomTransform)
transformer.Update()
boneModel1.SetAndObservePolyData(transformer.GetOutput())


maskPointsFilter = vtk.vtkMaskPoints()
maskPointsFilter.SetInputData(boneModel0.GetPolyData())

numberOfSampledPoints0 = 2000
ratio0 = int(boneModel0.GetPolyData().GetNumberOfPoints()/numberOfSampledPoints0)

#This works but the sampling could be biased spatially I think
maskPointsFilter.SetOnRatio(ratio0)
maskPointsFilter.RandomModeOn()
maskPointsFilter.Update()

polydata0 = vtk.vtkPolyData()
polydata0.ShallowCopy(maskPointsFilter.GetOutput())


maskPointsFilter = vtk.vtkMaskPoints()
maskPointsFilter.SetInputData(boneModel1.GetPolyData())

numberOfSampledPoints1 = 2000
ratio1 = int(boneModel1.GetPolyData().GetNumberOfPoints()/numberOfSampledPoints1)

#This works but the sampling could be biased spatially I think
maskPointsFilter.SetOnRatio(ratio1)
maskPointsFilter.RandomModeOn()
maskPointsFilter.Update()

polydata1 = vtk.vtkPolyData()
polydata1.ShallowCopy(maskPointsFilter.GetOutput())


#Calculate the SVD and mean
from vtk.util.numpy_support import vtk_to_numpy
model0Points = vtk_to_numpy(polydata0.GetPoints().GetData())
model1Points = vtk_to_numpy(polydata1.GetPoints().GetData())

# Calculate the mean of the points, i.e. the 'center' of the cloud
model0PointsMean = model0Points.mean(axis=0)
model1PointsMean = model1Points.mean(axis=0)

# Do an SVD on the mean-centered data.
uu0, dd0, eigenvectors0 = np.linalg.svd(model0Points - model0PointsMean)
uu1, dd1, eigenvectors1 = np.linalg.svd(model1Points - model1PointsMean)

# Create a frame for boneModel0
model0Z = np.zeros(3)
model0X = eigenvectors0[0]
model0Y = eigenvectors0[1]
vtk.vtkMath.Cross(model0X, model0Y, model0Z)
model0Z = model0Z/np.linalg.norm(model0Z)
model0Origin = model0PointsMean

def getAxes1ToWorldChangeOfFrameMatrix(axis1X,axis1Y,axis1Z,axisOrigin):
  axes1ToWorldChangeOfFrameMatrix = vtk.vtkMatrix4x4()
  axes1ToWorldChangeOfFrameMatrix.DeepCopy((1, 0, 0, 0,
                                        0, 1, 0, 0,
                                        0, 0, 1, 0,
                                        0, 0, 0, 1))
  axes1ToWorldChangeOfFrameMatrix.SetElement(0,0,axis1X[0])
  axes1ToWorldChangeOfFrameMatrix.SetElement(1,0,axis1X[1])
  axes1ToWorldChangeOfFrameMatrix.SetElement(2,0,axis1X[2])
  axes1ToWorldChangeOfFrameMatrix.SetElement(0,1,axis1Y[0])
  axes1ToWorldChangeOfFrameMatrix.SetElement(1,1,axis1Y[1])
  axes1ToWorldChangeOfFrameMatrix.SetElement(2,1,axis1Y[2])
  axes1ToWorldChangeOfFrameMatrix.SetElement(0,2,axis1Z[0])
  axes1ToWorldChangeOfFrameMatrix.SetElement(1,2,axis1Z[1])
  axes1ToWorldChangeOfFrameMatrix.SetElement(2,2,axis1Z[2])
  axes1ToWorldChangeOfFrameMatrix.SetElement(0,3,axisOrigin[0])
  axes1ToWorldChangeOfFrameMatrix.SetElement(1,3,axisOrigin[1])
  axes1ToWorldChangeOfFrameMatrix.SetElement(2,3,axisOrigin[2])
  return axes1ToWorldChangeOfFrameMatrix

model0ToWorldMatrix = getAxes1ToWorldChangeOfFrameMatrix(model0X,model0Y,model0Z,model0Origin)


# temporal frame for boneModel1
model1Z = np.zeros(3)
model1X = eigenvectors1[0]
model1Y = eigenvectors1[1]
vtk.vtkMath.Cross(model1X, model1Y, model1Z)
model1Z = model1Z/np.linalg.norm(model1Z)
model1Origin = model1PointsMean

temporalModel1ToWorldMatrix = getAxes1ToWorldChangeOfFrameMatrix(model1X,model1Y,model1Z,model1Origin)


def getChangeOfSignMatrix(i,j):
  changeOfSignMatrix = vtk.vtkMatrix4x4()
  changeOfSignMatrix.DeepCopy((1, 0, 0, 0,
                                0, 1, 0, 0,
                                0, 0, 1, 0,
                                0, 0, 0, 1))
  if i==0:
    changeOfSignMatrix.SetElement(0,0,1)
  else:
    changeOfSignMatrix.SetElement(0,0,-1)
  #
  if j==0:
    changeOfSignMatrix.SetElement(1,1,1)
  else:
    changeOfSignMatrix.SetElement(1,1,-1)
  #
  if j==i:
    changeOfSignMatrix.SetElement(2,2,1)
  else:
    changeOfSignMatrix.SetElement(2,2,-1)
  #
  return changeOfSignMatrix


# find the registration boneModel0ToBoneModel1Transform

boneModel0ToBoneModel1TransformListWithScore = []
for i in range(2):
  for j in range(2):
    boneModel0ToBoneModel1Transform = vtk.vtkTransform()
    boneModel0ToBoneModel1Transform.PostMultiply()
    #
    worldToBoneModel0Matrix = vtk.vtkMatrix4x4()
    worldToBoneModel0Matrix.DeepCopy(model0ToWorldMatrix)
    worldToBoneModel0Matrix.Invert()
    #
    boneModel0ToBoneModel1Transform.Concatenate(worldToBoneModel0Matrix)
    #
    model1ToWorldTransform = vtk.vtkTransform()
    model1ToWorldTransform.PostMultiply()
    model1ToWorldTransform.Concatenate(getChangeOfSignMatrix(i,j))
    model1ToWorldTransform.Concatenate(temporalModel1ToWorldMatrix)
    #
    boneModel0ToBoneModel1Transform.Concatenate(model1ToWorldTransform)
    #
    #boneModel0ToBoneModel1Transformer
    bone0ToBone1Transformer = vtk.vtkTransformFilter()
    bone0ToBone1Transformer.SetInputData(polydata0)
    bone0ToBone1Transformer.SetTransform(boneModel0ToBoneModel1Transform)
    bone0ToBone1Transformer.Update()
    #
    from vtk.util.numpy_support import vtk_to_numpy
    transformedModel0Points_vtk = bone0ToBone1Transformer.GetOutput().GetPoints().GetData()
    transformedModel0Points = vtk_to_numpy(transformedModel0Points_vtk)
    #
    pointsLocator = vtk.vtkPointLocator()
    pointsLocator.SetDataSet(bone0ToBone1Transformer.GetOutput())
    pointsLocator.BuildLocator()
    #
    distanceList = []
    for k in range(len(model1Points)):
      closestPointOfTransformedBone0ID = pointsLocator.FindClosestPoint(model1Points[k])
      difference = model1Points[k] - transformedModel0Points[closestPointOfTransformedBone0ID]
      distanceBetweenPoints = np.linalg.norm(difference)
      distanceList.append(distanceBetweenPoints)
    #
    distanceArray = np.array(distanceList)
    meanDistance = distanceArray.mean(axis=0)
    #
    boneModel0ToBoneModel1TransformListWithScore.append([boneModel0ToBoneModel1Transform,meanDistance])


boneModel0ToBoneModel1TransformListWithScore.sort(key = lambda item : item[1])

bone0ToBone1RegistrationTransformNode = slicer.vtkMRMLLinearTransformNode()
bone0ToBone1RegistrationTransformNode.SetName("Bone0ToBone1RegistrationTransform")
slicer.mrmlScene.AddNode(bone0ToBone1RegistrationTransformNode)

bone0ToBone1RegistrationTransformNode.SetMatrixTransformToParent(boneModel0ToBoneModel1TransformListWithScore[0][0].GetMatrix())

boneModel0.SetAndObserveTransformNodeID(bone0ToBone1RegistrationTransformNode.GetID())

</code></pre>
<p>The registration would work better if the sampled points were evenly distrubuted in the inputMeshes. The random selection of points makes it possible for ‘clusters’ of points of some part of the bone to appear. Although it is unlikely that this ‘clusters’ will be very dense, nevertheless this can make the registration less effective.</p>
<p>Maybe one way to solve this would be to sort the pointIds by geodesicDistance to some seed point, that way (maybe) you could just pickIteratively the next nth point and get an array of evenly distributed points in the mesh.</p>

---

## Post #4 by @lassoan (2021-10-28 19:08 UTC)

<p>Using moment or key feature point based initial alignment before robust ICP is a quite common pattern.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> would like to get a similar method ported from Open3D to VTK. See some more details <a href="https://discourse.vtk.org/t/vtk-point-cloud-and-mesh-filters-for-downsampling-registration-icp-transform/6974">here</a>.</p>
<p>You can also have a look at <a href="https://www.cloudcompare.org/doc/wiki/index.php?title=Alignment_and_Registration">CloudCompare’s mesh registration</a> and if you find methods that work well for you then port those to VTK/Slicer. <a href="https://github.com/cloudcompare/cloudcompare">CloudCompare is GPL</a>, so you cannot use anything from it as is, but it is good for testing an approach before spending time with implementing it (or searching for existing non-restricted implementations).</p>

---

## Post #5 by @muratmaga (2021-10-28 19:47 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="20388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The registration would work better if the sampled points were evenly distrubuted in the inputMeshes. The random selection of points makes it possible for ‘clusters’ of points of some part of the bone to appear. Although it is unlikely that this ‘clusters’ will be very dense, nevertheless this can make the registration less effective.</p>
</blockquote>
</aside>
<p>Yes, this sounds very much like how we use open3d to generate, orient and register point clouds derived from models for <a href="https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13689">ALPACA</a>. There are certain issues using open3d within Slicer (mostly very quickly changing API, lack of stability of code base) and would like to see similar methods implemented in VTK. As <a class="mention" href="/u/lassoan">@lassoan</a> pointed out, the proposal and discussion in summarized <a href="https://discourse.vtk.org/t/vtk-point-cloud-and-mesh-filters-for-downsampling-registration-icp-transform/6974">here</a>.</p>
<p>If possible, it will be great to join forces, as this will require some funding and development effort.</p>

---

## Post #6 by @mau_igna_06 (2021-10-28 20:04 UTC)

<p>It is interesting to work with transforms. Please let me know if there is any work proposal.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a>: did some of you tested the script? It would be great if you could give feedback.</p>

---

## Post #7 by @muratmaga (2021-10-28 20:33 UTC)

<p>Is this meant to be run on preview version, as I am getting bunch of errors in stable?</p>

---

## Post #8 by @mau_igna_06 (2021-10-28 20:45 UTC)

<p>It works in both the stable and the preview versions (2021-10-12)</p>
<p>You just need to define the 2 boneModels with getNode</p>
<p>You may need to decrease the numberOfSampledPoints if your data has very few points</p>
<p>You should replace all the code above this line:</p>
<pre><code class="lang-auto">boneModel1.SetAndObservePolyData(transformer.GetOutput())
</code></pre>
<p>That line should also be deleted and replaced with:</p>
<pre><code class="lang-auto">boneModel0 = getNode('movingBone')
boneModel1 = getNode('fixedBone)
</code></pre>
<p>And it should work well</p>

---

## Post #9 by @mau_igna_06 (2021-10-29 12:54 UTC)

<p><code>UNIFORM_SPATIAL_SURFACE</code> option of the maskPoints filter may make the registration algorithm work a little bit better. Although I cannot test that because it is only available in VTK 9. So that will have to wait.</p>

---

## Post #10 by @muratmaga (2021-10-29 15:53 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="8" data-topic="20388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>And it should work well</p>
</blockquote>
</aside>
<p>I have a scene that looks like this, this is where it starts to fail:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; def getAxes1ToWorldChangeOfFrameMatrix(axis1X,axis1Y,axis1Z,axisOrigin):
...   axes1ToWorldChangeOfFrameMatrix = vtk.vtkMatrix4x4()
... axes1ToWorldChangeOfFrameMatrix.DeepCopy((1, 0, 0, 0,
  File "&lt;console&gt;", line 3
    axes1ToWorldChangeOfFrameMatrix.DeepCopy((1, 0, 0, 0,
                                  ^
SyntaxError: invalid syntax
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a373c46bdc5e601a999d9167d1c057f700a0a1b.png" alt="image" data-base62-sha1="8j029oj5Ilr1cv5N42mcbJLmCWn" width="605" height="352"></p>

---

## Post #11 by @mau_igna_06 (2021-10-29 17:28 UTC)

<pre><code class="lang-auto">&gt;&gt;&gt; def getAxes1ToWorldChangeOfFrameMatrix(axis1X,axis1Y,axis1Z,axisOrigin):
...   axes1ToWorldChangeOfFrameMatrix = vtk.vtkMatrix4x4()
... axes1ToWorldChangeOfFrameMatrix.DeepCopy((1, 0, 0, 0,
  File "&lt;console&gt;", line 3
    axes1ToWorldChangeOfFrameMatrix.DeepCopy((1, 0, 0, 0,
</code></pre>
<p>Check if the indentation level is correct. Those lines go inside a function so it should have 2 spaces of indentation. I think your third line doesn’t have the correct indentation. I could replicate your problem by giving the the third line no-indentation.</p>
<p>The code I posted has correct indentation and works well just copy-pasting it to Slicer in my PC. I don’t know why you had this problem.</p>
<p>Let me know if you could get the script to work</p>

---

## Post #12 by @muratmaga (2021-10-29 18:06 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="11" data-topic="20388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The code I posted has correct indentation and works well just copy-pasting it to Slicer in my PC. I don’t know why you had this problem.</p>
</blockquote>
</aside>
<p>I copy/pasted it too… I had this problem before, I think there is some sort of whitespace conversion happening on different platforms.</p>

---

## Post #13 by @mau_igna_06 (2021-10-29 20:44 UTC)

<p>Here is the code. <a href="https://gist.github.com/mauigna06/cb2b81cd0e1945ea2165fb7f0841adf3" class="inline-onebox" rel="noopener nofollow ugc">This an example of registration by SVD decomposition of the data. Useful to register very similar bones · GitHub</a><br>
Let me know if it works for you.</p>

---

## Post #14 by @manjula (2021-10-30 09:04 UTC)

<p>Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>  for sharing the code.  I used a  copy of the same model. this is the results.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3ffc9354a322ad76f657526523c36bac78a4179.jpeg" data-download-href="/uploads/short-url/ufqLrl2r8LpoJV3OZH3czkYXk49.jpeg?dl=1" title="Screenshot_20211030_142121" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3ffc9354a322ad76f657526523c36bac78a4179_2_345x83.jpeg" alt="Screenshot_20211030_142121" data-base62-sha1="ufqLrl2r8LpoJV3OZH3czkYXk49" width="345" height="83" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3ffc9354a322ad76f657526523c36bac78a4179_2_345x83.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3ffc9354a322ad76f657526523c36bac78a4179_2_517x124.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3ffc9354a322ad76f657526523c36bac78a4179_2_690x166.jpeg 2x" data-dominant-color="CAD5D2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20211030_142121</span><span class="informations">1920×465 77.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @mau_igna_06 (2021-10-30 12:44 UTC)

<p>Thanks Manjula for being a tester.</p>
<p>The interesting thing to test next with this registration algorithm is two segmented bones of the same patient obtained by segmentation of two CTs taken on different dates.</p>
<p>I modified the script to also register linear scaling differences of the inputs: <a href="https://gist.github.com/mauigna06/e6a1f177a9f6210809cf1a52079c06d3" class="inline-onebox" rel="noopener nofollow ugc">Register two similar bones that has diffences in position, orientation and size (scaling) · GitHub</a></p>

---

## Post #16 by @lassoan (2021-10-30 13:16 UTC)

<p>This script is useful. It would be great if you could make it available as a module so that users can try it more easily. Maybe you could add it to the Model Registration module in SlicerIGT extension.</p>

---

## Post #17 by @mau_igna_06 (2021-10-30 13:35 UTC)

<p>I could do that although I would prefer someone tests this algorithm with real data first.</p>
<p>Maybe change the title to “New registration method: SVD Registration”</p>

---

## Post #18 by @mau_igna_06 (2021-10-30 20:14 UTC)

<p>I tested with two long bones (fibulas) of different patients. It doesn’t work so well. I only found useful the non-scaling version of the algorithm (because the scaling version makes the transforming mesh worst) and the only utility I found was to make the two bones share an axis (direction of the first eigenvector of bone1) that should be near the anatomical axis direction and make the centroids of the two bones coincide.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47b56847de7d9ab8d0bcb4c7c7c5b91f90de9d74.png" data-download-href="/uploads/short-url/aemyXr8ryLAw7vc04oLU4fnz0VK.png?dl=1" title="boneAxisSharedRegistration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47b56847de7d9ab8d0bcb4c7c7c5b91f90de9d74_2_690x411.png" alt="boneAxisSharedRegistration" data-base62-sha1="aemyXr8ryLAw7vc04oLU4fnz0VK" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47b56847de7d9ab8d0bcb4c7c7c5b91f90de9d74_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47b56847de7d9ab8d0bcb4c7c7c5b91f90de9d74.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47b56847de7d9ab8d0bcb4c7c7c5b91f90de9d74.png 2x" data-dominant-color="989BCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">boneAxisSharedRegistration</span><span class="informations">1025×612 31.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The problem is: the algorithm depends in accuracy of created frames. And the frames creation is done by finding the directions of most variation of the sample of points of the bones and using the centroids as origins. Most bones have one principal axis of variation (or maybe simmetry) that is anatomically stable (repeatable on different animals of the same species). But I don’t think it is usual there are two. So the direction of the second vector of the frame is unstable. And this makes the movedBone and the fixedBone be rotated around the fixedBone 1st eigenvector.</p>
<p>Maybe the rotation problem could be faced iteratively because you know the axis of rotation. I don’t know</p>

---

## Post #19 by @mau_igna_06 (2021-10-31 13:32 UTC)

<p>I think <a href="https://en.m.wikipedia.org/wiki/Canonical_correlation" rel="noopener nofollow ugc">canonical correlation</a> could be used (and may get I little bit better results). I’m not sure if this way would avoid the problems I mentioned in the earlier comment.</p>
<p>Maybe with this <a href="https://scikit-learn.org/stable/modules/cross_decomposition.html#predicting-the-targets-y" rel="noopener nofollow ugc">implementation</a> but I’m not sure how to make that matrix multiplication using <a href="https://vtk.org/doc/nightly/html/classvtkTransformFilter.html" rel="noopener nofollow ugc">the transform filter</a></p>

---

## Post #20 by @mau_igna_06 (2021-11-02 19:21 UTC)

<p>I found and algorithm that defines similarity matrix (rotation, translation and scaling).</p>
<aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/13432805/finding-translation-and-scale-on-two-sets-of-points-to-get-least-square-error-in/25223923#25223923">
  <header class="source">

      <a href="https://stackoverflow.com/questions/13432805/finding-translation-and-scale-on-two-sets-of-points-to-get-least-square-error-in/25223923#25223923" target="_blank" rel="noopener nofollow ugc">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/1229656/bendervader" target="_blank" rel="noopener nofollow ugc">
    <img alt="bendervader" src="https://i.stack.imgur.com/5vclf.jpg?s=256&amp;g=1" class="thumbnail onebox-avatar" width="256" height="256">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/13432805/finding-translation-and-scale-on-two-sets-of-points-to-get-least-square-error-in/25223923#25223923" target="_blank" rel="noopener nofollow ugc">Finding translation and scale on two sets of points to get least square error in their distance?</a>
</h4>

<div class="tags">
  <strong>algorithm, math, point, least-squares</strong>
</div>

<div class="date">
  
  answered by
  <a href="https://stackoverflow.com/users/1229656/bendervader" target="_blank" rel="noopener nofollow ugc">
    bendervader
  </a>
  on <a href="https://stackoverflow.com/questions/13432805/finding-translation-and-scale-on-two-sets-of-points-to-get-least-square-error-in/25223923#25223923" target="_blank" rel="noopener nofollow ugc">11:02PM - 09 Aug 14 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>How do you recommend to try it <a class="mention" href="/u/lassoan">@lassoan</a>?</p>

---

## Post #21 by @lassoan (2021-11-11 06:25 UTC)

<p>This method seems to require corresponding points in the meshes. This is rarely the case in medical image computing. We use this method (the Horn method) for landmark registration - for computeing initial approximate alignment from corresponding manually placed landmarks.</p>
<p>For registering meshes, a very robust method is to register their distance map images. The usual automatic intensity based image registration methods can be used and not just rigid but also warping transforms are supported. This is implemented in the SegmentRegistration extension.</p>

---

## Post #22 by @Prashant_Pandey (2021-11-11 19:10 UTC)

<p>Just came across this interesting thread!</p>
<p>For rigid registration between images, in addition to using distance maps and doing intensity-based registration as <a class="mention" href="/u/lassoan">@lassoan</a> suggested, I’ve found another fast and robust method to be using CPD<br>
(Coherent Point Drift) registration. I wrote a simple Matlab Module recently which can rigidly register two binary volumes together in Slicer. I found it to be quite robust despite bad initialization. Here is a short video demo to show rigid registration between the a pre-op and post-op scan of a patient’s pelvis. The scans were collected a few weeks apart and the the binary volumes are segmented slightly differently (for example there is a bit of the left femur selected in the pre-op pelvis scan not visible in post-op):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="kJzatoNfRc8" data-video-title="CPD (Coherent Point Drift) Rigid Registration in Slicer using Matlab Bridge" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=kJzatoNfRc8" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/kJzatoNfRc8/maxresdefault.jpg" title="CPD (Coherent Point Drift) Rigid Registration in Slicer using Matlab Bridge" width="" height="">
  </a>
</div>

<p>The downside is this particular implementation requires Matlab 2018b or newer, but I believe there is a Python CPD library which could be used to create a native module.</p>
<p>To plug my work a bit more, a while back I compared the performance of distance map rigid image-registration and CPD for CT-US registration of bone surfaces if anyone is curious: <a href="https://link.springer.com/article/10.1007/s11548-018-1788-5" rel="noopener nofollow ugc">https://link.springer.com/article/10.1007/s11548-018-1788-5</a></p>
<p>EDIT: This is the result I get with the SVD script posted by above:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be8d3bf69f875e776f3ed631a94f0c037dd70ba.jpeg" data-download-href="/uploads/short-url/aPwDGEM6RCw8i54WyNRvQYUR0Zs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4be8d3bf69f875e776f3ed631a94f0c037dd70ba_2_690x384.jpeg" alt="image" data-base62-sha1="aPwDGEM6RCw8i54WyNRvQYUR0Zs" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4be8d3bf69f875e776f3ed631a94f0c037dd70ba_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4be8d3bf69f875e776f3ed631a94f0c037dd70ba_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be8d3bf69f875e776f3ed631a94f0c037dd70ba.jpeg 2x" data-dominant-color="9597B5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1221×680 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
