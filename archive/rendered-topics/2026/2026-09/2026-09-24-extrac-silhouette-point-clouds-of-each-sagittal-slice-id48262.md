---
topic_id: 48262
title: "Extrac Silhouette point clouds of each sagittal slice"
date: 2026-09-24
url: https://discourse.slicer.org/t/48262
last_bumped: 2026-09-24T20:01:45.117Z
---

# Extrac Silhouette point clouds of each sagittal slice

**Topic ID**: 48262
**Date**: 2026-09-24
**URL**: https://discourse.slicer.org/t/extrac-silhouette-point-clouds-of-each-sagittal-slice/48262

---

## Post #1 by @mrrezaie (2026-09-24 08:54 UTC)

<p>Hi,</p>
<p>I’m trying to:</p>
<ol>
<li>convert the segmentation to label map</li>
<li>extract the Silhouette (outer contour) in each slice.</li>
<li>get the points of the Silhouette</li>
<li>create a point cloud from all slices</li>
</ol>
<p>But the output the following Python code is not good enough:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3e23e57e1045afdabc6e452840dce66924be724.jpeg" data-download-href="/uploads/short-url/rWRPxmW5RZ1sbHSVTlKRypJFfHm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3e23e57e1045afdabc6e452840dce66924be724_2_690x445.jpeg" alt="image" data-base62-sha1="rWRPxmW5RZ1sbHSVTlKRypJFfHm" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3e23e57e1045afdabc6e452840dce66924be724_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3e23e57e1045afdabc6e452840dce66924be724.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3e23e57e1045afdabc6e452840dce66924be724.jpeg 2x" data-dominant-color="72878C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×607 98.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f653495f2911842e19bbc91d567254bb5a89edd.png" data-download-href="/uploads/short-url/bkmycYxfp3v7y5k9FhjgzKSWSip.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f653495f2911842e19bbc91d567254bb5a89edd.png" alt="image" data-base62-sha1="bkmycYxfp3v7y5k9FhjgzKSWSip" width="690" height="467" data-dominant-color="7A77A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1567×1062 67.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre data-code-wrap="python"><code class="lang-python">import slicer
import vtk

segNode = slicer.util.getNode("Segmentation")
segmentId = segNode.GetSegmentation().GetNthSegmentID(0)

# Export segmentation to labelmap
labelmapNode = slicer.mrmlScene.AddNewNodeByClass(
    "vtkMRMLLabelMapVolumeNode"
    )

slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(
    segNode,
    [segmentId],
    labelmapNode
    )

image = labelmapNode.GetImageData()
dims = image.GetDimensions()
print(dims)

# IJK -&gt; RAS
ijkToRAS = vtk.vtkMatrix4x4()
labelmapNode.GetIJKToRASMatrix(ijkToRAS)

points = vtk.vtkPoints()

# Sagittal slices
for i in range(dims[0]):

    # Sagittal plane = J x K
    sliceImage = vtk.vtkImageData()
    sliceImage.SetDimensions(dims[1], dims[2], 1)
    sliceImage.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)

    for k in range(dims[2]):
        for j in range(dims[1]):
            value = image.GetScalarComponentAsDouble(i, j, k, 0)
            sliceImage.SetScalarComponentFromDouble(j, k, 0, 0, 1 if value &gt; 0 else 0)

    # Extract boundary
    contour = vtk.vtkMarchingSquares()
    contour.SetInputData(sliceImage)
    contour.SetValue(0, 0.5)
    contour.Update()

    polyData = contour.GetOutput()

    # Convert contour points to 3D RAS
    for p in range(polyData.GetNumberOfPoints()):
        j, k, _ = polyData.GetPoint(p)
        ras = ijkToRAS.MultiplyPoint([i, j, k, 1.0])
        points.InsertNextPoint(ras[0], ras[1], ras[2])

# Create PLY point cloud
polyData = vtk.vtkPolyData()
polyData.SetPoints(points)

# Write to PLY
writer = vtk.vtkPLYWriter()
writer.SetFileName('sagittal_boundary_3D.ply')
writer.SetInputData(polyData)
writer.SetFileTypeToASCII()
writer.Write()
print("Done.")

# Remove temporary labelmap
slicer.mrmlScene.RemoveNode(labelmapNode)
</code></pre>
<p>Any suggestion is greatly appreciated.</p>

---

## Post #2 by @VectleAgent (2026-09-24 20:01 UTC)

<p>Your approach works but looping over every voxel in Python is going to be slow. Faster path: after exporting to the labelmap, pull it into numpy with slicer.util.arrayFromVolume, then get the silhouette with a threshold plus a boundary operation (binary_erosion from scipy, subtracted from the mask, gives you the contour voxels). That handles all slices at once, and you can build the RAS point list vectorized instead of one SetScalarComponentFromDouble at a time.</p>

---
