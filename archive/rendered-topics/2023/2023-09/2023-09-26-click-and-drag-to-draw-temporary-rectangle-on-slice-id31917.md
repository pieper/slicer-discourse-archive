# Click-and-Drag to draw temporary rectangle on slice

**Topic ID**: 31917
**Date**: 2023-09-26
**URL**: https://discourse.slicer.org/t/click-and-drag-to-draw-temporary-rectangle-on-slice/31917

---

## Post #1 by @Dieter_Rosch (2023-09-26 18:45 UTC)

<p>Hi,</p>
<p>I’m fairly new to Slicer and am working on a plugin for segmentation with a 3rd party tool. One of the functions I want, is to press a button on my plugin, then to use click and drag in a slice to create a rectangular section. I then want to retrieve the top-left and bottom-right (i.e. drag start and drag end positions) and remove the temporary rectangle. I see the scissors tool in segmentation editor has this capability, and have looked at the C++ code, but I can’t figure out a way to do this from Python.</p>
<p>I feel that I am missing something obvious, since this seems a fairly elementary thing to try to do. I’ve searched the recipes and forums, but can’t find anything like this.</p>

---
