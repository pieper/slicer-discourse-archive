---
topic_id: 32309
title: "How To Unload A Volume From The 3D View"
date: 2023-10-18
url: https://discourse.slicer.org/t/32309
---

# How to unload a volume from the 3D View

**Topic ID**: 32309
**Date**: 2023-10-18
**URL**: https://discourse.slicer.org/t/how-to-unload-a-volume-from-the-3d-view/32309

---

## Post #1 by @Deep_Learning (2023-10-18 18:10 UTC)

<p>After dragging a volume/node to the 3D view for volume rendering, is it possible to remove/unload it with the mouse?</p>
<p>I want it to be visible in the 2D views, just not rendered, so turning off visibility is not an option.</p>

---

## Post #2 by @pieper (2023-10-18 18:13 UTC)

<p>Right click on the eye column and uncheck volume rendering<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/973414dc7f21969255baa8b314c508c65e5f0d40.jpeg" data-download-href="/uploads/short-url/lzBGi2Yw6IJsloSdVIlp81d1gZi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973414dc7f21969255baa8b314c508c65e5f0d40_2_690x171.jpeg" alt="image" data-base62-sha1="lzBGi2Yw6IJsloSdVIlp81d1gZi" width="690" height="171" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973414dc7f21969255baa8b314c508c65e5f0d40_2_690x171.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973414dc7f21969255baa8b314c508c65e5f0d40_2_1035x256.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/973414dc7f21969255baa8b314c508c65e5f0d40_2_1380x342.jpeg 2x" data-dominant-color="D4D8DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1542×384 90.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Deep_Learning (2023-10-18 18:34 UTC)

<p>Thank you.  Never thought of right clicking the eye…</p>

---

## Post #4 by @Deep_Learning (2023-10-26 13:51 UTC)

<p>Are there options for Multi 3D views?  Python only?</p>
<p>Can I not show a volume in View1, but in View 2?</p>

---

## Post #5 by @pieper (2023-10-26 13:58 UTC)

<p>You can set the ViewNodeIDs on the display nodes, like you can do with the GUI menus.</p>
<p>Like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #6 by @Deep_Learning (2023-10-26 16:45 UTC)

<p>Thank you,<br>
Where can I control the individual ViewNodeIDs  in the GUI?<br>
I looked under nodes and Volumes…</p>

---

## Post #7 by @lassoan (2023-10-26 17:36 UTC)

<p>Volumes in 3D views are displayed by Volume Rendering module. You can select views of n that module.</p>
<p>However, you may find it easier to drag-and-drop the volume from the tree in Data module to each 3D view you want it to appear in.</p>

---
