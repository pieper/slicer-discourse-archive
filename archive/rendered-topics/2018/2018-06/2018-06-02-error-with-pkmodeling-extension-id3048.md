# Error with Pkmodeling extension

**Topic ID**: 3048
**Date**: 2018-06-02
**URL**: https://discourse.slicer.org/t/error-with-pkmodeling-extension/3048

---

## Post #1 by @bmb777 (2018-06-02 20:29 UTC)

<p>Hello,</p>
<p>I am trying to use the Pkmodeling extension to analyze DCE-MRI images and I am receiving the error below:</p>
<p>itk::ExceptionObject (0000004C75F13E18)<br>
Location: “unknown”<br>
File: D:\D\N\S481-E-b\PkModeling\CLI\PkModeling.cxx<br>
Line: 244<br>
Description: itk::ERROR: itk::ERROR: Unrecognized frame identifying DICOM tag name Time Image C:/Users/brand/AppData/Local/Temp/Slicer/BCGEI_vtkMRMLMultiVolumeNodeC.nrrd does not contain sufficient attributes to support algorithms.</p>
<p>I believe this is due to my DICOM series not having a trigger time tag. However, I am a fairly novice user and do not know how to correct this missing information.</p>
<p>Any help is appreciated!</p>

---

## Post #2 by @fedorov (2018-06-03 17:06 UTC)

<p>Can you include the following details:</p>
<ul>
<li>did you import the DCE MRI into Slicer using DICOM Browser or MultiVolumeImporter?</li>
<li>what version of Slicer do you use?</li>
</ul>

---

## Post #3 by @bmb777 (2018-06-03 22:20 UTC)

<p>I have tried to use both the DICOM browser and MultiVolumeImporter and received the same error. I’m using version 4.8.1 for windows.</p>

---

## Post #4 by @fedorov (2018-06-04 01:06 UTC)

<p>I believe this issue was fixed this April, after 4.8.1 release in this commit: <a href="https://github.com/QIICR/PkModeling/commit/8e597589e761bde1ab17f17126ac002527cbd28d">https://github.com/QIICR/PkModeling/commit/8e597589e761bde1ab17f17126ac002527cbd28d</a>. Can you please try if the nightly build works for you?</p>

---

## Post #5 by @bmb777 (2018-06-04 18:04 UTC)

<p>The nightly build works and I am no longer receiving the error. Thank you for your time and advice!</p>

---
