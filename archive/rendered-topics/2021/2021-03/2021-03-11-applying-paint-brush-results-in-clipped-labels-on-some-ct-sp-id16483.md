# Applying paint brush results in clipped labels on some CT spine volumes

**Topic ID**: 16483
**Date**: 2021-03-11
**URL**: https://discourse.slicer.org/t/applying-paint-brush-results-in-clipped-labels-on-some-ct-spine-volumes/16483

---

## Post #1 by @Ron (2021-03-11 22:09 UTC)

<p>Operating system: Win 10<br>
Slicer version:4.11<br>
Expected behavior: Be able to mark the full vertebral anatomy<br>
Actual behavior: Using the paintbrush tool in the segment editor, label maps seem to be “clipped” anteriorly ( see L5-L3).  The volume was cropped and the voxel set to iso ( 0.3125^2, 0.5) to (0.3125^3). Happy to load up an image, but I do not see how.  This is likely a setting I am missing.  Goel is to use grow from seeds.  My first of many Q :). Thanks, Ron</p>

---

## Post #2 by @lassoan (2021-03-24 15:58 UTC)

<p>See this documentation section on <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">how to specify correct extents for your segmentation</a>.</p>

---
