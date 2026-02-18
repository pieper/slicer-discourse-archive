# Cannot view ultrasound DICOM files

**Topic ID**: 41595
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/cannot-view-ultrasound-dicom-files/41595

---

## Post #1 by @pat_rek (2025-02-07 02:27 UTC)

<p>Hi. I can’t view any .DCM files when I load it using “Import DICOM files”. Folders(with DCM files) are the only thing that I see but not the .DCM<br>
. I also tried using the latest preview release, same thing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade.jpeg" data-download-href="/uploads/short-url/29PgRgIigR8Ywzh86vbQsdQMXZc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_690x366.jpeg" alt="image" data-base62-sha1="29PgRgIigR8Ywzh86vbQsdQMXZc" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_1380x732.jpeg 2x" data-dominant-color="9C99AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1905×1012 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-02-09 23:19 UTC)

<p>Unfortunately, ultrasound imaging vendors save 3D/4D ultrasound in a proprietary format that only their own software can read. There are only a few exceptions - see more information in the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">documentation of SlicerHeart extension</a>.</p>
<p>Please ask for 3D image export feature from the company representative. Most likely they will not help you, but at least you make them aware that their users want this feature.</p>

---
