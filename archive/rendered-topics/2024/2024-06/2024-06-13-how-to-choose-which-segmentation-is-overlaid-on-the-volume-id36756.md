# How to choose which segmentation is overlaid on the volume

**Topic ID**: 36756
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/how-to-choose-which-segmentation-is-overlaid-on-the-volume/36756

---

## Post #1 by @Figaya (2024-06-13 13:23 UTC)

<p>Hello,</p>
<p>I am new to 3D Slicer and am having difficulty understanding a few things.</p>
<p>I’ve imported a single series volume data and created two segmentations. Both segmentations have the same source volume. Here are the steps I performed:</p>
<ol>
<li>In the first segmentation, I added a single red-colored segment with some threshold.</li>
<li>In the second segmentation, I followed the same step but with a yellow-colored segment.</li>
</ol>
<p>After performing both steps, when I go back to the first segmentation, I still see the results of the second segmentation, specifically yellow regions instead of red regions.</p>
<p>As per my understanding, shouldn’t red regions appear in the first segmentation and yellow regions in the second segmentation?</p>

---

## Post #2 by @lassoan (2024-06-13 13:29 UTC)

<p>You can see and edit multiple segmentations. If you want to show/hide a segmentation then you can click the eye icon. <code>Data</code> module gives a good overview of what data you have and allows you to show/hide them.</p>

---
