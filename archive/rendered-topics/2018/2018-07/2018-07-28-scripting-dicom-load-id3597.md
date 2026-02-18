# Scripting Dicom load

**Topic ID**: 3597
**Date**: 2018-07-28
**URL**: https://discourse.slicer.org/t/scripting-dicom-load/3597

---

## Post #1 by @bphilip (2018-07-28 01:42 UTC)

<p>Operating system: Windows 10</p>
<p>Slicer version: 4.8.1</p>
<p>Expected behavior/Goal: Load DICOMS --&gt; Show Scene --&gt; Rigid Register them --&gt; Export as nifti’s to an output dir</p>
<p>Programming Level: Beginner</p>
<p>Actual behavior: Imported DICOMLib, used importDicom function - got a True!</p>
<p>Problem: Scene didn’t change? Also lost on how to programmatically perform affine registration. (I see the gui and can do this using that. But I have a lot of images and want to just make it so I can for loop through the directory of images). I understand the for looping through dir part, I am lost on the getting Slicer to do its part.</p>

---

## Post #2 by @lassoan (2018-07-28 16:38 UTC)

<p>DICOM importing and loading are two separate steps. Import step: add files into Slicer’s DICOM database. Loading step: load data from DICOM database to the scene.</p>
<p>Details on how to do each step has been discussed before in several topics, such as <a href="https://discourse.slicer.org/t/load-dicom-series-using-python/3257/3">Load DICOM series using python</a>. If you cannot find answer to some questions in any of the topics, examples, or documentation then let us know.</p>

---
