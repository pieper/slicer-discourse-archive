# How to load with CTKWidgets and qMRMLWidgets

**Topic ID**: 5917
**Date**: 2019-02-25
**URL**: https://discourse.slicer.org/t/how-to-load-with-ctkwidgets-and-qmrmlwidgets/5917

---

## Post #1 by @Mr.wyr (2019-02-25 14:33 UTC)

<p>I read <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner</a>,and set the environment variable  <code>QT_PLUGIN_PATH</code>  to the directory  <em>Slicer-build/bin</em>,but widgets do not appear in Qt Designer</p>

---

## Post #2 by @adamrankin (2019-02-25 14:54 UTC)

<p>Does running<br>
<code>&lt;cmake-build-dir&gt;\Slicer-build\Slicer.exe --designer</code><br>
not provide those widgets?</p>

---

## Post #3 by @lassoan (2019-02-25 14:56 UTC)

<p>Also make sure Slicer and QtDesigner is built using the same build mode. If you use a precompiled Qt version then you need Slicer Qt designer plugins built in Release mode.</p>

---
