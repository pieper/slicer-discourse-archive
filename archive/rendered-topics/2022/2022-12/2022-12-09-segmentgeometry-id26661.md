---
topic_id: 26661
title: "Segmentgeometry"
date: 2022-12-09
url: https://discourse.slicer.org/t/26661
---

# SegmentGeometry

**Topic ID**: 26661
**Date**: 2022-12-09
**URL**: https://discourse.slicer.org/t/segmentgeometry/26661

---

## Post #1 by @francesca_flore (2022-12-09 12:47 UTC)

<p>Hi! I’m using SegmentGeometry tool to export a table with the maximum diameter of my segment along its section. But despite I’m computing on every slice in the segment. Not all the slices in which my segment appears are shown. In practice I don’t know exactly where it starts to compute and where it ends.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73b816735fa7355715973bfe28b0aa5ed9b29255.jpeg" data-download-href="/uploads/short-url/gvHjxx9JlNsMSoklsKlmLnPUb3v.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73b816735fa7355715973bfe28b0aa5ed9b29255_2_690x464.jpeg" alt="image" data-base62-sha1="gvHjxx9JlNsMSoklsKlmLnPUb3v" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73b816735fa7355715973bfe28b0aa5ed9b29255_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73b816735fa7355715973bfe28b0aa5ed9b29255_2_1035x696.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73b816735fa7355715973bfe28b0aa5ed9b29255_2_1380x928.jpeg 2x" data-dominant-color="838280"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1397×941 98.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jmhuie (2022-12-09 13:17 UTC)

<p>Hi <a class="mention" href="/u/francesca_flore">@francesca_flore</a>, I responded to your DM but I’ll post to my answer here too.</p>
<p>Can you confirm that you have the most recent version of Slicer and SegmentGeometry?</p>
<p>If so, my best guess is that you need to change the slice interval to 0. If your segment is more than 100 slices long, SegmentGeometry will by default only calculate on 100 slices in 1% intervals. Changing the slice interval to 0 will make it calculate on every slice.</p>
<p>The calculations start on the first segmented slice in the color view selected in the Slice View setting. The default is the Red view, which looks like what you’d want.</p>
<p>If you have any more issues, make sure to look at the GitHub repo which has some troubleshooting info. <a href="https://github.com/jmhuie/Slicer-SegmentGeometry" rel="noopener nofollow ugc">GitHub - jmhuie/Slicer-SegmentGeometry: Extension to calculate second moment of area and other cross-sectional properties in 3D Slicer</a></p>

---
