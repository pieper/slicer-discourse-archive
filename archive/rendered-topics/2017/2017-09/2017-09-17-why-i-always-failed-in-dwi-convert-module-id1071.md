---
topic_id: 1071
title: "Why I Always Failed In Dwi Convert Module"
date: 2017-09-17
url: https://discourse.slicer.org/t/1071
---

# Why I always failed in DWI Convert module?

**Topic ID**: 1071
**Date**: 2017-09-17
**URL**: https://discourse.slicer.org/t/why-i-always-failed-in-dwi-convert-module/1071

---

## Post #1 by @zjrichard (2017-09-17 15:50 UTC)

<p>Hi sir. When I use the module DWI Convert (Slicer 4.7.0), Dicom to Nrrd, and click Apply, it always shows the error as follows and I can’t convert the dicom data to nrrd:</p>
<p><strong>Diffusion-weighted DICOM Import (DWIConvert) standard error:</strong></p>
<p>**Exception creating converter **<br>
<strong>itk::ExceptionObject (000000000015CB60)</strong><br>
**Location: “unknown” **<br>
<strong>File: C:\D\N\Slicer-0-build\ITKv4\Modules\IO\DCMTK\src\itkDCMTKFileReader.cxx</strong><br>
<strong>Line: 963</strong><br>
<strong>Description: itk::ERROR: Cant find tag 29 1010</strong></p>
<p>Thank you very much if you could solve the problem!</p>

---

## Post #2 by @ihnorton (2017-09-20 17:40 UTC)

<p>Hello. That private tag, along with several others, is required in order to extract the diffusion acquisition parameters for Siemens data. There are several potential reasons why it could be missing, but the most likely is that the data was anonymized or exported without preserving the tag. Some anonymization routines do not preserve any private tags (including, in my experience, the Siemens anonymized-export functionality on some versions of scanner software and SynGo Via). You may need to discuss with your MR technicians or physicists in order to revise the transfer process.</p>
<p>(although it will likely not make a difference in this case, please also make sure you are using a recent nightly download, because many improvements by the DWIConvert team were incorporated in the Slicer build from early August)</p>

---
