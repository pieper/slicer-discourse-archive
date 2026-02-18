# Loading CT 3d DICOM files-

**Topic ID**: 5185
**Date**: 2018-12-24
**URL**: https://discourse.slicer.org/t/loading-ct-3d-dicom-files/5185

---

## Post #1 by @gptruncus (2018-12-24 21:26 UTC)

<p>I have same issue as others with loading a set of DICOM files from a CT from Osirix. they are in a folder with image numbered files. Files seem to be either saved as .dcm or just as text files with file type “file” from Osirix.</p>
<p>Trying to Load from DICOM browser I get same as others have noted here:<br>
"Could not read scalar volume using DCMTK approach. Error is FileFormatError<br>
Could not load: 5580: Greg as a scalar volume. "<br>
Advanced states: Reference image in series does not contain geometry information.</p>
<p>Other imaging has worked. Am I saving files incorrectly?</p>

---

## Post #3 by @lassoan (2018-12-27 06:35 UTC)

<p>“FileFormatError” indicates that the created file might be invalid, but we would need an example file to confirm. Could you please export one of the public sample data sets, upload the generated files to dropbox/onedrive/google drive, and post the link here so that we can investigate?</p>

---
