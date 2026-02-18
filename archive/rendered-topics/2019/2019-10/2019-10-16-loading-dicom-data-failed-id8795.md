# Loading DICOM data failed

**Topic ID**: 8795
**Date**: 2019-10-16
**URL**: https://discourse.slicer.org/t/loading-dicom-data-failed/8795

---

## Post #1 by @kuba_grepl (2019-10-16 05:12 UTC)

<p>Hello guys,<br>
after months of trouble-free use of Slicer3D 4.10.2 (Win10 Pro), I was surprised by error message this morning. I tried to load DICOM data  (CT and MR) as usual and loading failed. You can see the error message in the screenshot.<br>
Do you have any idea how to solve it? Thank you very much.<br>
Best regards from the heart of Europe. Kuba.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fc2a9a1f3f615f19c674768415edf31e3fcc4fd.jpeg" data-download-href="/uploads/short-url/mNiYNgfpU2GkjaGzGm8F6zTpHBj.jpeg?dl=1" title="V%C3%BDst%C5%99i%C5%BEek" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fc2a9a1f3f615f19c674768415edf31e3fcc4fd_2_690x452.jpeg" alt="V%C3%BDst%C5%99i%C5%BEek" data-base62-sha1="mNiYNgfpU2GkjaGzGm8F6zTpHBj" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fc2a9a1f3f615f19c674768415edf31e3fcc4fd_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fc2a9a1f3f615f19c674768415edf31e3fcc4fd_2_1035x678.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fc2a9a1f3f615f19c674768415edf31e3fcc4fd_2_1380x904.jpeg 2x" data-dominant-color="ECECF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">V%C3%BDst%C5%99i%C5%BEek</span><span class="informations">1444×946 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-10-16 05:16 UTC)

<p>Does it happen with all data sets that you are trying to load or only with certain ones?</p>
<p>How much disk space do you have on the drive where the Slicer DICOM database is located?</p>
<p>You may fix this by choosing a new empty folder for database location. You may also try the latest Slicer Preview Release, which has a greatly improved DICOM browser.</p>

---

## Post #3 by @kuba_grepl (2019-10-16 05:51 UTC)

<p>Thank you, Andras.<br>
The problem was that my allocated disk space was full.<br>
Have a nice day. Kuba.</p>

---
