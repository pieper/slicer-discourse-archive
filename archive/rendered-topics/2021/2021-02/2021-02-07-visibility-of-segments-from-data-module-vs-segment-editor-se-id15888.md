---
topic_id: 15888
title: "Visibility Of Segments From Data Module Vs Segment Editor Se"
date: 2021-02-07
url: https://discourse.slicer.org/t/15888
---

# Visibility of segments from Data Module vs Segment Editor/Segmentations

**Topic ID**: 15888
**Date**: 2021-02-07
**URL**: https://discourse.slicer.org/t/visibility-of-segments-from-data-module-vs-segment-editor-segmentations/15888

---

## Post #1 by @muratmaga (2021-02-07 23:46 UTC)

<p>When a segment visibility is turned off via Segment Editor (or Segmentations), associated visibility icon in the Data module doesn’t get updated, it stays turned on. The reciprocal case works fine.</p>
<p>It reproduces on windows r29669.</p>

---

## Post #2 by @lassoan (2021-02-08 01:08 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you check this?</p>

---

## Post #3 by @Sunderlandkyl (2021-02-08 02:33 UTC)

<p>Made a PR here: <a href="https://github.com/Slicer/Slicer/pull/5441" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix segment subject hierarchy visibility when display node modified by Sunderlandkyl · Pull Request #5441 · Slicer/Slicer · GitHub</a></p>

---

## Post #4 by @slicer365 (2021-02-08 03:13 UTC)

<p>Yes. This problem does exist, I also found it before, it is out of sync</p>

---

## Post #5 by @slicer365 (2021-02-08 03:19 UTC)

<p>I have provided a video, I hope you can fix this problem, thank you very much.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc9f3707d2c2c59bd0a9db0e860bfebb60c2272.gif" alt="GIF 2021-2-8 11-16-42" data-base62-sha1="zVqwqhpxQCLcsh5Qhc4K1yR3jge" width="517" height="274" class="animated"></p>

---

## Post #6 by @lassoan (2021-02-08 05:41 UTC)

<p>Thanks for reporting, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> fix the issue, it will be available in the Slicer Preview Release on Tuesday.</p>

---
