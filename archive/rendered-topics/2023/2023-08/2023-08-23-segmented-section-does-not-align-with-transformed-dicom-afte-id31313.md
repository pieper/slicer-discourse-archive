---
topic_id: 31313
title: "Segmented Section Does Not Align With Transformed Dicom Afte"
date: 2023-08-23
url: https://discourse.slicer.org/t/31313
---

# Segmented Section does not align with transformed DICOM after export

**Topic ID**: 31313
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/segmented-section-does-not-align-with-transformed-dicom-after-export/31313

---

## Post #1 by @DaSt (2023-08-23 10:47 UTC)

<p>Short: When I import a DICOM series to 3D Slicer it automatically adds a transformation to it, after segmenting a region and exporting it to an STL, I use a third party software to view if the dicom and the STL align which is not the case and there is a translation in between.</p>
<p>Long:<br>
Hello everyone, I am importing a CT Data DICOM Series to 3D slicer. I have several datasets and my issue only arises to those Series where after an import 3D slicer applies automatically a grid transformation. I segment a bone in the CT Data and export it as STL file. I postprocess this stl into an FEM mesh and then want to map the material properties on it using Bonemat. When I now import my DICOM series to Bonemat and add the Mesh, the mesh does not overlap with the DICOM series perfectly but a translation is present. For DICOM series without an automatic grid transformation this issue is not present.</p>
<p>Tried approaches:<br>
I exported the STL both as LPS and RAS<br>
I tried to apply the grid transform on the Segmentation that I created<br>
I tried transformation hardening on the dicom and exporting it as new series.</p>
<p>I’d be very grateful for any tipps regarding this issue, thank you very much in advance!</p>
<p>Greetings,<br>
Daniel</p>

---

## Post #2 by @lassoan (2023-08-23 11:22 UTC)

<p>Most likely the third-party software does not correctly reconstruct the 3D image from slices.</p>
<p>Most software can only reconstruct volumes by stacking slices into a rectangular box, but that is only correct when all slices have the same size and pixel spacing, they are all parallel, and each pair of neighbor slices have equal distance from each other and the vector connecting their origin is parallel to their normal direction. Many 3D imaging software applications just hope that all these assumptions are true and provides an incorrectly reconstructed image if any of the assumptions are violated.</p>
<p>CT images (especially brain CTs) are often acquired with tilted gantry. In such acquisitions, a “shearing” transform must be applied (in Slicer it is implemented by a grid transform) for reconstructing the correct shape. When imaging extremities slice spacing may be varied for reducing dose. In some cases image slices may be missing due to corrupted data transfers, causing irregular slice spacing. Some MRI and ultrasound imaging protocols acquire non-parallel slices. These images are all reconstructed incorrectly by many software?</p>
<p>I would recommend to report this error Bonemat developers and in the meantime do not use Bonemat for DICOM image import for images with non-trivial geometry. Instead, you can import these images into Slicer, harden the transform, and save that image as nrrd or nifti. I assume bonemat can read these formats.</p>
<p>Note that Slicer can do most of what Bonemat does - generate volumetric mesh using <code>SegmentMesher</code> extension, assign HU values to mesh points using <code>Probe volume with model</code> module, etc. For Abaqus/Ansys import/export you may need to use third-party packages, such as meshio. If you need these a convenient GUI for these import/export then it should be quite easy to add it within Slicer, by creating a small Python scripted module for it.</p>

---
