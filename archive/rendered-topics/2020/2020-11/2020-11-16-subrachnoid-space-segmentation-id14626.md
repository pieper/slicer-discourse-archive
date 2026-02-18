# Subrachnoid space segmentation

**Topic ID**: 14626
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/subrachnoid-space-segmentation/14626

---

## Post #1 by @Vytenis_R (2020-11-16 04:35 UTC)

<p>Hello,<br>
is there an easy way to segment brain subarachnoid space? When I use “Threshold” too many other parts are included.</p>

---

## Post #2 by @lassoan (2020-11-16 07:16 UTC)

<p>There are many tools that can help, but the first I would recommend to try is <a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233">Local thresholding</a> (provided by SegmentEditorExtraEffects extension). You can set a threshold range (optionally an additional region of interest), and then segment a structure by a single click (Ctrl+Left-click).</p>

---

## Post #3 by @Vytenis_R (2020-11-22 16:09 UTC)

<p>With Local thersholding still too many unwanted areas are selected, maybe I’m doing something wrong? Or there is another way to segment subarachnoid space?</p>

---

## Post #4 by @lassoan (2020-11-22 16:37 UTC)

<p>Local thresholding should work very well for this. Most important is to set the right threshold range. You can enforce further spatial smoothness by choosing watershed mode. You can also set the minimum connecting bridge size to prevent leaking.</p>

---
