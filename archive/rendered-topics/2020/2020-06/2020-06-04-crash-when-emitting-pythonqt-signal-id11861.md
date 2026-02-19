---
topic_id: 11861
title: "Crash When Emitting Pythonqt Signal"
date: 2020-06-04
url: https://discourse.slicer.org/t/11861
---

# Crash when emitting PythonQt.Signal

**Topic ID**: 11861
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/crash-when-emitting-pythonqt-signal/11861

---

## Post #1 by @Felipe_Silveira (2020-06-04 13:27 UTC)

<p>Hi, I have some qt widgets that have some extra callbacks as signals, but I have a crash every time that I call <code>emit</code>. I have this problem with the latest stable and also the nightly build from a few days ago.</p>
<p>The repro steps are quite simple:<br>
import qt<br>
qt.Signal().emit()</p>
<p>This issue seems to already have been reported but I can’t work around it by using another mechanism because I’d have to change a lot UI code that’s already written.</p>
<p>The mentioned threads are: <a href="https://discourse.slicer.org/t/custom-signal-slots-with-pythonqt/3278" class="inline-onebox">Custom Signal/Slots with PythonQt</a> and <a href="https://discourse.slicer.org/t/use-of-qt-signal-leads-to-a-crash-on-exit/8321" class="inline-onebox">Use of qt.Signal leads to a crash on exit</a></p>

---

## Post #2 by @lassoan (2020-06-06 05:33 UTC)

<p>You must not emit signals on behalf of another Qt object.</p>
<p>Tell us a bit more about what you are trying to achieve and we can help with finding a good design for it.</p>

---

## Post #3 by @Felipe_Silveira (2020-06-09 12:19 UTC)

<p>Sorry, the example was a bit too contrived.</p>
<p>As I was trying things out I was calling emit from the console and got the mentioned crash.<br>
Instantiating the widget and actually using the UI doesn’t show the crash.</p>

---
