---
topic_id: 41549
title: "Dicom File Doesnt Show A 3D Model"
date: 2025-02-07
url: https://discourse.slicer.org/t/41549
---

# DICOM file doesn't show a 3D Model

**Topic ID**: 41549
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/dicom-file-doesnt-show-a-3d-model/41549

---

## Post #1 by @pat_rek (2025-02-07 11:54 UTC)

<p>Hi I dont know what to do anymore. Does anyone know how to tackle this? Version is 5.8.0</p>
<p>So I cant open or see a DCM file when I click “Import DICOM file” under DCM module. All the DICOM files for some reason disappears and I only can see folder. Opening folders( that I know have DCM files ) becomes empty.</p>
<p>Here are samples:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05942ad6390d06b201512fb9fca607ac17609c52.png" data-download-href="/uploads/short-url/NlPJpNKPLL8oiJfdNbLv2s9bUu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05942ad6390d06b201512fb9fca607ac17609c52_2_690x363.png" alt="image" data-base62-sha1="NlPJpNKPLL8oiJfdNbLv2s9bUu" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05942ad6390d06b201512fb9fca607ac17609c52_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05942ad6390d06b201512fb9fca607ac17609c52_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05942ad6390d06b201512fb9fca607ac17609c52_2_1380x726.png 2x" data-dominant-color="9B99A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1010 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d645c9c7a49925b8ebaaa846602c7fb62b1466e6.jpeg" data-download-href="/uploads/short-url/uzxHlLrhXx3WGNtzB7ei9Zd0gOq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d645c9c7a49925b8ebaaa846602c7fb62b1466e6_2_690x360.jpeg" alt="image" data-base62-sha1="uzxHlLrhXx3WGNtzB7ei9Zd0gOq" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d645c9c7a49925b8ebaaa846602c7fb62b1466e6_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d645c9c7a49925b8ebaaa846602c7fb62b1466e6_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d645c9c7a49925b8ebaaa846602c7fb62b1466e6_2_1380x720.jpeg 2x" data-dominant-color="9998A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1002 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade.jpeg" data-download-href="/uploads/short-url/29PgRgIigR8Ywzh86vbQsdQMXZc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_690x366.jpeg" alt="image" data-base62-sha1="29PgRgIigR8Ywzh86vbQsdQMXZc" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f20b93a0e4fe23f98657e1bc5a749c08388fade_2_1380x732.jpeg 2x" data-dominant-color="9C99AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1905×1012 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-02-09 19:30 UTC)

<p>Those are screen captures of a 3D reconstruction done in other software, so you can’t use those for further 3D processing.  If the other images in the study didn’t load they are probably in a format that Slicer doesn’t support (there are lots of ultrasound machines with proprietary data formats unfortunately).</p>

---
