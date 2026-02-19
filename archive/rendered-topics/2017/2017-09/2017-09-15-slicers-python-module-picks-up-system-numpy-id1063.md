---
topic_id: 1063
title: "Slicers Python Module Picks Up System Numpy"
date: 2017-09-15
url: https://discourse.slicer.org/t/1063
---

# Slicer's Python module picks up system numpy

**Topic ID**: 1063
**Date**: 2017-09-15
**URL**: https://discourse.slicer.org/t/slicers-python-module-picks-up-system-numpy/1063

---

## Post #1 by @dzenanz (2017-09-15 18:21 UTC)

<p>I did a clean build of a recent version (9e9decc80e1bb922459799a260c558fc4ee90b06) yesterday. Build completed without errors. But when I try to run it, <code>DICOMScalarVolumePlugin.py</code> picks up system numpy which prevents some  python modules from loading (many modules depend on DICOMScalarVolumePlugin in my own fork of Slicer). Stack trace is below.</p>
<p>This happens on Linux, but not on Windows. It also happens to a version of Slicer from August 3rd with a few cherry-picked commits on top. Did anyone encounter this? Any suggestions on how to fix it?</p>
<pre><code>[461/461] Completed 'Slicer'
dzenan@corista:~/Slicer-rel$ Slicer-build/Slicer
Number of registered modules: 101 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 1, in &lt;module&gt;
    import numpy
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/__init__.py", line 180, in &lt;module&gt;
    from . import add_newdocs
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/add_newdocs.py", line 13, in &lt;module&gt;
    from numpy.lib import add_newdoc
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/lib/__init__.py", line 8, in &lt;module&gt;
    from .type_check import *
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/lib/type_check.py", line 11, in &lt;module&gt;
    import numpy.core.numeric as _nx
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/core/__init__.py", line 14, in &lt;module&gt;
    from . import multiarray
ImportError: /home/dzenan/.local/lib/python2.7/site-packages/numpy/core/multiarray.so: undefined symbol: _PyUnicodeUCS4_IsWhitespace
loadSourceAsModule - Failed to load file "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOMScalarVolumePlugin.py"  as module "DICOMScalarVolumePlugin" ! 
Fail to instantiate module  "DICOMScalarVolumePlugin" 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/Editor.py", line 4, in &lt;module&gt;
    import EditorLib
  File "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/EditorLib/__init__.py", line 14, in &lt;module&gt;
    from PaintEffect import *
  File "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/EditorLib/PaintEffect.py", line 9, in &lt;module&gt;
    import numpy
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/__init__.py", line 180, in &lt;module&gt;
    from . import add_newdocs
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/add_newdocs.py", line 13, in &lt;module&gt;
    from numpy.lib import add_newdoc
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/lib/__init__.py", line 8, in &lt;module&gt;
    from .type_check import *
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/lib/type_check.py", line 11, in &lt;module&gt;
    import numpy.core.numeric as _nx
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/core/__init__.py", line 14, in &lt;module&gt;
    from . import multiarray
ImportError: /home/dzenan/.local/lib/python2.7/site-packages/numpy/core/multiarray.so: undefined symbol: _PyUnicodeUCS4_IsWhitespace
loadSourceAsModule - Failed to load file "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/Editor.py"  as module "Editor" ! 
Fail to instantiate module  "Editor" 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 4, in &lt;module&gt;
    import vtk.util.numpy_support
  File "/home/dzenan/Slicer-rel/VTKv8-build/Wrapping/Python/vtk/util/numpy_support.py", line 30, in &lt;module&gt;
    import numpy
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/__init__.py", line 180, in &lt;module&gt;
    from . import add_newdocs
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/add_newdocs.py", line 13, in &lt;module&gt;
    from numpy.lib import add_newdoc
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/lib/__init__.py", line 8, in &lt;module&gt;
    from .type_check import *
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/lib/type_check.py", line 11, in &lt;module&gt;
    import numpy.core.numeric as _nx
  File "/home/dzenan/.local/lib/python2.7/site-packages/numpy/core/__init__.py", line 14, in &lt;module&gt;
    from . import multiarray
ImportError: /home/dzenan/.local/lib/python2.7/site-packages/numpy/core/multiarray.so: undefined symbol: _PyUnicodeUCS4_IsWhitespace
loadSourceAsModule - Failed to load file "/home/dzenan/Slicer-rel/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py"  as module "MultiVolumeImporterPlugin" ! 
Fail to instantiate module  "MultiVolumeImporterPlugin" 
Number of instantiated modules: 98 
Number of loaded modules: 98 
Switch to module:  "Welcome"</code></pre>

---

## Post #2 by @lassoan (2017-09-15 18:42 UTC)

<p>I don’t know about best practices on Linux, but on Windows you are not supposed to pollute system or user environment settings with application-specific paths. If you modify paths (e.g., for your convenience you add some Python directories) then you are responsible for getting rid of those customizations when you launch an application.</p>

---

## Post #3 by @jcfr (2017-09-15 19:05 UTC)

<p>Hi Dzenan,</p>
<p>This is a known problem. We will implement a solution next week. In the<br>
mean time, talk to Forest.</p>
<p>Hth<br>
Jc</p>

---

## Post #4 by @bpaniagua (2017-09-19 16:59 UTC)

<p>Has this been resolved? I am having the same problem in Ubuntu 16.04.</p>

---

## Post #5 by @fedorov (2017-09-19 21:54 UTC)

<p>I don’t know if this is the same issue or not, but I had issues with local python - if I remember correctly, it went away after I removed the offending python from PATH and VIRTUAL_ENV: <a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2013/033625.html">http://massmail.spl.harvard.edu/public-archives/slicer-devel/2013/033625.html</a></p>

---

## Post #6 by @forrest.li (2017-09-20 16:53 UTC)

<p>Here’s a temporary workaround until Jc pushes the fix into slicer.</p>
<p>Open the file <code>SlicerLauncherSettings.ini</code> for editing. This should be in Slicer’s <code>bin/</code> dir. Under the heading “[EnvironmentVariables]”, add the following line:</p>
<pre><code class="lang-auto">PYTHONUSERBASE=&lt;APPLAUNCHER_DIR&gt;/lib/Python/lib/python2.7/site-packages
</code></pre>
<p>(Re)start slicer, and slicer should now be using the bundled numpy, so no more undefined symbols from numpy imports.</p>

---

## Post #7 by @lassoan (2017-09-20 18:23 UTC)

<p>Should this be set in the launcher settings by default?</p>

---

## Post #8 by @jcfr (2017-09-20 19:00 UTC)

<p>Yes. That is the plan but since this had other implications, more testing<br>
is required to confirm it doesn’t break anything else …</p>

---

## Post #9 by @jcfr (2018-01-25 23:23 UTC)

<p>To follow up with this, back in december the issue was fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26688">r26688</a>  and the fix is included in Slicer 4.8.1.</p>
<p>Thanks <a class="mention" href="/u/dzenanz">@dzenanz</a> for the report, and <a class="mention" href="/u/forrest.li">@forrest.li</a> for his help understanding the problem.</p>
<p>Cc: <a class="mention" href="/u/laurapascal">@laurapascal</a></p>

---
