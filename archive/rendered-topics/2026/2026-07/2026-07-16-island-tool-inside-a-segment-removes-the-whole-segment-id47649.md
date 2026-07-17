---
topic_id: 47649
title: "Island tool inside a segment removes the whole segment"
date: 2026-07-16
url: https://discourse.slicer.org/t/47649
last_bumped: 2026-07-17T02:37:05.548Z
---

# Island tool inside a segment removes the whole segment

**Topic ID**: 47649
**Date**: 2026-07-16
**URL**: https://discourse.slicer.org/t/island-tool-inside-a-segment-removes-the-whole-segment/47649

---

## Post #1 by @muratmaga (2026-07-16 23:02 UTC)

<p>I want to remove these small specs left after a boolean. So I restricted the editable area to inside that specific segment, and then tried to use the island tools remove small islands with really small island size (like 10 voxel). It removed the whole segment.</p>
<p>Is this normal? What’s the combination of options for me to do that?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a.jpeg" data-download-href="/uploads/short-url/2Bktzqf6sbjfrOjYRxqjZH5jXBw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_690x416.jpeg" alt="image" data-base62-sha1="2Bktzqf6sbjfrOjYRxqjZH5jXBw" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_1380x832.jpeg 2x" data-dominant-color="60605E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-07-17 02:37 UTC)

<p>This feels like a bug to me. Because when I used the “Keep Selected Island” with the same masking options it completed successfully.</p>

---
