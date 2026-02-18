# QtWebEngine dependency

**Topic ID**: 4195
**Date**: 2018-09-26
**URL**: https://discourse.slicer.org/t/qtwebengine-dependency/4195

---

## Post #1 by @ihnorton (2018-09-26 19:38 UTC)

<p>From <a href="https://discourse.slicer.org/t/2018-09-18-hangout/4132/2" class="inline-onebox">2018.09.18 Hangout - #2 by Sam_Horvath</a></p>
<aside class="quote no-group" data-username="Sam_Horvath" data-post="2" data-topic="4132">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"><a href="https://discourse.slicer.org/t/2018-09-18-hangout/4132/2">2018.09.18 Hangout</a></div>
<blockquote>
<p>discussed the role of QtWebEngine in Slicer, and what would be needed to remove the dependency</p>
</blockquote>
</aside>
<p>+ <img src="https://emoji.discourse-cdn.com/twitter/infinity.png?v=12" title=":infinity:" class="emoji" alt=":infinity:" loading="lazy" width="20" height="20">,  QtWebEngine is by far the most brittle, difficult dependency to build, and it’s also the largest single library after SimpleITK (which could potentially be made smaller with some linking changes, I think).</p>
<p>(if anyone is hacking on this, a huge initial improvement would be to just make QtWebEngine optional –  the benefit is very limited for local builds, which cannot really use the extension manager anyway. I believe the other main use is the old jquery plotting system, but that could be disabled too)</p>

---

## Post #2 by @lassoan (2018-09-26 20:07 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="1" data-topic="4195">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>I believe the other main use is the old jquery plotting system, but that could be disabled too</p>
</blockquote>
</aside>
<p>That’s replaced by the much faster and more flexible <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots">table node based plotting</a> infrastructure. We can deprecate the old jquery based method anytime (probably we can do it after releasing 4.10).</p>

---

## Post #3 by @jamesobutler (2018-09-26 21:10 UTC)

<p>For Windows builds, Qt 5.11 updated QtWebEngine to use Chromium 65 which requires Visual Studio 2017 to build (<a href="http://doc.qt.io/qt-5/qtwebengine-platform-notes.html" rel="nofollow noopener">QtWebEngine platform notes</a> and <a href="https://chromium.googlesource.com/chromium/src/+/master/docs/windows_build_instructions.md#Setting-up-Windows" rel="nofollow noopener">Chromium build instructions</a>).  If downloading the Qt5 binary using the Qt Maintenance Tool, QtWebEngine will only be downloaded if you choose the MSVC 2017 64-bit option.</p>
<p>If Slicer is going to keep using QtWebEngine, Slicer will need to restrict using Qt &gt;5.11 if building QtWebEngine dependencies, or officially support Windows builds using MSVC 2017.</p>
<p><a href="https://wiki.qt.io/Qt_5.12_Release" rel="nofollow noopener">Qt 5.12</a> should be released by the end of November and will be a LTS release.  Might make sense to prepare for 5.12 by building Windows builds with MSVC 2017. It honestly will be a little more user friendly for people who aren’t frequent source builders since Visual Studio 2015 community doesn’t have a publicly available download anymore and you have to use Visual Studio 2017 w/v140 package and specify the v140 toolset during configuration.</p>

---

## Post #4 by @lassoan (2018-09-27 04:56 UTC)

<p>After we release Slicer-4.10 we plan to use the same Visual Studio version that is used for building official Python packages so that we can install binary packages directly. Currently, <a href="https://wiki.python.org/moin/WindowsCompilers">Python 3.5 and 3.6 uses VS2015</a> and <a href="https://devguide.python.org/setup/#windows">Python 3.6 and 3.7 can use VS2017</a>. So, we can jump to Python 3.6 + Qt 5.11 (with QtWebEngine).</p>
<p>However, due to problems listed above (size, difficulty to build, offering different look&amp;feel and somewhat limited interface with the application), it would be still nice to get rid of QtWebEngine.</p>

---

## Post #5 by @pieper (2018-09-27 12:54 UTC)

<p>For the near term it does appear that QtWebEngine is causing more trouble than it’s worth, given the limited number of places it’s currently used.  As we discussed on the last dev call it there is some work required to work around it and turn off the dependency.</p>
<p>Longer term we can keep an eye on how things evolve.  If it becomes a seamless first class part of Qt, then having a consistent and controllable cross-platform web infrastructure could be really powerful.</p>

---
