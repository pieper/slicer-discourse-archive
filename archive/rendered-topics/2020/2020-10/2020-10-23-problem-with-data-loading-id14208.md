---
topic_id: 14208
title: "Problem With Data Loading"
date: 2020-10-23
url: https://discourse.slicer.org/t/14208
---

# Problem with data loading

**Topic ID**: 14208
**Date**: 2020-10-23
**URL**: https://discourse.slicer.org/t/problem-with-data-loading/14208

---

## Post #1 by @doc-xie (2020-10-23 03:50 UTC)

<p>Hi everyone,<br>
How can kill the problem with data loading into Slicer. The information about the error was list below and the problem was the same between CT and MRI in DICOM:<br>
Imported a DICOM directory, checking for extensions<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 737, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “C:/Users/nzz/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules/DicomSroImportPlugin.py”, line 30, in examine<br>
examineInfo = slicer.vtkDICOMImportInfo()<br>
AttributeError: ‘module’ object has no attribute ‘vtkDICOMImportInfo’<br>
Warning: Plugin failed: DicomSroImportPlugin</p>
<p>See python console for error message.<br>
DICOM Plugin failed: ‘module’ object has no attribute ‘vtkDICOMImportInfo’<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 733, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)<br>
File “C:/Users/nzz/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules/DicomRtImportExportPlugin.py”, line 41, in examineForImport<br>
slicer.modules.dicomrtimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)<br>
AttributeError: ‘module’ object has no attribute ‘dicomrtimportexport’<br>
Warning: Plugin failed: DicomRtImportExportPlugin</p>
<p>See python console for error message.<br>
DICOM Plugin failed: ‘module’ object has no attribute ‘dicomrtimportexport’</p>
<p>ImportError: DLL load failed: ¾Ü¾ø·ÃÎÊ¡£<br>
Traceback (most recent call last):<br>
File “C:/Users/nzz/AppData/Roaming/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorWatershed.py”, line 30, in registerEditorEffect<br>
instance.self().register()<br>
AttributeError: ‘NoneType’ object has no attribute ‘register’<br>
Best wishes,<br>
Xie</p>

---

## Post #2 by @Sunderlandkyl (2020-10-23 04:02 UTC)

<p>Can you try with the latest stable release and let us know if the issue still occurs?</p>

---

## Post #3 by @doc-xie (2020-10-23 07:40 UTC)

<p>Hi,<br>
I installed the newest preview version(4.13.0,2020-10-22). The DICOM data can not be loaded successfully. The error showed as following:<br>
Could not read scalar volume using GDCM approach. Error is: FileFormatError</p>
<p>Loading with imageIOName: DCMTK</p>
<p>Could not read scalar volume using DCMTK approach. Error is: FileFormatError</p>
<p>Could not load: 4: Unnamed Series as a Scalar Volume</p>
<p>Best wishes,<br>
Xie</p>

---

## Post #4 by @lassoan (2020-10-23 17:56 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="3" data-topic="14208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p>Could not read scalar volume using DCMTK approach. Error is: FileFormatError</p>
</blockquote>
</aside>
<p>This indicates that the file is corrupted. If you can upload it somewhere (make sure there is no patient health information in the file) and post the link here then we can confirm.</p>

---

## Post #5 by @doc-xie (2020-10-26 01:44 UTC)

<p>Hi Lassoan,<br>
After the data was converted into *.nii format, it can be loaded into Slicer correctly and the size of the data was more bigger (448M)than the original data (261M). Here is the link of the data:<br>
Link:<a href="https://pan.baidu.com/s/1d8kGMruZ1mGyitUIl3qBFw" rel="noopener nofollow ugc">https://pan.baidu.com/s/1d8kGMruZ1mGyitUIl3qBFw</a><br>
PIN:sako<br>
But I am not sure whether you can download it successfully.<br>
Best wishes,<br>
Xie</p>

---

## Post #6 by @lassoan (2020-10-26 02:44 UTC)

<p>I could not download the file. The download page was all Chinese, I got it mostly translated in the browser but it wanted me to install something and register an account. Could you upload to anywhere else? Or somebody could help with downloading it and uploading to any file sharing service that allows direct download.</p>

---

## Post #7 by @doc-xie (2020-10-26 03:27 UTC)

<p>Hi Lassoan,<br>
I think it can be downloaded now for you.<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/sh/0gvgcaw88d09ts8/AADT4n6rFKRQ0zP_yOnKQGNVa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/0gvgcaw88d09ts8/AADT4n6rFKRQ0zP_yOnKQGNVa?dl=0" target="_blank" rel="noopener nofollow ugc">guoqiangxie</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Best wishes,<br>
Xie

---

## Post #8 by @lassoan (2020-10-27 02:45 UTC)

<p>Thank you I could open this nifti file and it looks good, but it does not help in determining what was the problem with the original file.</p>
<p>This nifti file uses “float” voxel type, which is the most probably reason why it uses 2x more space than the original (usually “short” type). If memory usage is a concern then you can cast the image back “short” using “Cast scalar volume” module and/or crop it to the relevant region using Crop volume module.</p>
<p>Have you converted from DICOM to nifti using dcm2niix? Maybe it is more tolerant to some DICOM format errors than DCMTK or GDCM (that Slicer uses for DICOM parsing by default). You can choose to use dcm2niix as DICOM image loader in Slicer by installing SlicerDcm2nii extension.</p>

---

## Post #9 by @doc-xie (2020-10-27 07:17 UTC)

<p>Hi Lassoan,<br>
The data can be loaded into Slicer normally from DICOM using dcm2niix and saved in .nhdr format. But I am not sure about the problem about the data and when the dcm2niix should be chose for data loading.<br>
Best wishes,<br>
Xie</p>

---
