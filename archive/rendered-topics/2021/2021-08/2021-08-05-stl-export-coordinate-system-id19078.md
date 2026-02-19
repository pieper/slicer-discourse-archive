---
topic_id: 19078
title: "Stl Export Coordinate System"
date: 2021-08-05
url: https://discourse.slicer.org/t/19078
---

# stl export coordinate system?

**Topic ID**: 19078
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/stl-export-coordinate-system/19078

---

## Post #1 by @Benjamin-Fouquet (2021-08-05 12:14 UTC)

<p>Hello everybody,</p>
<p>I would like to understand in what coordinate system an .stl is exported when exporting a segmentation. From what I understand from: <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox" rel="noopener nofollow ugc">Coordinate systems - Slicer Wiki</a> is that it would be exported in anatomical coordinate system, where you can then choose LPS or RAS.</p>
<p>Is there a way then to export in world coordinates, or to convert the exported points to world coordinates somehow?</p>
<p>With kind regards,</p>

---

## Post #2 by @pieper (2021-08-05 12:54 UTC)

<p>You can control this in the “Export to files” section of the <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#segmentations-module-overview">Segmentations module</a>.</p>

---

## Post #3 by @lassoan (2021-08-05 13:00 UTC)

<aside class="quote no-group" data-username="Benjamin-Fouquet" data-post="1" data-topic="19078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/b77776/48.png" class="avatar"> Benjamin-Fouquet:</div>
<blockquote>
<p>Is there a way then to export in world coordinates, or to convert the exported points to world coordinates somehow?</p>
</blockquote>
</aside>
<p>RAS are the world coordinates in Slicer, so exporting in world coordinates is the same as exporting in RAS. However, I would recommend LPS for file export for compatibility with other software.</p>
<p>If you applied a transform on the model then you need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden it on the model</a> before exporting.</p>

---

## Post #4 by @Benjamin-Fouquet (2021-08-12 12:48 UTC)

<p>Sorry, realized I never properly thanked you for that.</p>

---
