---
topic_id: 6012
title: "Updating Minimum Required Version Of Cmake To 3 13"
date: 2019-03-04
url: https://discourse.slicer.org/t/6012
---

# Updating minimum required version of CMake to 3.13

**Topic ID**: 6012
**Date**: 2019-03-04
**URL**: https://discourse.slicer.org/t/updating-minimum-required-version-of-cmake-to-3-13/6012

---

## Post #1 by @phcerdan (2019-03-04 18:33 UTC)

<p>We plan on updating the minimum required version of CMake to 3.13, this will allow simplifying a lot of CMake logic.</p>
<p>It is a good opportunity to update now while we are working toward Slicer 5 which will introduce C++11 features and support for ITKv5.</p>
<p>Ubuntu 18.04 LTS CMake version is too old already (3.10.2 at the time of writing this). Ubuntu 19.04 uses 3.13.4.</p>
<p>Windows and macOS users install CMake from binaries or homebrew, so it is not a problem for those users. Other Linux distros update CMake regularly. For Ubuntu LTS and other linux distribution users, they can download and install from binaries</p>
<p>Work-in-progress PR introducing the changes: <a href="https://github.com/Slicer/Slicer/pull/1095" rel="nofollow noopener">1095</a></p>
<p>Co-authored by <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @jcfr (2019-03-05 01:24 UTC)

<p>Thanks <a class="mention" href="/u/phcerdan">@phcerdan</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"></p>
<p>To follow up, starting with Slicer <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27988" rel="nofollow noopener">r27988</a>, CMake &gt;= 3.13.4 is now required.</p>

---

## Post #3 by @lassoan (2019-03-05 02:37 UTC)

<p>Thanks for the update. Could you please review/update the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">Slicer build instructions</a> accordingly?</p>

---

## Post #4 by @jcfr (2019-03-05 03:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="6012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you please review/update the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">Slicer build instructions</a> accordingly?</p>
</blockquote>
</aside>
<p>Sounds good.</p>
<p>The plan initial was to update the instructions by the end of the week after removing the Qt4/VTK7 support.</p>
<p>Tomorrow, I will talk with <a class="mention" href="/u/phcerdan">@phcerdan</a> so that we archive the current instruction (useful for Slicer 4.10) and start update  them.</p>

---

## Post #5 by @lassoan (2019-03-05 04:14 UTC)

<p>If it’s a major rewrite then it might make sense to move it to ReadTheDocs.</p>

---

## Post #6 by @adamrankin (2019-04-09 14:35 UTC)

<p>Sorry to resurrect a thread, but just wondering what is missing from 3.10.2? 18.04LTS is still a <em>very</em> common OS.</p>

---

## Post #7 by @jcfr (2019-04-09 14:59 UTC)

<p>CMake is now official distributed on Ubuntu, you should be able to install CMake 3.14.1 very easily. See <a href="https://blog.kitware.com/ubuntu-cmake-repository-now-available/">https://blog.kitware.com/ubuntu-cmake-repository-now-available/</a></p>
<blockquote>
<p>just wondering what is missing from 3.10.2?</p>
</blockquote>
<p>Looking at the change log should help answer the question. But support for recent Visual Studio is one thing.</p>

---
