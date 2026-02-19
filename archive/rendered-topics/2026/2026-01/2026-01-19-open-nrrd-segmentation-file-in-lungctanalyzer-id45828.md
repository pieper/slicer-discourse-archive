---
topic_id: 45828
title: "Open Nrrd Segmentation File In Lungctanalyzer"
date: 2026-01-19
url: https://discourse.slicer.org/t/45828
---

# open nrrd segmentation file in lungctanalyzer

**Topic ID**: 45828
**Date**: 2026-01-19
**URL**: https://discourse.slicer.org/t/open-nrrd-segmentation-file-in-lungctanalyzer/45828

---

## Post #1 by @Letizia_Saviozzi (2026-01-19 16:44 UTC)

<p>I apologize in advance for my very bad computer knowledge.</p>
<p>Operating system: Windows 11, 64 bit<br>
Slicer version: 5.10.0<br>
Expected behavior: A year ago I save some scenes (Slicer version 5.6.2), leaving them open in the segmentation: the scenes were saved, on a USB, like 2 nnrd file (including the segmentation), one png file and one “link” direct to that Slicer version.<br>
Actual behavior: Now I need to re-compute the results with the Lung CT Analyzer, modifying the thresholds, but I can’t open these nrrd files. Every time I try Slicer announces an error like so:</p>
<p>“ Slicer has caught an application error, please save your work and restart. If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: D:\D\S\S-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx:769:</p>
<p>ITK ERROR: NrrdImageIO(000001AC463953B0): Read: Error reading C:/Users/Letizia/Desktop/TESI/scene segmetazione aperte/roggia/roggia cpap/Lung segmentation.seg.nrrd:</p>
<p>[nrrd] nrrdLoad: trouble reading “C:/Users/Letizia/Desktop/TESI/scene segmetazione aperte/roggia/roggia cpap/Lung segmentation.seg.nrrd”</p>
<p>[nrrd] nrrdRead: trouble[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read:</p>
<p>[nrrd] _nrrdEncodingGzip_read: error reading from gzFile</p>
<p>[nrrd] _nrrdGzRead: data read error</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a></p>

---
