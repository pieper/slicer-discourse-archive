# How to Convert .mhd + .raw 3D Time-Series Images into a 4D DICOM in 3D Slicer?

**Topic ID**: 44280
**Date**: 2025-08-30
**URL**: https://discourse.slicer.org/t/how-to-convert-mhd-raw-3d-time-series-images-into-a-4d-dicom-in-3d-slicer/44280

---

## Post #1 by @sprp2025uci (2025-08-30 03:59 UTC)

<p>Hi,</p>
<p>I am working with publicly available 3D echocardiographic datasets stored as .mhd + .raw files, along with corresponding .vtk mesh files for each time frame. I would like to convert these into a single 4D DICOM (cine loop of 3D volumes).</p>
<p>My ultimate goal is to process these datasets in Philips’ ultrasound workspace, which only accepts DICOM/DICOMDIR formats. From what I understand, there are two main steps involved:</p>
<ol>
<li>
<p>Combining all time steps into a single patient/study dataset.</p>
</li>
<li>
<p>Exporting the result as a single 4D DICOM.</p>
</li>
</ol>
<p>Can this workflow be achieved in 3D Slicer? If so, I would greatly appreciate any guidance on how to proceed.</p>
<p>The public datasets can be accessed here: <a href="https://humanheart-project.creatis.insa-lyon.fr/database/?utm_source=chatgpt.com#collection/587de6f4e1af3f30a2980a58/folder/587f5c8ce1af3f30a298173d" rel="noopener nofollow ugc">Human Heart Project Dataset</a></p>
<p>Any advice is welcome!</p>
<p>Thank you,<br>
Satya</p>

---

## Post #2 by @lassoan (2025-08-30 04:12 UTC)

<p>In theory, you can store 3D+t echo data in DICOM, but unfortunately, no 3D ultrasound vendors have implemented it. Instead, all of them store 3D+t ultrasound data in private attributes in proprietary format. If you generate 3D+t ultrasound in standard DICOM format, you will not be able to load it into the Philips software.</p>
<p>Probably SlicerHeart is your best bet if you want to process multimodality cardiac data. It has lots of analysis and visualization tools; and if something is missing then it can be added, as it is all open-source.</p>

---
