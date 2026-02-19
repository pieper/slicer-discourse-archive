---
topic_id: 3325
title: "Pip In Nightly Build Not Working"
date: 2018-06-28
url: https://discourse.slicer.org/t/3325
---

# Pip in nightly build not working

**Topic ID**: 3325
**Date**: 2018-06-28
**URL**: https://discourse.slicer.org/t/pip-in-nightly-build-not-working/3325

---

## Post #1 by @mcfly3001 (2018-06-28 12:41 UTC)

<p>Hi,</p>
<p>for another problem I had I was upgrading my Slicer install to the nightly build version. Unfortunately I have problems running the pip installer in the Python Interactive console. I am running the nightly version on a windows system and get the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a21f47d6f64e488aa422ceefb26e326e9877ab1b.png" data-download-href="/uploads/short-url/n8cmR3h818NtvTnuNyZ0uNJ6Wlt.png?dl=1" title="0-2018-06-26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a21f47d6f64e488aa422ceefb26e326e9877ab1b.png" alt="0-2018-06-26" data-base62-sha1="n8cmR3h818NtvTnuNyZ0uNJ6Wlt" width="690" height="101" data-dominant-color="FAFBF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0-2018-06-26</span><span class="informations">1676×247 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The same command works fine with the release version of Slicer. Is there a new way for installing packages?</p>
<p>Thanks!</p>

---

## Post #2 by @ihnorton (2018-06-28 14:14 UTC)

<p><code>pip.main</code> was removed in newer versions of pip. For interactive/one-shot use you can run it from the command line in a Slicer-aware shell (look at <code>Slicer --launcher-show-set-environment-commands</code>); for dependency installation as part of a module build, you can shell out from your CMake build.</p>

---

## Post #3 by @lassoan (2018-06-30 13:26 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="3325">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p><code>pip.main</code> was removed in newer versions of pip</p>
</blockquote>
</aside>
<p>That’s unfortunate. It makes more cumbersome to install packages from Slicer modules.</p>
<p>Would it make sense to add Slicer launcher application shortcut for pip? Pip could then launched as: Slicer.exe --pip install…</p>

---

## Post #4 by @jcfr (2018-06-30 19:43 UTC)

<blockquote>
<p>Slicer.exe --pip install…</p>
</blockquote>
<p>Or <code>SlicerPython --pip ...</code> that way user would have terminal output on windows.</p>

---

## Post #5 by @ihnorton (2018-07-02 15:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="3325">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would it make sense to add Slicer launcher application shortcut for pip? Pip could then launched as: Slicer.exe --pip install…</p>
</blockquote>
</aside>
<p>I think <code>Slicer --launch</code> already prefers binaries in Slicer’s PATH, so the other option is to document pip as <code>Slicer --launch pip</code> (only a few more characters).</p>

---

## Post #6 by @patrickcox3 (2018-07-18 21:55 UTC)

<p>pip.main can be found in pip._internal</p>
<p>I was able to utilize it in my project as shown:</p>
<pre><code class="lang-auto">from pip._internal import main as pipmain
pipmain(['install', 'scipy'])
</code></pre>
<p>However, using pip within your program <a href="https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program" rel="nofollow noopener">is strongly discouraged</a>.<br>
An alternative method, such as spoken to in this thread, would be extremely helpful.</p>

---

## Post #7 by @lassoan (2018-07-26 13:07 UTC)

<p>I’ve added a ticket to add <code>pip</code> to Slicer install package: <a href="https://issues.slicer.org/view.php?id=4586">https://issues.slicer.org/view.php?id=4586</a></p>

---
