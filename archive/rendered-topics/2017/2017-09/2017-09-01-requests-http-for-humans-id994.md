---
topic_id: 994
title: "Requests Http For Humans"
date: 2017-09-01
url: https://discourse.slicer.org/t/994
---

# Requests: HTTP for Humans

**Topic ID**: 994
**Date**: 2017-09-01
**URL**: https://discourse.slicer.org/t/requests-http-for-humans/994

---

## Post #1 by @ebremer (2017-09-01 22:18 UTC)

<p>Would it be possible to add:</p>
<p><a href="http://docs.python-requests.org/en/latest/" class="onebox" target="_blank" rel="nofollow noopener">http://docs.python-requests.org/en/latest/</a></p>
<p>to the Slicer distribution.  It has an Apache 2.0 license and is a lot easier to use than urllib or urllib2</p>

---

## Post #2 by @lassoan (2017-09-01 22:29 UTC)

<p>I agree that it would be useful. This package is Python-only, but it depends on a couple of other packages.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> What is the recommended process now for adding more Python packages to the Slicer distribution?</p>

---

## Post #3 by @lassoan (2017-09-01 22:51 UTC)

<p>Note that you can install <code>requests</code> using <code>pip</code> as shown in this post: <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/9?u=lassoan">Slicer-Python Packages Use and Install</a>. The only limitation is that on Windows you need to start Slicer as an admin, which may not be very user friendly.</p>

---

## Post #4 by @jcfr (2017-09-01 23:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="994">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The only limitation is that on Windows you need to start Slicer as an admin</p>
</blockquote>
</aside>
<p>We may have a way around that. I will follow up with more details later.</p>

---

## Post #5 by @ebremer (2017-09-14 21:24 UTC)

<p>Would that work around allow an extension to load dynamically the python requests package like the above example?</p>

---

## Post #6 by @lassoan (2017-09-15 00:45 UTC)

<p>Until <a class="mention" href="/u/jcfr">@jcfr</a> fixes the installation issue, you can add these packages to your extension. Simply copy the unzipped package into your module directory. See for example the ptvsd module in <a href="https://github.com/SlicerRt/SlicerDebuggingTools/tree/master/PyDevRemoteDebug">https://github.com/SlicerRt/SlicerDebuggingTools/tree/master/PyDevRemoteDebug</a></p>

---
