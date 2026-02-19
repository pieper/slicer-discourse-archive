---
topic_id: 29664
title: "Rtstruct Display In Slice View"
date: 2023-05-26
url: https://discourse.slicer.org/t/29664
---

# RTstruct display in Slice View

**Topic ID**: 29664
**Date**: 2023-05-26
**URL**: https://discourse.slicer.org/t/rtstruct-display-in-slice-view/29664

---

## Post #1 by @ma1282029525 (2023-05-26 08:35 UTC)

<p>I used vtkPlanarContourToClosedSurfaceConversionRule in slicerRT to convert RTstruct to closed surface, but the display effect in my program is different from that in 3Dslicer? I want to know why, in 3DSlicer, the effect appears to be a closed surface sliced like the original image, while in my program, the effect appears to be a simple projection.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34d1c8c32ed42a471ad00850ce0ec845c1bef221.png" data-download-href="/uploads/short-url/7xghViviXymRLhGO4EU0ACs5Te9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34d1c8c32ed42a471ad00850ce0ec845c1bef221_2_468x499.png" alt="image" data-base62-sha1="7xghViviXymRLhGO4EU0ACs5Te9" width="468" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34d1c8c32ed42a471ad00850ce0ec845c1bef221_2_468x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34d1c8c32ed42a471ad00850ce0ec845c1bef221_2_702x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34d1c8c32ed42a471ad00850ce0ec845c1bef221.png 2x" data-dominant-color="051202"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">851×908 80.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11c18edddbfa605c903123b0e778cd82b7847491.jpeg" data-download-href="/uploads/short-url/2x4Oq9GLBAB8NdbGaZuImaN7jln.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11c18edddbfa605c903123b0e778cd82b7847491_2_690x454.jpeg" alt="image" data-base62-sha1="2x4Oq9GLBAB8NdbGaZuImaN7jln" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11c18edddbfa605c903123b0e778cd82b7847491_2_690x454.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11c18edddbfa605c903123b0e778cd82b7847491_2_1035x681.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11c18edddbfa605c903123b0e778cd82b7847491_2_1380x908.jpeg 2x" data-dominant-color="31463B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1665×1096 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I achieve the same display effect as in 3Dslicer？</p>

---

## Post #2 by @ma1282029525 (2023-05-26 09:17 UTC)

<p>Do I need to execute vtkimagerereslice on polydata？</p>

---
