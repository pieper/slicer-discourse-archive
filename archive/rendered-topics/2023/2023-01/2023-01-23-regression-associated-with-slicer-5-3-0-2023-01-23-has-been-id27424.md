---
topic_id: 27424
title: "Regression Associated With Slicer 5 3 0 2023 01 23 Has Been"
date: 2023-01-23
url: https://discourse.slicer.org/t/27424
---

# Regression associated with Slicer 5.3.0 2023-01-23 has been fixed

**Topic ID**: 27424
**Date**: 2023-01-23
**URL**: https://discourse.slicer.org/t/regression-associated-with-slicer-5-3-0-2023-01-23-has-been-fixed/27424

---

## Post #1 by @jcfr (2023-01-23 22:36 UTC)

<p>For future reference, the corresponding regression preventing from starting the application has been identified and fixed in <a href="https://github.com/Slicer/Slicer/pull/6793">PR-6793</a>.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20">  <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a>, <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> and <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2023-01-24 00:06 UTC)

<p>Thanks for the fix. It was my mistake, I touched up a pull request with a seemingly innocent QString formatting change and there was no build error. I didn’t expect that QString::arg could fail completely at runtime like this.</p>

---

## Post #3 by @jcfr (2023-01-24 00:15 UTC)

<p>The root cause of the crash was the missing return statement fixed in <a href="https://github.com/Slicer/Slicer/commit/cffc0f3e4757d72e0649f696639059058e77f0e4">Slicer@cffc0f3e4</a></p>
<p>The problematic <code>.arg()</code> fixed in <a href="https://github.com/Slicer/Slicer/commit/08fe346009554f82e63e7d7aaaaec06c16f0a233">Slicer@08fe34600</a> was found out while investigating and would have likely (only) returned an invalid string.</p>

---
