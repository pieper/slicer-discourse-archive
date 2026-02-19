---
topic_id: 41945
title: "Segmentations In Segment Editor Isolated To One Axial Ct Sli"
date: 2025-03-03
url: https://discourse.slicer.org/t/41945
---

# Segmentations in segment editor isolated to one axial CT slice

**Topic ID**: 41945
**Date**: 2025-03-03
**URL**: https://discourse.slicer.org/t/segmentations-in-segment-editor-isolated-to-one-axial-ct-slice/41945

---

## Post #1 by @Camilla_Nielsen (2025-03-03 18:24 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.8.0</p>
<p>I hope someone can help.</p>
<p>I need to make a segmentation on two different CT scans on only one axial slice, but when I make the first segmentation using “segment editor” a shaded segmentation is automatically created on the slice below and above. I can’t remove them using the scissor or Island tools - it just removes the segmentation completly.</p>
<p>How do I make a segmentation on just one axial slice? I am not an expirienced user, so maybe it is an easy solve.</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea377d12dfa508588afaa7acb11f96c69a8bf1ff.png" data-download-href="/uploads/short-url/xpYBVKcXHnT0wpfficmydwhwA4D.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea377d12dfa508588afaa7acb11f96c69a8bf1ff.png" alt="image" data-base62-sha1="xpYBVKcXHnT0wpfficmydwhwA4D" width="256" height="165"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">256×165 36.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7744a8c6103543942a1f4f60d32432f40a61128.png" data-download-href="/uploads/short-url/x1xrNLv4VCBZCza6IbWZiTh9Cf6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7744a8c6103543942a1f4f60d32432f40a61128.png" alt="image" data-base62-sha1="x1xrNLv4VCBZCza6IbWZiTh9Cf6" width="258" height="171"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">258×171 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-03-03 18:28 UTC)

<p>The segmentation geometry (origin, spacing, axis directions, extents) are set when you <em>first</em> select a source volume. It seems that rhe first volume you selected had thicker slices, so the segmentation has thicker slices, which shows up on several slices of your second volume.</p>
<p>You can use the “Specify geometry” button to change the segmentation geometry to match your second volume (or create a new segmentation and choose the second volume as source volume).</p>

---

## Post #3 by @Camilla_Nielsen (2025-03-04 07:52 UTC)

<p>That did the trick. Thank you</p>

---
