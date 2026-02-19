---
topic_id: 10725
title: "Slicer Constantly Crashing Sometimes During Save"
date: 2020-03-18
url: https://discourse.slicer.org/t/10725
---

# Slicer constantly crashing, sometimes during save. 

**Topic ID**: 10725
**Date**: 2020-03-18
**URL**: https://discourse.slicer.org/t/slicer-constantly-crashing-sometimes-during-save/10725

---

## Post #1 by @alexjamesmajor (2020-03-18 02:09 UTC)

<p>Slicer constantly crashing, sometimes during save. Sometimes, depsite a non-crash save, saved file will not load. I’ve attached two error messages that occurred during my attempt to load:</p>
<p>Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35</p>
<p>vtkArchive Error: Unzip error: Inconsistent uncompressed size: 0 in central directory, 282334 in local header Error</p>
<p>Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35</p>
<p>vtkArchive Error: Unzip error: Truncated ZIP file data Error</p>
<p>…</p>
<p>could not find mrml file in archive</p>

---

## Post #2 by @lassoan (2020-03-18 02:13 UTC)

<p>Thousands of users test Slicer very extensively and we are not aware of any issues that would cause Slicer to crash - other than when you run out of memory.</p>
<p>Make sure the available memory (physical RAM + virtual memory size that you set in your system settings) is at least 10x larger than the size of the data set you load.</p>

---

## Post #3 by @alexjamesmajor (2020-03-18 19:24 UTC)

<p>Hi Andras,</p>
<p>Thanks for your quick reply. I am currently working with 128 GB RAM on a ~50 MB file. Virtual memory is automatically set, currently ~20 GB. Working in Slicer v 4.11.0-2020-03-15 (I was having more problems with v4.10).</p>
<p>I changed the Settings&gt;Cache settings to 10,000 MB Cache size and 200 MB Cache free buffer. Changing this seemed to reduce crashing during saving of files.</p>
<p>However, I’m still having this issue: I will save a file, Close Scene, and attempt to Load that .mrb, and nothing will load. I will get the following three error messages:</p>
<p>(1) Debug Qt<br>
Unpacking bundle  “C:/Users/Alex James Major/Documents/SlicerSavedFiles/Lucky/Lucky_02252020_V4 Origin_laminar locations_rotated back to stereotax_specific areas_2.mrb”  to  “C:/Users/Alex James Major/AppData/Local/Temp/__BundleLoadTemp2020-03-18_15+21+16.480”</p>
<p>(2) Info VTK<br>
Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35<br>
vtkArchive Error: Unzip error: Inconsistent uncompressed size: 0 in central directory, 312279 in local header Error</p>
<p>Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35<br>
vtkArchive Error: Unzip error: Truncated ZIP file data Error</p>
<p>(3) Error VTK<br>
could not find mrml file in archive</p>
<p>Any information on how to proceed would be greatly appreciated. Do I need to adjust “GPU memory size”?</p>
<p>Thanks for your time,</p>
<p>Alex</p>

---

## Post #4 by @lassoan (2020-03-18 19:44 UTC)

<p>Can you share an mrb file that you cannot load (upload somewhere and post the link here)?</p>

---

## Post #5 by @alexjamesmajor (2020-03-18 20:02 UTC)

<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://easyupload.io/img/favicon/android-icon-192x192.png" class="site-icon" width="16" height="16">
      <a href="https://easyupload.io/3ngco5" target="_blank" rel="nofollow noopener">easyupload.io</a>
  </header>
  <article class="onebox-body">
    <img src="https://easyupload.io/img/logo.jpg" class="thumbnail onebox-avatar" width="24" height="24">

<h3><a href="https://easyupload.io/3ngco5" target="_blank" rel="nofollow noopener">easyupload.io</a></h3>

<p>easyupload.io</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>password: slicer</p>

---

## Post #6 by @lassoan (2020-03-18 22:07 UTC)

<p>The file is corrupted (cannot even be unzipped).</p>
<p>Did you try to save the mrb file to a network drive, external drive, or some other special storage space?</p>
<p>Do you have plenty of space in your temporary folder (menu: Edit / Application settings / Modules / Temporary directory)?</p>

---

## Post #7 by @alexjamesmajor (2020-03-18 22:45 UTC)

<p>I’m saving to a folder in my C drive, which has over 220 GB of space. Temporary directory is also in C drive.</p>

---

## Post #8 by @lassoan (2020-03-18 22:56 UTC)

<p>Can you reproduce the problem? Can you describe those steps?</p>

---

## Post #9 by @alexjamesmajor (2020-03-18 23:08 UTC)

<p>The next time this problem occurs I will try to copy/paste the log messages during the save. Thanks.</p>

---

## Post #10 by @lassoan (2020-03-18 23:09 UTC)

<p>You can find logs of the last 10 sessions in menu: Help / Report a bug.</p>

---

## Post #11 by @alexjamesmajor (2020-10-27 18:43 UTC)

<p>Hi Andras,</p>
<p>Thank you for your help, this issue is resolved.</p>
<p>Alex</p>

---
