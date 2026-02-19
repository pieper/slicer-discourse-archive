---
topic_id: 38104
title: "Creating A Dicom From A Jpeg"
date: 2024-08-28
url: https://discourse.slicer.org/t/38104
---

# Creating a DICOM from a JPEG

**Topic ID**: 38104
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/creating-a-dicom-from-a-jpeg/38104

---

## Post #1 by @vedantr09 (2024-08-28 21:29 UTC)

<p>Hi,<br>
Is there a way to create a DICOM file from a JPEG image if I have all the header information. For example, I have a X-ray image with imaging metadata and I would like to create a DICOM with the metadata as tags.<br>
Any help would be appreciated!</p>

---

## Post #2 by @pieper (2024-08-29 00:03 UTC)

<p>You can load it in Slicer and then export as dicom.</p>
<p>Or it might be just as easy to use a tool like this:</p>
<p><a href="https://manpages.debian.org/experimental/dcmtk/img2dcm.1.en.html" class="onebox" target="_blank" rel="noopener">https://manpages.debian.org/experimental/dcmtk/img2dcm.1.en.html</a></p>

---
