# How to hold the imageWidget display

**Topic ID**: 13246
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/how-to-hold-the-imagewidget-display/13246

---

## Post #1 by @aiden.zhu (2020-08-31 10:19 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.0<br>
Expected behavior: show() to have the image shown<br>
Actual behavior: the image flashed and disappear</p>
<p>Hi all,<br>
I tried the following scripts,<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Using_matplotlib" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Using_matplotlib</a></p>
<h1>Static image view</h1>
<p>pm = qt.QPixmap(“MatplotlibExample.png”)<br>
imageWidget = qt.QLabel()<br>
imageWidget.setPixmap(pm)<br>
imageWidget.setScaledContents(True)<br>
imageWidget.show()</p>
<p>if I  input the above scripts into “Python Interactor”, I had the plot shown.<br>
But if I run it via a GUI click button, the plot seems flashed and disappeared right away. What’s wrong with my settings?</p>
<p>Thanks a lot.<br>
Best,<br>
Aiden</p>

---

## Post #2 by @pieper (2020-08-31 14:03 UTC)

<p>Probably your variable goes out of scope so it is cleaned up.  If you are writing a scripted module you can keep a reference to it in the <code>self</code> of the widget instance.</p>

---

## Post #3 by @aiden.zhu (2020-08-31 14:10 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:">Thanks a lot.<br>
Forget about this clearance rule.</p>

---
