---
topic_id: 34337
title: "Can I Change The Color Of Only Certain Parts Of The Mesh"
date: 2024-02-15
url: https://discourse.slicer.org/t/34337
---

# Can I change the color of only certain parts of the mesh?

**Topic ID**: 34337
**Date**: 2024-02-15
**URL**: https://discourse.slicer.org/t/can-i-change-the-color-of-only-certain-parts-of-the-mesh/34337

---

## Post #1 by @dsa934 (2024-02-15 00:49 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.4</p>
<p>hi slicer users,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e643d7cafd234f8c3af3bf197be4ffc27629e32b.png" data-download-href="/uploads/short-url/wR1aBsfF6PTOcbsfxRAhXEeojqP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e643d7cafd234f8c3af3bf197be4ffc27629e32b.png" alt="image" data-base62-sha1="wR1aBsfF6PTOcbsfxRAhXEeojqP" width="568" height="500" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">636×559 5.18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it possible in slicer to select a specific area on the mesh (e.g. by dragging the mouse) and change the color of only that area?</p>
<p>If it is possible, what should I refer to?</p>

---

## Post #2 by @RafaelPalomar (2024-02-15 13:59 UTC)

<p>Hello <a class="mention" href="/u/dsa934">@dsa934</a>. One option is to associate scalar values to the vertices and enable coloring  based on the scalar value. The following is a simple python script that exemplifies how to do that:</p>
<pre data-code-wrap="python"><code class="lang-python">import vtk
from slicer import mrmlScene
import slicer

# Create a sphere
sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0.0, 0.0, 0.0)
sphereSource.SetRadius(50.0)
sphereSource.SetPhiResolution(30)
sphereSource.SetThetaResolution(30)
sphereSource.Update()

# Create a model node
modelNode = slicer.vtkMRMLModelNode()
modelNode.SetScene(mrmlScene)
modelNode.SetName("Sphere")
modelNode.SetAndObserveMesh(sphereSource.GetOutput())

# Create a display node
displayNode = slicer.vtkMRMLModelDisplayNode()
mrmlScene.AddNode(displayNode)
modelNode.SetAndObserveDisplayNodeID(displayNode.GetID())
displayNode.SetActiveScalarName("Colors")
displayNode.SetAndObserveColorNodeID("vtkMRMLColorTableNodeRainbow")
displayNode.SetScalarVisibility(True)

# Assign scalar values to represent colors
mesh = modelNode.GetMesh()
scalars = vtk.vtkFloatArray()
scalars.SetName("Colors")
for i in range(mesh.GetNumberOfPoints()):
    scalars.InsertNextValue(i / mesh.GetNumberOfPoints())
mesh.GetPointData().SetScalars(scalars)

# Add the model node to the scene
mrmlScene.AddNode(modelNode)
</code></pre>
<p>This is the result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40848bcd10a385409c1ac3f729ce458b66e9a2b2.jpeg" data-download-href="/uploads/short-url/9cKxhvHCGRSPSh729grmEcDfErg.jpeg?dl=1" title="Screenshot from 2024-02-15 14-55-58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40848bcd10a385409c1ac3f729ce458b66e9a2b2_2_690x376.jpeg" alt="Screenshot from 2024-02-15 14-55-58" data-base62-sha1="9cKxhvHCGRSPSh729grmEcDfErg" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40848bcd10a385409c1ac3f729ce458b66e9a2b2_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40848bcd10a385409c1ac3f729ce458b66e9a2b2_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40848bcd10a385409c1ac3f729ce458b66e9a2b2_2_1380x752.jpeg 2x" data-dominant-color="95A8C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-02-15 14-55-58</span><span class="informations">1920×1048 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note how in the left panel the scalar visibility is turned on, the array that should be used as scalar is selected (<code>Colors</code>), as well as the color table.</p>

---

## Post #3 by @cpinter (2024-02-15 14:20 UTC)

<p>I made a module in the past for a very specific case where the main function was this. It never worked 100% reliably but it was possible to use for my purpose.</p>
<pre><code class="lang-auto">def paintModelWithSegment(classScalar, parameterNode, currentSegmentID):
  modelNode = slicer.util.getNode('Model')
  if not modelNode:
    return
  segmentationNode = slicer.util.getNode('Segmentation')
  if not segmentationNode:
    return

  # Get segment bounds
  currentSegment = segmentationNode.GetSegmentation().GetSegment(currentSegmentID)
  bounds = np.zeros(6)
  currentSegment.GetBounds(bounds)

  # Go through each point in model
  pointIDsInSegment = []
  pointClassArray = modelNode.GetPolyData().GetPointData().GetArray('ArrayName')
  sliceViewLabel = "Red"  # any slice view where segmentation node is visible works
  sliceViewWidget = slicer.app.layoutManager().sliceWidget(sliceViewLabel)
  segmentationsDisplayableManager = sliceViewWidget.sliceView().displayableManagerByClassName("vtkMRMLSegmentationsDisplayableManager2D")
  points = modelNode.GetPolyData().GetPoints()
  for pointIdx in range(modelNode.GetPolyData().GetNumberOfPoints()):
    pointRas = points.GetPoint(pointIdx)
    if pointRas[0] &lt; bounds[0] or pointRas[0] &gt; bounds[1] or pointRas[1] &lt; bounds[2] or pointRas[1] &gt; bounds[3] or pointRas[2] &lt; bounds[4] or pointRas[2] &gt; bounds[5]:
      continue  # Point outside simple bounds, skip

    # Get segment IDs at vertex position
    segmentIDsAtPoint = vtk.vtkStringArray()
    segmentationsDisplayableManager.GetVisibleSegmentsForPosition(pointRas, segmentationNode.GetDisplayNode(), segmentIDsAtPoint)
    for idIndex in range(segmentIDsAtPoint.GetNumberOfValues()):
      if segmentIDsAtPoint.GetValue(idIndex) == currentSegmentID and int(pointClassArray.GetValue(pointIdx)) != classScalar:
        pointIDsInSegment.append(pointIdx)

  if not pointIDsInSegment:
    logging.error(f'Failed to paint. Bounds: {bounds}')  #TODO: Remove if works fully reliably

  # Include selected vertices in painted class
  for pointIdx in pointIDsInSegment:
    pointClassArray.SetValue(pointIdx, classScalar)
  pointClassArray.Modified()
</code></pre>
<p>It uses a segment painted in Segment Editor to set scalars to the vertices of the model that are contained in the segment. I connected it to <code>slicer.vtkSegmentation.RepresentationModified</code> so that it automatically paints after painting.</p>

---

## Post #4 by @dsa934 (2024-02-15 22:40 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> <a class="mention" href="/u/cpinter">@cpinter</a><br>
Fantastic!<br>
I will proceed by referring to your code.</p>

---
