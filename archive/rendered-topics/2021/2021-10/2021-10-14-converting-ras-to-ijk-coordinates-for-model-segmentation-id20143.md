# Converting ras to ijk coordinates for model, segmentation

**Topic ID**: 20143
**Date**: 2021-10-14
**URL**: https://discourse.slicer.org/t/converting-ras-to-ijk-coordinates-for-model-segmentation/20143

---

## Post #1 by @Karthik (2021-10-14 04:13 UTC)

<p>Operating system: Ubuntu 20.04<br>
Slicer version: 4.11.20210226</p>
<p>I understand how to convert ras to ijk coordinates using <strong>volumeNode.GetRASToIJKMatrix(mat)</strong>.<br>
However, I am placing fiducials on a surface (i use model, segmentation but not volume). I don’t have an input volume to apply volumeNode. How do I then convert the RAS coordinates obtained from fiducial points to ijk coordinates?<br>
I want to obtain IJK coordinates as I need them for vmtk.</p>

---

## Post #2 by @lassoan (2021-10-14 05:19 UTC)

<p>IJK coordinates are voxel indices. If you don’t have a volume, only models then there are no voxels, and there are no IJK coordinates.</p>
<p>A segmentation can store various representations. If it contains labelmap representation then you can retrieve its geometry using this code snippet:</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
commonGeometryString = segmentationNode.GetSegmentation().DetermineCommonLabelmapGeometry(slicer.vtkSegmentation.EXTENT_UNION_OF_SEGMENTS, None)
commonGeometryImage = slicer.vtkOrientedImageData()
slicer.vtkSegmentationConverter.DeserializeImageGeometry(commonGeometryString, commonGeometryImage, False) 
ijkToRas = vtk.vtkMatrix4x4()
commonGeometryImage.GetImageToWorldMatrix(ijkToRas)
print(ijkToRas)
</code></pre>
<p>This is so complex because it the geometry of the internal binary labelmap representations of a segmentation is an internal implementation details that generally you should generally not rely on. For example, if you import a model and “Crop to reference image geometry” representation conversion option is disabled then internal labelmap’s geometry may change.</p>
<p>Instead, if you want to manipulate labelmap representation in segments, it is simpler and more clear if you export the internal labelmap representation of segments to labelmap volume node(s).</p>

---
