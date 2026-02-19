---
topic_id: 22850
title: "Segmenteditor How To Keep The Outline Size The Same"
date: 2022-04-06
url: https://discourse.slicer.org/t/22850
---

# SegmentEditor: How to keep the outline size the same？

**Topic ID**: 22850
**Date**: 2022-04-06
**URL**: https://discourse.slicer.org/t/segmenteditor-how-to-keep-the-outline-size-the-same/22850

---

## Post #1 by @caiqj1203 (2022-04-06 12:38 UTC)

<p>I use SegmentEditor Module to add a segmentation and paint contour of nodule<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b24caac153a2217a8c49e9ac9c00f183116f2169.png" data-download-href="/uploads/short-url/prjfnwOoJR9yIISdqKlf7Sms81b.png?dl=1" title="segmentation_pre" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b24caac153a2217a8c49e9ac9c00f183116f2169.png" alt="segmentation_pre" data-base62-sha1="prjfnwOoJR9yIISdqKlf7Sms81b" width="690" height="266" data-dominant-color="6A6B69"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation_pre</span><span class="informations">711×275 65.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then, I export segmentation to file, reload it, show it’s contour of 2d view, the contour change smaller<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3770234c97cb258dc48405c5e2d7e21698f76f.jpeg" data-download-href="/uploads/short-url/aSf3UXiSYXhRhYmh6DZomusQ36f.jpeg?dl=1" title="segmentation_after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3770234c97cb258dc48405c5e2d7e21698f76f.jpeg" alt="segmentation_after" data-base62-sha1="aSf3UXiSYXhRhYmh6DZomusQ36f" width="690" height="238" data-dominant-color="6B6C6B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation_after</span><span class="informations">714×247 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How to keep the outline size the same？</p>

---

## Post #2 by @pieper (2022-04-06 14:11 UTC)

<p>Here you are seeing two different representations of the same underlying segmentation.  One is the binary labelmap (above) with the stairsteps, and the smoothed polygonal reconstruction (below).  If you save and reload and reload with the detaults the original labelmap will be preserved.</p>

---

## Post #3 by @lassoan (2022-04-06 15:09 UTC)

<p>Also note that you can choose to show the closed surface representation in slice views: in Segmentations module → Display → Advanced → Representation in 2D views → Closed surface.</p>

---
