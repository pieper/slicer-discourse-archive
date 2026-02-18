# How to judge a roinode changed or not by python code?

**Topic ID**: 22393
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/how-to-judge-a-roinode-changed-or-not-by-python-code/22393

---

## Post #1 by @jumbojing (2022-03-09 03:12 UTC)

<p>How to judge a roinode changed or not?</p>
<p>markupsROInode 可以很方便地在slice里调节大小, 我想在程序里判断这个node是否发生改变, 我该怎么做呢?</p>
<blockquote>
<p>markupsROInode can easily adjust the size in slice, I want to judge whether this node has changed or not in the program, what should I do?</p>
</blockquote>

---

## Post #2 by @lassoan (2022-03-09 06:20 UTC)

<p>Can you tell a bit more about your use case? Do you want to prevent changes, get notified about changes when they happen, or just want to check at some point that the ROI was changed compared to some previous state?</p>

---

## Post #3 by @jumbojing (2022-03-09 07:03 UTC)

<p>I “want to check at some point that the ROI was changed compared to some previous state”.</p>

---

## Post #4 by @lassoan (2022-03-09 07:08 UTC)

<p>The simplest is to check the modification time of the MRML node (you can get it by calling <code>node.GetMTime()</code>). Any modification of the node will make the timestamp value larger.</p>
<p>If you need to be more specific, for example only check control point position changes: you can then save the old positions in a variable and compare it to the current positions when you want to check if there were modifications.</p>

---

## Post #5 by @yuvsaha123 (2022-03-15 11:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22393" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The simplest is to check the modification time of the MRML node (you can get it by calling <code>node.GetMTime()</code> ). Any modification of the node will make the timestamp value larger.</p>
<p>If you need to be more specific, for example only check control point position changes: you can then save the old positions in a variable and compare it to the current positions when you want to check if there were modifications.</p>
</blockquote>
</aside>
<p>thanks for the awesome information.</p>

---
