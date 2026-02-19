---
topic_id: 1231
title: "Solved Address Build Error Related To Overwritten Setup Cfg"
date: 2017-10-16
url: https://discourse.slicer.org/t/1231
---

# Solved: Address build error related to overwritten 'setup.cfg'

**Topic ID**: 1231
**Date**: 2017-10-16
**URL**: https://discourse.slicer.org/t/solved-address-build-error-related-to-overwritten-setup-cfg/1231

---

## Post #1 by @jcfr (2017-10-16 05:39 UTC)

<p>Following <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26470">r26470</a>, we update the version of setuptools used in Slicer, as a side effect you may get an error like the one reported below.</p>
<p>To address the problem</p>
<pre><code class="lang-auto">cd Slicer-Superbuild/python-setuptools
git reset --hard  HEAD
</code></pre>
<p>Error:</p>
<pre><code class="lang-auto">error: Your local changes to the following files would be overwritten by checkout:
	setup.cfg
Please, commit your changes or stash them before you can switch branches.
Aborting
CMake Error at /home/jcfr/Projects/Slicer-2-Qt5-VTK8-build/python-setuptools-prefix/tmp/python-setuptools-gitupdate.cmake:147 (message):
  Failed to checkout tag:
</code></pre>

---

## Post #2 by @lassoan (2017-10-17 20:45 UTC)

<p>I’m getting this error too frequently and it is quite annoying. Would it be possible to patch the file outside the source tree or somehow suppress this error automatically?</p>

---

## Post #3 by @jcfr (2017-10-17 20:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1231" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m getting this error too frequently and it is quite annoying. Would it be possible to patch the file outside the source tree or somehow suppress this error automatically?</p>
</blockquote>
</aside>
<p>We could also make a release and download a zip of the version of setuptools.</p>

---

## Post #4 by @lassoan (2017-10-17 20:53 UTC)

<p>Yes, that would work.</p>

---

## Post #5 by @lassoan (2017-10-23 17:06 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you please address this issue? I use scripts for building Slicer and this bug keeps making those fail and require me to go manually and fix the problem. I’ve also added a ticket to track its resolution: <a href="https://issues.slicer.org/view.php?id=4466">https://issues.slicer.org/view.php?id=4466</a></p>

---

## Post #6 by @lassoan (2017-10-26 20:46 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> has fixed the problem in recent nightly version.</p>

---
