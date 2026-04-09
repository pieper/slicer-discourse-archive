---
topic_id: 46688
title: "Best Tutorials And Added Tools For Volume Rendering"
date: 2026-04-08
url: https://discourse.slicer.org/t/46688
---

# Best tutorials and added tools for volume rendering

**Topic ID**: 46688
**Date**: 2026-04-08
**URL**: https://discourse.slicer.org/t/best-tutorials-and-added-tools-for-volume-rendering/46688

---

## Post #1 by @sulli419 (2026-04-08 22:23 UTC)

<p>The flexibility of the volume rendering feature is quite impressive, and it seems like this would be useful for finding things in 3D (not just making them pretty).  Are there any good expert tutorials that go through how to optimize color and opacity schemes?</p>
<p>I was also dreaming up a tools where you could draw around objects/subregions in 2D or 3D, and then use the histogram here for pointing different colors/opacities at the dominant pixel values of interest. Does such a feature/extension exist?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2026-04-08 22:42 UTC)

<p>You may be interested in the <a href="https://github.com/SlicerMorph/Tutorials/blob/main/ColorizeVolume/README.md">ColorizeVolume</a> module.</p>
<p>Also there’s this tutorial in <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Slicer_Modules/Volume_Rendering/README.MD">SlicerMorph</a>.</p>

---

## Post #3 by @sulli419 (2026-04-08 23:15 UTC)

<p>Thanks.  These are helpful.  I haven’t tried Colorize Volume yet, but exploiting segmentations is a clever trick.  However, at least in the example it doesn’t look like you can independently tweak each segmented piece with its own volume render color scheme (just a solid color?).  I bet you could make some very stunning images combining a “regional volume render” with total segmentor.</p>

---

## Post #4 by @pieper (2026-04-08 23:33 UTC)

<p>Yes, Colorize Volume has lots of untapped potential.  Right now you can control some aspects of the per-segment rendering, but not everything.  It’s traditionally been tricky and time consuming to make good user interfaces for controlling such things.  Maybe now in the age of LLMs we can do better.</p>

---
