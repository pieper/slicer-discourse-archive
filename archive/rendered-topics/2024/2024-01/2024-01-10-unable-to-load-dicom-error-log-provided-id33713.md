# unable to load dicom -- error log provided

**Topic ID**: 33713
**Date**: 2024-01-10
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-error-log-provided/33713

---

## Post #1 by @wc2023 (2024-01-10 04:29 UTC)

<p>Operating system: Mac OS Ventura 13.6.1<br>
Slicer version: 5.6.1</p>
<p>In advance, thanks for any assistance/suggestions.  I am unable to load diccom.  Attached is first page of error log.  Perhaps someone w/ background in these matters would be able to sift through the information and identify potential issue.  First page below, able to send more if needed. Thank you.</p>
<p>Switch to module: “DICOM”</p>
<p>2024-01-09 08:30:39.525 Slicer[20516:8552159] +[CATransaction synchronize] called within transaction</p>
<p>E: DcmSequenceOfItems: Parse error in sequence (7fe0,0010), found (4fff,51ff) instead of sequence delimiter (fffe,e0dd)</p>
<p>Could not load “/Volumes/NS-Projects/CIREN/Belly and Mesentery Stuff/C1-2020-004/20203C1004_V1_O1_CTCP/IM-0002-0700.dcm”</p>
<p>DCMTK says: Sequence Delimitation Item missing</p>
<p>Could not read DICOM file:/Volumes/NS-Projects/CIREN/Belly and Mesentery Stuff//C1-2020-004/20203C1004_V1_O1_CTCP/IM-0002-0700.dcm</p>

---

## Post #2 by @pieper (2024-01-10 15:51 UTC)

<p>Looks like the files are non-conformant or possibly corrupted.  You could try the DICOMPatcher module.  Also read the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">DICOM FAQ</a> for suggestions.</p>

---
