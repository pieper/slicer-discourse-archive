---
topic_id: 3020
title: "Brain Cortex Volume Rendering"
date: 2018-05-30
url: https://discourse.slicer.org/t/3020
---

# Brain Cortex Volume Rendering

**Topic ID**: 3020
**Date**: 2018-05-30
**URL**: https://discourse.slicer.org/t/brain-cortex-volume-rendering/3020

---

## Post #1 by @carba86 (2018-05-30 15:49 UTC)

<p>Hi everyone, I am trying to do a volume render of the human brain cortex. I do not know if Slicer is the right tool to do it. A good result would be something like this.</p>
<p>Thank you very much in advanced</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beec3e6456da8086abd53b3fae7e7a49478a73be.jpeg" data-download-href="/uploads/short-url/reYRTgZ2OiaaZY0Ss2mmMtvmOqa.jpg?dl=1" title="Snip20180530_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/beec3e6456da8086abd53b3fae7e7a49478a73be_2_532x500.jpg" alt="Snip20180530_1" data-base62-sha1="reYRTgZ2OiaaZY0Ss2mmMtvmOqa" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/beec3e6456da8086abd53b3fae7e7a49478a73be_2_532x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/beec3e6456da8086abd53b3fae7e7a49478a73be_2_798x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beec3e6456da8086abd53b3fae7e7a49478a73be.jpeg 2x" data-dominant-color="272727"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snip20180530_1</span><span class="informations">1042×978 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-05-30 16:21 UTC)

<p>Yes, you should be able to get a rendering like this in Slicer. You need to strip the skull first, using for example SwissSkullStripper extension and then use Volume Rendering module on the created brain image. These are all quite quick, fully automatic steps.</p>
<p>Depending on the original image quality, volume rendering may not provide such nice images. In that case, you may try to tune volume rendering settings and slightly adjust the brain mask (e.g., using Segment editor module, Mask volume effect).</p>
<p>If this still not provides the images that you would like, then you need to segment the brain. You can either use FreeSurfer for automatic segmentation or use Segment Editor in Slicer for manual segmentation.</p>

---
