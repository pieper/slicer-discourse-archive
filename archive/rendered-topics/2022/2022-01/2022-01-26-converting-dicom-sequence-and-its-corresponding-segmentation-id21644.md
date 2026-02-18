# Converting DICOM sequence and its corresponding segmentation into world coordinates

**Topic ID**: 21644
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/converting-dicom-sequence-and-its-corresponding-segmentation-into-world-coordinates/21644

---

## Post #1 by @Dmitry_Cherezov (2022-01-26 22:36 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8</p>
<p>Dear Community,</p>
<p>I need some help with Python coding in the 3DSlicer environment.</p>
<p>The task is relatively simple, but I got lost in numerous methods Slicer provides.</p>
<p>By having a path to a folder with DICOM sequence and a path to a segmentation file. I need to read both, then bring them into a world coordinates and save both volumes as numpy arrays.</p>
<p>I figured out how to read a dicom folder:</p>
<blockquote>
<p>from DICOMLib import DICOMUtils<br>
dicomDataDir = ‘path\to\DICOM\’  # input folder with DICOM files<br>
with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
t = DICOMUtils.loadPatientByUID(patientUID)<br>
s = slicer.util.array(t[0])<br>
loadedNodeIDs.extend(t)</p>
</blockquote>
<p>I figured out how to read a segmentation file:</p>
<blockquote>
<p>loadedNodeIDs = ‘path\to\segmentation’  # this list will contain the list of all loaded node IDs<br>
sv = slicer.util.loadVolume(loadedNodeIDs)<br>
svv = slicer.util.array(sv.GetID())</p>
</blockquote>
<p>Now, can someone please show me how to convert both volumes into world coordinates?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2022-01-27 03:04 UTC)

<p>Both volumes are already in RAS coordinate system. Does something suggest that they are not? Do they appear misaligned?</p>
<p>To get them as numpy array, you can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume"><code>arrayFromVolume</code></a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromSegmentBinaryLabelmap"><code>arrayFromSegmentBinaryLabelmap</code></a> functions. Use a recent Slicer Preview Release, because <code>arrayFromSegmentBinaryLabelmap</code> in Slicer-4.11 returned a numpy array that was cropped to th minimum necessary size, so you had to do extra work to get the voxels in the same geometry as the reference volume.</p>

---

## Post #3 by @Dmitry_Cherezov (2022-08-02 18:07 UTC)

<p>This is correct, 3D Slicer reads volumes in the RAS coordinate system. However, here is the trick - the origin of coordinates could be different. Simple overlapping of IJK coordinates for both files will lead to misalignment of volumetric data. Data should be converted to XYZ coordinate system and then the data will be aligned.</p>
<p>In particular, what problem I have. I want to write a code in Slicer so that given two paths - DICOM folder and segmentation file (NIFTI, NRRD, MHD, etc) it opens both volumes and aligns them in world (XYZ) coordinates.</p>
<p>I know how to read volumes, but do not know how to bring them to world coordinates and then iterate data.</p>

---

## Post #4 by @lassoan (2022-08-09 10:12 UTC)

<p>What you describe is correct and it is a good practice to check image geometry (origin, spacing, axis directions, and extent) when working with images and resample them as needed.</p>
<p>If you want to get the voxel array in a specific geometry (not the current one) in Slicer then you can specify a reference volume node in <code>arrayFromSegmentBinaryLabelmap</code>. You can also specify reference geometry on most other export and conversion methods.</p>

---
