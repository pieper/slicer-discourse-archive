---
topic_id: 26453
title: "Slicer Program Crash Suddenly In Macbook"
date: 2022-11-26
url: https://discourse.slicer.org/t/26453
---

# Slicer program crash suddenly in MacBook

**Topic ID**: 26453
**Date**: 2022-11-26
**URL**: https://discourse.slicer.org/t/slicer-program-crash-suddenly-in-macbook/26453

---

## Post #1 by @Mohamed1 (2022-11-26 13:18 UTC)

<p>Hey folks! hope your are doing pretty good today.<br>
My question is the Slicer program crash every time I use scissor tool and “Slicer quit unexpectedly”<br>
Thanks for your help in advance.</p>

---

## Post #2 by @lassoan (2022-11-26 20:59 UTC)

<p>Thanks a lot for reporting. We are aware of this issue - see <a href="https://github.com/Slicer/Slicer/issues/6705">here</a>, but each report may contain additional useful information.</p>
<p>I’ve now added some more checks and debugging options to the Scissors effect. Please do these steps to help figuring out what the issue is:</p>
<ul>
<li>download and install the latest Slicer Preview Release tomorrow (2022-11-27) or later</li>
<li>hit <kbd>Cmd</kbd>+<kbd>3</kbd> to open the Python console</li>
<li>type this command to enable writing the scissor brush to a file at each scissor operation - replace <code>/Users/...</code> by a path somewhere in your user folder</li>
</ul>
<pre><code class="lang-auto">slicer.qSlicerSegmentEditorScissorsEffect().setDebugOutputFolder("/Users/...")
</code></pre>
<ul>
<li>try to reproduce the crash</li>
<li>if you reproduced it then share (upload somewhere and post the download link) the <code>DebugScissorBrush.vtp</code> file that was created in the folder that you specified</li>
</ul>

---

## Post #3 by @pieper (2022-11-27 07:14 UTC)

<p><a class="mention" href="/u/mohamed1">@Mohamed1</a> can you report if your macbook has an intel chip or Apple silicon (M1 or M2)?</p>

---
