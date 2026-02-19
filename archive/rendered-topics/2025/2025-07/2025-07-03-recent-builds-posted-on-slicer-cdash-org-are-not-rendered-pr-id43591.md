---
topic_id: 43591
title: "Recent Builds Posted On Slicer Cdash Org Are Not Rendered Pr"
date: 2025-07-03
url: https://discourse.slicer.org/t/43591
---

# Recent builds posted on slicer.cdash.org are not rendered properly

**Topic ID**: 43591
**Date**: 2025-07-03
**URL**: https://discourse.slicer.org/t/recent-builds-posted-on-slicer-cdash-org-are-not-rendered-properly/43591

---

## Post #1 by @jcfr (2025-07-03 15:00 UTC)

<p>This issue is now tracked here: <a href="https://github.com/Kitware/CDash/issues/2970">https://github.com/Kitware/CDash/issues/2970</a></p>
<h3><a name="p-126476-expected-behavior-1" class="anchor" href="#p-126476-expected-behavior-1" aria-label="Heading link"></a>Expected Behavior</h3>
<p>The “Nightly-Packages” section of the CDash project page should consistently display all expected builds for a given day. For example, all 3 builds (<code>metroplex.kitware</code>, <code>bluestreak.kitware</code>, and <code>computron.kitware</code>) should be visible each day if they were submitted.</p>
<h3><a name="p-126476-actual-behavior-2" class="anchor" href="#p-126476-actual-behavior-2" aria-label="Heading link"></a>Actual Behavior</h3>
<p>On July 1st, 2025, two builds (<code>bluestreak.kitware</code> and <code>computron.kitware</code>) are properly listed under “Nightly-Packages,” showing detailed results including Update, Configure, Build, and Test status.</p>
<h4><a name="p-126476-screenshots-3" class="anchor" href="#p-126476-screenshots-3" aria-label="Heading link"></a>Screenshots</h4>
<ul>
<li>
<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> July 1st: Summary <strong>and</strong> detailed build/test data visible</p>
<p><img src="https://github.com/user-attachments/assets/035789b8-0aea-48cc-a172-0b1724f2641b" alt="Image" width="690" height="110"></p>
</li>
<li>
<p><img src="https://emoji.discourse-cdn.com/twitter/cross_mark.png?v=15" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> July 3rd: Only summary rows visible, no details<br>
<img src="https://github.com/user-attachments/assets/b9fc17ea-0d71-426a-80ce-c25ed9722703" alt="Image" width="690" height="120"></p>
</li>
</ul>

---

## Post #2 by @jcfr (2025-07-03 16:41 UTC)

<p>Issue has been addressed and build reports are now listed as expected.</p>
<blockquote>
<p>[CDash is now all caught up on parsing submissions again.</p>
<p>the asynchronous submission parsers were paused during a recent upgrade and are not re-enabled</p>
</blockquote>
<p><em>Source: <a href="https://github.com/Kitware/CDash/issues/2970#issuecomment-3032731385">https://github.com/Kitware/CDash/issues/2970#issuecomment-3032731385</a></em></p>

---
