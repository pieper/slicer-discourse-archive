---
topic_id: 6624
title: "Cant Change The Windowing Of Ct"
date: 2019-04-27
url: https://discourse.slicer.org/t/6624
---

# Can't change the windowing of CT

**Topic ID**: 6624
**Date**: 2019-04-27
**URL**: https://discourse.slicer.org/t/cant-change-the-windowing-of-ct/6624

---

## Post #1 by @sarvpriya1985 (2019-04-27 16:56 UTC)

<p>Operating system:Windows 10<br>
Slicer version: 4.11<br>
Hi,<br>
I installed the latest nightly build. After importing Dicom data, I am unable to change the windowing of CT sets, though zoom works. It was working fine previously. Also I am unable to work with surface cut in this build. I can just drop fiducial points, but nothing works to select area of interest.</p>
<p>Would appreciate help to fix this.<br>
Thanks,<br>
Sarv</p>

---

## Post #2 by @pieper (2019-04-27 17:56 UTC)

<p>Yes, this is a new thing - you need to enable window/level mode:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e1ae92ceab5266808375ad30ecd11e2be2a11e7.png" alt="image" data-base62-sha1="b8WTJoMlftMHw2d3cugMcR72lfN" width="98" height="49"></p>
<p>Personally, I’m thinking it should be enabled by default for backwards compatibility for long-time users.  Or perhaps the setting should persist across runs.</p>
<p>Here are some polls in case anyone wants to express their opinion:</p>
<p>Should Window/Level mode be on or off by default?</p>
<div class="poll" data-poll-name="default" data-poll-public="true" data-poll-results="always" data-poll-status="open" data-poll-type="regular">
<div class="poll-container">
<ul>
<li data-poll-option-id="758be3054f49dccf2acb5c7f3310b705">Default off (like current nightly)</li>
<li data-poll-option-id="4c70aa1707a478498f388e2c5918479b">Default on like before</li>
</ul>
</div>
<div class="poll-info">
<div class="poll-info_counts">
<div class="poll-info_counts-count">
<span class="info-number">0</span>
<span class="info-label">voters</span>
</div>
</div>
</div>
</div>
<p>Should the state be preserved across runs?</p>
<div class="poll" data-poll-name="persist" data-poll-public="true" data-poll-results="always" data-poll-status="open" data-poll-type="regular">
<div class="poll-container">
<ul>
<li data-poll-option-id="8e46a166708bdf1cc508f6c8909f1f16">Persist across runs</li>
<li data-poll-option-id="54d7cf90d730f0c3f5e82219600345d1">Always reset to default</li>
</ul>
</div>
<div class="poll-info">
<div class="poll-info_counts">
<div class="poll-info_counts-count">
<span class="info-number">0</span>
<span class="info-label">voters</span>
</div>
</div>
</div>
</div>

---

## Post #3 by @lassoan (2019-04-27 18:41 UTC)

<p>Yes, this is a new behavior, but it is necessary because there were <em>many</em> complaints about accidentally change window/level. Accidental changes have become even more frequent since the introduction of the numerous new mouse gestures in markups, slice intersection rotation (Ctrl + Alt + Left-click-and-drag), etc. and a dedicated mouse mode also allows regional auto-window/level (Ctrl + Left-click-and-drag) and reset (double-click).</p>
<p>It requires one single click to switch to window/level adjustment mode. You can also add this single line to your <code>.slicerrc</code> file (menu: Edit / Application settings / Application startup script):</p>
<p><code>slicer.app.applicationLogic().GetInteractionNode().SetCurrentInteractionMode(slicer.vtkMRMLInteractionNode.AdjustWindowLevel)</code></p>

---

## Post #4 by @sarvpriya1985 (2019-04-27 18:48 UTC)

<p>For now I have switched back to 4.10 as 4.11 was crashing and windowing is working fine in it.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #5 by @lassoan (2019-04-27 19:13 UTC)

<p>Slicer-4.11 is under heavy development, so it is expected to be unstable for probably a few months, but window/level adjustment already works better in 4.11:</p>
<ul>
<li>You can easily enable/disable window/level adjustment by clicking on the toolbar</li>
<li>Ctrl + Left-click-and-drag sets optimal window/level based on the selected region</li>
<li>Double-click resets default window/level</li>
</ul>

---

## Post #6 by @JanWitowski (2019-04-30 18:06 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a> I’ve been testing the nightly build and overall impressed with changes, no matter what the default window adjustment mode. I am just wondering if you think the default behavior of Ctrl + Left-click-and-drag should create a region using click origin as the center point of the rectangular region (currently) or should it rather be a corner of created region? For me it seemed a little unintuitive, but you have definitely tested it longer so maybe at the end it will be better.</p>

---

## Post #7 by @lassoan (2019-05-01 03:00 UTC)

<aside class="quote no-group" data-username="JanWitowski" data-post="6" data-topic="6624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/janwitowski/48/4512_2.png" class="avatar"> JanWitowski:</div>
<blockquote>
<p>I am just wondering if you think the default behavior of Ctrl + Left-click-and-drag should create a region using click origin as the center point of the rectangular region (currently) or should it rather be a corner of created region?</p>
</blockquote>
</aside>
<p>First I used first click as corner but it was harder to set the region: I often had to redraw the rectangle because it included too much or not enough of the background. Since starting point was a corner of the rectangle, it was always somewhat off from the point of interest - typically in an empty area. It was hard to remember where exactly I started dragging last time and make a larger or smaller rectangle on the next attempt.</p>
<p>In contrast, I can now start dragging the mouse from the point of interest, which is easy to remember and find again. Therefore, it is easier to resize (and if needed redraw) the rectangle.</p>
<p>I could add Ctrl+Shift+Left-click-and-drag shortcut for drawing rectangle by marking corners if you really want to try it yourself.</p>

---
