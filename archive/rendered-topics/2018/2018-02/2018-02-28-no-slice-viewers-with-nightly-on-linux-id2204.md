---
topic_id: 2204
title: "No Slice Viewers With Nightly On Linux"
date: 2018-02-28
url: https://discourse.slicer.org/t/2204
---

# No slice viewers with nightly on Linux

**Topic ID**: 2204
**Date**: 2018-02-28
**URL**: https://discourse.slicer.org/t/no-slice-viewers-with-nightly-on-linux/2204

---

## Post #1 by @fedorov (2018-02-28 03:50 UTC)

<p>I’ve just tried running nightly on Ubuntu Linux (within Parallels on Mac), and all slice viewers are blank.</p>
<p>In the log, I see the following messages:</p>
<pre><code class="lang-auto">SystemError: /home/kitware/Dashboards/Nightly/Slicer-0-build/Python-2.7.13/Objects/classobject.c:521: bad argument to internal function
qSlicerPythonCppAPI::instantiateClass  - [ "__init__" ] - Failed to instantiate scripted pythonqt class "__init__" 0x7f91702d9f50 
Fail to instantiate module  "__init__" 
</code></pre>

---
