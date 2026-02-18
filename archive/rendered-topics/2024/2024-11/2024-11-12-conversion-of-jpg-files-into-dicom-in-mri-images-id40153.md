# Conversion of .jpg files into DICOM in MRI images

**Topic ID**: 40153
**Date**: 2024-11-12
**URL**: https://discourse.slicer.org/t/conversion-of-jpg-files-into-dicom-in-mri-images/40153

---

## Post #1 by @benedettabottelli (2024-11-12 17:10 UTC)

<p>I have three different folders containing .jpg images of three different views of a shoulder MRI (axial, coronal, sagittal). How can I convert them into DICOM format? Additionally, if I upload the sequences as they are, 3D Slicer treats all the folders as axial views and does not differentiate them. How can I change this? How can I upload everything as a single volume?</p>

---

## Post #2 by @pieper (2024-11-13 14:52 UTC)

<p>If you only have jpg then you will have trouble working in 3D.  You’ll need to figure out the geometry that has already been thrown away by the conversion.  You should really get original dicom images that contain the scan parameters needed to reconstruct.</p>

---

## Post #3 by @benedettabottelli (2024-11-18 07:37 UTC)

<p>So, is it not possible to set in 3D Slicer what type of view I am considering? Also, to check if it treats the slices as a 3D volume, do I need dimensions of NxNxN?</p>

---

## Post #4 by @pieper (2024-11-18 16:05 UTC)

<p>If you are reading the data from jpg then the orientation and spacing information is lost and you need to reconstruct it manually to map it back to patient space.  The needed transforms are described here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html</a></p>
<p>One way to do this is to save the volume in into a nrrd file and then edit the header to fill in the missing data.</p>
<p><a href="https://teem.sourceforge.net/nrrd/format.html" class="onebox" target="_blank" rel="noopener">https://teem.sourceforge.net/nrrd/format.html</a></p>

---
