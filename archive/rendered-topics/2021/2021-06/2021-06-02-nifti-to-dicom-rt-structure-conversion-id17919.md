# Nifti to DICOM-RT structure conversion

**Topic ID**: 17919
**Date**: 2021-06-02
**URL**: https://discourse.slicer.org/t/nifti-to-dicom-rt-structure-conversion/17919

---

## Post #1 by @laura.gelcano (2021-06-02 10:06 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.11.20200930</p>
<p>Hi all,</p>
<p>I have a binary mask in a Nifti file and I want to convert it into a DicomRT structure. I have tried 3D Slicer to perform this conversion using Dicom export plugins. Also, I have found a package, RT-Utils, that deals with it. However, the resulted DicomRT structures of both tools are not exactly the same.</p>
<p>Can anyone give me some details about this exportation in 3D Slicer?</p>
<p>I think the problem may be due to the way of extracting/storing the contours (e.g., the interpolation method), which may be somewhat different for both tools, thus providing slightly different results.</p>
<p>Can anyone ensure me that the exportation in 3D Slicer is robust? Has it being tested with “round-trip” experiments from Nifti to DicomRT and back (from DicomRT to Nifti).</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-06-02 11:28 UTC)

<p>DICOM RTSTRUCT cannot store arbitrarily shaped segments. It was developed decades ago for storing manually drawn contours. I would strongly recommend to use to DICOM Segmentation Object to store segmentations, which allows lossless storage of binary labelmaps.</p>
<p>Slicer uses Plastimatch library for RTSTRUCT export. You can look up papers about this library to see what validations were done. Maybe <a class="mention" href="/u/gcsharp">@gcsharp</a> can give you some pointers, too.</p>

---

## Post #3 by @gcsharp (2021-06-02 17:13 UTC)

<p>The plastimatch algorithm uses marching squares within image planes to generate planar polygons from a binary image.  No special interpolation is done, meaning that polygon vertices lie at voxel face centers.  The output will vary according to the resolution of the referenced image (the CT); if the referenced image has a different resolution than the Nifti file, this could affect round trip calculations.</p>
<p>In the past I have performed round trip tests within plastimatch and the sequence image → RTSTRUCT → image produces an output identical to the input.  However, I have not tried this in 3D Slicer, which uses a different implementation for DICOM import and rasterization.</p>

---

## Post #4 by @laura.gelcano (2021-06-04 16:02 UTC)

<p>Thanks a lot for your quick replies and the valuable information given.<br>
It has already helped me.</p>

---
