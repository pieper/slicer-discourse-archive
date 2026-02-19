---
topic_id: 3728
title: "Git Svn Commit Issue With Svn Log Line Endings"
date: 2018-08-10
url: https://discourse.slicer.org/t/3728
---

# Git-svn commit issue with svn:log line endings

**Topic ID**: 3728
**Date**: 2018-08-10
**URL**: https://discourse.slicer.org/t/git-svn-commit-issue-with-svn-log-line-endings/3728

---

## Post #1 by @pieper (2018-08-10 20:32 UTC)

<p>I was trying to commit <a class="mention" href="/u/fernando">@Fernando</a>’s  <a href="https://github.com/Slicer/Slicer/pull/1004">pull request</a> but I’m getting this weird error on both linux and mac, even with a fresh checkout.</p>
<p>Does anyone know what causes this and how to fix it?</p>
<pre><code class="lang-auto">$ git svn dcommit --add-author-from
Committing to http://svn.slicer.org/Slicer4/trunk ...
ERROR from SVN:
Wrong or unexpected property value: Cannot accept non-LF line endings in 'svn:log' property
W: b93e822eca6301b93fbfebd304b1e99108221439 and refs/remotes/git-svn differ, using rebase:
:040000 040000 6f1b934ec1c536468148dd1dbe5c51bb6ebc5808 fa4599719cd15b1427e9f0b8e09bfa696202de7b M Modules
Current branch master is up to date.
ERROR: Not all changes have been committed into SVN, however the committed
ones (if any) seem to be successfully integrated into the working tree.
Please see the above messages for details.
</code></pre>

---

## Post #2 by @ihnorton (2018-08-10 20:40 UTC)

<p>Maybe the file has windows line endings?</p>

---

## Post #3 by @pieper (2018-08-10 20:53 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="3728" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Maybe the file has windows line endings?</p>
</blockquote>
</aside>
<p>But which file?  The pull request has just a couple of line changes and I don’t see any windows line endings in there.  The error message refers to “‘svn:log’ property” but I’m not sure where that is and how it would have been modified…</p>

---

## Post #4 by @pieper (2018-08-10 21:11 UTC)

<p>Maybe someone else can try merging that pull request to see if they run into the same issue.</p>

---

## Post #5 by @jcfr (2018-08-10 21:46 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="3728">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>someone else can try merging</p>
</blockquote>
</aside>
<p>All set.  I tweaked the commit message and integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27344">r27344</a></p>
<p>May be editing the commit message was sufficient to prevent the error you experienced.</p>

---
