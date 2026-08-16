---
topic_id: 47870
title: "Analyzer Results in report Extended analysis (Table 2) all results are zero (0)."
date: 2026-08-12
url: https://discourse.slicer.org/t/47870
last_bumped: 2026-08-15T23:46:32.551Z
---

# Analyzer Results in report Extended analysis (Table 2) all results are zero (0).

**Topic ID**: 47870
**Date**: 2026-08-12
**URL**: https://discourse.slicer.org/t/analyzer-results-in-report-extended-analysis-table-2-all-results-are-zero-0/47870

---

## Post #1 by @yilinguo256 (2026-08-12 19:36 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> How to solve this problem? Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d70649370c72eadb698aa1b82fcc974967975f43.png" data-download-href="/uploads/short-url/uGc7G0tACULZ3bJ0rNDiv8fPi7N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d70649370c72eadb698aa1b82fcc974967975f43.png" alt="image" data-base62-sha1="uGc7G0tACULZ3bJ0rNDiv8fPi7N" width="690" height="316" data-dominant-color="EFF3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×366 7.02 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c56a53f02729007d77aa92197f68d8c0b0fff4e8.png" data-download-href="/uploads/short-url/sapRP2IX5KItGfwbRSmbNZfRhpK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c56a53f02729007d77aa92197f68d8c0b0fff4e8.png" alt="image" data-base62-sha1="sapRP2IX5KItGfwbRSmbNZfRhpK" width="690" height="140" data-dominant-color="F3F6F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1567×318 9.22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @aiden.zhu (2026-08-15 23:46 UTC)

<p>This is a known bug in newer releases of 3D Slicer caused by recent API/dependency updates within the extension’s scripting interface.</p>
<p><strong>Downgrade to Slicer 5.6.2:</strong> Community testing shows that reverting to <strong>3D Slicer 5.6.2</strong> resolves the bug, allowing Table 2 to compute and output proper volume values as expected.</p>
<p><strong>or</strong></p>
<p><strong>Check for Extension Updates:</strong> Open the <strong>Extension Manager</strong> in 3D Slicer and ensure <code>LungCTAnalyzer</code> is updated to the latest available patch, as fixes for output parsing are routinely pushed.</p>

---
