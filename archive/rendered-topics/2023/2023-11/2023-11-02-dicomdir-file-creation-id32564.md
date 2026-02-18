# DICOMDIR file creation

**Topic ID**: 32564
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/dicomdir-file-creation/32564

---

## Post #1 by @Gonzalo_Rojas_Costa (2023-11-02 18:40 UTC)

<p>Hi:<br>
The option “Create a DICOM Series” creates DICOM slices in a specified folder, but it lacks DICOMDIR file. How can I create it?</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @pieper (2023-11-02 18:43 UTC)

<p>We don’t tend to use DICOMDIR files in Slicer since they are often out of sync with the data on disk (they are mainly used with CDs and DVDs).</p>
<p>You can use other tools to make a DICOMDIR though:</p>
<p><a href="https://support.dcmtk.org/docs-snapshot/dcmmkdir.html" class="onebox" target="_blank" rel="noopener">https://support.dcmtk.org/docs-snapshot/dcmmkdir.html</a></p>

---
