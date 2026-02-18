# "Constrain points to surface" feature 

**Topic ID**: 36632
**Date**: 2024-06-07
**URL**: https://discourse.slicer.org/t/constrain-points-to-surface-feature/36632

---

## Post #1 by @taylorfisher (2024-06-07 01:18 UTC)

<p>Operating system: 3D Slicer<br>
Slicer version: 5.6.1<br>
Expected behavior: My colleague has an older version of 3D slicer. In Markups → Resample section he has an option of “constrain points to surface”<br>
Actual behavior: I cannot seem to locate a similar feature in my version (5.6.1) and was wondering if this feature was disable or moved? If so, where could I find it or constrain my landmarks in a similar fashion?</p>
<p>For transparency, I am very new to 3D slicer. Appreciate the help!</p>

---

## Post #2 by @lassoan (2024-06-07 01:27 UTC)

<aside class="quote no-group" data-username="taylorfisher" data-post="1" data-topic="36632">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/b487fb/48.png" class="avatar"> taylorfisher:</div>
<blockquote>
<p>My colleague has an older version of 3D slicer. In Markups → Resample section he has an option of “constrain points to surface”</p>
</blockquote>
</aside>
<p>Constraining options are moved out from the resampling section to <code>Curve settings</code> section because constraining is no longer limited to be used during resampling but is applied to the curve continuously.</p>
<p>Constraining was also greatly improved: you can not only project the curve to the surface but you can also place just a few points and find shortest path on the surface (optionally taking into account surface data, e.g., to avoid or prefer certain regions).</p>

---

## Post #3 by @taylorfisher (2024-06-09 23:14 UTC)

<p>Thank you, appreciate that information very much!</p>

---
