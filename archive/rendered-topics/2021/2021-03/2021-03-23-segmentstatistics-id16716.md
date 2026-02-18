# SegmentStatistics

**Topic ID**: 16716
**Date**: 2021-03-23
**URL**: https://discourse.slicer.org/t/segmentstatistics/16716

---

## Post #1 by @Rachele (2021-03-23 12:04 UTC)

<p>Operating system: macOS Big Sur version 11.2.2<br>
Slicer version: 4.11.20200930</p>
<p>Hi, I’m trying to understand why the number of voxels computed by scalar volume statistics plugin is much different from the number of voxels computed by labelmap statistics plugin. I would like to compute the mean activity inside each VOI, so I need to multiply the mean value by the correspondent number of voxels… which one should I use, scalar or labelmap-computed number?<br>
If anyone could help me I would be very grateful <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5372f5def6a0b065554c3afbdc9c00bef5932caa.png" data-download-href="/uploads/short-url/bUdVLdSeIA44OSaBz8FYwT1CkKS.png?dl=1" title="Schermata 2021-03-23 alle 12.22.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5372f5def6a0b065554c3afbdc9c00bef5932caa_2_690x194.png" alt="Schermata 2021-03-23 alle 12.22.50" data-base62-sha1="bUdVLdSeIA44OSaBz8FYwT1CkKS" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5372f5def6a0b065554c3afbdc9c00bef5932caa_2_690x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5372f5def6a0b065554c3afbdc9c00bef5932caa_2_1035x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5372f5def6a0b065554c3afbdc9c00bef5932caa.png 2x" data-dominant-color="EDECE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermata 2021-03-23 alle 12.22.50</span><span class="informations">1052×297 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-03-24 17:23 UTC)

<p>The difference is most likely due to that the scalar volume plugin only considers that region of the segmentation that overlaps with the chosen scalar volume.</p>

---
