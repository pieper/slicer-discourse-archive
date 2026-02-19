---
topic_id: 21183
title: "Segmentation Saving Support"
date: 2021-12-22
url: https://discourse.slicer.org/t/21183
---

# Segmentation saving support

**Topic ID**: 21183
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/segmentation-saving-support/21183

---

## Post #1 by @19lollo95 (2021-12-22 15:28 UTC)

<p>Hi everyone,<br>
I did a segmentation of a brain with a tumor (specifically the MRBrainTumor2 in BuiltIn). I’m having trouble with the save operation. How can I get 2 different mhd files for the two objects? In the save list there are only these objects (see photo). I have to use the two images to build a tetrahedral mesh with vmtk.<br>
Thanks in advance<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0818f7122faa55c16819a8a766ec0ee574d4f983.jpeg" data-download-href="/uploads/short-url/19Dj3dChizKhZn0AlN5JXBosX1p.jpeg?dl=1" title="Schermata 2021-12-22 alle 16.25.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0818f7122faa55c16819a8a766ec0ee574d4f983_2_690x329.jpeg" alt="Schermata 2021-12-22 alle 16.25.48" data-base62-sha1="19Dj3dChizKhZn0AlN5JXBosX1p" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0818f7122faa55c16819a8a766ec0ee574d4f983_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0818f7122faa55c16819a8a766ec0ee574d4f983_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0818f7122faa55c16819a8a766ec0ee574d4f983_2_1380x658.jpeg 2x" data-dominant-color="E9E9E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermata 2021-12-22 alle 16.25.48</span><span class="informations">1748×834 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-12-23 16:01 UTC)

<aside class="quote no-group" data-username="19lollo95" data-post="1" data-topic="21183">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/1/82dd89/48.png" class="avatar"> 19lollo95:</div>
<blockquote>
<p>How can I get 2 different mhd files for the two objects?</p>
</blockquote>
</aside>
<p>When you export a segmentation to a labelmap then by default only the visible segments are exported. So, you can have two labelmap volumes, each containing one segment by showing one segment, export, showing the other segment, export.</p>
<p>For volumetric mesh generation I would recommend to use SegmentMesher extension, which can generate multimaterial tetrahedral mesh directly from segmentation.</p>

---
