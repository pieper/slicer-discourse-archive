# How to export multiple volumes and a RTSTRUCT into DICOM from one study

**Topic ID**: 9746
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/how-to-export-multiple-volumes-and-a-rtstruct-into-dicom-from-one-study/9746

---

## Post #1 by @TingtingYu (2020-01-09 02:34 UTC)

<p>Dear Slicer Developers,</p>
<p>I want to export 3 volumes and one RTSTUCT in DICOM at the same time. Below are my steps,</p>
<ol>
<li>I put them under one study and choose export to DICOM…</li>
<li>For export type, I choose RT (48%, 4 series) (DicomRtImportExportPlugin)</li>
</ol>
<p>However, when I check exported files, it has two folders. One folder only contains the DICOM files for one volume. Another folder only has one DICOM file, which is RTSTRUCT. DICOM files for two volumes are missing. May I know which step am I missing?</p>
<p>Best,<br>
Tingting</p>

---

## Post #2 by @cpinter (2020-01-09 10:31 UTC)

<p>Currently only exporting a DICOM-RT study containing one volume, structure set, and dose is supported. If you want to have multiple structure sets, then you can either merge the three segmentations into one, or export three studies. The only disadvantage of the latter case is that you will have redundant volumes, besides having to do three export steps.</p>

---

## Post #3 by @TingtingYu (2020-01-10 03:26 UTC)

<p>Got it. Thank you.</p>
<p>Best,<br>
Tingting</p>

---
