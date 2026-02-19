---
topic_id: 19072
title: "How To Handle The Resize Event Of Mainwindow"
date: 2021-08-05
url: https://discourse.slicer.org/t/19072
---

# How to handle the resize event of mainwindow

**Topic ID**: 19072
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/how-to-handle-the-resize-event-of-mainwindow/19072

---

## Post #1 by @wycstar (2021-08-05 08:38 UTC)

<p>hi all, i added a new widget to the top toolbar of the slicer mainwindow, now i wish it have a maximum width equal to the width of the main window, no matter how i resize the mainwindow. what i want to do is handle the resize event of the mainwindow, and set the width of the widget in the event handler, any better ideas to implement this?</p>

---

## Post #2 by @jamesobutler (2021-08-05 11:09 UTC)

<p>Seems like you want to use standard Qt size policy stuff to set the horizontal policy to be expanding.</p>
<p><a href="https://doc.qt.io/qt-5/qsizepolicy.html#Policy-enum" class="onebox" target="_blank" rel="noopener nofollow ugc">https://doc.qt.io/qt-5/qsizepolicy.html#Policy-enum</a></p>

---
