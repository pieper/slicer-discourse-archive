# How can I convert vtk.vtkImageData() to an OpenCv Image?

**Topic ID**: 13120
**Date**: 2020-08-21
**URL**: https://discourse.slicer.org/t/how-can-i-convert-vtk-vtkimagedata-to-an-opencv-image/13120

---

## Post #1 by @apparrilla (2020-08-21 17:52 UTC)

<p>I want to work arround with images from slices but I have problems converting them to a cv2 format.<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-08-21 18:00 UTC)

<p>Would you like to extract 2D slices from a volume?</p>

---

## Post #3 by @apparrilla (2020-08-21 18:18 UTC)

<p>I have extracted 2D slice with a peace of code from script repository but I can’t convert them to a openCV Mat to play with it.</p>

---

## Post #4 by @lassoan (2020-08-21 18:37 UTC)

<p>If you are working in Python then the easiest is to get the image as a numpy array and pass that array to OpenCV.</p>

---

## Post #5 by @apparrilla (2020-08-21 22:16 UTC)

<p>I´ve converted 40 index Red slice to numpy array with:</p>
<pre><code>sliceNodeID = 'vtkMRMLSliceNodeRed'
# Get image data from slice view
sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)
appLogic = slicer.app.applicationLogic()
sliceLogic = appLogic.GetSliceLogic(sliceNode)
sliceLayerLogic = sliceLogic.GetBackgroundLayer()
reslice = sliceLayerLogic.GetReslice()
reslicedImage = vtk.vtkImageData()
reslicedImage.DeepCopy(reslice.GetOutput())

# Create new volume node using resliced image
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
volumeNode.SetIJKToRASMatrix(sliceNode.GetXYToRAS())
volumeNode.SetAndObserveImageData(reslicedImage)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()

# Get voxels as a numpy array
voxels = slicer.util.arrayFromVolume(volumeNode)

sliceIndex = 40
slice = voxels[sliceIndex:,:]
</code></pre>
<p>but I don´t know how to convert slice in a openCv Mat.</p>

---

## Post #6 by @lassoan (2020-08-21 22:44 UTC)

<p>I don’t use OpenCV in Python, but it should be a trivial operation to convert numpy array to OpenCV image. Do a web search for <code>numpy array to opencv image</code> - the solution should be among the first few hits.</p>

---
