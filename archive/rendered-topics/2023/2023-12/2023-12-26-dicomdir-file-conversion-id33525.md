# DICOMDIR file conversion

**Topic ID**: 33525
**Date**: 2023-12-26
**URL**: https://discourse.slicer.org/t/dicomdir-file-conversion/33525

---

## Post #1 by @anamcastano (2023-12-26 19:17 UTC)

<p>Hi all<br>
Could anyone help me to manage with DICOMDIR instead of DICOM files to create NRRD, DWI and DTI? Is there any converter DICOMDIR to DICOM?<br>
Thanks in advance</p>

---

## Post #2 by @pieper (2023-12-26 19:26 UTC)

<aside class="quote no-group" data-username="anamcastano" data-post="1" data-topic="33525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/848f3c/48.png" class="avatar"> anamcastano:</div>
<blockquote>
<p>Is there any converter DICOMDIR to DICOM?</p>
</blockquote>
</aside>
<p>A DICOMDIR file is a kind of index into a directory hierarchy of DICOM files, so it doesn’t actually contain any image data.  While it can speed up access to files, say on a CDROM or DVD, we don’t rely on it in Slicer because it can be out of date with the actual files, say when they are copied from a DVD to a file system.  Instead, we suggest importing the directory into the local Slicer DICOM Database and processing the files.  For DWI, the SlicerDMRI extension provides tools.  Be aware that DWI representations in DICOM vary by manufacturer and model, so don’t be surprised if some file types are not supported or are challenging to work with.</p>

---
