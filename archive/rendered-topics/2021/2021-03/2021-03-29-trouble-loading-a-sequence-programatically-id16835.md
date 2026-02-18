# Trouble loading a sequence programatically

**Topic ID**: 16835
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/trouble-loading-a-sequence-programatically/16835

---

## Post #1 by @Teresa_Gadda (2021-03-29 21:48 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: Sequence loaded from python interactor<br>
Actual behavior: RuntimeError: Failed to load node from file</p>
<p>I have a tracked ultrasound file (generated using Plus) that I would like to load from the python interactor window with the eventual goal of being able to batch process similar files.  When I drag and drop this file into Slicer and select Sequence Metafile it loads up great and I can do all kinds of things with it.  However trying to load it with slicer.util.loadSequence results in an error (shown below).  I’ve triple checked that the file actually exists and my spelling is correct. Anyone have thoughts or ideas?</p>
<p>Thanks</p>
<pre><code>&gt;&gt;&gt;yo = slicer.util.loadSequence('C:\\Users\\teres\\OneDrive\\Desktop\\TIS_0317_rayTraced.mha')
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Slicer 4.11.20200930\bin\Python\slicer\util.py", line 818, in loadSequence
    return loadNodeFromFile(filename, filetype, properties)
  File "C:\Program Files\Slicer 4.11.20200930\bin\Python\slicer\util.py", line 598, in loadNodeFromFile
    raise RuntimeError(errorMessage)
RuntimeError: Failed to load node from file: C:\Users\teres\OneDrive\Desktop\TIS_0317_rayTraced.mha</code></pre>

---

## Post #2 by @Teresa_Gadda (2021-03-29 22:13 UTC)

<p>Nevermind.  Solved it myself.<br>
<code>yo = slicer.util.loadNodeFromFile('C:\\Users\\teres\\OneDrive\\Desktop\\TIS_0317_rayTraced.mha','Sequence Metafile')</code></p>

---
