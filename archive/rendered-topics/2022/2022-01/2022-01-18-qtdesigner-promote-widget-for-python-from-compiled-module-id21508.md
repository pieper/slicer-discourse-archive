# QtDesigner: promote widget for python from compiled module

**Topic ID**: 21508
**Date**: 2022-01-18
**URL**: https://discourse.slicer.org/t/qtdesigner-promote-widget-for-python-from-compiled-module/21508

---

## Post #1 by @keri (2022-01-18 03:55 UTC)

<p>Hi,</p>
<p>I’m wondering if I have compiled widget <code>qMyWidget</code> and binded it to python (standard case in Slicer). Is it possible to promote widget to <code>qMyWidget</code> for python module in QDesigner?</p>

---

## Post #2 by @lassoan (2022-03-13 04:48 UTC)

<p>You can directly use a widget in Qt Designer if you created a designer plugin for it. Most widgets in Slicer have a designer plugin, so you can use those as examples.</p>
<p>If you don’t have a plugin then maybe promotion works, but I don’t know if it is done anywhere. If we need to add a custom widget somewhere then we usually add a frame in Qt designer and then instantiate and add the custom widget in the widget’s setup method.</p>

---

## Post #3 by @keri (2022-03-15 19:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you don’t have a plugin then maybe promotion works, but I don’t know if it is done anywhere.</p>
</blockquote>
</aside>
<p>That was my case<br>
As I remember I used to have custom widget written in C++ and tried to <code>promote</code> to it and use the generated <code>.ui</code> file with python… I didn’t succeded.</p>
<p>Probably later I will try it again</p>

---
