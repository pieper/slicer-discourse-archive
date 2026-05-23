---
topic_id: 47118
title: "On End Capping In Slicer Vs A Commercial Software Treatment"
date: 2026-05-22
url: https://discourse.slicer.org/t/47118
---

# On end capping in slicer vs a commercial software ( Treatment Planning System)

**Topic ID**: 47118
**Date**: 2026-05-22
**URL**: https://discourse.slicer.org/t/on-end-capping-in-slicer-vs-a-commercial-software-treatment-planning-system/47118

---

## Post #1 by @G_Tom (2026-05-22 16:09 UTC)

<p>I have exported a structure which is a simple sphere from Eclipse to slicer via DICOM export/import</p>
<p>I noticed some difference at the “end caps” in slicer. I compare the result with a commercial software, Varian Eclipse. Can anyone explain the differences between slicer and Eclipse ? has this been discussed elsewhere? looks like slicer caps to include whole slice while eclipse caps to include only a fraction of the slice ?</p>
<p>I am computing some conformity metrics for small targets. This means every small voxel discrepancy counts. Any way to adjust capping in slicer ? I am using 3D Slicer 5.8.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb6ce0ed8c798c4e3e27395ceeabad6370e92b69.png" data-download-href="/uploads/short-url/zSd7dFKEsmjLaQuYXGlcvT1Yj0d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb6ce0ed8c798c4e3e27395ceeabad6370e92b69_2_690x268.png" alt="image" data-base62-sha1="zSd7dFKEsmjLaQuYXGlcvT1Yj0d" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb6ce0ed8c798c4e3e27395ceeabad6370e92b69_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb6ce0ed8c798c4e3e27395ceeabad6370e92b69_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb6ce0ed8c798c4e3e27395ceeabad6370e92b69_2_1380x536.png 2x" data-dominant-color="606060"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1774×691 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @mau_igna_06 (2026-05-22 19:32 UTC)

<p>I can see a light red “circle” on the right side image. Could you explain more?</p>

---

## Post #3 by @lassoan (2026-05-22 22:32 UTC)

<p>We implemented end-capping in SlicerRT so that the segment ends exactly halfway between the center of the slice where the last contour was drawn and the center of the next slice (where no contour is visible). Ending the segment in the middle of a slice (as it is visible on the left image) would be hard to justify and I’m not sure if Eclipse actually does this for computations - it may be just a choice for visualization or export.</p>
<p>Probably the end-capping does not make meaningful difference anyway. We  compared dose volume histograms computed by Eclipse and SlicerRT and the difference was negligible. SlicerRT non-regressions tests still use Eclipse-computed results as reference.</p>

---
