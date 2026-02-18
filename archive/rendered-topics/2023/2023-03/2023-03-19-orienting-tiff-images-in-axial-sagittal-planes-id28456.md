# Orienting .tiff images in axial/sagittal planes

**Topic ID**: 28456
**Date**: 2023-03-19
**URL**: https://discourse.slicer.org/t/orienting-tiff-images-in-axial-sagittal-planes/28456

---

## Post #1 by @Liza_Harold (2023-03-19 18:28 UTC)

<p>I have two stacks of .png images, imported as .tiff files, corresponding to axial and sagittal MRI data. Once I put them into Slicer using the “Data” panel, both stacks are only visible using the “Axial” view. I am trying to segment a 3D volume using the segmentation editor, but since the views are both marked as Axial, the paint tool for each volume is not aligned. I have tried using transforms to switch the plane of the Sagittal .tiff image stack, but it only flips the data in the axial view. Is there a way to line up these image stacks so that segmentation can occur? Thanks!</p>

---

## Post #2 by @lassoan (2023-03-19 19:17 UTC)

<p>TIFF images have many issues. The most important one is that when you convert the original DICOM images to TIFF, the 3D image origin, spacing, and axis directions are lost. You could try to guess these and <a href="https://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#a55550614d4cc322eed7bc9ed533dfed4">set them into the loaded volume’s IJKToRAS matrix</a>, but I would recommend to work with the original DICOM images instead.</p>

---
