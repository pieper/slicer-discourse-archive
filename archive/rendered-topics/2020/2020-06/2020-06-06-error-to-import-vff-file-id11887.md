# Error to import vff file

**Topic ID**: 11887
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/error-to-import-vff-file/11887

---

## Post #1 by @Paulo_Tavares (2020-06-06 00:11 UTC)

<p>When I try to import a vff file in 3Dslicer it noticed a error.</p>
<p>Warning: In D:\D\S\S-4102-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 104</p>
<p>vtkSlicerVffFileReaderLogic (000001F7636E6030): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘filter’</p>
<p>Warning: In D:\D\S\S-4102-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 104</p>
<p>vtkSlicerVffFileReaderLogic (000001F7636E6030): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘batch’</p>
<p>Warning: In D:\D\S\S-4102-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 104</p>
<p>vtkSlicerVffFileReaderLogic (000001F7636E6030): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘gel’</p>
<p>Warning: In D:\D\S\S-4102-E-b\SlicerRT\VffFileReader\Logic\vtkSlicerVffFileReaderLogic.cxx, line 104</p>
<p>vtkSlicerVffFileReaderLogic (000001F7636E6030): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘modification_history’</p>

---

## Post #2 by @Paulo_Tavares (2020-06-06 04:38 UTC)

<p>I have downloaded SlicerRT and GelDosimetry to analyse a .vff file. Although, I couldn’t import these files. It doesn’t show nothing when I click to import.</p>

---

## Post #3 by @cpinter (2020-06-08 08:43 UTC)

<p>Can you check if in the latest Slicer preview with SlicerRT installed the same thing happens? Don’t use Gel Dosimetry just drag&amp;drop the VFF file onto Slicer.</p>
<p>If the same errors happen, then probably your VFF file is a different version of the format or some fields are omitted, in which case some changes will be needed in the reader code.</p>

---

## Post #4 by @Paulo_Tavares (2020-06-08 11:32 UTC)

<p>Hello, thank you for reply.<br>
Yes, the error continues. But now it just warns this:<br>
<strong>LoadVffFile: The specified file could not be opened.</strong></p>

---

## Post #5 by @lassoan (2020-06-08 14:12 UTC)

<p>How did you create this file? With what software and which version? Can you upload a sample somewhere (dropbox, onedrive, gdrive) and post the link here?</p>

---

## Post #6 by @Paulo_Tavares (2020-06-08 17:12 UTC)

<p>I’m using Vista Scan. It’s for a academy reaserchy in gel dosimetry. I’m sending a gdrive link.<br>
</p><aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1k6-U4xs5VAnT9CoiupjV5cJbGlrfc6Ns/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1k6-U4xs5VAnT9CoiupjV5cJbGlrfc6Ns/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1k6-U4xs5VAnT9CoiupjV5cJbGlrfc6Ns/view?usp=sharing" target="_blank" rel="nofollow noopener">20Gy 24.01.2020(0.25 mm)_Batch_2_OSC-TV.vff</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
