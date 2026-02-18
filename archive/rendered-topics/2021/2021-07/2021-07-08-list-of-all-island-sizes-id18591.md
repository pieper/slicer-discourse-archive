# List of all island sizes?

**Topic ID**: 18591
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/list-of-all-island-sizes/18591

---

## Post #1 by @hherhold (2021-07-08 20:35 UTC)

<p>Is there an incantation in vtk (maybe in vtkIslandMath?) that will give a list of the sizes of all islands?</p>

---

## Post #2 by @pieper (2021-07-08 21:17 UTC)

<p>Wouldn’t you just use Segment Statistics for that?</p>

---

## Post #3 by @lassoan (2021-07-09 05:58 UTC)

<p>Yes, you can split islands to segments (using Islands effect) and then use Segment Statistics. You may run into performance issues if you have thousands of segments. In this case it may be better to run the filters from a Python script.</p>

---

## Post #4 by @hherhold (2021-07-09 12:04 UTC)

<p>Yeah, it’s potentially thousands of islands. I’ll look through the code in <code>SegmentEditorIslandsEffect.py</code> - thanks for the pointer to Islands effect!</p>
<p>-Hollister</p>

---
