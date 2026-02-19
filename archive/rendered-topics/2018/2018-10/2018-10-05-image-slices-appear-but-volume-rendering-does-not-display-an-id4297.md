---
topic_id: 4297
title: "Image Slices Appear But Volume Rendering Does Not Display An"
date: 2018-10-05
url: https://discourse.slicer.org/t/4297
---

# Image slices appear but volume rendering does not display anything

**Topic ID**: 4297
**Date**: 2018-10-05
**URL**: https://discourse.slicer.org/t/image-slices-appear-but-volume-rendering-does-not-display-anything/4297

---

## Post #1 by @hina (2018-10-05 13:46 UTC)

<p>From dicom data R,Y,G data are displayed as the attached picture.But volume rendering doesn’t work.Also R,Y,G’s slide bars don’t work,slice data don’t change.Will you please advice me how to make rendering. Thanks.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/749dea36e90a419d34a4d86ac9ad0e3035acd1c8.jpeg" data-download-href="/uploads/short-url/gDDIuMBRHHt4cDuTF7MQLWDO8Gs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/749dea36e90a419d34a4d86ac9ad0e3035acd1c8_2_690x388.jpeg" alt="image" data-base62-sha1="gDDIuMBRHHt4cDuTF7MQLWDO8Gs" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/749dea36e90a419d34a4d86ac9ad0e3035acd1c8_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/749dea36e90a419d34a4d86ac9ad0e3035acd1c8_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/749dea36e90a419d34a4d86ac9ad0e3035acd1c8_2_1380x776.jpeg 2x" data-dominant-color="B1B2BD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-10-05 14:11 UTC)

<p>It seems that you have loaded 3 orthogonal slices. Make sure you load a 3D data set, not individual slices. These page should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---
