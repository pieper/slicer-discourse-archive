---
topic_id: 33642
title: "Mouse Focus Issue When Using Keyboard Shortcuts In 2023 12 3"
date: 2024-01-05
url: https://discourse.slicer.org/t/33642
---

# Mouse Focus issue when using keyboard shortcuts in 2023-12-31 preview

**Topic ID**: 33642
**Date**: 2024-01-05
**URL**: https://discourse.slicer.org/t/mouse-focus-issue-when-using-keyboard-shortcuts-in-2023-12-31-preview/33642

---

## Post #1 by @hherhold (2024-01-05 15:33 UTC)

<p>I think there is an issue with focus (maybe). I can replicate this with any scene.</p>
<ol>
<li>Paint a small section in a segment, preferably isolated.</li>
<li>Click on Islands effect, select remove selected island.</li>
<li>Click on the painted island - it disappears.</li>
<li>Click on paint tool.</li>
<li>Repaint small section - it appears.</li>
</ol>
<p>NOW -</p>
<ol start="6">
<li>Hit “space” (space bar) to toggle back to islands tool.</li>
<li>Click on island to remove it. Note that mouse click does not remove island.</li>
<li>Click again. Note that this time, island is removed.</li>
<li>Hit “space” to toggle back to paint.</li>
<li>Click and drag to paint - note that nothing appears.</li>
<li>Click and drag again - note that painting works.</li>
</ol>
<p>It looks like hitting the space bar pulls mouse click focus away from the 2D view (I’m probably getting a lot of Qt terminology wrong here, but hopefully you’ll get the idea.)</p>
<p>Any ideas?</p>
<p>THANKS!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2024-01-17 16:18 UTC)

<p>Bump… Any ideas on this?</p>

---

## Post #3 by @lassoan (2024-01-17 19:39 UTC)

<p>I cannot reproduce this on Windows, using the current Slicer Preview Release.</p>
<p>The instructions you provided seemed to be clear enough, but maybe there is some subtle difference between what you and I did. Could you record a screen capture video (preferably with a software that can also record/show mouse clicks and maybe even keypresses), upload it somewhere, and post the link here?</p>

---

## Post #4 by @hherhold (2024-01-17 19:53 UTC)

<p>It’s my MOUSE! What the heck?</p>
<p>I double checked and the problem doesn’t occur on my Mac (I’ve been doing 90% of my slicer work on my windows machine, didn’t think to check my Mac). Then on a whim I just checked using my touchpad, and the problem doesn’t happen at all - I only get this when I use my external USB mouse!</p>
<p>Well, obviously not a Slicer issue. Thanks, Andras! Now to find out what’s so weird about my mouse… it’s an Evoluent vertical mouse with weird drivers and extensions, so maybe something they’re updated behind the scenes and messed things up.</p>
<p>Thanks again for checking! Hope you’re well.</p>

---

## Post #5 by @hherhold (2024-01-17 20:05 UTC)

<p>Verified - I uninstalled the Evoluent Mouse Manager so now it’s just a standard mouse, and everything works fine. (Shrug.) Whatever.</p>

---
