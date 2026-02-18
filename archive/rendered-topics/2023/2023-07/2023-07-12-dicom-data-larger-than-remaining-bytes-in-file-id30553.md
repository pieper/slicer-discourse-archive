# DICOM data larger than remaining bytes in file

**Topic ID**: 30553
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/dicom-data-larger-than-remaining-bytes-in-file/30553

---

## Post #1 by @FunctionalDoc (2023-07-12 14:49 UTC)

<p>Loading MRI DICOM data from a disc drive physically connected to computer into a directory physically housed on the computer.  The Load DICOM module will try to parse all the individual files in the main file, but nothing is added to the DICOM directory after completion.  In the log file, the following is repeated for each image file in the larger main file:<br>
[CRITICAL][Stream] 12.07.2023 10:29:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - E: DcmElement: Unknown Tag &amp; Data (8030,0906) larger (2252899882) than remaining bytes in file<br>
[DEBUG][Qt] 12.07.2023 10:29:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not load  “D:/0561/0565/056624”<br>
DCMTK says:  I/O suspension or premature end of stream<br>
[WARNING][Qt] 12.07.2023 10:29:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not read DICOM file:D:/0561/0565/056624</p>
<p>Is this an issue with the data itself (e.g. file naming convention), or a problem on the Slicer end?</p>

---

## Post #2 by @lassoan (2023-07-12 14:54 UTC)

<p>The error message indicates that the DICOM file is corrupted. The (8030, 0906) tag has even group number, which means it is a standard tag, but I don’t think that such tag exists. Where is this DICOM file from?</p>

---

## Post #3 by @FunctionalDoc (2023-07-12 16:11 UTC)

<p>Thanks!  The DICOM file is from an CD burned at my institutions film library.  It comes on the disc with a preloaded DICOM viewer.  I can view the images using the viewer without a problem.  The disc states that it is DICOM encrypted.  Your question prompted me to dig in the view to find a way to export a decrypted file, which I found.  I suspect that the errors were the result of the encryption on the disc.  I have exported a decrypted file to the computer, and now Slicer is recognizing it.</p>

---
