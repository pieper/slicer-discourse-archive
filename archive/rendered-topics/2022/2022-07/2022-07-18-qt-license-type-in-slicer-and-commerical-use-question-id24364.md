---
topic_id: 24364
title: "Qt License Type In Slicer And Commerical Use Question"
date: 2022-07-18
url: https://discourse.slicer.org/t/24364
---

# QT license type in Slicer and commerical use question?

**Topic ID**: 24364
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/qt-license-type-in-slicer-and-commerical-use-question/24364

---

## Post #1 by @StephenLeePeng (2022-07-18 11:27 UTC)

<p>Hi everybody.<br>
As QT is GUI Framework for Slicer, and QT has two types license, LGPL and GPL.<br>
LGPL includes: Core, Widgets, QML and so on.<br>
GPL includes Qt Chats and so on.</p>
<p>As I develop a product, built as an extension, running on Slicer platform. I change some logo, or view controller font in C++, others codes are written by Python.</p>
<p>So I want to know, the product of extension can be used in commerical without open source? <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2022-07-18 13:09 UTC)

<p>We don’t use any GPL-licensed components for building 3D Slicer. You are free to use it for commercial purposes, for free, without asking permission from anyone.</p>

---

## Post #3 by @pieper (2022-07-18 18:26 UTC)

<p>Note also that if you choose to use GPL licensed portions of Qt or use Qt in a way that is inconsistent with the terms of the LGPL you may need a commercial license to Qt.  For a commercial product this is generally not a problem so you should do it if required by the terms of the licenses.</p>

---

## Post #4 by @jcfr (2022-07-18 20:06 UTC)

<p>The following page is useful to find out which licenses are used by each Qt components and dependencies. See <a href="https://doc.qt.io/qt-5/licenses-used-in-qt.html" class="inline-onebox">Licenses Used in Qt | Qt 5.15</a></p>

---
