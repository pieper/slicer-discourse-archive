---
topic_id: 29316
title: "Threshold In The Segment Editor"
date: 2023-05-06
url: https://discourse.slicer.org/t/29316
---

# Threshold in the segment editor

**Topic ID**: 29316
**Date**: 2023-05-06
**URL**: https://discourse.slicer.org/t/threshold-in-the-segment-editor/29316

---

## Post #1 by @duan (2023-05-06 14:23 UTC)

<p>What is the threshold in the segment editor? Does this threshold represent the window width of the corresponding CT value of human tissue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86b1028a1623eb2ba7fd6c2d1b00c443b1fb3fa2.jpeg" data-download-href="/uploads/short-url/jdxdPnz2zCz3RoZMtdLT8nrXwUq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b1028a1623eb2ba7fd6c2d1b00c443b1fb3fa2_2_690x376.jpeg" alt="image" data-base62-sha1="jdxdPnz2zCz3RoZMtdLT8nrXwUq" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b1028a1623eb2ba7fd6c2d1b00c443b1fb3fa2_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b1028a1623eb2ba7fd6c2d1b00c443b1fb3fa2_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b1028a1623eb2ba7fd6c2d1b00c443b1fb3fa2_2_1380x752.jpeg 2x" data-dominant-color="9B9A9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1816×990 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-05-06 14:40 UTC)

<p>The threshold is in terms of the data values in your images.  If the data is a clinical CT, then it would be <a href="https://radiopaedia.org/articles/hounsfield-unit">HU</a>.  But your data appears to be a scan of a printed film, so the units are probably not calibrated.</p>

---
