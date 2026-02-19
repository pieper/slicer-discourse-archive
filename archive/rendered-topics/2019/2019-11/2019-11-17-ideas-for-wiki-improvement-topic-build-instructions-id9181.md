---
topic_id: 9181
title: "Ideas For Wiki Improvement Topic Build Instructions"
date: 2019-11-17
url: https://discourse.slicer.org/t/9181
---

# Ideas for Wiki Improvement - Topic: Build Instructions

**Topic ID**: 9181
**Date**: 2019-11-17
**URL**: https://discourse.slicer.org/t/ideas-for-wiki-improvement-topic-build-instructions/9181

---

## Post #1 by @marie (2019-11-17 20:02 UTC)

<p>Hi there!</p>
<p>I am referencing to this page:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#BUILD_Slicer" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#BUILD_Slicer</a></p>
<p>I finally figured out how to build Slicer!!! (Ubuntu 18.04) Anyway, it took me soo long to fix my problem. The following notes would have helped a lot:</p>
<blockquote>
<h2>BUILD Slicer</h2>
<p>…<br>
$ make -j</p>
</blockquote>
<p>When you use the <code>-j</code> option of make you won’t typically see the error message so run make without <code>-j</code> to see where it actually errors out. Source: [<a href="https://discourse.slicer.org/t/installation-issues-macos-mojave-10-14-6/7950" class="inline-onebox">Installation issues: macOS Mojave 10.14.6</a>]</p>
<p>Second I had to face this problem:<br>
<a href="https://issues.slicer.org/view.php?id=4616" rel="noopener nofollow ugc">https://issues.slicer.org/view.php?id=4616</a><br>
So it would be really nice to find a note for Ubuntu &gt;=18.04 :</p>
<ul>
<li>open Slicer-SuperBuild/LibArchive/libarchive/archive_pack_dev.c</li>
<li>do the following changes (see line 55 and following):<br>
<span class="hashtag-raw">#include</span> &lt;string.h&gt;<br>
<span class="hashtag-raw">#endif</span><br>
<span class="hashtag-raw">#ifdef</span> HAVE_SYS_TYPES_H<br>
<strong>//<span class="hashtag-raw">#include</span> &lt;sys/types.h&gt;</strong><br>
<strong><span class="hashtag-raw">#include</span> &lt;sys/sysmacros.h&gt;</strong><br>
<span class="hashtag-raw">#endif</span><br>
<span class="hashtag-raw">#ifdef</span> HAVE_SYS_STAT_H<br>
<span class="hashtag-raw">#include</span> &lt;sys/stat.h&gt;</li>
</ul>
<p>I think these hints aren’t given anywhere in the wiki. Maybe they could be helpful.</p>

---

## Post #2 by @pieper (2019-11-18 21:36 UTC)

<p>Hi <a class="mention" href="/u/marie">@marie</a> - thanks for the suggestions.  I added your note about -j plus a little extra info to the wiki.</p>
<p>For the libarchive issue, hopefully people will find this thread to learn this workaround.  Longer term it would be great to have a real fix to the build so the workaround isn’t needed.  Lately we have been keeping more info here in discourse where multiple people can comment but not necessarily duplicating it in the wiki.</p>
<p>We are hoping to transition documentation into git for better version control so it will be clearer which workaround are required for which specific slicer versions.  We definitely appreciate help with this.</p>

---

## Post #3 by @lassoan (2019-11-19 00:24 UTC)

<p><a class="mention" href="/u/marie">@marie</a> <a class="mention" href="/u/pieper">@pieper</a> Could you please check if updating LibArchive to v3.4.0 fixes the issue? See pull request here: <a href="https://github.com/Slicer/Slicer/pull/1263">https://github.com/Slicer/Slicer/pull/1263</a></p>

---

## Post #4 by @marie (2019-11-19 18:02 UTC)

<p>Ubuntu 18.04.3<br>
CMake v3.15.5<br>
git v2.17.1<br>
Qt v5.11.0 (as recommended)<br>
subversion v1.9.7-4 and libapache2-mod-svn v1.9.7-4<br>
gcc v7.4.0</p>
<p>Slicer-SuperBuild/LibArchive/libarchive/archive_pack_dev.c <strong>remained untouched</strong>.<br>
I built the master branch including your changes and it worked! Thanks!</p>

---
