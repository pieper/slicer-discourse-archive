---
topic_id: 23414
title: "Is It Possible To Integrate Slicer Ui Module View Into Our Q"
date: 2022-05-13
url: https://discourse.slicer.org/t/23414
---

# Is it possible to integrate Slicer UI module/view into our Qt 6 QML application?

**Topic ID**: 23414
**Date**: 2022-05-13
**URL**: https://discourse.slicer.org/t/is-it-possible-to-integrate-slicer-ui-module-view-into-our-qt-6-qml-application/23414

---

## Post #1 by @luxel (2022-05-13 16:40 UTC)

<p>We already have a surgical device application built with Qt 6.2 + QML (using C++ and JavaScript), and we’re looking for integrating some of the 3D Slicer UI modules or UI views as part of our UI, without building/running the standalone Slicer application. Is it possible to do that? We have been digging in github/forum/document for a few days and couldn’t find any information covering this scenario. Thank you for your time!</p>

---

## Post #2 by @pieper (2022-05-13 17:06 UTC)

<p>It might eventually be possible, but for now Slicer uses Qt 5.x and won’t port to Qt 6.x until upstream libs are all ported (VTK, PythonQt, CTK).  Once that’s working you should be able to mix and match C++ code, but some parts of Slicer is in python so you might end up needing some work to make it happen.</p>

---

## Post #3 by @lassoan (2022-05-14 21:24 UTC)

<aside class="quote no-group" data-username="luxel" data-post="1" data-topic="23414">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luxel/48/15298_2.png" class="avatar"> luxel:</div>
<blockquote>
<p>We have been digging in github/forum/document for a few days and couldn’t find any information covering this scenario</p>
</blockquote>
</aside>
<p>Slicer users classic QWidget based widgets. You can mix these widgets and QML based regions in a single application.</p>
<p>There is also a QML-based VTK render widget, but it would take some effort to reimplement view and layout classes using this class.</p>

---

## Post #4 by @Xiaowei_Chen (2024-02-20 13:53 UTC)

<p>Any luck to get this working?</p>

---

## Post #5 by @jcfr (2024-02-20 18:50 UTC)

<p>In the next few weeks, we should have the Qt6 integration finalized and will transition the “Preview” build of Slicer to build against it.</p>

---

## Post #6 by @Xiaowei_Chen (2024-03-26 17:27 UTC)

<p>Where are you on the integration?</p>

---
