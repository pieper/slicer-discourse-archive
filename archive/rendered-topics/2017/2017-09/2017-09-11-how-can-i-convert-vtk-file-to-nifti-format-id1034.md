---
topic_id: 1034
title: "How Can I Convert Vtk File To Nifti Format"
date: 2017-09-11
url: https://discourse.slicer.org/t/1034
---

# How Can I Convert VTK file to nifti format?

**Topic ID**: 1034
**Date**: 2017-09-11
**URL**: https://discourse.slicer.org/t/how-can-i-convert-vtk-file-to-nifti-format/1034

---

## Post #1 by @shahrokh (2017-09-11 11:35 UTC)

<p>Hi users and developes of Slicer</p>
<p>For creating surface model from one nifti image file, I used “Grayscale Model Maker” module in the category of “Surface Models”. I can save this surface model in vtk format successfully.</p>
<p>At now, I want to save this surface model in nifti format. How can I do it (convert vtk to nifti or dicom)?</p>
<p>I do not know to do it using Slicer modules. How can do it using Slicer?</p>
<p>I try to do it using applications such as Convert3D (c3d), itksnap or gdcm (gdcm2vtk), but I do not success. I get the following error messages.</p>
<p><strong>in gdcm:</strong><br>
[sn@localhost Documents]$ gdcm2vtk -h<br>
gdcm2vtk: gdcm 2.8.2 $Date$<br>
vtk version 6.3.0<br>
Usage: gdcm2vtk [OPTION] input output<br>
Convert a vtk-supported file into DICOM.<br>
…<br>
[sn@localhost Documents]$ ll -h *.vtk<br>
-rw-rw-r–. 1 sn sn 68K Sep 11 08:52 myTest.vtk<br>
[sn@localhost Documents]$ gdcm2vtk myTest.vtk myTest.dcm<br>
Warning: In /builddir/build/BUILD/VTK-6.3.0/IO/Legacy/vtkDataReader.cxx, line 490<br>
vtkStructuredPointsReader (0x2bbb860): Reading file version: 4.1 with older reader version 4.0</p>
<p>could not find no reader to handle file: myTest.vtk<br>
[sn@localhost Documents]$</p>
<p><strong>In Convert3D:</strong><br>
[sn@localhost Documents]$ c3d myTest.vtk -o myTest.dcm<br>
Exception caught of type 16ConvertException</p>
<p>[sn@localhost Documents]$</p>
<p><strong>In itksnap:</strong><br>
After select myTest.vtk in the window of “Open Image - ITK-SNAP”, I get this error message: "Error: Wrong Format: The IO library for the format ‘VTK Image’ can not read the image file.’</p>
<p>Please guid me to solve it. How can I convert vtk file to nifti format?<br>
Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2017-09-11 13:37 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="1034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>I want to save this surface model in nifti format</p>
</blockquote>
</aside>
<p>I don’t think that current NIfTI (<a href="https://nifti.nimh.nih.gov/nifti-1/documentation/">NIfTI1</a>), can store surface model.</p>

---

## Post #3 by @shahrokh (2017-09-11 15:29 UTC)

<p>Thanks a Andras.<br>
I think that I solved it. After creating surface model from nifti image file(32<em>20</em>24 voxels with spacing 1.5625<em>1.5625</em>1.5625 mm)  by “Grayscale Model Maker” module, I used “Mesh To Label Map” module. This module was created label map with nrrd format with the same dimensions and spacing such as input nifti image file. I save it with nifti format.</p>

---

## Post #4 by @lassoan (2017-09-11 17:25 UTC)

<p>To edit labelmaps stored in image files, such as NIfTI, I would recommend to import it into a segmentation node (using Segmentations module import/export section), edit using Segment Editor module, then export it to labelmap image node (using Segmentations module import/export section).</p>

---

## Post #5 by @lassoan (2018-03-15 18:21 UTC)

<p>A post was split to a new topic: <a href="/t/convert-vtk-file-to-nifti-or-dicom/2330">Convert VTK file to NIFTI or DICOM</a></p>

---
