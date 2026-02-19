---
topic_id: 11176
title: "Error When Importing Cv2 Aruco In Python File"
date: 2020-04-18
url: https://discourse.slicer.org/t/11176
---

# Error when importing cv2.aruco in python file

**Topic ID**: 11176
**Date**: 2020-04-18
**URL**: https://discourse.slicer.org/t/error-when-importing-cv2-aruco-in-python-file/11176

---

## Post #1 by @cyrillajarge (2020-04-18 14:02 UTC)

<p>Hi guys,</p>
<p>I’m developing a module for a school project in which I need to use OpenCV combined with Aruco.<br>
I have installed the extension SlicerOpenCV and OpenCV is working correctly when I import <code>cv2</code> in my python file.<br>
However, it seems that there is no aruco submodule. When I do <code>cv2.aruco.some_function</code>, I get the error <code>object has no attribute 'aruco'</code>.<br>
I’ve installed <code>opencv-contrib-python</code> manually using pip in the python interpreter but it doesn’t fix the problem.<br>
cv2 version installed is <strong>3.3.1</strong> on 3DSlicer.</p>
<p>Operating system: MacOS Catalina <strong>10.15.2</strong><br>
Slicer version: <strong>4.10.2</strong></p>
<p>Many thanks in advance!</p>

---

## Post #2 by @lassoan (2020-04-18 14:03 UTC)

<p>If you switch to a recent Slicer-4.11 version then you can run <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.pip_install"><code>slicer.util.pip_install()</code></a> to install any python package. No need to use SlicerOpenCV anymore.</p>

---

## Post #3 by @cyrillajarge (2020-04-20 18:44 UTC)

<p>It worked!<br>
Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
