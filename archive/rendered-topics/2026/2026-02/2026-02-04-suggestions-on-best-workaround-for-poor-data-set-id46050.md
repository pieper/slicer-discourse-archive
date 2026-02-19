---
topic_id: 46050
title: "Suggestions On Best Workaround For Poor Data Set"
date: 2026-02-04
url: https://discourse.slicer.org/t/46050
---

# Suggestions on best workaround for poor data set

**Topic ID**: 46050
**Date**: 2026-02-04
**URL**: https://discourse.slicer.org/t/suggestions-on-best-workaround-for-poor-data-set/46050

---

## Post #1 by @Learn34 (2026-02-04 02:36 UTC)

<p>While I’m now attempting to follow the workflow described in <a href="https://www.nature.com/articles/s41598-025-19664-6" rel="noopener nofollow ugc">this paper</a>, I’m still stymied by the poor fitness of my baseline dataset (a SPECT of my spine) for segmentation of soft tissue (or it may be a limitation of the <a href="https://github.com/lassoan/SlicerTotalSegmentator" rel="noopener nofollow ugc">TotalSegmentator module</a>. What suggestions to any of you have for filling in the missing intervertebral discs? Am I just stuck working to manually segment those structures slice by slice?</p>
<p>Example of both the dataset and segments attached.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfa7a4a9dbe5ed6973e6e19b4f1cc246f8313c7d.jpeg" data-download-href="/uploads/short-url/rlsmZjXJVhCFcUPHSSHnr5dfdq5.jpeg?dl=1" title="Example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfa7a4a9dbe5ed6973e6e19b4f1cc246f8313c7d_2_564x500.jpeg" alt="Example" data-base62-sha1="rlsmZjXJVhCFcUPHSSHnr5dfdq5" width="564" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfa7a4a9dbe5ed6973e6e19b4f1cc246f8313c7d_2_564x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfa7a4a9dbe5ed6973e6e19b4f1cc246f8313c7d_2_846x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfa7a4a9dbe5ed6973e6e19b4f1cc246f8313c7d_2_1128x1000.jpeg 2x" data-dominant-color="5B5A5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Example</span><span class="informations">1439×1274 309 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-02-04 16:16 UTC)

<aside class="quote no-group" data-username="Learn34" data-post="1" data-topic="46050">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c6cbf5/48.png" class="avatar"> Learn34:</div>
<blockquote>
<p>for segmentation of soft tissue</p>
</blockquote>
</aside>
<p>There is no soft tissue visible in the image you shared. it is all noise.</p>

---

## Post #3 by @cpinter (2026-02-05 09:20 UTC)

<p>What is the scalar range of the volume? If you try optimizing window/level values can you achieve a less noisy visualization? The segmentation seems quite good to me btw.</p>

---
