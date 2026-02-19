---
topic_id: 28910
title: "Patched Dicom Will Not Open As Image Sequence"
date: 2023-04-14
url: https://discourse.slicer.org/t/28910
---

# Patched DICOM will not open as Image Sequence

**Topic ID**: 28910
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/patched-dicom-will-not-open-as-image-sequence/28910

---

## Post #1 by @Tannadrake (2023-04-14 11:36 UTC)

<p>I am attempting to open a DICOM image that required patching. I used the DICOM Patcher module, then when I attempt to open an imaging sequence it gives me an error saying it cannot open as an Image Sequence.</p>
<p>This is the log file content. Any assistance is appreciated.</p>
<p>[ERROR][Python] 14.04.2023 07:28:50 [Python] (C:\Users\amyta\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\DICOMLib\DICOMUtils.py:794) - DICOM plugin failed to load ‘4001: MR MPRAGE’ as a ‘Image sequence’.<br>
Traceback (most recent call last):<br>
File “C:\Users\amyta\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 790, in loadLoadables<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Users/amyta/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMImageSequencePlugin.py”, line 354, in load<br>
imageData, ijkToRas = self.loadImageData(filePath, loadable.grayscale, tempFrameVolume)<br>
File “C:/Users/amyta/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/lib/Slicer-5.2/qt-scripted-modules/DICOMImageSequencePlugin.py”, line 231, in loadImageData<br>
f"Could not read image {loadable.name} from file {filePath}. Error is: {errorString}")<br>
NameError: name ‘loadable’ is not defined<br>
[WARNING][Python] 14.04.2023 07:28:50 [Python] (C:\Users\amyta\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py:2736) - Could not load: 4001: MR MPRAGE as a Image sequence</p>

---

## Post #2 by @pieper (2023-04-14 12:14 UTC)

<p>The map from dicom to sequences is complex due to the wide variety of acquisition types and the ways vendors choose to encode them.  Your best bet is to study the dicom headers in terms of what you know about the images and if needed extend the dicom patcher so that there’s a recognized delimiter between sequence items that will map to Slicer data structures.  The delimiter could be time, acquisition parameter, physiological signal, etc.  It’s generally straightforward to solve any specific case, but not easy to solve the general problem.</p>

---

## Post #3 by @Tannadrake (2023-04-14 12:17 UTC)

<p>I am a clinician and have no programing experience. If I provide my specific image data could you help me further? It is animal data, so not protected health information</p>

---

## Post #4 by @pieper (2023-04-14 12:21 UTC)

<p>I can’t promise to solve the problem for you myself, but yes, if you post the data and describe what you are trying to accomplish then I or someone with the right experience might be able to help out.  In general yes, we want Slicer to be compatible with as many scenarios as possible and having example data is critical.  Often with human data we as developers can never see the real data so things may stall.  But with animal data sharing the images and acquisition context can really move things forward.</p>

---

## Post #5 by @Tannadrake (2023-04-14 13:28 UTC)

<p>Here is a link to one of the studies.<br>
I am trying to open the MPRage sequence in slicer so that I can segment the lateral ventricles to assess volume and surface area for a research study.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://onedrive.live.com/redir?resid=6D4A380DBC8A33EB%2125526&amp;authkey=%21AIOyiYMnRrI88RM&amp;ithint=folder&amp;e=0JmUwR">
  <header class="source">

      <a href="https://onedrive.live.com/redir?resid=6D4A380DBC8A33EB%2125526&amp;authkey=%21AIOyiYMnRrI88RM&amp;ithint=folder&amp;e=0JmUwR" target="_blank" rel="noopener nofollow ugc">onedrive.live.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://p.sfx.ms/icons/v2/Large/NonEmptyDocumentFolder.png" class="thumbnail onebox-avatar" width="96" height="96">

<h3><a href="https://onedrive.live.com/redir?resid=6D4A380DBC8A33EB%2125526&amp;authkey=%21AIOyiYMnRrI88RM&amp;ithint=folder&amp;e=0JmUwR" target="_blank" rel="noopener nofollow ugc">4502907- March 6 2023</a></h3>

  <p>Folder</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @pieper (2023-04-14 14:00 UTC)

<p>Thanks for sharing, that makes it easier to see what is going on.  These are not the original scan images, but some kind of post-processed result (secondary capture) and reports (structured reports) that are not compatible with Slicer.  Probably you can go back to the scanner and pull out the original images.</p>

---

## Post #7 by @issakomi (2023-04-14 14:43 UTC)

<p>If this helps, here <a href="https://drive.google.com/file/d/1peQ5Je5s3Z3TLPy4ut517HA_xPm6jhKA/view?usp=sharing" rel="noopener nofollow ugc">MRPAGE</a> series in Nrrd format. Slicer (5.3.0-2023-04-11) doesn’t see all series in the folder.</p>

---

## Post #8 by @pieper (2023-04-14 18:51 UTC)

<aside class="quote no-group" data-username="issakomi" data-post="7" data-topic="28910">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9e5f3/48.png" class="avatar"> issakomi:</div>
<blockquote>
<p>Slicer (5.3.0-2023-04-11) doesn’t see all series in the folder.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/issakomi">@issakomi</a> - did you use another tool that recognized additional files?  Can you describe what’s different?</p>

---

## Post #9 by @Tannadrake (2023-04-14 23:16 UTC)

<p>That helped! I was able to segment the images. How did you do that?</p>

---

## Post #10 by @issakomi (2023-04-14 23:17 UTC)

<p>Probably the images were damaged during compression (?).<br>
<code>0x0008,0x2111 "Derivation Description" Compress Pegasus JPEG Lossless</code><br>
PixelData looks strange, there is <em>Basic Offset Table</em> and <strong>2</strong> fragments for single slice. Should be <em>Basic Offset Table</em> and 1 fragment (usually). Maybe duplicated. Many viewers skip these files, not only Slicer. Seems to be possible to recover.</p>

---

## Post #11 by @issakomi (2023-04-14 23:28 UTC)

<p><em>dcmcjpeg</em> detected</p>
<p>W: DcmSequenceOfItems: Reached end of stream before the end of sequence PixelData (7fe0,0010)<br>
F: Sequence Delimitation Item missing: reading file: 34123105</p>
<p>BTW. If you drop single file (not using DICOM database import), it opens in Slicer too. It is not a big help, but FYI. Bare ITK’s GDCM IO seems to work.</p>

---

## Post #12 by @pieper (2023-04-15 14:54 UTC)

<p>Nice detective work <a class="mention" href="/u/issakomi">@issakomi</a> <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=12" title=":clap:" class="emoji" alt=":clap:" loading="lazy" width="20" height="20"></p>
<p><a class="mention" href="/u/tannadrake">@Tannadrake</a> the images appear to have come from a Siemens syngo.via system.  If you or your colleagues used a standard feature of the machine you should report this non-conformance to Siemens and ask the to fix it.</p>

---

## Post #13 by @Tannadrake (2023-04-26 14:51 UTC)

<p>Thank you. Will do. In the end we went back to the scanner and pulled the original images onto a flash drive instead of CD which resolved our issue.</p>

---
