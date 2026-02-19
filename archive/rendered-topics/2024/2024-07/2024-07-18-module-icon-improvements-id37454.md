---
topic_id: 37454
title: "Module Icon Improvements"
date: 2024-07-18
url: https://discourse.slicer.org/t/37454
---

# Module icon improvements

**Topic ID**: 37454
**Date**: 2024-07-18
**URL**: https://discourse.slicer.org/t/module-icon-improvements/37454

---

## Post #1 by @wenples (2024-07-18 16:03 UTC)

<p>Hi all, I’m working on slice viewer and segment editor icon improvements – focusing on the SEGMENT EDITOR MODULE here, I’d like to get feedback about clarifying the meaning any of the editor’s icons.</p>
<p>For any of the tools shown below, if you feel that the existing icon can better represent the SPIRIT and USE of the tool, please offer some clarifying information! I’ll use that to modify existing design for new light and dark mode icon versions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e21082b28a7d6c76779723dc65dc6abd16d2544.jpeg" data-download-href="/uploads/short-url/20ZsduMFdnpokEkfGXn40munS04.jpeg?dl=1" title="SegEdTools"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e21082b28a7d6c76779723dc65dc6abd16d2544_2_353x500.jpeg" alt="SegEdTools" data-base62-sha1="20ZsduMFdnpokEkfGXn40munS04" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e21082b28a7d6c76779723dc65dc6abd16d2544_2_353x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e21082b28a7d6c76779723dc65dc6abd16d2544_2_529x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e21082b28a7d6c76779723dc65dc6abd16d2544_2_706x1000.jpeg 2x" data-dominant-color="F2F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SegEdTools</span><span class="informations">794×1123 53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We hope not to make everyone re-learn a vastly different set of icons, so smaller  changes are preferred.</p>
<p>Thank you for your help!</p>

---

## Post #2 by @muratmaga (2024-07-18 16:35 UTC)

<p>I don’t really have a suggestion to improve them. But I do want to mention, I find the hollow and island tool icons visually too similar and have to look very carefully to find the right one.</p>
<p>To some extend I find a similar confusion with margin and smoothing tool, even through they don’t look anything like each other. I have to think a minute to remember which one is which…</p>

---

## Post #3 by @lassoan (2024-07-18 17:04 UTC)

<ul>
<li>Paint: paint with a brush (a circle or sphere around the mouse pointer is filled)</li>
<li>Erase: same as paint, but erasing with a brush</li>
<li>Draw: draw a contour, internal of the contour is filled</li>
<li>Scissors: similar to draw, but the internal may be filled or deleted</li>
<li>Grow from seeds: region growing from scribbles or strokes</li>
<li>Margin: uniformly grow or shrink the segment by a specified margin; the arrows are supposed to indicate that the original green contour is moved inside according to the arrow direction</li>
<li>Smoothing: makes boundary of segments smoother (internal boundaries, too, so it may remove holes), the icon shows the original red sharp edge is changed to the smoother green edge</li>
<li>Islands: various operations related to connected pieces of the segment (e.g., remove small disconnected pieces, keep only the largest connected piece, keep a piece that is connected to the position where the user clicks), I just kept the original icon, it is not very descriptive</li>
<li>Mask volume: blank out the volume inside or outside the segment. The icon is supposed to show that the region of the volume that is outside the colored area is blanked out.</li>
<li>Threshold: Creates a segment from the region of the source volume that is in the specified intensity range. The top of the icon shows a continuous volume and in the bottom it shows that it is discretized. Not the most intuitive.</li>
<li>Level tracing: Creates a segment from an iso-value contour at the mouse position.</li>
<li>Fill between slices: User segments a few slices (shown with darker colors in the icon) and this effect computes a full segmentation (the interpolated slices are shown with lighter colors, similarly how the full segmentation preview looks like)</li>
<li>Hollow: removes internal filling of the segment and only keeps a shell around it.</li>
<li>Logical operators: Combines segments using logical operators (AND, OR) or fills or clears a segment.</li>
<li>Undo/redo: standard undo/redo funtionality and corresponding standard icons.</li>
</ul>
<p>The main issue with the icons for me that even after years of using them and having them at the same location in the layout, I still often spend several seconds to find the one I need. I hope that changing them to better capture the essence of the effect and making them more distinguishable will help.</p>
<p>There are 8 additional effects in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" class="inline-onebox">GitHub - lassoan/SlicerSegmentEditorExtraEffects: Many additional segmentation tools for 3D Slicer's Segment Editor</a> extension, that are close to getting into the Slicer core, so it would be good if you could work on those icons, too.</p>

---

## Post #4 by @wenples (2024-07-18 18:20 UTC)

<p>These comments are very useful – thank you for this thoughtful feedback!</p>

---
