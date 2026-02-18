# Segmentation Node AddSegmentFromClosedSurfaceRepresentation's color only effective on 2d viewer

**Topic ID**: 2435
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/segmentation-node-addsegmentfromclosedsurfacerepresentations-color-only-effective-on-2d-viewer/2435

---

## Post #1 by @Yingli_Lu (2018-03-27 12:30 UTC)

<p>Slicer version:4.8.1<br>
Platform:  Windows 10<br>
Pic: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5491e036ea7c25f96776a2bd0d524962ef1c7506.jpeg" data-download-href="/uploads/short-url/c48DZBEkY3cL76bwcjCzzhREgDA.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5491e036ea7c25f96776a2bd0d524962ef1c7506_2_690x380.jpg" alt="image" data-base62-sha1="c48DZBEkY3cL76bwcjCzzhREgDA" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5491e036ea7c25f96776a2bd0d524962ef1c7506_2_690x380.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5491e036ea7c25f96776a2bd0d524962ef1c7506_2_1035x570.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5491e036ea7c25f96776a2bd0d524962ef1c7506.jpeg 2x" data-dominant-color="656679"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1297×715 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Code:</p>
<blockquote>
<p>import SampleData</p>
<p>sampleDataLogic = SampleData.SampleDataLogic()<br>
masterVolumeNode = sampleDataLogic.downloadCTChest()</p>
<p>segmentationNode = slicer.vtkMRMLSegmentationNode()<br>
slicer.mrmlScene.AddNode(segmentationNode)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)<br>
masterVolumeNode.UpdateDisplayNodeImageData()</p>
<p>marchingCubes = vtk.vtkMarchingCubes()<br>
marchingCubes.SetInputData(masterVolumeNode.GetImageData())<br>
marchingCubes.SetValue(0, 1500)<br>
marchingCubes.Update()</p>
<p>ijk2rasmat = vtk.vtkMatrix4x4()<br>
masterVolumeNode.GetIJKToRASMatrix(ijk2rasmat)</p>
<p>transform = vtk.vtkTransform()<br>
transform.Concatenate(ijk2rasmat)</p>
<p>applyTransform = vtk.vtkTransformPolyDataFilter()<br>
applyTransform.SetTransform(transform)</p>
<p>applyTransform.SetInputData(marchingCubes.GetOutput())<br>
applyTransform.Update()</p>
<p>segmentName=“segment”<br>
segmentationNode.AddSegmentFromClosedSurfaceRepresentation(applyTransform.GetOutput(), segmentName, [0.0,1.0,0.0])</p>
</blockquote>
<p>Any suggestions are greatly appreciated!</p>
<p>YingLi</p>

---

## Post #2 by @lassoan (2018-03-27 14:04 UTC)

<p>Marching cubes created a scalar and set it active, which overwrote the color set by segmentation.</p>
<p>We’ll change the segmentation display in to ignore any scalar values that may be present in the input mesh. For now, you have to remove the scalar values from the mesh if you want to see correct color:</p>
<pre><code>import SampleData
masterVolumeNode = SampleData.SampleDataLogic().downloadCTChest()

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

marchingCubes = vtk.vtkMarchingCubes()
marchingCubes.SetInputData(masterVolumeNode.GetImageData())
marchingCubes.SetValue(0, 1000)
marchingCubes.Update()
ijk2rasmat = vtk.vtkMatrix4x4()
masterVolumeNode.GetIJKToRASMatrix(ijk2rasmat)
transform = vtk.vtkTransform()
transform.SetMatrix(ijk2rasmat)
applyTransform = vtk.vtkTransformPolyDataFilter()
applyTransform.SetTransform(transform)
applyTransform.SetInputData(marchingCubes.GetOutput())
applyTransform.Update()
surface = applyTransform.GetOutput()

# Remove point arrays to make sure they don't affect display color
while surface.GetPointData().GetNumberOfArrays()&gt;0:
  surface.GetPointData().RemoveArray(0)

segmentationNode.AddSegmentFromClosedSurfaceRepresentation(surface, "segment", [0.0,1.0,0.0])</code></pre>

---

## Post #3 by @Yingli_Lu (2018-03-27 14:17 UTC)

<p>Got it. Thanks Andras!</p>

---
