---
topic_id: 14115
title: "Fatal Python Error Py Initialize Unable To Load The File Sys"
date: 2020-10-18
url: https://discourse.slicer.org/t/14115
---

# Fatal Python error: Py_Initialize: unable to load the file system codec

**Topic ID**: 14115
**Date**: 2020-10-18
**URL**: https://discourse.slicer.org/t/fatal-python-error-py-initialize-unable-to-load-the-file-system-codec/14115

---

## Post #1 by @Warthou (2020-10-18 15:05 UTC)

<p>Hello everyone,</p>
<p>I have downloaded and built 3DSlicer. However, I am now running into these runtime errors:</p>
<p>[SSL] Failed to load Slicer.crt<br>
Fatal Python error: Py_Initialize: unable to load the file system codec</p>
<p>Visual Studio tells me it’s occurring from this line:</p>
<p>PythonQt::init(flags);</p>
<p>So I thought I needed to download PythonQt but it did not help. Does anyone know why these errors could be happening?</p>

---

## Post #2 by @lassoan (2020-10-18 15:09 UTC)

<p>Most likely you have some other Python in your path and/or you did not start Visual Studio with <code>Slicer.exe --VisualStudio</code>.</p>

---
