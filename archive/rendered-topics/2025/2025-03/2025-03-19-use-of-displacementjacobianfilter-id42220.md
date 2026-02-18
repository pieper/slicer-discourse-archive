# Use of displacementJacobianFilter

**Topic ID**: 42220
**Date**: 2025-03-19
**URL**: https://discourse.slicer.org/t/use-of-displacementjacobianfilter/42220

---

## Post #1 by @Posiz (2025-03-19 13:57 UTC)

<p>Hi experts.</p>
<p>I am trying to use the displacementJacobianFilter within simple filters for a displacement field obtained from a deformable registration. The problem is that it seems that the simple filter does not accept vector volumes. What Should I do?</p>
<p>thanks a lot.</p>

---

## Post #2 by @pieper (2025-03-19 20:17 UTC)

<p>You could have a look in the SimpleFilters source code and see if you can add the feature, or you could access simpleitk directly from python code.</p>

---
