# Adding widget above or below the toolbar

**Topic ID**: 19464
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/adding-widget-above-or-below-the-toolbar/19464

---

## Post #1 by @Chintha_Siva_Prasad (2021-09-01 14:34 UTC)

<p>I am running a custom python script with slicer main window. And I want to add a widget or layout between above or below the toolbar.</p>

---

## Post #2 by @jamesobutler (2021-09-01 15:39 UTC)

<p>A <a href="https://doc.qt.io/qt-5/qmainwindow.html" rel="noopener nofollow ugc">QMainWindow</a> does not support widgets above the top toolbar area.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efce75bfc26add9cd65c62fd4a3eb587c13efe6e.png" alt="image" data-base62-sha1="ydqs8CwGIB7zF9zXr5acR5TEEkC" width="455" height="302"></p>

---

## Post #3 by @lassoan (2021-09-01 16:55 UTC)

<p>If you want to place anything above toolbars then they have to be toolbars, too. You can have any number of toolbar rows, put any number of toolbars in them, put any widgets in any of the toolbars, and you can move the toolbars between toolbar rows any way you want. This is all standard Qt API, so look for details in the Qt documentation, Stack Overflow, etc.</p>

---
