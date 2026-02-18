# Python qt library is missing from today's mac nightly

**Topic ID**: 2072
**Date**: 2018-02-12
**URL**: https://discourse.slicer.org/t/python-qt-library-is-missing-from-todays-mac-nightly/2072

---

## Post #1 by @pieper (2018-02-12 18:11 UTC)

<p>The 2018-02-11 mac nightly won’t start for me because it’s missing the PythonQT library.</p>
<pre><code class="lang-auto">  Library not loaded: @rpath/lib/Slicer-4.9/libPythonQt.dylib
  Referenced from: /private/var/folders/*/Slicer.app/Contents/MacOS/Slicer
  Reason: image not found
</code></pre>
<p>But if I manually copy in an older version of that file (from the 2018-02-07 build) it works.</p>
<p>Oddly today’s nightly windows version does have a correct pythonqt library and works so there must be something mac-specific about why this is missing.</p>
<p>The only thing I can think of is that I <a href="https://github.com/Slicer/Slicer/commit/83e1a22e56ab1c97d9ac6c6a6e545e2b6a7de1f7">updated PythonQT and CTK</a> with <a href="https://github.com/commontk/PythonQt/commits/patched-8">this change to the wrapping</a> but it shouldn’t have changed the packaging and it doesn’t have anything mac specific.</p>
<p>Any other reason why that file would be missing from the nightly?</p>

---

## Post #2 by @jcfr (2018-02-12 18:43 UTC)

<aside class="quote no-group" data-username="pieper" data-post="1" data-topic="2072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Any other reason why that file would be missing from the nightly?</p>
</blockquote>
</aside>
<p>Look like this commit is also new: <a href="https://github.com/Slicer/Slicer/commit/83e1a22e56ab1c97d9ac6c6a6e545e2b6a7de1f7">https://github.com/Slicer/Slicer/commit/83e1a22e56ab1c97d9ac6c6a6e545e2b6a7de1f7</a> and most likely introduced the regression.</p>

---

## Post #3 by @jcfr (2018-02-12 18:59 UTC)

<p>When I first  integrated this patch, I incorrectly assessed its impact. I will be pushing a fix before the end of the day.</p>

---

## Post #4 by @pieper (2018-02-12 19:06 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> - let me know if I accidentally broke something with that - it should have been a small change unrelated to packaging.</p>

---

## Post #5 by @jcfr (2018-02-12 19:10 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="2072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>it should have been a small change unrelated to packaging.</p>
</blockquote>
</aside>
<p>It is a side effect of updating the version. The commit I referenced wasn’t yet used to build the version of PythonQt indirectly integrated into Slicer</p>

---

## Post #6 by @pieper (2018-02-12 19:25 UTC)

<p>Ah, I see - thanks for clarifying.</p>

---

## Post #7 by @jcfr (2018-02-12 21:33 UTC)

<p>This should be fixed by <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26911">r26911</a></p>

---
