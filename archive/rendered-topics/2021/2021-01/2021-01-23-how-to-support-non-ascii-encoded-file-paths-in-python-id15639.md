# How to support non-ASCII encoded file paths in python?

**Topic ID**: 15639
**Date**: 2021-01-23
**URL**: https://discourse.slicer.org/t/how-to-support-non-ascii-encoded-file-paths-in-python/15639

---

## Post #1 by @slicer365 (2021-01-23 13:45 UTC)

<p>Slicer should start python when it starts. I want to know where the python source files are. I want to add the code <span class="hashtag">#coding:utf-8</span> to it so that it can support non-ASCII encoded file paths.</p>

---

## Post #2 by @lassoan (2021-01-23 14:26 UTC)

<p>You can already use utf8 in your source files if you use latest Slicer Stable or Preview Release.</p>
<p>You currently cannot easily pass command-line arguments with utf8 encoding from the console - see more details here: <a href="https://github.com/Slicer/Slicer/issues/5383" class="inline-onebox">SimpleITK is not available on Windows if Slicer is installed in a path that contains special characters · Issue #5383 · Slicer/Slicer · GitHub</a></p>
<p>It is unlikely that adding utf8 encoding indicator to any Python files would fix the issue, as it seems that it is due to how the main Python executable is initialized, but we are open to test any suggestions.</p>

---

## Post #3 by @slicer365 (2021-01-23 14:59 UTC)

<p>In fact, I hope it be able to allow the Chinese path file. The version I used before seems to be OK, but the latest version 4.1120200930 does not allow the direct import of Chinese path files</p>

---

## Post #4 by @lassoan (2021-01-23 15:22 UTC)

<p>I would suggest to use ASCII filenames, as it is done in all the millions of Python packages out there.</p>
<p>There are problems with utf8 on Windows with latest stable because we switched to utf8 code page in the application so that internally we can use utf8 everywhere. However, the Windows console and/or Python 3.6 has limited support for utf8 application code page.</p>
<p>If this is important for you then please investigate. For example, try building Slicer with Python 3.8 or later or ask around on Python forums about how to embed Python in applications that use utf8 code page.</p>

---

## Post #5 by @jcfr (2021-04-13 18:58 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-load-script-in-hellopython-tutorial/17072">How to load script in HelloPython tutorial?</a></p>

---
