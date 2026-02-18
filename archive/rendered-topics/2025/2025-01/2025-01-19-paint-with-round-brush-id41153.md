# Paint with round brush

**Topic ID**: 41153
**Date**: 2025-01-19
**URL**: https://discourse.slicer.org/t/paint-with-round-brush/41153

---

## Post #1 by @Tobias_Koffer (2025-01-19 13:25 UTC)

<p>Hi, I have to segment a laryngeal tumor, but the paint function doesnt work on the tumor tissue, in other words, it doesnt recognize the tissue? Is there a better tool for tumor segmentation in that area?<br>
Thank you</p>

---

## Post #2 by @lassoan (2025-01-19 13:30 UTC)

<p>Tumors can often be quickly and accurately segmented using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds"><code>Grow from seeds</code></a> effect. Just paint a scribble inside and outside the tumor in two orthogonal slices and click <code>Initialize</code> to see a preview. Then review and make corrections as needed (by drawing additional scribbles).</p>

---
