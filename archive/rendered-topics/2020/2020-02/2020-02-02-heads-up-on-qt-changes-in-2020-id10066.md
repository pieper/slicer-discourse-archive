# Heads up on Qt changes in 2020

**Topic ID**: 10066
**Date**: 2020-02-02
**URL**: https://discourse.slicer.org/t/heads-up-on-qt-changes-in-2020/10066

---

## Post #1 by @jamesobutler (2020-02-02 02:14 UTC)

<p>I was reading a recent Qt blog post titled <a href="https://www.qt.io/blog/qt-offering-changes-2020" rel="noopener nofollow ugc">“Qt offering changes 2020”</a> which might impact some Slicer development.</p>
<p>Quick Excerpts:</p>
<blockquote>
<p>From February onward, everyone, including open-source Qt users, will require valid Qt accounts to download Qt binary packages.</p>
</blockquote>
<blockquote>
<p>Starting with Qt 5.15, long term support (LTS) will only be available to commercial customers. This means open-source users will receive patch-level releases of 5.15 until the next minor release will become available.</p>
</blockquote>
<blockquote>
<p>The offline installer will also become commercial-only.</p>
</blockquote>
<p>The fact that LTS support won’t be a thing for open-source users, it looks like we will have 6 months of bug fixes as they typically release a new minor version on that timeline. Then we will have to update to use the latest minor version if we want the latest bug fixes.</p>

---

## Post #2 by @pieper (2020-02-02 14:40 UTC)

<p>Thanks for bringing this to our attention <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Qt 5.x has been pretty stable compared to 4.x so I hope it won’t be much trouble keeping up with the latest releases.  Time will tell.</p>

---

## Post #3 by @jamesobutler (2020-02-02 17:20 UTC)

<p>I believe Qt 5.15 will be the last release on the Qt 5.x series as Qt 6 is expected for the last half of 2020. It isn’t supposed to be an immediate big departure in the first release, but as a new major version it could break some things in the future. It’s not clear from the blog post, but I would assume the release of Qt 6 would mean no more patch releases for Qt 5.15 for open source users.</p>

---

## Post #4 by @lassoan (2020-02-02 17:31 UTC)

<p>It is a smart move, as it essentially converts all free users to beta testers.</p>
<p>Qt is free and we want Qt company to stay alive and maintain Qt, so we cannot complain that they are trying to bring in revenue, but this will make our life a bit harder.</p>
<p>LTS releases were great because they contained fixes for operating system and compiler updates. Now we’ll be forced to keep updating Qt more often, spending more time with updates and risking more regressions (or buy a few licenses).</p>

---

## Post #5 by @jcfr (2020-02-03 14:09 UTC)

<p>At Kitware, we will be downloading Qt installers as they come. I will update this post when I have more details.</p>

---
