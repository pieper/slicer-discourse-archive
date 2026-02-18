# Can't visualize volume created with `vtkProbeFilter`

**Topic ID**: 20532
**Date**: 2021-11-08
**URL**: https://discourse.slicer.org/t/cant-visualize-volume-created-with-vtkprobefilter/20532

---

## Post #1 by @keri (2021-11-08 15:16 UTC)

<p>Hi,</p>
<p>Can’t understand why I cannot visualize volume node created with <code>vtkProbeFilter</code>.<br>
Here is the example where I create two image data with intersecting areas and different spacings. The second volume I calculate based on probe filter:</p>
<pre><code class="lang-python"># Create parameters for two volume nodes
nodeName1 = "volume1"
image1Size = [10, 10, 10]
image1Origin = [0.0, 0.0, 0.0]
image1Spacing = [1.0, 1.0, 1.0]

nodeName2 = "volume2"
image2Size = [100, 100, 100]
image2Origin = [5.0, 5.0, 5.0]
image2Spacing = [0.1, 0.1, 0.1]

# Prepare scalars for the first node
scalars = vtk.vtkDoubleArray()
scalars.SetName("my_scalars")

for i in range(0, image1Size[0]*image1Size[1]*image1Size[2]):
    v = scalars.InsertNextValue(i)

# Create two image volumes
imageData1 = vtk.vtkImageData()
imageData1.SetDimensions(image1Size)
imageData1.SetOrigin(image1Origin)
imageData1.SetSpacing(image1Spacing)
imageData1.GetPointData().SetScalars(scalars)

imageData2 = vtk.vtkImageData()
imageData2.SetDimensions(image2Size)
imageData2.SetOrigin(image2Origin)
imageData2.SetSpacing(image2Spacing)

# Create probe filter to interpolate `imageData1` on `imageData2`
interpolator = vtk.vtkProbeFilter()
interpolator.SetSourceData(imageData1)
interpolator.SetInputData(imageData2)
interpolator.Update()

# Create volume nodes
volumeNode1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName1)
volumeNode1.SetOrigin(image1Origin)
volumeNode1.SetSpacing(image1Spacing)
volumeNode1.SetAndObserveImageData(imageData1)
volumeNode1.CreateDefaultDisplayNodes()
volumeNode1.CreateDefaultStorageNode()

volumeNode2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName2)
volumeNode2.SetOrigin(image2Origin)
volumeNode2.SetSpacing(image2Spacing)
volumeNode2.SetAndObserveImageData(interpolator.GetImageDataOutput()) # output from probe filter
volumeNode2.CreateDefaultDisplayNodes()
volumeNode2.CreateDefaultStorageNode()
</code></pre>
<p>If I try to visualize the second node then I get empty window while I can see that scalar range varies from 0 to 999 in volume module.<br>
There is no such problem when visualizing the first node</p>

---

## Post #2 by @keri (2021-11-09 00:56 UTC)

<p>It seems that Slicer don’t like when I set spacings and origing directly to <code>vtkImageData</code>. And even if I set these parameters to both <code>vtkImageData</code> and to <code>vtkMRMLScalarVolumeNode</code> then I also encounter strange behaviour. To solve my issue I needed to create new <code>vtkImageData imageData3</code> and set only dimensions and scalars from interpolator. Then add this imageData3 to the volume node and set origin and spacing.</p>
<p>But if I also set origin and spacing directly to <code>imageData3</code> then Slicer behaves incorrectly.</p>
<p>For example this code is incorrect:</p>
<pre><code class="lang-python">nodeName = "MyNewVolume"
imageSize = [10, 10, 10]
imageOrigin = [5.0, 5.0, 5.0]
imageSpacing = [1.0, 1.0, 1.0] # `X` spacing is negative

scalars = vtk.vtkDoubleArray()
scalars.SetName("my_scalars")

for i in range(0, imageSize[0]*imageSize[1]*imageSize[2]):
    v = scalars.InsertNextValue(i)

# Create an image volume
imageData = vtk.vtkImageData()

##################################################
# remove these two lines and Slicer will work better
##################################################
imageData.SetOrigin(imageOrigin)	
imageData.SetSpacing(imageSpacing)

imageData.SetDimensions(imageSize)
imageData.GetPointData().SetScalars(scalars)
# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()
</code></pre>
<p>But if I remove two marked lines then everything will be fine.</p>
<p>May I get some information why this happens to better understand Slicer</p>

---

## Post #3 by @mikebind (2021-11-09 01:21 UTC)

<p>I believe Slicer only respects origin and spacing data as specified on the MRML volume node, not in the vtkImageData.  I don’t know why this is, and it does seem counterintuitive (I expect especially if you are very familiar with VTK!), but try leaving the vtkImageData with only default origin and spacing and specify those parameters through the MRML volume node instead.  Slicer should then respond the way you expect.</p>

---

## Post #4 by @keri (2021-11-09 01:36 UTC)

<p>Good to know, thank you!</p>

---

## Post #5 by @lassoan (2021-11-09 03:20 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="20532">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I believe Slicer only respects origin and spacing data as specified on the MRML volume node, not in the vtkImageData. I don’t know why this is, and it does seem counterintuitive</p>
</blockquote>
</aside>
<p>Until about a year ago, vtkImageData could not store axis directions. Therefore, the origin and spacing values stored in the vtkImageData object was useless for medical image computing, where images often have arbitrary axis directions. Therefore we have been storing the IJK to world mapping outside vtkImageData - in the MRML volume node.</p>
<p>Now vtkImageData can store axis directions, but before we can transition to use it, we need to make sure that the most important VTK filters work correctly with non-trivial axis directions. This will probably take about a half year or a year.</p>

---
