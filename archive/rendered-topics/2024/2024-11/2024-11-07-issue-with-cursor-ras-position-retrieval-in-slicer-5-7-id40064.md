---
topic_id: 40064
title: "Issue With Cursor Ras Position Retrieval In Slicer 5 7"
date: 2024-11-07
url: https://discourse.slicer.org/t/40064
---

# Issue with Cursor RAS Position Retrieval in Slicer 5.7

**Topic ID**: 40064
**Date**: 2024-11-07
**URL**: https://discourse.slicer.org/t/issue-with-cursor-ras-position-retrieval-in-slicer-5-7/40064

---

## Post #1 by @park (2024-11-07 07:53 UTC)

<p>Hi all,</p>
<p>I’m trying to retrieve the cursor’s RAS position using the following code:</p>
<pre><code class="lang-auto">ras = [0, 0, 0]
crosshairNode.GetCursorPositionRAS(ras)
</code></pre>
<p>In <strong>Slicer 5.6</strong>, when the cursor was positioned over the <code>modelNode</code>, it would return the coordinates on that <code>modelNode</code>. However, in <strong>5.7</strong>, even when the cursor is over the <code>modelNode</code>, it instead returns coordinates from the camera plane.</p>
<p>Could you please let me know if there were any updates or changes in this new version that could explain this behavior?</p>
<p>Thank you!</p>

---

## Post #2 by @Sunderlandkyl (2024-11-07 18:39 UTC)

<p>It’s possible that this pull request could fix the issue: <a href="https://github.com/Slicer/Slicer/pull/8021" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix issue preventing interacting with Markups curves by Sunderlandkyl · Pull Request #8021 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @park (2024-11-08 00:33 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="40064">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>pull request</p>
</blockquote>
</aside>
<p>Thank you for the response <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>.<br>
Is there a way to resolve this issue in Python before the pull request is merged?</p>

---

## Post #4 by @Sunderlandkyl (2024-11-12 19:33 UTC)

<p>PR is now merged. The fix should be available in tomorrows preview release.</p>

---
