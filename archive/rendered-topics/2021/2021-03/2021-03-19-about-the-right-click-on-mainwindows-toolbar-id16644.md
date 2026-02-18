# About the right click on mainwindow's toolbar

**Topic ID**: 16644
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/about-the-right-click-on-mainwindows-toolbar/16644

---

## Post #1 by @qin (2021-03-19 15:26 UTC)

<p>Operating system:windows10 64 bit<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:<br>
When i was right clicked the toolbars on mainwindow, a menu manager the toolbars like ‘module panel’,‘load/save’…was poped up. And i want to know where is code about the event on slicer source code…</p>

---

## Post #2 by @jamesobutler (2021-03-19 17:42 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e97bb1c03ca8a01d438cb46e3403d5212aae073d.png" alt="image" data-base62-sha1="xjugoNiTVYolrRM7hOYNKUC4qaF" width="406" height="293"><br>
This is controlled by Qt which is the GUI framework dependency used by Slicer. Therefore it is not something in the Slicer source code.</p>
<p>You can see information about a QMainWindow’s toolbar pop-up menu at: <a href="https://doc.qt.io/qt-5/qmainwindow.html#createPopupMenu" rel="noopener nofollow ugc">https://doc.qt.io/qt-5/qmainwindow.html#createPopupMenu</a></p>

---

## Post #3 by @qin (2021-03-23 06:02 UTC)

<p>thanks for your help!</p>

---
