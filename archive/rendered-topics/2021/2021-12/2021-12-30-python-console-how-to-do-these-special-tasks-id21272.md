# Python console : how to do these special tasks?

**Topic ID**: 21272
**Date**: 2021-12-30
**URL**: https://discourse.slicer.org/t/python-console-how-to-do-these-special-tasks/21272

---

## Post #1 by @chir.set (2021-12-30 11:49 UTC)

<ol>
<li>While testing things, we may get trapped with variables previously declared and assigned in the Python console. I’m looking for a way to completely clear/clean/reset the Python console to avoid the need of restarting Slicer.</li>
</ol>
<p>slicer.app.pythonConsole().reset() does not work as expected, previous declared variables persist.</p>
<ol start="2">
<li>How can we load/run a Python script saved on disk ? Something like ‘source’ in bash.</li>
</ol>
<p>Thanks for any advice.</p>

---

## Post #2 by @pieper (2021-12-30 20:28 UTC)

<p>When I’m just experimenting, I’ll often make <a href="https://github.com/pieper/facenav/blob/master/facenav.py">a script like this</a> that conditionally initializes some bulk data (e.g. downloading a sample volume) if the node is not found and leaves the intermediate values in the python console for interactive query and also to test invoking methods.</p>
<p>Then I use a command like this:</p>
<pre><code class="lang-auto">path="c:/pieper/facenav/facenav.py"
exec(open(path).read())
</code></pre>
<p>to load the script which works like <code>source</code> in bash.  It can typically just be re-run dozens of times while refining the logic.  Then sometimes if the logic is wrong you may need to re-start Slicer but it just means the initialization needs to run again.</p>

---

## Post #3 by @chir.set (2021-12-31 10:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21272">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Then I use a command like this:</p>
</blockquote>
</aside>
<p>This works very well, thank you.</p>

---
