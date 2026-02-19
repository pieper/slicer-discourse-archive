---
topic_id: 20797
title: "Calculate Surface Area Of A Xct Volume"
date: 2021-11-26
url: https://discourse.slicer.org/t/20797
---

# Calculate surface area of a XCT Volume

**Topic ID**: 20797
**Date**: 2021-11-26
**URL**: https://discourse.slicer.org/t/calculate-surface-area-of-a-xct-volume/20797

---

## Post #1 by @lolamartinalonso (2021-11-26 09:17 UTC)

<p>Operating system:64 bit<br>
Slicer version:4.11.20210226<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I would want to calculate the surface area of an XCT Volume. Could anyone help me with some ideas of how to approach it?</p>
<p>I attach the screen with the volume.</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e900652de4eb2436c7fc841bc5c219104ac18dc.jpeg" data-download-href="/uploads/short-url/6DUxb5cO9Fhi70yV87juuWN8Qck.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e900652de4eb2436c7fc841bc5c219104ac18dc_2_690x375.jpeg" alt="image" data-base62-sha1="6DUxb5cO9Fhi70yV87juuWN8Qck" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e900652de4eb2436c7fc841bc5c219104ac18dc_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e900652de4eb2436c7fc841bc5c219104ac18dc_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e900652de4eb2436c7fc841bc5c219104ac18dc_2_1380x750.jpeg 2x" data-dominant-color="8C8D9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1045 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-11-26 14:07 UTC)

<p>You can just segment it (probably just threshold) with the Segment Editor and then use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">SegmentStatistics</a> module.</p>

---
