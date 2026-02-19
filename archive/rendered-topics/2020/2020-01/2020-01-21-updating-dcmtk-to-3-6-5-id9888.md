---
topic_id: 9888
title: "Updating Dcmtk To 3 6 5"
date: 2020-01-21
url: https://discourse.slicer.org/t/9888
---

# Updating DCMTK to 3.6.5

**Topic ID**: 9888
**Date**: 2020-01-21
**URL**: https://discourse.slicer.org/t/updating-dcmtk-to-3-6-5/9888

---

## Post #1 by @fedorov (2020-01-21 03:33 UTC)

<p>Last time Slicer DCMTK was updated was over a year ago, and I would like to update to the latest 3.6.5 release. Currently, Slicer is using a <a href="https://github.com/commontk/DCMTK/commits/patched-DCMTK-3.6.3_20180621">patched version of DCMTK</a>, but the only patch applied is this, as I understand: <a href="https://github.com/commontk/DCMTK/commit/e79118cd2f40b77654630a56bbb17fe0bccc354c">https://github.com/commontk/DCMTK/commit/e79118cd2f40b77654630a56bbb17fe0bccc354c</a>.</p>
<p>It looks like DCMTK 3.6.5 already has this policy applied, see <a href="http://git.dcmtk.org/?p=dcmtk.git;a=commit;h=09d352dd240f36451107665ddece85f9809f4d01">http://git.dcmtk.org/?p=dcmtk.git;a=commit;h=09d352dd240f36451107665ddece85f9809f4d01</a>.</p>
<p>Any objections to trying this out? Should we just update Slicer to check out 3.6.5 from <a href="http://git.dcmtk.org/">http://git.dcmtk.org/</a>, or there is a good reason to keep a fork on GitHub?</p>

---

## Post #2 by @fedorov (2020-01-21 19:21 UTC)

<p>PR submitted and is green on CircleCI:</p>
<p><a href="https://github.com/Slicer/Slicer/pull/1308">https://github.com/Slicer/Slicer/pull/1308</a> (corrected)</p>

---

## Post #3 by @dzenanz (2020-01-21 21:46 UTC)

<p>Correct PR number is <a href="https://github.com/Slicer/Slicer/pull/1308" rel="nofollow noopener">1308</a>.</p>

---

## Post #4 by @lassoan (2020-01-22 00:57 UTC)

<p>Thank you <a class="mention" href="/u/fedorov">@fedorov</a>. We are very busy with many things at the project week now but if it’s not that urgent then I would test it on Windows next week.</p>

---

## Post #5 by @fedorov (2020-01-22 01:14 UTC)

<p>Andras, that sounds good, thank you!</p>

---

## Post #6 by @fedorov (2020-02-04 16:26 UTC)

<p>Any updates on this topic and the corresponding PR? Anything else I can do to expedite this?</p>

---

## Post #7 by @fedorov (2020-02-11 13:38 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for testing on Windows and merging! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
