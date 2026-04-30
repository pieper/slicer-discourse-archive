---
topic_id: 46868
title: "Segementing Mri Doesnt Do Continous Layer"
date: 2026-04-29
url: https://discourse.slicer.org/t/46868
---

# Segementing mri doesnt do continous layer

**Topic ID**: 46868
**Date**: 2026-04-29
**URL**: https://discourse.slicer.org/t/segementing-mri-doesnt-do-continous-layer/46868

---

## Post #1 by @mohammed_alshakhas (2026-04-29 15:03 UTC)

<p>im experimenting with mri segmentation . sometimes it works fine but started to get this error more often . when i draw or pain i get some area segmented some are not .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4627ce22c75e2eb8d5a2253c02ffefb0f98be7e1.jpeg" data-download-href="/uploads/short-url/a0CHIRdaFVnv2HhWekKWNJSd9K1.jpeg?dl=1" title="Screenshot 2026-04-29 at 18.02.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4627ce22c75e2eb8d5a2253c02ffefb0f98be7e1_2_685x500.jpeg" alt="Screenshot 2026-04-29 at 18.02.46" data-base62-sha1="a0CHIRdaFVnv2HhWekKWNJSd9K1" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4627ce22c75e2eb8d5a2253c02ffefb0f98be7e1_2_685x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4627ce22c75e2eb8d5a2253c02ffefb0f98be7e1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4627ce22c75e2eb8d5a2253c02ffefb0f98be7e1.jpeg 2x" data-dominant-color="4C4C4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-04-29 at 18.02.46</span><span class="informations">984×718 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2026-04-29 20:57 UTC)

<p>I wonder if your segmentation geometry has very large voxels, and your slice view is grazing these from an oblique angle.  Something like the second figure at this link: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" rel="noopener nofollow ugc">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---
