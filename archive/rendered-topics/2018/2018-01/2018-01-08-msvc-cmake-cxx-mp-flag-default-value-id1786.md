---
topic_id: 1786
title: "Msvc Cmake Cxx Mp Flag Default Value"
date: 2018-01-08
url: https://discourse.slicer.org/t/1786
---

# [MSVC] CMAKE_CXX_MP_FLAG default value

**Topic ID**: 1786
**Date**: 2018-01-08
**URL**: https://discourse.slicer.org/t/msvc-cmake-cxx-mp-flag-default-value/1786

---

## Post #1 by @adamrankin (2018-01-08 19:50 UTC)

<p>Hello,</p>
<p>Just wanted to start a conversation around the default value of CMAKE_CXX_MP_FLAG on MSVC builds. Would there be any objection to setting it to ON?</p>
<p>Adam</p>

---

## Post #2 by @lassoan (2018-01-08 20:02 UTC)

<p>This has been discussed in the past, see <a href="http://slicer-devel-archive.65872.n3.nabble.com/Reducing-Slicer-build-time-on-Windows-using-CMAKE-CXX-MP-FLAG-td4035926.html">http://slicer-devel-archive.65872.n3.nabble.com/Reducing-Slicer-build-time-on-Windows-using-CMAKE-CXX-MP-FLAG-td4035926.html</a></p>
<p><a class="mention" href="/u/adamrankin">@adamrankin</a> How much does it reduce the build time for you?</p>
<p>As I remember, there were some potential issues in parallel builds - but maybe it was about parallel execution of test. <a class="mention" href="/u/jcfr">@jcfr</a> is there any risk or disadvantage of enabling parallel builds?</p>

---

## Post #3 by @adamrankin (2018-01-08 20:04 UTC)

<p>I have not quantified it, but it is noticeable. Is it worth me quantifying it in addition to your results?</p>
<p>Edit: it will be more and more noticeable with the introduction of higher and higher multicore count (see Ryzen Threadripper 16 core).</p>

---

## Post #4 by @adamrankin (2018-01-08 20:18 UTC)

<p>From <a href="https://blogs.msdn.microsoft.com/vcblog/2016/10/26/recommendations-to-speed-c-builds-in-visual-studio/" rel="noopener nofollow ugc">here</a></p>
<blockquote>
<p>/MP – Parallelize compilation of source files<br>
Invokes multiple instances of cl.exe to compile project source files in parallel. See documentation for /MP for a detailed discussion of the switch including conflicts with other compiler features. In addition to documentation this blog post has good information about the switch.</p>
<p>Resolving conflicts with other compiler features<br>
/Gm (enable minimal rebuild): I recommend using /MP over /Gm to reduce build time.<br>
<span class="hashtag-raw">#import:</span> Documentation for /MP discusses one option to resolve this conflict. Another option is to move all import directives to precompiled header.<br>
/Yc (create precompiled header): /MP does not help with creating precompiled header so not an issue.<br>
/EP, /E, /showIncludes: These switches are typically used to diagnose issues hence should not be an issue.</p>
</blockquote>
<p>Depending on the <a href="https://docs.microsoft.com/en-ca/cpp/build/reference/mp-build-with-multiple-processes" rel="noopener nofollow ugc">incompatibility</a>:</p>
<blockquote>
<p>If you use an incompatible compiler option with the /MP option, the compiler issues warning D9030 and ignores the /MP option.  If you use an incompatible language feature, the compiler issues error C2813 then ends or continues depending on the current compiler warning level option.</p>
</blockquote>

---

## Post #5 by @jcfr (2018-01-08 20:18 UTC)

<p>The flag is set to do the nightly build. See <a href="https://github.com/Slicer/DashboardScripts/blob/4efec4e330f4e79da9d9eef3ac445a350bde4618/overload-vs2013-slicer_release_nightly.cmake#L57">https://github.com/Slicer/DashboardScripts/blob/4efec4e330f4e79da9d9eef3ac445a350bde4618/overload-vs2013-slicer_release_nightly.cmake#L57</a></p>
<p>Since having four cores (or more) is fairly common, may be we could make this the default ?</p>

---

## Post #6 by @ihnorton (2018-01-08 21:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As I remember, there were some potential issues in parallel builds</p>
</blockquote>
</aside>
<p>The problem I’ve seen with ninja (mac) is nested external project builds. For example, building with <code>-j4</code> at the superbuild level means potentially four top-level projects can build in parallel. But when the flag is passed to the child process, in ninja <em>each</em> one of those tries to use four cores so the computer ends up swapping/thrashing. I don’t know if <code>msbuild</code> is susceptible to such an issue.</p>
<p>(there is a “job pool” concept in GNU make, and now available in ninja, to avoid this problem)</p>

---
