# Segmentation Editor - visualizing the segmented 3D model isssue

**Topic ID**: 20498
**Date**: 2021-11-05
**URL**: https://discourse.slicer.org/t/segmentation-editor-visualizing-the-segmented-3d-model-isssue/20498

---

## Post #1 by @suranga (2021-11-05 14:15 UTC)

<p>I used Sementation Editor to segment the right lung from a 3D CT volume, as shown in the screen shot below. However, when I view the 3D model from that, all I see is the painting seeds route. What may be the cause of this?</p>
<p>I started by creating two label maps, one for the right lung and the other for the remaining areas. Then, using the painting tool, paint the required sections in the specified colours. After we I finished this phase, we I employed the Grow from Seeds effect to segment the right lung.</p>
<p>Please help me to resolve this issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aec60a350de94a93b7cbcd1c8ae9160ca5974e5.jpeg" data-download-href="/uploads/short-url/cYlplm2T4bvBcIxE3akp2ZmJN7n.jpeg?dl=1" title="slicer_issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5aec60a350de94a93b7cbcd1c8ae9160ca5974e5_2_690x336.jpeg" alt="slicer_issue" data-base62-sha1="cYlplm2T4bvBcIxE3akp2ZmJN7n" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5aec60a350de94a93b7cbcd1c8ae9160ca5974e5_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5aec60a350de94a93b7cbcd1c8ae9160ca5974e5_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5aec60a350de94a93b7cbcd1c8ae9160ca5974e5_2_1380x672.jpeg 2x" data-dominant-color="878790"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_issue</span><span class="informations">1913×934 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-11-05 15:37 UTC)

<p>When you run grow from the seeds, it shows you a “preview” of what the result of segmentation will be with given seed. If you are happy with it, you need to hit “apply” to finalize the segmentation.<br>
I presume that’s why you are not seeing it.</p>

---
