---
topic_id: 32746
title: "Obb Not Aligned With Segmentde"
date: 2023-11-11
url: https://discourse.slicer.org/t/32746
---

# OBB Not Aligned with Segmentde

**Topic ID**: 32746
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/obb-not-aligned-with-segmentde/32746

---

## Post #1 by @jamieawren (2023-11-11 18:22 UTC)

<p>Hi Everyone,</p>
<p>I’m calculating a bounding box for a segment, and the output’s measurement appear to be correct, i.e. I’m using a 20mm paint brush and the height and width are 20mm. When I use the code found here (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>) to view the box though, it’s not aligned with the segment.</p>
<p>Any thoughts? Is the just an annoying fluke, or is it affecting the calculation of the bounding box?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22f9d017dd59182062252810ccd16c7c1e4675f9.jpeg" data-download-href="/uploads/short-url/4ZpsfhryUKW1TXeMxSo2yL1pgo1.jpeg?dl=1" title="Screenshot 2023-11-11 at 1.17.40 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22f9d017dd59182062252810ccd16c7c1e4675f9_2_690x431.jpeg" alt="Screenshot 2023-11-11 at 1.17.40 PM" data-base62-sha1="4ZpsfhryUKW1TXeMxSo2yL1pgo1" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22f9d017dd59182062252810ccd16c7c1e4675f9_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22f9d017dd59182062252810ccd16c7c1e4675f9_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22f9d017dd59182062252810ccd16c7c1e4675f9_2_1380x862.jpeg 2x" data-dominant-color="B8B9D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-11 at 1.17.40 PM</span><span class="informations">1920×1200 71.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!</p>

---

## Post #2 by @mikebind (2023-11-11 20:15 UTC)

<p>Is the original segmentation transformed?  If so, perhaps the SegmentStatistics calculations ignore any parent transforms.  Try applying the same parent transform of the original segmentation to the bounding box ROI object and see if it lines up then.</p>

---

## Post #3 by @jamieawren (2023-11-11 20:28 UTC)

<p>The original segmentation isn’t transformed, so I’m not quite sure.</p>

---

## Post #4 by @mikebind (2023-11-11 20:54 UTC)

<p>I don’t have time to test independently at the moment, but in that case it may be a bug.  If you can reproduce with a minimal example and share the scene here, that would help anyone trying to debug it.</p>

---

## Post #5 by @lassoan (2023-11-11 23:38 UTC)

<p>I’ve just tested and the script still works well. The problem was that you used a Slicer version that is 2.5 years old (Slicer-4.11) with the documentation of the latest Slicer version (Slicer-5.5).</p>
<p>I would recommend to use the current Slicer version as we implemented hundreds of fixes and improvements since Slicer-4.11 was released.</p>

---
