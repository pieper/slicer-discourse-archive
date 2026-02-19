---
topic_id: 557
title: "Keystrokes From Editor To Segment Editor"
date: 2017-06-22
url: https://discourse.slicer.org/t/557
---

# Keystrokes from Editor to Segment Editor

**Topic ID**: 557
**Date**: 2017-06-22
**URL**: https://discourse.slicer.org/t/keystrokes-from-editor-to-segment-editor/557

---

## Post #1 by @MMMPPPMMM (2017-06-22 20:57 UTC)

<p>Would it be possible to transfer all Keystrokes from the Editor:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Editor" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Editor</a><br>
to the SegmentEditor<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentEditor" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentEditor</a><br>
?</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2017-06-22 21:16 UTC)

<p>The Segment editor has more shortcuts and they are optimized for blind one-handed use. See complete list here: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>

---

## Post #3 by @MMMPPPMMM (2017-06-23 06:12 UTC)

<p>Thanks for the hint <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>
<p>I’ll try out and give some feedback.</p>

---

## Post #4 by @MMMPPPMMM (2017-06-28 07:56 UTC)

<p>Works great. Thank you.</p>
<p>I think there is only a bug that the view is reset to the default view if you use the Segment Editor for the first time or switch between different Segmentations?</p>

---

## Post #5 by @lassoan (2017-06-28 09:05 UTC)

<p>Actually, I think it is a feature, not a bug. Can you describe what you did, what you wanted to happen, and what happened instead?</p>

---

## Post #6 by @MMMPPPMMM (2017-07-27 10:17 UTC)

<p>For example:</p>
<ul>
<li>I use Segment Editor and segement the hip joint in the coronal plane (View: “Green slice only”)</li>
<li>I use the shift key to move the other planes Red and Yellow to the same position.</li>
<li>Now I change view to “Red slice only”.</li>
<li>IMO the Red slice should be somewhere in the hip joint now, but it is in the default position.</li>
</ul>
<p>This works in the “Four-Up” view. But it doesn’t work if I switch between "Green / Red / Yellow slice only"<br>
The slice position is always reset to default, if I change between different Views.</p>
<p>Kind regards</p>

---

## Post #7 by @lassoan (2017-07-27 15:23 UTC)

<p>When you switch between layouts the slice position should not change. This seems to be a bug - I’ll look into this.</p>

---

## Post #8 by @lassoan (2017-07-27 17:02 UTC)

<p>I’ve fixed the problem, it’ll work correctly in the nightly version that you download tomorrow or later.</p>

---

## Post #9 by @MMMPPPMMM (2017-07-28 09:18 UTC)

<p>Thank you! Works fine.</p>
<p>By the way. I forgot to mention that the “Subject Hierarchy” Button is not working for me.</p>
<p>And may it be possible to store the last settings of the Segment Editor in the mrml file somehow?<br>
For example the last segmentation, master volume, segment, view, zoom, pan, …</p>
<p>Kind regards</p>

---

## Post #10 by @lassoan (2017-07-28 13:37 UTC)

<blockquote>
<p>Subject Hierarchy” Button is not working for me</p>
</blockquote>
<p><code>Subject Hierarchy</code> module has been merged with <code>Data</code> module. In menu: <code>Edit</code> / <code>Application settings</code>, <code>Modules</code> section, <code>Favorite Modules</code> list (at the bottom) you need to:</p>
<ol>
<li>Remove the old <code>Subject Hierarchy</code> shortcut (click on the shortcut then click <code>Remove</code>)</li>
<li>Create new shortcut: drag-and-drop the <code>Data</code> module from the list above into the <code>Favorite Modules</code> (you can adjust order of shortcuts with left/right arrow buttons)</li>
</ol>
<blockquote>
<p>And may it be possible to store the last settings of the Segment Editor in the mrml file somehow?<br>
For example the last segmentation, master volume, segment, view, zoom, pan, …</p>
</blockquote>
<p>All these settings are already stored in the scene file and restored when you load the scene.</p>

---

## Post #11 by @MMMPPPMMM (2017-07-28 14:32 UTC)

<blockquote>
<p>In menu: Edit / Application settings, Modules section, Favorite Modules</p>
</blockquote>
<p>Thank you, works fine.</p>
<blockquote>
<p>All these settings are already stored in the scene file and restored when you load the scene.</p>
</blockquote>
<p>This doesn’t work for me. If I open scene file and select the Segment Editor the view is set to default.</p>

---

## Post #12 by @lassoan (2017-07-28 16:49 UTC)

<p>There may be some unnecessary reset of views, Ill see if Incan reproduce it. In the meantime, you can try if it works well if you switch to Segment editor, Close scene (even if you haven’t loaded any data yet), and then load your scene.</p>

---

## Post #13 by @MMMPPPMMM (2017-07-29 10:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In the meantime, you can try if it works well if you switch to Segment editor, Close scene (even if you haven’t loaded any data yet), and then load your scene.</p>
</blockquote>
</aside>
<p>This seems to work.</p>
<p>Thanks a lot &amp; kind regards</p>

---

## Post #14 by @MMMPPPMMM (2017-12-06 10:52 UTC)

<aside class="quote no-group" data-username="MMMPPPMMM" data-post="11" data-topic="557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>If I open scene file and select the Segment Editor the view is set to default.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There may be some unnecessary reset of views, Ill see if Incan reproduce it.</p>
</blockquote>
</aside>
<p>This bug is still present in the latest nightly build. Would be great if this could be fixed.</p>
<p>Maybe another small bug, that I’ve recognized in the Segment Editor:<br>
If “Show 3D” is deactivated through the button, the button of “Show 3D” is still in active mode.</p>
<p>Thanks in advance</p>

---

## Post #15 by @lassoan (2017-12-06 15:05 UTC)

<aside class="quote no-group" data-username="MMMPPPMMM" data-post="14" data-topic="557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>This bug is still present in the latest nightly build. Would be great if this could be fixed.</p>
</blockquote>
</aside>
<p>I cannot reproduce this. Could you capture a video of your screen, upload it somewhere, and post the link here?</p>
<aside class="quote no-group" data-username="MMMPPPMMM" data-post="14" data-topic="557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>If “Show 3D” is deactivated through the button, the button of “Show 3D” is still in active mode.</p>
</blockquote>
</aside>
<p>Deactivate using which button?<br>
What do you mean by “still in active mode”?</p>

---

## Post #16 by @MMMPPPMMM (2017-12-07 11:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I cannot reproduce this. Could you capture a video of your screen, upload it somewhere, and post the link here?</p>
</blockquote>
</aside>
<p>Here a video after starting slicer:<br>
<a href="https://streamable.com/aj1dl" class="onebox" target="_blank" rel="noopener nofollow ugc">https://streamable.com/aj1dl</a></p>

---

## Post #17 by @lassoan (2017-12-08 04:59 UTC)

<p>I’ve changed the segment editor widget to not reset slice view when switching master volume (when switching to Editor module). The new version will be available in the nightly build that you can download on Saturday or later.</p>

---

## Post #18 by @MMMPPPMMM (2017-12-09 21:36 UTC)

<p>Thank you!<br>
Works fine.</p>

---

## Post #19 by @lassoan (2023-03-21 02:54 UTC)



---
