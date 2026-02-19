---
topic_id: 12084
title: "Dicom Segmentation Import Problem On Windows"
date: 2020-06-18
url: https://discourse.slicer.org/t/12084
---

# DICOM segmentation import problem on Windows

**Topic ID**: 12084
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/dicom-segmentation-import-problem-on-windows/12084

---

## Post #1 by @laurenz (2020-06-18 02:49 UTC)

<p>I am trying to view DICOM segmentations on slicer as an overlay on PET and CT images. The DICOM segmentations won’t load. I have tried uninstalling and reinstalling the extensions one by one as well as all at once. The PET and CT images both load with no problems.</p>
<p>Slicer Version: 4.10.2<br>
Operating System: Windows 10<br>
Extensions that are causing the error messages: PETDICOMExtension, SlicerRT, LongitudinalPETCT<br>
Error Message when Slicer loads: DLL load failed: The specified module could not be found.</p>

---

## Post #2 by @fedorov (2020-06-18 02:54 UTC)

<aside class="quote no-group" data-username="laurenz" data-post="1" data-topic="12084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/bc79bd/48.png" class="avatar"> laurenz:</div>
<blockquote>
<p>The DICOM segmentations won’t load.</p>
</blockquote>
</aside>
<p>When you say “DICOM segmentations” - what is the modality that shows up in the series list? Does it say “SEG” for the series you are trying to load in the DICOM browser? There are many ways how a segmentation could be saved in a DICOM file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12a249661769b4d31665018e728f8472db02ffd7.png" data-download-href="/uploads/short-url/2EQi71n0xqHoCkpAne5zZs1I4ED.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12a249661769b4d31665018e728f8472db02ffd7_2_690x222.png" alt="image" data-base62-sha1="2EQi71n0xqHoCkpAne5zZs1I4ED" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12a249661769b4d31665018e728f8472db02ffd7_2_690x222.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12a249661769b4d31665018e728f8472db02ffd7_2_1035x333.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12a249661769b4d31665018e728f8472db02ffd7.png 2x" data-dominant-color="C9D9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1183×381 56.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What happens when they don’t load?</p>
<aside class="quote no-group" data-username="laurenz" data-post="1" data-topic="12084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/bc79bd/48.png" class="avatar"> laurenz:</div>
<blockquote>
<p>I have tried uninstalling and reinstalling the extensions</p>
</blockquote>
</aside>
<p>Which extensions did you install?</p>
<p>If it is a DICOM Segmentation image object that you are trying to load, you will need to install “Quantitative Reporting” extension, and also all of the dependencies it will prompt you to install.</p>

---

## Post #3 by @laurenz (2020-06-18 16:32 UTC)

<p>When I try to load it, it is labelled as “SEG”.</p>
<p>When they don’t load, multiple error messages pop up. “Warning: Plugin failed: DICOMPETSUVPlugin”,<br>
“Warning: Plugin failed: DICOMSroImportPlugin” and “Warning: Plugin failed: DICOMRTImportExportPlugin”</p>
<p>I have DCMQI, PETDICOMExtension, LongitudinalPETCT, SlicerRT, QuantitativeReporting, SlicerDevelopmentToolbox, SlicerRadiomics</p>
<p>When they don’t load, the PET and CT will load but the DICOM segmentations will not and the error box appears that says they are unable to load as a DICOM segmentation.</p>

---

## Post #4 by @fedorov (2020-06-18 17:10 UTC)

<p>Can you share the error log?</p>
<p>You can get it in “Help &gt; Report a bug”.</p>

---

## Post #5 by @laurenz (2020-06-19 16:52 UTC)

<p>The error log is extremely long. Cannot load library is repeated throughout</p>
<p>Cannot load library C:\Users\laure\AppData\Roaming\NA-MIC\Extensions-28257\SlicerRT\lib\Slicer-4.10\qt-loadable-modules\qSlicerDoseAccumulationModule.dll: The specified module could not be found.</p>
<p>DLL load failed: The specified module could not be found.</p>

---

## Post #6 by @lassoan (2020-06-19 22:01 UTC)

<p>Maybe your extension installation is incomplete. Reinstall your extensions. Make sure you wait for the “Restart” button to appear (even if it takes several minutes) and click that (do not click “Close”). If it does not help then send us the log (upload somewhere and post just the download link here).</p>

---

## Post #7 by @lassoan (2020-06-20 04:08 UTC)

<p>You might run into the error described <a href="https://discourse.slicer.org/t/slicerrt-dicom-rt-import-issue/11881/2">here</a>. Installing Visual Studio redistributables may fix the problem.</p>

---

## Post #8 by @laurenz (2020-06-23 01:50 UTC)

<p>After installing the Visual Studio redistributables the segmentations loaded and all extensions seemed to be working! Thank you!</p>

---

## Post #9 by @lassoan (2020-06-23 02:12 UTC)

<p>Thank you, this is very useful feedback. I’ve filed a bug report <a href="https://github.com/Slicer/Slicer/issues/5001">here</a>.</p>

---
