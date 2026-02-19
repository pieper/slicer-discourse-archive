---
topic_id: 25102
title: "Scalars Not Calculated When Creating New Volume"
date: 2022-09-05
url: https://discourse.slicer.org/t/25102
---

# Scalars not calculated when creating new volume

**Topic ID**: 25102
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/scalars-not-calculated-when-creating-new-volume/25102

---

## Post #1 by @Niels (2022-09-05 13:55 UTC)

<p>I am recently using Slicer 5.0.3 r30893 / 7ea0f43 and I noticed a strange behaviour when it comes to the scalar range that i get back after filling the vtkImageData.</p>
<p>I have a python module that reads scalar values from a file (the values are correct).</p>
<p>After writing the values to the image data I noticed by looking at the volumenode properties the scalar ranges are very strange. For example from 0 to 0 or from 0 to a huge number.</p>
<p>After some debugging I noticed that the vtkImageData.GetScalarRange() returns the incorrect number. With Slicer 4.11 it all works fine.</p>
<p>I used some code I found on the forum to trigger the modified() flag. But this partially solves the problem, because the slice views are updated with the correct ranges only after I right-click on the volume in the data view.</p>
<pre><code>imageData = vtk.vtkImageData()
imageData.SetDimensions(imageDimention[0],imageDimention[1],imageDimention[2])
imageData.AllocateScalars(vtk.VTK_FLOAT, 1)

newVolumeNode = slicer.vtkMRMLScalarVolumeNode()
newVolumeNode.CreateDefaultDisplayNodes()
newVolumeNode.SetOrigin(imageOrigin[0], imageOrigin[1], imageOrigin[2])
newVolumeNode.SetSpacing(imageSpacing[0], imageSpacing[1], imageSpacing[2])
newVolumeNode.SetAndObserveImageData(imageData)
newVolumeNode.SetName("import_scan")

slicer.mrmlScene.AddNode(newVolumeNode)


# set the image data
index = 0
for z in range(0, imageDimention[2]):
  for y in range(0, imageDimention[1]):
    for x in range(0, imageDimention[0]):
      voxelData[z][y][x] = voxels[index] # set the values from the file
      index = index + 1

# Mark scalars as modified
# This is required for getting up-to-date scalar range.
if (imageData.GetPointData() and imageData.GetPointData().GetScalars()):
  imageData.GetPointData().GetScalars().Modified();
imageData.Modified()

# mark the volume as modified
newVolumeNode.Modified()
</code></pre>

---
