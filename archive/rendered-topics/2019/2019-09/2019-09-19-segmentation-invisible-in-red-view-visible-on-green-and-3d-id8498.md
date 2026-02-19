---
topic_id: 8498
title: "Segmentation Invisible In Red View Visible On Green And 3D"
date: 2019-09-19
url: https://discourse.slicer.org/t/8498
---

# Segmentation invisible in red view, visible on green and 3d

**Topic ID**: 8498
**Date**: 2019-09-19
**URL**: https://discourse.slicer.org/t/segmentation-invisible-in-red-view-visible-on-green-and-3d/8498

---

## Post #1 by @JoeCrozier (2019-09-19 16:02 UTC)

<p>As you can see in this video:  <a href="https://1drv.ms/v/s!AnsEucAtFS_SgZVk9CAlzLc-IM6OLw" rel="nofollow noopener">https://1drv.ms/v/s!AnsEucAtFS_SgZVk9CAlzLc-IM6OLw</a></p>
<p>When I segment an area, it shows up in the 3d view, and the color I want shows up on the green view, but on the red view that I’m actually drawing on, it looks like its erasing it.  I checked under the “segmentations” module to see if the opacity somehow got tripped down to zero, its not, and that wouldn’t explain why it was showing up on the green view anyway.  I’ve also closed and reopened 3dslicer and it still does it.</p>
<p>Windows 10,<br>
Slicer 4.11</p>

---

## Post #2 by @cpinter (2019-09-19 16:14 UTC)

<p>I suspect it may be related to the masking options that are set in Segment Editor. Please see <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">here</a> and search for masking.</p>

---

## Post #3 by @lassoan (2019-09-19 18:45 UTC)

<p>From the video it looks like that the drawing is successful and changes are visible in orthogonal views, but not in the red slice view. Most likely cause of this is that the red slice view is positioned exactly at the boundary of two slices. To fix this, hold down Shift key while moving the mouse (not clicking) in an yellow or green slice views near the center of a slice.</p>

---
