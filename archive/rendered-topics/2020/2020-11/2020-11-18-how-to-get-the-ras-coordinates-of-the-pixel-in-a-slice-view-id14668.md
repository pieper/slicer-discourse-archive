---
topic_id: 14668
title: "How To Get The Ras Coordinates Of The Pixel In A Slice View"
date: 2020-11-18
url: https://discourse.slicer.org/t/14668
---

# How to get the RAS coordinates of the pixel in a slice view by using python code

**Topic ID**: 14668
**Date**: 2020-11-18
**URL**: https://discourse.slicer.org/t/how-to-get-the-ras-coordinates-of-the-pixel-in-a-slice-view-by-using-python-code/14668

---

## Post #1 by @Changing (2020-11-18 01:47 UTC)

<p>Hello,I am using the SlicerHeart module.There is a valve view function there.It can rotate the slice view(‘red’,‘green’,‘yellow’) to any angle.<br>
My goal is as followed:I want to add fiducial in the rotating slice view in a pixel(the position of the pixel will be showed as numpy array) by programming.<br>
My question is as followed:How can I get the RAS coordinates of the pixel in any angle slice view by python code.Or is there other way to achieve my goal.</p>

---

## Post #2 by @lassoan (2020-11-19 03:12 UTC)

<p>What would you like to achieve? Segment annulus curve? Leaflets?</p>

---

## Post #3 by @Changing (2020-11-19 03:29 UTC)

<p>Yes.I want to use deep learning method to identify the mitral annulus point in each slice view.I haven’t finished that.Maybe I think it is possible,although the accuracy is low.The problem is if I know the location of the point in a slice view(the location will be shown as [posx,posy] in the numpy array), how can I get the RAS coordinate of this point to add the fiducial automatically.Thanks for your reply.</p>

---

## Post #4 by @lassoan (2020-11-19 04:04 UTC)

<p>Markup point positions are defined in RAS coordinates, so you are all good. You can get control point positions using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromMarkupsControlPoints">slicer.util.arrayFromMarkupsControlPoints</a> or curve points using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromMarkupsCurvePoints">slicer.util.arrayFromMarkupsCurvePoints</a>.</p>
<p>Note that defining the annulus curve takes about 1-2 minutes with the current module and it takes about 10-20 seconds if you use a more optimized module (we will publicly release such a module soon). Once you have the annulus contour in one frame, you can track it along the cardiac cycle using Sequence Registration. So, annulus contouring and tracking has a quite good solution already with traditional approaches. I would recommend to use deep learning for more challenging problems, such as leaflet segmentation.</p>

---

## Post #5 by @Changing (2020-11-19 07:45 UTC)

<p>May be something wrong.I try explaining as followed:The deep learning method can give the location of the  mitral annulus point in an image.So I want to add fiducial in the corresponding position.My thought is to use the ScriptRepository examples( Get reformatted image from a slice viewer as numpy array ) to get the  slice view as numpy array and use the deep learning result model to identify it.After that, I add fiducial in the location of the corresponding pixel automatically by python.How can I know the RAS coordinate of this pixel.Is it possible?Or there is another way to achieve that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a3fd2d14f591d1e74a8230d8f9903529baa1587.jpeg" data-download-href="/uploads/short-url/aAQ4ACXRAV54S1jaWDt6pkvkIfB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fd2d14f591d1e74a8230d8f9903529baa1587_2_690x450.jpeg" alt="image" data-base62-sha1="aAQ4ACXRAV54S1jaWDt6pkvkIfB" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fd2d14f591d1e74a8230d8f9903529baa1587_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fd2d14f591d1e74a8230d8f9903529baa1587_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3fd2d14f591d1e74a8230d8f9903529baa1587_2_1380x900.jpeg 2x" data-dominant-color="67677E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1409×919 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also,I am trying using deep learning for leaflet segmentation based on 3D slicer.But all things are just in the beginning.So if I have other problems I will post here.</p>
<p>Thanks for your help and this discussion forum.</p>

---

## Post #6 by @Changing (2020-11-19 08:56 UTC)

<p>I have achieve my goal according to the ScriptRepository examples.For example, add the fiducial in the middle position of green slice view code is as followed:</p>
<blockquote>
<p>import numpy as np<br>
sliceNodeID = ‘vtkMRMLSliceNodeGreen’<br>
markupsNode = getNode(‘F’)<br>
<span class="hashtag-raw">#Get</span> image data from slice view<br>
sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)<br>
appLogic = slicer.app.applicationLogic()<br>
sliceLogic = appLogic.GetSliceLogic(sliceNode)<br>
sliceLayerLogic = sliceLogic.GetBackgroundLayer()<br>
reslice = sliceLayerLogic.GetReslice()<br>
reslicedImage = vtk.vtkImageData()<br>
reslicedImage.DeepCopy(reslice.GetOutput())<br>
<span class="hashtag-raw">#Create</span> new volume node using resliced image<br>
volumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”)<br>
volumeNode.SetIJKToRASMatrix(sliceNode.GetXYToRAS())<br>
volumeNode.SetAndObserveImageData(reslicedImage)<br>
volumeNode.CreateDefaultDisplayNodes()<br>
volumeNode.CreateDefaultStorageNode()<br>
<span class="hashtag-raw">#Get</span> voxels as a numpy array<br>
volumeArray = slicer.util.arrayFromVolume(volumeNode)<br>
print(voxels.shape)<br>
<span class="hashtag-raw">#the</span> middle pixel position<br>
point_Ijk = [voxels.shape[1]/2, voxels.shape[2]/2, 0]<br>
<span class="hashtag-raw">#Get</span> physical coordinates from voxel coordinates<br>
volumeIjkToRas = vtk.vtkMatrix4x4()<br>
volumeNode.GetIJKToRASMatrix(volumeIjkToRas)<br>
point_VolumeRas = [0, 0, 0, 1]<br>
volumeIjkToRas.MultiplyPoint(np.append(point_Ijk,1.0), point_VolumeRas)<br>
<span class="hashtag-raw">#If</span> volume node is transformed, apply that transform to get volume’s RAS coordinates<br>
transformVolumeRasToRas = vtk.vtkGeneralTransform()<br>
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(volumeNode.GetParentTransformNode(), None, transformVolumeRasToRas)<br>
point_Ras = transformVolumeRasToRas.TransformPoint(point_VolumeRas[0:3])<br>
<span class="hashtag-raw">#Add</span> a markup at the computed position and print its coordinates<br>
markupsNode.AddFiducial(point_Ras[0], point_Ras[1], point_Ras[2], “test”)<br>
print(point_Ras)</p>
</blockquote>

---
