---
topic_id: 4786
title: "Error With Dscmrianalysis Extension"
date: 2018-11-18
url: https://discourse.slicer.org/t/4786
---

# Error with DSCMRIanalysis extension

**Topic ID**: 4786
**Date**: 2018-11-18
**URL**: https://discourse.slicer.org/t/error-with-dscmrianalysis-extension/4786

---

## Post #1 by @happyle (2018-11-18 15:43 UTC)

<p>Dear Dr. Fedorov, <a class="mention" href="/u/fedorov">@fedorov</a></p>
<p>Thank you for your awesome work on DSCMRIAnalysis module.</p>
<p>I am trying to use the DSCMRIanalysis extension to analyze DSC-MRI images and I am receiving the error below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/030e6c1af8a8af17d72bb2db70414479f8b9974a.png" alt="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20181118233839" data-base62-sha1="r2kAh8adyjZWebgzR3NDeHGK2S" width="654" height="425"></p>
<p>DSCMRIAnalysis standard error:</p>
<p>C:/Users/happyle/AppData/Roaming/NA-MIC/Extensions-27560/DSCMRIAnalysis/lib/Slicer-4.11/cli-modules/DSCMRIAnalysis.exe: exception caught !</p>
<p>itk::ExceptionObject (0000006EF28F4EE8)</p>
<p>Location: "unknown"</p>
<p>File: D:\D\P\S-0-E-b\DSCMRIAnalysis\CLI\DSCMRIAnalysis.cxx</p>
<p>Line: 231</p>
<p>Description: itk::ERROR: itk::ERROR: Unrecognized frame identifying DICOM tag name NA Image C:/Users/happyle/AppData/Local/Temp/Slicer/ECFC_vtkMRMLMultiVolumeNodeB.nrrd does not contain sufficient attributes to support algorithms.</p>
<p>I’m using version 4.11.0 for windows 10.<br>
Any help is appreciated!</p>

---

## Post #2 by @fedorov (2018-12-01 23:29 UTC)

<p>This happens when the DICOM tags needed for the analysis were not parsed or recognized on load. How did you load the dataset? Can you enable advanced mode in the DICOM browser and see if there is more than one option to load the dataset?</p>

---
