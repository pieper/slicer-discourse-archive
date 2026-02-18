# slicer.mrmlScene.Clear() not working

**Topic ID**: 42556
**Date**: 2025-04-14
**URL**: https://discourse.slicer.org/t/slicer-mrmlscene-clear-not-working/42556

---

## Post #1 by @dpvaldes (2025-04-14 13:36 UTC)

<p>I’m running Slicer 5.8.1 on Windows 11. Inputting slicer.mrmlScene.Clear() in the python console is not clearing it as before. Is this an issue or is it just me? Is there another way of clearing it?</p>

---

## Post #2 by @pieper (2025-04-14 14:54 UTC)

<p>I can’t reproduce this.  Clearing the scene works fine for me.  What’s not clearing for you?</p>

---

## Post #3 by @jcfr (2025-04-14 15:12 UTC)

<p>Thanks for the report.</p>
<p>To help us understand, could you report the following:</p>
<ul>
<li>The version of Slicer used to reproduce the issue</li>
<li>The extensions installed if any</li>
</ul>
<p>Also, does the issue happen using a newly installed Slicer just after loading MRHead sample data ? Or after running installing extensions and/or running scripts ?</p>

---

## Post #4 by @cpinter (2025-04-14 15:14 UTC)

<p>She uses 5.8.1.</p>
<p>Further concrete questions:</p>
<ul>
<li>Is there any error in the log after a failed clear scene execution?</li>
<li>Does Slicer crash?</li>
<li>Or what you said means that some nodes are not removed?</li>
</ul>

---

## Post #5 by @dpvaldes (2025-04-14 17:19 UTC)

<p>Maybe I didn’t state it correctly. The Scene clears but the console does not. Is this normal behavior for slicer.mrmlScene.Clear()?</p>
<p>I don’t have extensions installed. I’m using it after running a script.</p>

---

## Post #6 by @pieper (2025-04-14 17:28 UTC)

<p>That’s normal - we typically don’t clear the python console when the scene closes.</p>
<p>But you can do this if you want:</p>
<pre><code class="lang-auto">slicer.util.pythonShell().clear()
</code></pre>

---
