# How to access qtcore constants in Python?

**Topic ID**: 13137
**Date**: 2020-08-24
**URL**: https://discourse.slicer.org/t/how-to-access-qtcore-constants-in-python/13137

---

## Post #1 by @Chintha_Siva_Prasad (2020-08-24 06:49 UTC)

<p>I can import qt in a slicelet and use all qtwidgets. But how can I qtcore.<br>
And also is there a way to PyQt5 so that I can use the qtcore from there…</p>

---

## Post #2 by @lassoan (2020-08-24 14:39 UTC)

<p>Slicer uses <strong>PythonQt</strong> library for Python wrapping of Qt. <strong>PyQt</strong> is not free to use (it has GPL/commercial license), so we have never even considered using it. <strong>Python for Qt</strong> is very popular, as it is provided by the Qt company, but PythonQt has many advantages - most importantly that it is intended for applications that embed Python.</p>
<p>Anyway, Slicer imports all Qt packages in <code>qt</code> namespace. For example, <code>QFile</code> class in <code>qtcore</code> can be accessed as <code>qt.QFile()</code></p>

---

## Post #3 by @Chintha_Siva_Prasad (2020-08-24 15:04 UTC)

<p>But how can I get the core variables like qtCore.horizontal, vertical etc… to set the orientations,  behaviour etc. of various widgets.</p>

---

## Post #4 by @lassoan (2020-08-24 15:07 UTC)

<p>Constants in the global C++ <code>Qt</code> namespace are in <code>Qt</code> namespace in Python. For example <code>qt.Qt.Horizontal</code>.</p>

---

## Post #5 by @Chintha_Siva_Prasad (2020-08-24 15:10 UTC)

<p>That worked…<br>
Thank You sir…</p>

---
