# Open files with Overlay Plane tags set

**Topic ID**: 12990
**Date**: 2020-08-14
**URL**: https://discourse.slicer.org/t/open-files-with-overlay-plane-tags-set/12990

---

## Post #1 by @Roman_Kovtuh (2020-08-14 00:21 UTC)

<p>System: Linux Ubuntu 18.04<br>
Slicer version: 4.10.2 r28257<br>
Expected behaviour: Slicer opens files in Scalar Overlay mode and shows overlay.<br>
Current behaviour: Opening DICOM file <a href="https://github.com/pydicom/pydicom/blob/e8de9d31fc97e1162441adf4bd2742b82149ce18/pydicom/data/test_files/MR-SIEMENS-DICOM-WithOverlays.dcm" rel="noopener nofollow ugc">from pydicom library tests</a> that contains Overlay Plane tags set, we get an error:</p>
<blockquote>
<p>virtual bool qSlicerScalarOverlayReader::load(const IOProperties&amp;)  failed: missing fileName or modelNodeId property</p>
</blockquote>

---

## Post #2 by @Roman_Kovtuh (2020-08-14 00:22 UTC)

<p>Operating system: Linux 4.15.0-112-generic <span class="hashtag">#113-Ubuntu</span> 18.04<br>
Slicer version: 4.10.2 r28257<br>
Expected behavior: Open file [1] with Overlay Plane tags set and show stored overlay.<br>
Actual behavior: When opening such file not in volume mode but as “Scalar Overlay” got an error: “virtual bool qSlicerScalarOverlayReader::load(const IOProperties&amp;)  failed: missing fileName or modelNodeId property”</p>
<p>File I try to open is from tests for pydicom Python library:<br>
[1] <a href="https://github.com/pydicom/pydicom/blob/e8de9d31fc97e1162441adf4bd2742b82149ce18/pydicom/data/test_files/MR-SIEMENS-DICOM-WithOverlays.dcm" rel="nofollow noopener">https://github.com/pydicom/pydicom/blob/e8de9d31fc97e1162441adf4bd2742b82149ce18/pydicom/data/test_files/MR-SIEMENS-DICOM-WithOverlays.dcm</a></p>

---

## Post #3 by @lassoan (2020-08-14 00:32 UTC)

<p>“Scalar overlay” in Add data window refers to FreeSurfer overlays, they are not related to DICOM overlays.</p>
<p>DICOM overlays were introduced decades ago and they are largely obsolete. Slicer does not support them, and we don’t plan to add support for them. Of course, we will not prevent anybody to implement importer/exporter for them, but instead I would recommend to use modern DICOM (structured reports, segmentation objects, etc.) to store various image annotations.</p>

---

## Post #4 by @Roman_Kovtuh (2020-08-14 03:14 UTC)

<p>Hello, <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>Thank you for your quick and helpful reply.</p>

---
