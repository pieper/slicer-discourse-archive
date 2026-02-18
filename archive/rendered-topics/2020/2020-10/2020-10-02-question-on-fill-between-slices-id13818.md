# Question on Fill between slices

**Topic ID**: 13818
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/question-on-fill-between-slices/13818

---

## Post #1 by @Deepa (2020-10-02 14:18 UTC)

<p>Hello Everyone,</p>
<p>I’ve reconstructed a 3D volume using 2D slices. Next, in the segment editor I have used <code>Scissors</code><br>
to cut out a sub-volume. When I try to trace vessel connections visually, I find that sometimes the vessel points are disconnected (looks like broken vessel). I would like to know if <code>Fill between Slices</code> can be used in such cases to create continuous vessel segments.</p>

---

## Post #2 by @lassoan (2020-10-02 23:58 UTC)

<p>“Fill between slices” ignores regions that already have multiple neighbor slices segmented (you need to skip at least one slice empty on both sides of a segmented slice), so this effect will not connect fractured vessel segments.</p>
<p>If discontinuities are short then Smoothing effect may fix them. If larger pieces are missing then you can use “Draw tube” effect (provided by SegmentEditorExtraEffects extension) to draw them manually.</p>

---
