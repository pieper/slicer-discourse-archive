---
topic_id: 21069
title: "Loading Mrml Files Fails And Stalls"
date: 2021-12-15
url: https://discourse.slicer.org/t/21069
---

# Loading mrml files fails and stalls

**Topic ID**: 21069
**Date**: 2021-12-15
**URL**: https://discourse.slicer.org/t/loading-mrml-files-fails-and-stalls/21069

---

## Post #1 by @lucast4 (2021-12-15 05:33 UTC)

<p>Loading an MRML file (by dragging and dropping) stalls. The progress bar will reach a specific number (e…g, 99%) and won’t load. Then usually Slicer will crash. I have on the order of 10s to couple hundred objects that are included in this load (e.g., markups, segmentations, columns, transforms).<br>
It loads fine if I separately load all the objects (not using the scene, but using drag and drop<br>
What might cause this?</p>

---

## Post #2 by @pieper (2021-12-16 00:06 UTC)

<p>There could be some other information in the scene file that leads to an error condition or slow loading / memory use.  You could look in the error log for any clues.  If you can reproduce the issue on public data or can share a scene that replicates the issue then someone could have a look.</p>

---

## Post #3 by @lucast4 (2021-12-16 14:18 UTC)

<p>Thanks, I ended up loading the individual objects and recreating the scene. If it happens again I’ll dig into it more</p>

---

## Post #4 by @lassoan (2021-12-16 18:25 UTC)

<p>Recent Slicer Preview Releases do thorough error checking and reporting during loading, so next time you run into an issue you may get more information by using a new Slicer version.</p>

---
