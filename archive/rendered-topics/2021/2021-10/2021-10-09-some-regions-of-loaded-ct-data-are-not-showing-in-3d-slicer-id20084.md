---
topic_id: 20084
title: "Some Regions Of Loaded Ct Data Are Not Showing In 3D Slicer"
date: 2021-10-09
url: https://discourse.slicer.org/t/20084
---

# Some regions of loaded CT data are not showing in 3d slicer

**Topic ID**: 20084
**Date**: 2021-10-09
**URL**: https://discourse.slicer.org/t/some-regions-of-loaded-ct-data-are-not-showing-in-3d-slicer/20084

---

## Post #1 by @Sliceeeeee (2021-10-09 16:41 UTC)

<p>When I am loading the data into 3d slicer some of its regions are not showing , but somehow when I am changing the master volume that regions are showing but I am not able to paint(Or edit them ) . Please help me in this</p>

---

## Post #2 by @lassoan (2021-10-09 19:44 UTC)

<p>Extent of the segmentation is specified by the master volume that you selected first. See instructions for changing it <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>.</p>
<p>To show a volume in a slice view in full, you can click the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">reset field of view button</a>. If you switch to a recent Slicer Preview Release then clicking the eye icon in Data module will show the entire volume by default (no need to click the reset field of view button).</p>

---
