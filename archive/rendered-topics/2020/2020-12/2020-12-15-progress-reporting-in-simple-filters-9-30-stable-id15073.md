# Progress reporting in Simple Filters? (9-30 Stable)

**Topic ID**: 15073
**Date**: 2020-12-15
**URL**: https://discourse.slicer.org/t/progress-reporting-in-simple-filters-9-30-stable/15073

---

## Post #1 by @hherhold (2020-12-15 13:34 UTC)

<p>I just checked through the post history and didn’t seen an update on this…?</p>
<p>Is progress reporting supposed to be working in Simple Filters? (Running 9-30 latest stable on MacOS)</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2020-12-15 14:16 UTC)

<p>SimpleFilters progress bar works for me (also on mac with 4.11-9-30).  What filter are you applying?</p>

---

## Post #3 by @hherhold (2020-12-15 14:17 UTC)

<p>BinaryThinningImageFilter. Input volume is a volume, output is a labelmap. Taking a while.</p>

---

## Post #4 by @lassoan (2020-12-15 16:37 UTC)

<p>If you have problems with progress reporting in a specific filter then let ITK developers know - it may be an easy fix.</p>
<p>Nevertheless, binary thinning may take forever!, so I would suggest to use VMTK-s centerline extraction instead, which usually takes just seconds and provides a network or a tree that is ready for further processing.</p>

---

## Post #5 by @hherhold (2020-12-16 14:16 UTC)

<p>Got it, thanks Andras. I think this was covered elsewhere, but I think you can use the Voronoi diagram to subsequently do a probe volume with model operation to color a model by radius? (Similar to Danielsson distance image filter).</p>

---

## Post #6 by @lassoan (2020-12-16 14:22 UTC)

<p>The Voronoi model already contains the radius. You can probably use it to color the original model surface, if that’s the goal. If it is not easy to figure out how to do it then post a question to <a href="https://discourse.slicer.org/c/community/vmtk/28">VMTK category</a>.</p>

---

## Post #7 by @hherhold (2020-12-16 14:38 UTC)

<p>Awesome, thanks, as always!</p>
<p>Hope you’re doing well.</p>
<p>-Hollister</p>

---
