# Is there a way to record full log of actions?

**Topic ID**: 6513
**Date**: 2019-04-16
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-record-full-log-of-actions/6513

---

## Post #1 by @Alex_Vergara (2019-04-16 16:24 UTC)

<p>I am using several modules and I want to recreate the procedure used but I cant find a proper way to log everything. Some modules simply dont give any useful information. The only logged information currently are warnings and errors, but I know there is info, it is just not used.</p>
<p>Example: I select the segment Editor module, then I select Pant brush. I expect the info to show Segment Editor: Selected Paint Brush.</p>
<p>Where can I change the info verbosity??</p>

---

## Post #2 by @lassoan (2019-04-16 17:15 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="6513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I cant find a proper way to log everything</p>
</blockquote>
</aside>
<p>It is of course not possible to log “everything”, but I agree that it would be nice to log more user actions. Pull requests are welcome!</p>
<p>From what I understand from your questions above, logging would not be useful for you, because you know what buttons you press, etc. Probably you would need a macro recorder instead.</p>
<p>You can already record and replay most GUI actions using QtTesting. Usually it is a bit too low level for general purpose usage, but you can give it a try. Enable QtTesting in Application settings and use Edit / Record/Play macro.</p>
<p>You can record all state changes of MRML nodes using Sequences extension, but it only records result of actions, so you cannot apply them to a new node.</p>
<p>If you want to automate a segmentation process, then you can find several examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>

---

## Post #3 by @Alex_Vergara (2019-04-17 13:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6513">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably you would need a macro recorder instead.</p>
</blockquote>
</aside>
<p>Yes, this did the trick!!<br>
Thanks</p>

---
