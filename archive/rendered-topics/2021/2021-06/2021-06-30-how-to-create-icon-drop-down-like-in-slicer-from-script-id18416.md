# How to create icon drop down like in slicer from script?

**Topic ID**: 18416
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/how-to-create-icon-drop-down-like-in-slicer-from-script/18416

---

## Post #1 by @Chintha_Siva_Prasad (2021-06-30 05:03 UTC)

<p>I was able to create an icon drop-down from python-qt5 by setting the text argument to empty text. But it’s not at looking good, I want icon drop-down as it looks in slicer. How can I create it from script?</p>

---

## Post #2 by @jamesobutler (2021-06-30 11:18 UTC)

<p>Can you provide an image of an example that you are trying to replicate? Is it a QMenu, QComboBox?</p>

---

## Post #3 by @Chintha_Siva_Prasad (2021-07-01 12:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="18416">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>that</p>
</blockquote>
</aside>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad0e119f18aa759ca07a8e48d043febf21bdc630.png" alt="Screenshot from 2021-07-01 17-30-03" data-base62-sha1="oGUKaISgre9FKXbdeZYW2vCKl9u" width="64" height="60"></p>

---

## Post #4 by @jamesobutler (2021-07-01 12:12 UTC)

<p>This is a question about standard Qt functionality and is not Slicer specific, but here are some details about it.</p>
<p>Create a <a href="https://doc.qt.io/qt-5/qaction.html" rel="noopener nofollow ugc">QAction</a> with an icon set to it and add it to the <a href="https://doc.qt.io/qt-5/qmenu.html" rel="noopener nofollow ugc">QMenu</a> of a <a href="https://doc.qt.io/qt-5/qtoolbutton.html" rel="noopener nofollow ugc">QToolButton</a>.</p>

---
