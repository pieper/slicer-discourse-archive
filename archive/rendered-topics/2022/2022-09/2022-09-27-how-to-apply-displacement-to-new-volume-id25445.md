---
topic_id: 25445
title: "How To Apply Displacement To New Volume"
date: 2022-09-27
url: https://discourse.slicer.org/t/25445
---

# How to apply displacement to new volume?

**Topic ID**: 25445
**Date**: 2022-09-27
**URL**: https://discourse.slicer.org/t/how-to-apply-displacement-to-new-volume/25445

---

## Post #1 by @ryu (2022-09-27 12:21 UTC)

<p>Hello, 3D slicer experts!</p>
<p>I want to register images from two modalities (CT and CBCT) with 3D Slicer.</p>
<p>First, I apply the deformable register to adjust CT image (moving volume) to CBCT (fixed volume) using “Elastix extension”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/275158b70a492ab710cecb78624b82d7df3c106b.jpeg" data-download-href="/uploads/short-url/5BOU8MS9aK98kNE4E9cS2gA4RB1.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/275158b70a492ab710cecb78624b82d7df3c106b_2_690x492.jpeg" alt="1" data-base62-sha1="5BOU8MS9aK98kNE4E9cS2gA4RB1" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/275158b70a492ab710cecb78624b82d7df3c106b_2_690x492.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/275158b70a492ab710cecb78624b82d7df3c106b_2_1035x738.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/275158b70a492ab710cecb78624b82d7df3c106b_2_1380x984.jpeg 2x" data-dominant-color="F4EFEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1483×1058 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and I saved the computed displacement field named .</p>
<p>However, when I applied the displacement field to origin CT image using “Transforms module”, it takes the wrong place.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bb94e1b705ba04ffe16651a3192ee238101e9d8.jpeg" data-download-href="/uploads/short-url/hEvK4X8Q9lL68c1BkGCHQuNYUVW.jpeg?dl=1" title="그림2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb94e1b705ba04ffe16651a3192ee238101e9d8_2_690x366.jpeg" alt="그림2" data-base62-sha1="hEvK4X8Q9lL68c1BkGCHQuNYUVW" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb94e1b705ba04ffe16651a3192ee238101e9d8_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb94e1b705ba04ffe16651a3192ee238101e9d8_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb94e1b705ba04ffe16651a3192ee238101e9d8_2_1380x732.jpeg 2x" data-dominant-color="AFAEAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">그림2</span><span class="informations">2000×1063 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Am I wrong? How can I apply displacement to a new volume?</p>
<p>Thanks a lot</p>

---
