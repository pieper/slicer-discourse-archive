---
topic_id: 46920
title: "Segmentation Bounds Cropped Even When Cropped To Minimum Ext"
date: 2026-05-04
url: https://discourse.slicer.org/t/46920
---

# Segmentation bounds cropped even when "cropped to minimum extent" is unchecked

**Topic ID**: 46920
**Date**: 2026-05-04
**URL**: https://discourse.slicer.org/t/segmentation-bounds-cropped-even-when-cropped-to-minimum-extent-is-unchecked/46920

---

## Post #1 by @hherhold (2026-05-04 18:48 UTC)

<p>Sequence of events:</p>
<ol>
<li>Create segmentation using slicer</li>
<li>modify segmentation in external python script using pynrrd</li>
<li>re-import segmentation into slicer</li>
<li>modify segmentation in slicer</li>
<li>save segmentation</li>
<li>This saved segmentation has been cropped to its minimum extent even though checkbox in save dialog is not checked.</li>
</ol>
<p>I ran this through Claude Opus 4.7 and it had a couple of suggestions, which I did try but did not appear to fix the problem; I haven’t had a chance to investigate further. Just wondering if anyone has run into this before.</p>
<p>The segmentation in question is fed into biomedisa (<a href="https://biomedisa.info/" rel="noopener nofollow ugc">https://biomedisa.info/</a>), which requires the segmentation and the volume data to have the same dimensions.</p>
<p>Anyway, this is an odd corner case and likely hasn’t been a huge issue. I can post Claude Opus’ suggestions if anyone is interested.</p>

---
