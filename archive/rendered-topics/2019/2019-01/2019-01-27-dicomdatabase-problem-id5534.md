---
topic_id: 5534
title: "Dicomdatabase Problem"
date: 2019-01-27
url: https://discourse.slicer.org/t/5534
---

# DICOMDatabase problem

**Topic ID**: 5534
**Date**: 2019-01-27
**URL**: https://discourse.slicer.org/t/dicomdatabase-problem/5534

---

## Post #1 by @javier_roman (2019-01-27 22:22 UTC)

<p>Hello.<br>
Really sorry, but I am “really brand new” in slicer.<br>
I can’t fix this problem and I need help to continue<br>
Thanks,<br>
Javier</p>
<p>“/Users/jotaerre/Documents/SlicerDICOMDatabase/ctkDICOM.sql” cannot be used.  Directory is not empty and not an existing DICOM database.<br>
Please pick a different database directory using the LocalDatabase button in the DICOM Browser<br>
[DEBUG][Qt] 27.01.2019 18:35:55 [] (unknown:0) - Switch to module:  “DICOM”<br>
[CRITICAL][Stream] 27.01.2019 18:35:55 [] (unknown:0) - The database file path “/Users/jotaerre/Documents/SlicerDICOMDatabase/ctkDICOM.sql” cannot be used.  Directory is not empty and not an existing DICOM database.</p>

---

## Post #2 by @lassoan (2019-01-27 22:37 UTC)

<p>You need to pick a different database directory using the LocalDatabase button in the DICOM Browser. The directory must be empty and writeable.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb5b239fe7b2791d71d312af0c5b14f70cdddabd.png" data-download-href="/uploads/short-url/xA3t9QfRU5PkbWkWn8uem3ReGJL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb5b239fe7b2791d71d312af0c5b14f70cdddabd_2_690x418.png" alt="image" data-base62-sha1="xA3t9QfRU5PkbWkWn8uem3ReGJL" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb5b239fe7b2791d71d312af0c5b14f70cdddabd_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb5b239fe7b2791d71d312af0c5b14f70cdddabd_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb5b239fe7b2791d71d312af0c5b14f70cdddabd_2_1380x836.png 2x" data-dominant-color="DFDEE4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2119×1286 439 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @javier_roman (2019-01-27 23:14 UTC)

<p>Thanks Andras<br>
Problem solved with your help!<br>
Great support with the screenshot<br>
Best Regards<br>
Javier</p>

---
