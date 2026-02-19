---
topic_id: 37548
title: "Extracting Point Clouds"
date: 2024-07-24
url: https://discourse.slicer.org/t/37548
---

# Extracting Point Clouds

**Topic ID**: 37548
**Date**: 2024-07-24
**URL**: https://discourse.slicer.org/t/extracting-point-clouds/37548

---

## Post #1 by @Jessica_de_Kort (2024-07-24 20:01 UTC)

<p>Hello, I have a custom-made module that creates catheters inside of patients from passing through a 3D U-Net to produce a point cloud. The point cloud passes through curve fitting to produce the final predictions. I want to take a look at the point cloud immediately after the U-Net, before the curve fitting. Does anyone have any suggestions?</p>
<p>I have tried this snippet of code:</p>
<p>segmentationNode=getNode(‘Segmentation’)<br>
segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)<br>
segmentPolyData=segmentationNode.GetClosedSurfaceInternalRepresentation(segmentId)<br>
import vtk.util.numpy_support<br>
pointData = segmentPolyData.GetPoints().GetData()<br>
pointCoordinates = vtk.util.numpy_support.vtk_to_numpy(pointData)</p>
<p>The problem with this code is that it only gives a point cloud for the final catheter after the curve fitting. I want it to include the points that were excluded.</p>

---

## Post #2 by @JASON (2024-07-24 21:41 UTC)

<p><a class="mention" href="/u/jessica_de_kort">@Jessica_de_Kort</a> I’m not 100% sure this will work, but you may try turning off smoothing and recreating the ClosedSurface Representation before getting the points</p>
<pre><code class="lang-auto">segNode.GetSegmentation().SetConversionParameter('Smoothing factor',str(0))
segNode.RemoveClosedSurfaceRepresentation()
segNode.CreateClosedSurfaceRepresentation()
</code></pre>

---

## Post #3 by @Jessica_de_Kort (2024-07-25 19:08 UTC)

<p>I do not have segmentation nodes before I run the module which is where I run into my issue with that snippet of code. I keep running into this error:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘segmentationNode’ is not defined</p>
<p>Any suggestions?</p>

---

## Post #4 by @JASON (2024-07-25 19:20 UTC)

<p>Your code assumes there’s a segmentation node in the scene named ‘<strong>Segmentation</strong>’, so it will fail if it doesn’t find a node with this name.</p>
<p>Try this, but replace the first line with the name of the node in your scene.</p>
<pre><code class="lang-auto">segmentationName = 'Your Segmentation Name'

segmentationNode=getNode(segmentationName)
segmentationNode.GetSegmentation().SetConversionParameter('Smoothing factor',str(0))
segmentationNode.RemoveClosedSurfaceRepresentation()
segmentationNode.CreateClosedSurfaceRepresentation()
segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)
segmentPolyData=segmentationNode.GetClosedSurfaceInternalRepresentation(segmentId)
import vtk.util.numpy_support
pointData = segmentPolyData.GetPoints().GetData()
pointCoordinates = vtk.util.numpy_support.vtk_to_numpy(pointData)
</code></pre>

---

## Post #5 by @Jessica_de_Kort (2024-07-29 16:43 UTC)

<p>Thank you for your suggestion. I want to get the point clouds before any segmentations have been made which it does not look like that code does. From my understanding, not all of the points in the cloud are present once the predicted catheter has been made. Lines of best fit are made to represent the catheters and the rest are disregarded. I am still unsure on how to view all of the points that have been disregarded.</p>

---

## Post #6 by @mikebind (2024-07-29 18:05 UTC)

<p>I think we’d need to know a little more about the software pipeline your data is passing through to be able to help.  What format is the point cloud data in before it is suppled to whatever smoothing routine you apply?  If it is vtkPolyData, you can probably do the equivalent of the last few lines of the above code, just starting from the vtkPolyData rather than from a segmentation.  If it is in some other format, then what you need to do depends on what format it is in.</p>

---

## Post #7 by @Jessica_de_Kort (2024-07-29 18:27 UTC)

<p>It looks like they are vtkMRMLScalarVolumeNode.</p>

---

## Post #8 by @mikebind (2024-07-29 19:00 UTC)

<p>vtkMRMLScalarVolumeNode is the format used in Slicer for holding image volume data (i.e. voxels). This might be something like a binary mask holding thresholded classified results from the UNet, or it might be a range of values representing probabilities or likelihoods which are to be turned into classifications by thresholding later.  Either way, Slicer is an excellent tool for inspecting image volumes to try to understand what it is you are looking at. If you just modify the code you are using to be interrupted before the smoothing step, you will likely find the image you want to inspect already in the Slicer scene. If you don’t you can add it to the scene in your code using <code>slicer.mrmlScene.AddNode(yourNodeHere)</code></p>

---
