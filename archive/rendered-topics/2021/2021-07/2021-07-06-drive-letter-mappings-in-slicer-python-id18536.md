# Drive letter mappings in Slicer Python

**Topic ID**: 18536
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/drive-letter-mappings-in-slicer-python/18536

---

## Post #1 by @rohan_n (2021-07-06 16:45 UTC)

<p>Is there an easy way to give the Slicer copy of Python access to the network drive letter mappings so that I can use something like os.path.realpath() in my Slicer modules?</p>
<p>Right now my local (non-Slicer) copy of Python 3.8 has no problem converting something like<br>
<code>path = r'B:\folder1</code><br>
into a full path using<br>
<code>os.path.realpath(path)</code></p>
<p>But I am unable to reproduce this result in Slicer’s Python Interactor.</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @lassoan (2021-07-06 16:48 UTC)

<p>This is what I get in Slicer:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import os
&gt;&gt;&gt; path=r"m:\tmp"
&gt;&gt;&gt; os.path.realpath(path)
'm:\\tmp'
</code></pre>
<p>Do you expect to see something different?</p>

---

## Post #3 by @rohan_n (2021-07-06 16:51 UTC)

<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="18536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>But I am unable to reproduce this result in Slicer’s Python Interactor.</p>
</blockquote>
</aside>
<p>Yes, I am hoping to see the full path.<br>
For example, if m: stands for <strong>\networkdrive1</strong>, I want the os.path.realpath command to<br>
convert the path into <strong>r’\\networkdrive1\tmp’</strong><br>
This is what happens when I use os.path.realpath on my non-Slicer local copy of Python and I would like Slicer Python to have the same access to these drive letter mappings.</p>

---

## Post #4 by @lassoan (2021-07-06 17:31 UTC)

<p>Behavior of <code>os.path.realpath</code> on Windows was changed in Python 3.7 or 3.8. To resolve symlinks in a way that is compatible with a wider range of Python versions and operating systems, you can use <code>pathlib</code>:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; path = r"m:\tmp"
&gt;&gt;&gt; import pathlib
&gt;&gt;&gt; pathlib.Path(path).resolve()
WindowsPath('//SERVER01/data/tmp')
</code></pre>

---
