# Fast Marching gone for good

**Topic ID**: 10059
**Date**: 2020-02-01
**URL**: https://discourse.slicer.org/t/fast-marching-gone-for-good/10059

---

## Post #1 by @three_wise_surgeons (2020-02-01 09:43 UTC)

<p>Hi there… after a while segmenting manually, I’ve tried to find Fast Marching button… and it’s gone…</p>
<p>Should i install it from ext. manager or the latest nightly build version for mac doesn´t has it?</p>
<p>And the simple filters… crash when trying to Apply changes… anyone having this problem?</p>
<p>Thanks<br>
F Fusaro</p>

---

## Post #2 by @lassoan (2020-02-01 13:31 UTC)

<p>Fast marching has always been part of SegmentEditorExtraEffects extension.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> can you confirm that SimpleFilters is crashing on Mac? (it works well on Windows)</p>

---

## Post #3 by @jamesobutler (2020-02-01 14:41 UTC)

<p>Regarding SimpleFilters which uses SimpleITK, I don’t believe the issue on Mac as described here has been addressed. <a href="https://discourse.slicer.org/t/sitkutils-pullvolumefromslicer-makes-slicer-crash/9781/2" class="inline-onebox">sitkUtils.PullVolumeFromSlicer makes Slicer crash</a></p>

---

## Post #4 by @pieper (2020-02-01 16:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> can you confirm that SimpleFilters is crashing on Mac? (it works well on Windows)</p>
</blockquote>
</aside>
<p>Yes, SimpleFilters still crashes on mac with the most current Preview build (downloaded today).   My local debug build does not crash for the same operations.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="10059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Regarding SimpleFilters which uses SimpleITK, I don’t believe the issue on Mac as described here has been addressed. <a href="https://discourse.slicer.org/t/sitkutils-pullvolumefromslicer-makes-slicer-crash/9781/2">sitkUtils.PullVolumeFromSlicer makes Slicer crash </a></p>
</blockquote>
</aside>
<p>Yes, the behavior and stack trace is identical to what is reported in that issue.</p>

---

## Post #5 by @lassoan (2020-02-01 16:14 UTC)

<p>Thanks for confirming. Then let’s continue the discussion in that topic - <a href="https://discourse.slicer.org/t/sitkutils-pullvolumefromslicer-makes-slicer-crash/9781/2" class="inline-onebox">sitkUtils.PullVolumeFromSlicer makes Slicer crash</a></p>

---
