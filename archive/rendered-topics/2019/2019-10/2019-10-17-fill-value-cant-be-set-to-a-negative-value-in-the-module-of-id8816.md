---
topic_id: 8816
title: "Fill Value Cant Be Set To A Negative Value In The Module Of"
date: 2019-10-17
url: https://discourse.slicer.org/t/8816
---

# Fill value can't be set to a negative value in the module of volume Clip with model in the newest version!

**Topic ID**: 8816
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/fill-value-cant-be-set-to-a-negative-value-in-the-module-of-volume-clip-with-model-in-the-newest-version/8816

---

## Post #1 by @researchtomliu (2019-10-17 15:28 UTC)

<p>I have installed the newest version of 4.10.2 today. But when I wanted to clip the volume with a model, I found that the fill value can’t be set to a negative value (such as -1000) as in the former version. Is it a new bug?!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccea4e7c2052b8f122b99e8febed4d1bd301fa28.jpeg" data-download-href="/uploads/short-url/teLp155zw3cLyhLT6xi6JY9XQk8.jpeg?dl=1" title="clip%20with%20model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccea4e7c2052b8f122b99e8febed4d1bd301fa28_2_690x264.jpeg" alt="clip%20with%20model" data-base62-sha1="teLp155zw3cLyhLT6xi6JY9XQk8" width="690" height="264" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccea4e7c2052b8f122b99e8febed4d1bd301fa28_2_690x264.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccea4e7c2052b8f122b99e8febed4d1bd301fa28_2_1035x396.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccea4e7c2052b8f122b99e8febed4d1bd301fa28.jpeg 2x" data-dominant-color="F7F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clip%20with%20model</span><span class="informations">1108×424 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-10-17 17:04 UTC)

<p>Thanks for reporting this. It was indeed a regression introduced by the last commit in the repository. I’ve fixed it now and you can download the updated version tomorrow.</p>
<p>We don’t use this extension much anymore because these features have been made available directly in Segment Editor module. Install SegmentEditorExtraEffects extension and you will find that <em>Surface Cut</em> and <em>Mask Volume</em> effects do the same but they are much better integrated into segmentation workflow.</p>

---

## Post #3 by @researchtomliu (2019-10-18 06:53 UTC)

<p>Mr. Lassoan, thank you very much for your solution.</p>

---
