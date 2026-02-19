---
topic_id: 5565
title: "Dicom Displaying Error In Slicer 4 8 It Only Displays Axial"
date: 2019-01-29
url: https://discourse.slicer.org/t/5565
---

# DICOM displaying error in Slicer 4.8: it only displays Axial planes

**Topic ID**: 5565
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/dicom-displaying-error-in-slicer-4-8-it-only-displays-axial-planes/5565

---

## Post #1 by @xmc2018_ucl (2019-01-29 17:14 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/798b74cacc7ad0e517ead9edc71a6ccff7dbe432.png" data-download-href="/uploads/short-url/hleyz12uQ0bxMvJAPWP5VlwdQrw.png?dl=1" title="display_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/798b74cacc7ad0e517ead9edc71a6ccff7dbe432_2_654x500.png" alt="display_error" data-base62-sha1="hleyz12uQ0bxMvJAPWP5VlwdQrw" width="654" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/798b74cacc7ad0e517ead9edc71a6ccff7dbe432_2_654x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/798b74cacc7ad0e517ead9edc71a6ccff7dbe432_2_981x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/798b74cacc7ad0e517ead9edc71a6ccff7dbe432.png 2x" data-dominant-color="373642"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">display_error</span><span class="informations">981×749 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi<br>
I am a new user of Slicer and it seems I can’t load DICOM image properly? It works for some cases but not for other cases, it keeps giving me display errors… it would be really appreciated if you could help me with it.</p>
<p>Best Regards<br>
Moucheng</p>

---

## Post #2 by @lassoan (2019-01-30 01:52 UTC)

<p>In simple cases, drag-and-dropping a single DICOM file works, you just need to make sure to uncheck the “single file” option in the Add data dialog (click “Show options” to see this option).</p>
<p>In general, to be able to load any kind of DICOM data: Drag-and-drop the parent folder (that contain all the image slices) into the application window and choose to import the files into Slicer’s DICOM database. Then you can load images from the database using DICOM browser.</p>

---
