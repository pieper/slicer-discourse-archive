---
topic_id: 39608
title: "Best Way To Create Same Domain Size For Segmentation Masks A"
date: 2024-10-09
url: https://discourse.slicer.org/t/39608
---

# Best way to create same domain size for segmentation masks and 3D .nrrd files?

**Topic ID**: 39608
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/best-way-to-create-same-domain-size-for-segmentation-masks-and-3d-nrrd-files/39608

---

## Post #1 by @Yue-Hin_Loke1 (2024-10-09 12:10 UTC)

<p>Hi all,</p>
<p>I have a series of 3D .nrrd files of MRI images and corresponding segmentation masks that I created from slicer that I am hoping to train for autosegmentation.</p>
<p>I am trying to prepare the data by make them share the same coordinates/domain size, but I’m struggling due to if there are more than differences RAS (for 3D .nrrd files) vs. LPS coordinates (for the segmentation masks), even when I get the metadata for both. Any advice on the best way of approaching this issue? Thanks!</p>
<pre data-code-wrap="python"><code class="lang-python">import SimpleITK as sitk
import numpy as np

# Load MRI and label images
volume_image = sitk.ReadImage('Pros Normal 002.nrrd')
label_image = sitk.ReadImage('Pros Normal 002.seg.nrrd')

# Convert images to arrays for processing
volume_array = sitk.GetArrayFromImage(volume_image)
label_array = sitk.GetArrayFromImage(label_image)

# Get metadata from label image
label_shape = label_array.shape
label_origin = label_image.GetOrigin()
label_spacing = label_image.GetSpacing()

# Calculate the bounding box of the label
non_zero_indices = np.argwhere(label_array)
label_bbox_min = non_zero_indices.min(axis=0)  # min (z_min, y_min, x_min)
label_bbox_max = non_zero_indices.max(axis=0) + 1  # max (z_max, y_max, x_max)

# Define ROI start based on label's bounding box in RAS coordinates
roi_start = [
    int(label_bbox_min[0]),
    int(label_bbox_min[1]),
    int(label_bbox_min[2])
]

# Define size based on label's bounding box dimensions
roi_size = [
    int(label_bbox_max[0] - label_bbox_min[0]),
    int(label_bbox_max[1] - label_bbox_min[1]),
    int(label_bbox_max[2] - label_bbox_min[2])
]

# Adjust roi_start for RAS coordinates
# Negate x and y indices for conversion from LPS to RAS
roi_start[1] = volume_array.shape[1] - roi_start[1]  # Adjust y-coordinate
roi_start[2] = volume_array.shape[2] - roi_start[2]  # Adjust x-coordinate

# Crop the volume using SimpleITK
cropped_volume = sitk.RegionOfInterest(volume_image, size=roi_size, index=roi_start)

# Save the cropped volume
sitk.WriteImage(cropped_volume, 'C:/Machine Learning/cropped_images/Pros_Normal_002_cropped.nrrd')

# Print out metadata
print("Label Shape:", label_shape)
print("Label Origin (world coordinates):", label_origin)
print("Cropped Volume Origin (world coordinates):", cropped_volume.GetOrigin())
print("Cropped Volume Size:", cropped_volume.GetSize())
</code></pre>

---

## Post #2 by @lassoan (2024-10-09 12:52 UTC)

<p>You can run this code snippet in Slicer’s Python environment to resample and crop/pad the segmentation to exactly match a reference volume’s geometry:</p>
<pre data-code-wrap="python"><code class="lang-python">referenceVolumeNode = slicer.util.loadVolume("c:/tmp/image.nrrd")
segmentationNode = slicer.util.loadSegmentation("c:/tmp/segmentation.seg.nrrd")

# Set segmentation's geometry (origin, spacing, axis direction, extents) to the reference image geometry
# (it does not resample existing segments)
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)

# Resample existing segments to the reference image geometry
segGeomLogic = slicer.vtkSlicerSegmentationGeometryLogic()
segGeomLogic.SetInputSegmentationNode(segmentationNode)
segGeomLogic.SetSourceGeometryNode(referenceVolumeNode)
segGeomLogic.SetPadOutputGeometry(False)
segGeomLogic.CalculateOutputGeometry()
segGeomLogic.ResampleLabelmapsInSegmentationNode()

slicer.util.saveNode(segmentationNode, "c:/tmp/resampled-segmentation.seg.nrrd")
</code></pre>

---
