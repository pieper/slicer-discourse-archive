# JSON file contents questions

**Topic ID**: 14832
**Date**: 2020-12-01
**URL**: https://discourse.slicer.org/t/json-file-contents-questions/14832

---

## Post #1 by @muratmaga (2020-12-01 17:34 UTC)

<p>We discussed this <a href="https://github.com/Slicer/Slicer/issues/5261" rel="noopener nofollow ugc">here</a>, but as far as I can it is not implemented for the latest stable.</p>
<p>Also, what is the purpose of the “orientation” tag?</p>

---

## Post #2 by @lassoan (2020-12-01 18:41 UTC)

<p>Markups measurements are going through a large refactoring (allowing multiple measurements, measurment selection, per-control-point values, use that for coloring, etc.). We’ll get back to <a href="https://github.com/Slicer/Slicer/issues/5261">https://github.com/Slicer/Slicer/issues/5261</a> after <a href="https://github.com/Slicer/Slicer/pull/5322">https://github.com/Slicer/Slicer/pull/5322</a> is integrated.</p>
<p>Orientation allows you to record an orientation (surface normal, digitizer stylus orientation, etc) and use it for orienting point glyphs or use it for various comoutations. Currently it is not used for much and so the implementation is not fully complete. We need to decide to keep it (and fully complete the implementation) or drop it (and remove orientation support completely). We can now store custom per-point values, so we could store orientation there, but it would not automatically transform when the node is transformed, and orientation is not recorded automatically when the point is placed, so it is not a complete replacement yet.</p>

---
