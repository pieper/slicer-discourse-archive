---
topic_id: 1664
title: "Close Scene In Python"
date: 2017-12-15
url: https://discourse.slicer.org/t/1664
---

# "Close Scene" in python

**Topic ID**: 1664
**Date**: 2017-12-15
**URL**: https://discourse.slicer.org/t/close-scene-in-python/1664

---

## Post #1 by @Frederic (2017-12-15 09:23 UTC)

<p>Hi,<br>
before it was: “Slicer.slicer.ApplicationGUI.ProcessCloseSceneCommand()”, but what is the command line now?<br>
Thanks in advance.</p>

---

## Post #2 by @cpinter (2017-12-15 14:52 UTC)

<p>The way you programmatically closed the scene is a fragile call to a handler function. This is the proper way to close the scene:</p>
<pre><code>slicer.mrmlScene.Clear(0)</code></pre>

---

## Post #3 by @Frederic (2017-12-15 15:16 UTC)

<p>Thanks a lot Csaba!<br>
Best</p>

---
