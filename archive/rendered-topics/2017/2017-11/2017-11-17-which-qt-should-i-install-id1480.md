# Which Qt should I install?

**Topic ID**: 1480
**Date**: 2017-11-17
**URL**: https://discourse.slicer.org/t/which-qt-should-i-install/1480

---

## Post #1 by @Fernando (2017-11-17 10:19 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Mac_OSX_10.12_.28Sierra.29" rel="nofollow noopener">This link</a> says Qt4, but I think Slicer now uses Qt5. Should I blindly follow the build instructions of that wiki or try installing Qt5?</p>
<p>I’m on macOS Sierra 10.12.6.</p>

---

## Post #2 by @cpinter (2017-11-17 13:28 UTC)

<p>Hi Fernando! Transition to Qt5 is underway, but the official is still 4.8.7, and probably will be for a few more months, as not everything works yet with Qt5. If you feel advanterous, you can go ahead and build with Qt 5.9.1 <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #3 by @Fernando (2017-11-17 13:47 UTC)

<p>Hi Csaba, thanks! I’ll let you know of my adventures.</p>

---

## Post #4 by @fedorov (2018-03-02 15:31 UTC)

<p>I had the same question, and needed to build with Qt5 in an attempt to reproduce a failure in the nightly.</p>
<p>It was not easy to find instructions how to build Slicer against Qt5 (wiki build instructions refer to Qt4), even though Qt5 is used by the dashboard.</p>
<p>After some searching I figured I should follow steps in this page: <a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8">https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8</a>, which is what I am trying now.</p>
<p>Just in case someone else attempts to build with Qt5.</p>

---

## Post #5 by @jcfr (2018-03-02 15:48 UTC)

<p>If you can, the latest Qt 5.10. This is was we used for testing.</p>
<p>That said, we there is no hard requirements … Slicer should compile with Qt 5.6 and above.</p>
<blockquote>
<p>to find instructions how to build Slicer against Qt5</p>
</blockquote>
<p>We didn’t get a chance to update the wiki. Help from everyone is welcome <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @fedorov (2018-03-02 16:09 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="1480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>We didn’t get a chance to update the wiki. Help from everyone is welcome <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>I <a href="https://www.slicer.org/w/index.php?title=Documentation%2FNightly%2FDevelopers%2FBuild_Instructions%2FPrerequisites&amp;type=revision&amp;diff=58704&amp;oldid=57518">added the pointer</a> to the Labs page from the build instructions wiki page. Downloading Qt5 and configuring as suggested there is working so far for me on Ubuntu 16.</p>

---
