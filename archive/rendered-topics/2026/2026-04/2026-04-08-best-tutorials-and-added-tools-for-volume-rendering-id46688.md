---
topic_id: 46688
title: "Best tutorials and added tools for volume rendering"
date: 2026-04-08
url: https://discourse.slicer.org/t/46688
last_bumped: 2026-04-09T21:52:48.070Z
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

## Post #5 by @muratmaga (2026-04-09 04:27 UTC)

<p>I don’t think there is a good tutorial explaining how to use volume rendering and all it has to offer in detail, using specific examples. As <a class="mention" href="/u/pieper">@pieper</a> pointed out Slicermorph do have some basic tutorials that’s more comprehensive then the user documentation (which simply points out what certain buttons do).</p>
<p>It would be great if somebody develops a comprehensive tutorial for volume rendering illustrating the features.</p>
<p>And it would be even better if we can share custom volume rendering properties.</p>

---

## Post #6 by @sulli419 (2026-04-09 20:59 UTC)

<p>Yes, a repository of custom volume properties would also be quite useful; at least as a way to see how creative people can get with the existing features.</p>

---

## Post #7 by @muratmaga (2026-04-09 21:52 UTC)

<p>I am prototyping a test. More details here: <a href="https://discourse.slicer.org/t/sharing-custom-presets/46690/4" class="inline-onebox">Sharing custom presets - #4 by muratmaga</a></p>

---
