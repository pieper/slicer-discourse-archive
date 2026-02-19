---
topic_id: 43921
title: "Threshold Segmentation Not Captures The Areas I Intended"
date: 2025-08-01
url: https://discourse.slicer.org/t/43921
---

# Threshold segmentation not captures the areas I intended

**Topic ID**: 43921
**Date**: 2025-08-01
**URL**: https://discourse.slicer.org/t/threshold-segmentation-not-captures-the-areas-i-intended/43921

---

## Post #1 by @mina.dehghan (2025-08-01 06:57 UTC)

<p>Hello,</p>
<p>I have a cubic shape of Al and Zn (High difference in density). Within the cubic there are some voids that I’m not able to capture them using the threshold segmentation for volume measurements. Is there a way I can make a segmentation selecting the voids all at once other than thresholding? Or is there a more accurate thresholding approach I can use?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8f0806600156314a8701143300ba9fdc550280a.jpeg" data-download-href="/uploads/short-url/zwdGsFYhr6Hra1kJQFIdcZPJdBU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8f0806600156314a8701143300ba9fdc550280a_2_690x496.jpeg" alt="image" data-base62-sha1="zwdGsFYhr6Hra1kJQFIdcZPJdBU" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8f0806600156314a8701143300ba9fdc550280a_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8f0806600156314a8701143300ba9fdc550280a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8f0806600156314a8701143300ba9fdc550280a.jpeg 2x" data-dominant-color="3D4B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×692 51.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot,</p>
<p>Mina</p>

---

## Post #2 by @cpinter (2025-08-04 15:04 UTC)

<p>Please confirm that these “voids” indeed have a lower voxel intensity than the other parts of the object you can threshold. (To know if this is a bug or not, but since threshold is as simple and as old a tool as it gets, I guess not)</p>
<p>To fill these holes I’d first try WrapSolidify. If it does not work the way you want, you can also try Scissors or SurfaceCut. Please let us know how it goes.</p>

---
