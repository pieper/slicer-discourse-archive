---
topic_id: 9468
title: "Can I Import A Py With No Class"
date: 2019-12-10
url: https://discourse.slicer.org/t/9468
---

# Can I import a py with no class?

**Topic ID**: 9468
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/can-i-import-a-py-with-no-class/9468

---

## Post #1 by @timeanddoctor (2019-12-10 23:36 UTC)

<p>I writed a py file which could run in my connda and I went implant it in slicer just litter modify.<br>
When I test it and some erro happen just like:<br>
RuntimeError: qSlicerScriptedLoadableModule::setPythonSource - Failed to load scripted loadable module: class off2obj was not found in file C:/Users/1/Desktop/3dp/off2obj.py…</p>
<p>So, firstly, can I import it with no class?</p>
<p>and secondly, can I run my py file in python interactor(slicer) directly just like run it in Anaconda Prompt?</p>

---

## Post #2 by @lassoan (2019-12-11 01:45 UTC)

<p>If you want to run your script at every startup then you can put it into your .slicerrc.py file (Application settings / General / Application startup script).</p>
<p>If you want to run your script from the command-line then you can launch Slicer like this: <code>Slicer.exe --python-script /tmp/test.py</code></p>
<p>However, the simplest and most flexible is to create a Python scripted module. You can then offer a GUI to use your script (not mandatory, but useful) and the function can be executed from Slicer’s Python console or from other modules.</p>

---

## Post #3 by @pieper (2019-12-11 15:11 UTC)

<p>In python2 there was also <code>execfile('/tmp/code.py')</code> but it was removed for python3.  Instead I tend to use this little recipe for quick tests: <code>eval(open('/tmp/code.py').read())</code></p>

---
