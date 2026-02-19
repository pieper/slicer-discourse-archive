---
topic_id: 30373
title: "Triggering Main Window Exit When Exiting From Qdialog Window"
date: 2023-07-03
url: https://discourse.slicer.org/t/30373
---

# triggering main window exit when exiting from qdialog window

**Topic ID**: 30373
**Date**: 2023-07-03
**URL**: https://discourse.slicer.org/t/triggering-main-window-exit-when-exiting-from-qdialog-window/30373

---

## Post #1 by @pcg12131415 (2023-07-03 15:59 UTC)

<p>Hi!</p>
<p>I have a Slicer module that opens a different window (using QDialog) from the Slicer main one. I would like to connect the two of them in order to close Slicer when the second one gets closed.<br>
I saw I could override some methods in QDialog (like closeEvent()), but I guess I can’t since I am importing it in the Widget class from the UI file through:<br>
self.uiWidget = slicer.util.loadUI(self.resourcePath(‘UI/Module.ui’))</p>
<p>This is the QDialog creation in the UI file (cutting out ‘&gt;’ and ‘&lt;’):</p>
<p>widget class=“QDialog” name=“Module”<br>
property name=“windowModality”<br>
enum&gt;Qt::ApplicationModal&lt;/enum</p>
<p>is there a way to trigger the closing of Slicer from the Logic of the second window?</p>

---

## Post #2 by @pieper (2023-07-03 17:14 UTC)

<p>You should be able to get a signal from the QDialog and call <code>slicer.util.exit()</code> to exit the app.</p>

---

## Post #3 by @pcg12131415 (2023-07-05 15:29 UTC)

<p>I found the reason, i was defining the signal connection after the qdialog exec() (this was in an external function so i had no idea), therefore it wasn’t seen.</p>

---
