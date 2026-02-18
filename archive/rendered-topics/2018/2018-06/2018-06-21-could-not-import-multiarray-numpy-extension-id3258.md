# Could not import multiarray numpy extension

**Topic ID**: 3258
**Date**: 2018-06-21
**URL**: https://discourse.slicer.org/t/could-not-import-multiarray-numpy-extension/3258

---

## Post #1 by @pranavkgaur (2018-06-21 13:33 UTC)

<p>Operating system: Ubuntu 16.04<br>
Slicer version: 4.8<br>
Expected behavior: Slicer successfully loads all modules<br>
Actual behavior: Throws following error:</p>
<pre><code class="lang-auto">pranav@pranav-desktop:~/Libraries/Slicer-4.8.0-linux-amd64$ ./Slicer 
Number of registered modules: 135 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/pranav/Libraries/Slicer-4.8.0-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 1, in &lt;module&gt;
    import numpy
  File "/home/pranav/anaconda3/lib/python3.6/site-packages/numpy/__init__.py", line 142, in &lt;module&gt;
    from . import add_newdocs
  File "/home/pranav/anaconda3/lib/python3.6/site-packages/numpy/add_newdocs.py", line 13, in &lt;module&gt;
    from numpy.lib import add_newdoc
  File "/home/pranav/anaconda3/lib/python3.6/site-packages/numpy/lib/__init__.py", line 8, in &lt;module&gt;
    from .type_check import *
  File "/home/pranav/anaconda3/lib/python3.6/site-packages/numpy/lib/type_check.py", line 11, in &lt;module&gt;
    import numpy.core.numeric as _nx
  File "/home/pranav/anaconda3/lib/python3.6/site-packages/numpy/core/__init__.py", line 26, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 
Importing the multiarray numpy extension module failed.  Most
likely you are trying to import a failed build of numpy.
If you're working with a numpy git repo, try `git clean -xdf` (removes all
files not under version control).  Otherwise reinstall numpy.
</code></pre>
<p>Original error was: cannot import name multiarray</p>
<pre><code class="lang-auto">loadSourceAsModule - Failed to load file "/home/pranav/Libraries/Slicer-4.8.0-linux-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOMScalarVolumePlugin.py"  as module "DICOMScalarVolumePlugin" ! 
Fail to instantiate module  "DICOMScalarVolumePlugin" 
</code></pre>
<p>As it can be observed from the logs, I am using numpy from the anaconda package repository. I would like to know how to fix this issue?</p>

---

## Post #2 by @pieper (2018-06-21 18:04 UTC)

<p>When you use the launcher, as you have, Slicer should always be setting the environment paths to pick up it’s own version of numpy.  Did you do something that overrides this?</p>

---

## Post #3 by @pranavkgaur (2018-06-22 10:08 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> for pointing out the possibility of overriding default settings, which in fact I did during anaconda installation. Specifically, I(unnecessarily) modified the PYTHONPATH  variable to point to anaconda site-packages, from which Slicer was trying to import numpy. The problem is fixed now, by re-exporting PYTHONPATH with default value.</p>

---
