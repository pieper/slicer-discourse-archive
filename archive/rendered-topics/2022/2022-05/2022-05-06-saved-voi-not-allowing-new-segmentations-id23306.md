---
topic_id: 23306
title: "Saved Voi Not Allowing New Segmentations"
date: 2022-05-06
url: https://discourse.slicer.org/t/23306
---

# saved VOI not allowing new segmentations

**Topic ID**: 23306
**Date**: 2022-05-06
**URL**: https://discourse.slicer.org/t/saved-voi-not-allowing-new-segmentations/23306

---

## Post #1 by @artycho (2022-05-06 12:50 UTC)

<p>Operating system: windwos<br>
Slicer version: 4.11<br>
Expected behavior: saved ROI should allow new segmentations<br>
Actual behavior: saved ROI only allows new segmentations within the area within the saved ROI.</p>
<p>I have drawn a VOI on the liver of a patient. I then exported the VOI as VOI.nfti (clicked on the segmentations, export to files), during which i included the reference volume (which was the CT),<br>
I then closed the slicer, reopened the CT, and re-uploaded the VOI.nifti. the VOI registered well with the liver. However, when I added another segment to the VOI.nifti, I could only draw on the area of the liver (for example the spleen), but not in the lungs.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2543fca3d501b6df959625af49858545dd322829.jpeg" data-download-href="/uploads/short-url/5jFkjlEoi1N2ynYadItZyMBGioh.jpeg?dl=1" title="voi problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2543fca3d501b6df959625af49858545dd322829_2_690x305.jpeg" alt="voi problem" data-base62-sha1="5jFkjlEoi1N2ynYadItZyMBGioh" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2543fca3d501b6df959625af49858545dd322829_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2543fca3d501b6df959625af49858545dd322829_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2543fca3d501b6df959625af49858545dd322829_2_1380x610.jpeg 2x" data-dominant-color="999E9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">voi problem</span><span class="informations">1421×629 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Please help!</p>

---
