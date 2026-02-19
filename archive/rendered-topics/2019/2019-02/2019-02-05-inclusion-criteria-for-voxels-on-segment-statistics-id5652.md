---
topic_id: 5652
title: "Inclusion Criteria For Voxels On Segment Statistics"
date: 2019-02-05
url: https://discourse.slicer.org/t/5652
---

# Inclusion Criteria For Voxels on Segment Statistics

**Topic ID**: 5652
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/inclusion-criteria-for-voxels-on-segment-statistics/5652

---

## Post #1 by @Nassir (2019-02-05 21:36 UTC)

<p>Hi all,</p>
<p>I’m using segment statistics to use some MRI-defined segments to export some quantitative PET data. This usually works pretty well, but does not work if my segmentation is small (less than half the PET voxel volume). I suspect this might be because of the inclusion criteria - binary mode as some softwares support (example on pg 188 <a href="http://doc.pmod.com/PDF/PBAS.pdf" rel="nofollow noopener">http://doc.pmod.com/PDF/PBAS.pdf</a>). I think it would make sense in my scenario to use fraction mode (example also on pg 188 of the previous link). Is there a way I can use fraction mode in Slicer? If not - is this something that might get implemented?</p>
<p>Thanks,<br>
Nassir</p>

---

## Post #2 by @lassoan (2019-02-05 21:50 UTC)

<p>There is fractional labelmap support in Slicer but it would require some work to make it work with Segment statistics. If you could contribute to this then let us know.</p>
<p>Alternatively, you can choose the segmentation geometry to have 2-3x oversampled resolution relative to the master volume (and if the input volume is highly anisotropic then it may worth forcing isotropic spacing):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b286f2116c120f8de305839591673aa2f9a4dbc.png" data-download-href="/uploads/short-url/d0q4Vtnapwkj55ZcKs6KZ0cRBo0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b286f2116c120f8de305839591673aa2f9a4dbc_2_379x500.png" alt="image" data-base62-sha1="d0q4Vtnapwkj55ZcKs6KZ0cRBo0" width="379" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b286f2116c120f8de305839591673aa2f9a4dbc_2_379x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b286f2116c120f8de305839591673aa2f9a4dbc_2_568x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b286f2116c120f8de305839591673aa2f9a4dbc.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">606×798 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Nassir (2019-02-07 15:46 UTC)

<p>Hi Andras,</p>
<p>Thank you for the prompt reply. It’s good to know that labelmap can use this. I ought to contribute to that, but right now I have to go with a quick solution. I did not attempt the suggested alternative because the segmentation geometry was already oversampled (high resolution MRI) relative to the PET, and I suspect that’s what got me in this pickle. Instead, I used the module Crop Volume to resample the PET image at 4 times the 1D resolution using nearest neighbour interpolation (to preserve the numbers).</p>
<p>Many thanks,<br>
Nassir</p>

---
