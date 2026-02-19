---
topic_id: 34752
title: "Looking For Old Slicer 3D Source Code With Wxwidgets And Vtk"
date: 2024-03-06
url: https://discourse.slicer.org/t/34752
---

# Looking for old Slicer 3D source code with wxWidgets and VTK

**Topic ID**: 34752
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/looking-for-old-slicer-3d-source-code-with-wxwidgets-and-vtk/34752

---

## Post #1 by @keri (2024-03-06 20:26 UTC)

<p>Hi,</p>
<p>The question is not about Slicer 3D but I remember I’ve read that Slicer used to be using wxWidgets before it was translated to Qt.</p>
<p>Now there is a task to understand how can I combine wxWidgets with VTK (even I don’t have experience with wxWidgets yet). Mostly the question is how to create a widget with VTK render window in it and then to be able to connect wxWidgets signals (or events) with VTK observers.</p>
<p>Maybe somebody could give some hints about that? Or maybe there is still old Slicer 3D releases where it is already implemented?</p>

---

## Post #2 by @muratmaga (2024-03-06 20:28 UTC)

<p>This is probably better asked in the <a href="https://discourse.vtk.org/">VTK forum</a>. However, it looks like this link might of some interest to you:<br>
<a href="https://forums.wxwidgets.org/viewtopic.php?p=212799&amp;sid=facae6786160e8638a52c0a41423a10b#p212799" class="onebox" target="_blank" rel="noopener">https://forums.wxwidgets.org/viewtopic.php?p=212799&amp;sid=facae6786160e8638a52c0a41423a10b#p212799</a></p>

---

## Post #3 by @keri (2024-03-06 20:33 UTC)

<p>Thank you!</p>
<p>Actually I was thinking where to ask this question but decided to ask there as most of the time Slicer 3D community helped a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thank you for the link! It is in Python and this will be the most easiest way to make first attempts.</p>

---

## Post #4 by @jcfr (2024-03-06 20:37 UTC)

<aside class="quote no-group" data-username="keri" data-post="1" data-topic="34752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Slicer used to be using wxWidgets before it was translated to Qt.</p>
</blockquote>
</aside>
<p>To clarify, prior to Slicer 4.x, the cross-platform <code>KWWidgets</code><sup class="footnote-ref"><a href="#footnote-107907-1" id="footnote-ref-107907-1">[1]</a></sup>  toolkit was used  and not <code>wxWidgets</code></p>
<p>For reference:</p>
<blockquote>
<p>KWWidgets [was] a free, cross-platform and open-license GUI Toolkit. Over a hundred C++ classes have been developed and used by Kitware, Inc. to create open-source and commercial end-user applications like ParaView or VolView […]. Is [was] also used by the National Alliance for Medical Image Computing for the 3D Slicer project.</p>
</blockquote>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-107907-1" class="footnote-item"><p><a href="https://web.archive.org/web/20200123234643/http://www.kwwidgets.org/Wiki/KWWidgets" class="inline-onebox">KWWidgets - KitwarePublic</a> <a href="#footnote-ref-107907-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #5 by @keri (2024-03-06 20:41 UTC)

<p>Oh! I’m sorry.</p>
<p>Good to know, thank you!</p>

---

## Post #6 by @lassoan (2024-03-07 05:59 UTC)

<p>I’m just curious, why are you thinking about using wxWidgets? Qt license costs? What alternatives have you considered?</p>

---

## Post #7 by @keri (2024-03-07 09:43 UTC)

<p>Hello Andras,</p>
<p>It is all about sanctions. Qt have officially quited our country. Some companies don’t want to risk.</p>
<p>Also I remember <a href="https://discourse.vtk.org/t/build-an-desktop-application-using-vtk/8542/6?u=kerim" rel="noopener nofollow ugc">your post about Qt licensing</a>. But as I remember since Qt6 it started to use GPL3 (not LGPL) everywhere. This is going to add more restrictions right?</p>

---

## Post #8 by @pieper (2024-03-07 14:42 UTC)

<p>Regarding Qt6, from what I see the core is still available under LGPL:</p>
<p><a href="https://doc.qt.io/qt-6/licensing.html">https://doc.qt.io/qt-6/licensing.html</a></p>
<p>There are some Qt add-ons that are GPL or commercial only, so people should keep that in mind if they want to use them.  We shouldn’t use these in Slicer:</p>
<p><a href="https://doc.qt.io/qt-6/qtmodules.html#gpl-licensed-addons">https://doc.qt.io/qt-6/qtmodules.html#gpl-licensed-addons</a></p>

---

## Post #9 by @keri (2024-03-07 16:33 UTC)

<p>Thank you! Good to know.</p>

---

## Post #10 by @lassoan (2024-03-07 19:03 UTC)

<p>I agree, I don’t think a lot has changed in Qt regarding GPL/LGPL (some very niche Qt components has been GPL but we don’t need any of them). The main difference in Qt6 that you cannot get long-term support versions for free from the Qt Company. If you need stable Qt distributions for free then you need to go elsewhere. For example you can get it from <a href="https://www.phoronix.com/news/KDE-Qt-5-Patch-Collection">KDE</a>, but probably they only work on fixes for Linux.</p>
<p>In general, Qt Company is not behaving in a developer-friendly way, it does not invest much effort into classic widgets, and it does not focus on making it possible to run Qt applications with classic widgets in web browsers. So, it would be nice to find a possible alternatives.</p>
<p>wxWidget has no licensing issues, but it has very limited feature set, its development is quite slow, and I am not sure if it officially supports usage in the web browser. What other frameworks have you considered? Have you found any more actively developed, more modern, more web-friendly GUI framework?</p>

---

## Post #11 by @keri (2024-03-08 00:12 UTC)

<p>I don’t think we have many choices because we need to use GUI framework along with VTK.</p>
<p>I know that wxWidgets have some (limited) support for VTK that is pros to use it.</p>
<p>Another option is to use client-server solutions and the use some other languages for frontend along with some remote VTK features. Here is the problem that not all the VTK functionality will be available (I guess) and it will be very sad to fall into such situation.</p>
<p>And for future references there was a <a href="https://discourse.vtk.org/t/what-are-the-best-gui-toolkits-that-can-be-used-to-make-a-vtk-based-app/9550/9" rel="noopener nofollow ugc">similar topic</a></p>

---

## Post #12 by @lassoan (2024-03-08 00:16 UTC)

<p>That topic is 1.5 years old, which is quite a long time these days. Now VTK can run natively in the web browser. No need for server-side rendering and remoting anymore.</p>

---

## Post #13 by @keri (2024-03-08 00:44 UTC)

<p>Do you mean Trame and VTK.js?</p>

---

## Post #14 by @lassoan (2024-03-08 00:50 UTC)

<p>I mean C++ application using proper VTK (not vtk.js) compiled using webassembly and running in the web browser. See all the interactive examples in the VTK examples website: <a href="https://examples.vtk.org/site/Cxx/IO/ReadAllPolyDataTypesDemo/">https://examples.vtk.org/site/Cxx/IO/ReadAllPolyDataTypesDemo/</a></p>

---

## Post #15 by @keri (2024-03-08 00:58 UTC)

<p>Thank you, cempletely forgot about that approach. I have to test that because it seems very attractive.</p>

---

## Post #16 by @chir.set (2024-03-08 07:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="34752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I mean C++ application using proper VTK (not vtk.js) compiled using webassembly and running in the web browser.</p>
</blockquote>
</aside>
<p>Would the <a href="https://www.webtoolkit.eu/wt" rel="noopener nofollow ugc">Wt</a> libraries have a place in this discussion? This is just a pointer since it aims at building web applications in C++.</p>

---

## Post #17 by @keri (2024-03-08 09:02 UTC)

<p>Looks interesting, thank you.</p>
<p>The only thing is how to combine it with VTK (no information in internet yet).<br>
And another thing is GPL license: <a href="https://www.webtoolkit.eu/wt/download" rel="noopener nofollow ugc">they claim to open source code for any user</a>. Do they mean to open the whole project?</p>

---

## Post #18 by @chir.set (2024-03-08 09:11 UTC)

<aside class="quote no-group" data-username="keri" data-post="17" data-topic="34752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>how to combine it with VTK</p>
</blockquote>
</aside>
<p>Don’t know, it was just a suggestion.</p>
<aside class="quote no-group" data-username="keri" data-post="17" data-topic="34752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Do they mean to open the whole project?</p>
</blockquote>
</aside>
<p>Quoting the page you pointed to:</p>
<p><code>**The Commercial License** has no such limitations: you may redistribute applications developed with Wt without needing to redistribute the source code.</code></p>
<p>Buying a license is mandatory for closed source applications.</p>

---
