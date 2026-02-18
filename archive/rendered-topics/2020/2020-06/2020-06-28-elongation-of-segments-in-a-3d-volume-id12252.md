# Elongation of segments in a 3D volume

**Topic ID**: 12252
**Date**: 2020-06-28
**URL**: https://discourse.slicer.org/t/elongation-of-segments-in-a-3d-volume/12252

---

## Post #1 by @Deepa (2020-06-28 14:40 UTC)

<p>Hello Everyone,</p>
<p>I’ve a 3D volume like the following<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5aff7d06b6475433fc086522d62bd45865d1ae.png" alt="Untitled" data-base62-sha1="mASoXMLL9PkI1N9CIci9Zx61iLc" width="130" height="178"></p>
<p>I would like to elongate all the vessel segments (say, by a factor of 5 times the current length).<br>
Is there a way to elongate the vessel segments in Slicer?</p>

---

## Post #2 by @lassoan (2020-06-28 16:06 UTC)

<p>You can scale the entire segmentation along an axis by applying a linear transform in Transformation module. Scaling factors are the first three values in the diagonal matrix.</p>

---

## Post #3 by @Deepa (2020-06-29 16:14 UTC)

<p>Thanks a lot . I’d like to know if scaling can alter the thickness of the vessel segments too. I’d like to scale only the lengths.</p>

---

## Post #4 by @lassoan (2020-06-30 15:32 UTC)

<p>Of course, scaling affects everything. Unless all the vessels are parallel, you cannot change their lengths without affecting their thickness.</p>

---

## Post #5 by @Deepa (2020-06-30 15:57 UTC)

<p>Thanks a lot for the clarification</p>

---

## Post #6 by @sandress (2020-07-01 20:14 UTC)

<p>You can use the margin effect in the segment editor to grow or shrink your segmentation, this would affect the thickness of the vessels too.</p>

---
