# How to use "Segment statics"

**Topic ID**: 1491
**Date**: 2017-11-19
**URL**: https://discourse.slicer.org/t/how-to-use-segment-statics/1491

---

## Post #1 by @beerlover (2017-11-19 19:39 UTC)

<p>Dear Developer</p>
<p>I am so new to use 3D silicer. I used it to calculate volume of alveolar bone graft in cleft site through segment editor tool. When I calculated the volume it gave me in three options, LM volume, GS volume, CS volume. What does the different of them. I tried to find the help topic but found nothing.</p>
<p>Thank you for your answer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7ce18d352e5c7a181282f5f92d903c6a7aee215b.jpeg" data-download-href="/uploads/short-url/hOKrNCWyulFJy0Am69XJB0XP3TB.jpg?dl=1" title="u" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7ce18d352e5c7a181282f5f92d903c6a7aee215b_2_690x369.jpg" alt="u" data-base62-sha1="hOKrNCWyulFJy0Am69XJB0XP3TB" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7ce18d352e5c7a181282f5f92d903c6a7aee215b_2_690x369.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7ce18d352e5c7a181282f5f92d903c6a7aee215b_2_1035x553.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7ce18d352e5c7a181282f5f92d903c6a7aee215b_2_1380x738.jpg 2x" data-dominant-color="959395"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">u</span><span class="informations">1920×1028 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-11-19 19:44 UTC)

<p>Use at least the latest stable (or recent nightly)  version. The user interface and metrics were reworked and meaning of fields should be more clear now (shown in tooltips).</p>
<p>LM and GS means the volume is computed from labelmap representation. CS means that it is computed from closed surface representation. Difference between LM and GS is that GS only considers the region that overlaps with the selected grayscale volume.</p>

---
