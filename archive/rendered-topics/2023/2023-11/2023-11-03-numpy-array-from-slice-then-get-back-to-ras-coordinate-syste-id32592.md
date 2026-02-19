---
topic_id: 32592
title: "Numpy Array From Slice Then Get Back To Ras Coordinate Syste"
date: 2023-11-03
url: https://discourse.slicer.org/t/32592
---

# Numpy array from slice, then get back to RAS coordinate system

**Topic ID**: 32592
**Date**: 2023-11-03
**URL**: https://discourse.slicer.org/t/numpy-array-from-slice-then-get-back-to-ras-coordinate-system/32592

---

## Post #1 by @David_Roberto_Brenes (2023-11-03 23:34 UTC)

<p>Hello,</p>
<p>Similar to this post <a href="https://discourse.slicer.org/t/how-to-get-the-ras-coordinates-of-the-pixel-in-a-slice-view-by-using-python-code/14668">(link)</a> I am trying to:</p>
<ol>
<li>Visualize in the view node a slice that is perpendicular to a curve defined by two control points</li>
<li>Generate a numpy array from slice (similar to the straighten volume example script)</li>
<li>Process the numpy array to identify a single pixel coordinate (ijk) of interest</li>
<li>Plot the ijk coordinate of the point of interest, in this case the middle of the array, on 3D slicer as marker (as in the post above). This new marker should align with the original marked used to get the slice.</li>
</ol>
<p>However, my calculated coordinates are off center (see attached image). The point with the label “MarkupsCurve” is a manually placed center point used to get the slice and the point without a label is the point placed by the python script.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1db953e9f79e636d3b19407cc5c2b5c51d351f14.jpeg" data-download-href="/uploads/short-url/4eWUouYZ6cTMlK1DIsLIgrmoTsM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1db953e9f79e636d3b19407cc5c2b5c51d351f14_2_690x380.jpeg" alt="image" data-base62-sha1="4eWUouYZ6cTMlK1DIsLIgrmoTsM" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1db953e9f79e636d3b19407cc5c2b5c51d351f14_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1db953e9f79e636d3b19407cc5c2b5c51d351f14_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1db953e9f79e636d3b19407cc5c2b5c51d351f14_2_1380x760.jpeg 2x" data-dominant-color="9394A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1059 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">point_list = list(np.arange(numberOfPoints))
for pointIndex in point_list:
    print(pointIndex)
    curvePointToWorldMatrix = vtk.vtkMatrix4x4()
    curveNode.GetCurvePointToWorldTransformAtPointIndex(pointIndex, curvePointToWorldMatrix)
    curvePointToWorldTransform.SetMatrix(curvePointToWorldMatrix)
    sliceToWorldTransform.Update()
    sliceNode.GetSliceToRAS().DeepCopy(sliceToWorldTransform.GetMatrix())
    sliceNode.UpdateMatrices()
    slicer.app.processEvents()

    
    slicer.util.setSliceViewerLayers(background = volume)
    slicer.app.processEvents()
    slicer.util.forceRenderAllViews()
    # Get RAW slice and add it to the straightened volume
    tempSlice_RAW = vtk.vtkImageData()
    tempSlice_RAW.DeepCopy(reslice.GetOutput())
    append_RAW.AddInputData(tempSlice_RAW)
    
#     Get slice as volume to output into numpy array for processing by external network
    volumeNodeResliced_RAW.SetIJKToRASMatrix(sliceNode.GetXYToRAS())
    volumeNodeResliced_RAW.SetAndObserveImageData(tempSlice_RAW)
    volumeNodeResliced_RAW.CreateDefaultDisplayNodes()
    volumeNodeResliced_RAW.CreateDefaultStorageNode()
    voxels_RAW = slicer.util.arrayFromVolume(volumeNodeResliced_RAW)
    slices_RAW.append(voxels_RAW)
    
    # find RAS of middle pixel position in array - dummy example 
    print(voxels_RAW.shape)
    point_ijk = [voxels_RAW.shape[1]/2, voxels_RAW.shape[2]/2, 0]
    print(point_ijk)
    #Get physical coordinates from voxel coordinates
    volumeIjkToRas = vtk.vtkMatrix4x4()
    volumeNodeResliced_RAW.GetIJKToRASMatrix(volumeIjkToRas)
    point_VolumeRas = [0, 0, 0, 1]
    volumeIjkToRas.MultiplyPoint(np.append(point_ijk,1.0), point_VolumeRas)
    #If volume node is transformed, apply that transform to get volume’s RAS coordinates
    transformVolumeRasToRas = vtk.vtkGeneralTransform()
    slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(volumeNodeResliced_MASK.GetParentTransformNode(), None, transformVolumeRasToRas)
    print(point_VolumeRas)
    point_Ras = transformVolumeRasToRas.TransformPoint(point_VolumeRas[0:3])
    print(point_Ras)
    curveNode.AddControlPoint(vtk.vtkVector3d(point_Ras))
    break
</code></pre>

---

## Post #2 by @lassoan (2023-11-03 23:46 UTC)

<p>I would recommend to use the Curved Planar Reformat module to get the slices of the curve (or straight line). You can then process each slice of the straightened volume, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-markup-control-point-ras-coordinates-from-volume-voxel-coordinates">get the physical (RAS) coordinates from voxel (IJK) coordinates</a>, add the markup point using the RAS coordinates in each slice. You can apply the inverse of the straightening transform to move the points to the original image’s space.</p>

---
