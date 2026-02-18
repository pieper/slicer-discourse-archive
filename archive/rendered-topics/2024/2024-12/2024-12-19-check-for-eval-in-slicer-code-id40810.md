# Check for eval in Slicer code

**Topic ID**: 40810
**Date**: 2024-12-19
**URL**: https://discourse.slicer.org/t/check-for-eval-in-slicer-code/40810

---

## Post #1 by @pieper (2024-12-19 19:59 UTC)

<p>We should do a similar check for eval in our dicom code, and probably in all the rest of our python as a sanity check.</p>
<p><a href="https://github.com/pydicom/pydicom/issues/2193#issue-2751187573">https://github.com/pydicom/pydicom/issues/2193#issue-2751187573</a></p>
<p>Like the CLI they mention in pydicom, and application is less of a global security threat but an exploited dicom (or other) file would be a bad thing in any case.</p>
<p>I did a search and didn’t see any inappropriate evals in our python code (only in either controlled contexts or where the intent is to let the user execute code).</p>
<p>-Steve</p>

---
