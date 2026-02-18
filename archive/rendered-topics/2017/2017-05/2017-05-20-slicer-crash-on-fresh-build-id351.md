# Slicer crash on fresh build

**Topic ID**: 351
**Date**: 2017-05-20
**URL**: https://discourse.slicer.org/t/slicer-crash-on-fresh-build/351

---

## Post #1 by @gregsharp.geo (2017-05-20 15:36 UTC)

<p>Hi, I am trying to get Slicer to build and run on my home computer.<br>
It is debian testing with gcc 6 (unfortunately gcc 5 no longer offered).<br>
Clean directory, disable SimpleITK, disable BRAINS,<br>
ignore inevitible BRAINSCommon build failures.  Slicer builds.<br>
Got the following error when trying to run.  Any ideas?<br>
Thanks,<br>
Greg</p>
<pre><code class="lang-auto">$ ./Slicer-build/Slicer
Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
  File "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/Python/slicer/slicerqt.py", line 6, in &lt;module&gt;
    import vtk
  File "/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/Wrapping/Python/vtk/__init__.py", line 41, in &lt;module&gt;
    from .vtkCommonKit import *
  File "/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/Wrapping/Python/vtk/vtkCommonKit.py", line 9, in &lt;module&gt;
    from vtkCommonKitPython import *
ImportError: /home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkCommonKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
  File "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/Python/slicer/slicerqt-with-tcl.py", line 42, in &lt;module&gt;
    slicer.sliceWidgets = {}
NameError: name 'slicer' is not defined
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'getSlicerRCFileName' is not defined
Number of registered modules: 85 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/CompareVolumes.py", line 3, in &lt;module&gt;
    from __main__ import vtk, qt, ctk, slicer
ImportError: cannot import name vtk
loadSourceAsModule - Failed to load file "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/CompareVolumes.py"  as module "CompareVolumes" ! 
Fail to instantiate module  "CompareVolumes" 
error: [/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.
gsharp@wormwood:~/build/slicer-4/Slicer-build$ rm -rf ~/.config/NA-MIC/
gsharp@wormwood:~/build/slicer-4/Slicer-build$ ./Slicer-build/Slicer
Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
  File "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/Python/slicer/slicerqt.py", line 6, in &lt;module&gt;
    import vtk
  File "/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/Wrapping/Python/vtk/__init__.py", line 41, in &lt;module&gt;
    from .vtkCommonKit import *
  File "/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/Wrapping/Python/vtk/vtkCommonKit.py", line 9, in &lt;module&gt;
    from vtkCommonKitPython import *
ImportError: /home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkCommonKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
  File "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/Python/slicer/slicerqt-with-tcl.py", line 42, in &lt;module&gt;
    slicer.sliceWidgets = {}
NameError: name 'slicer' is not defined
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/./libvtkRenderingKitPython27D-7.1.so.1: undefined symbol: PyUnicodeUCS2_DecodeUTF8
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'getSlicerRCFileName' is not defined
Number of registered modules: 85 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/CompareVolumes.py", line 3, in &lt;module&gt;
    from __main__ import vtk, qt, ctk, slicer
ImportError: cannot import name vtk
loadSourceAsModule - Failed to load file "/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/CompareVolumes.py"  as module "CompareVolumes" ! 
Fail to instantiate module  "CompareVolumes" 
error: [/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @lassoan (2017-05-20 15:38 UTC)

<p>Do you have the error if you don’t disable BRAINS?</p>

---

## Post #3 by @pieper (2017-05-20 16:16 UTC)

<p>Looks like a mix of python versions.  Maybe check that your environment doesn’t have and LD_PRELOAD.  Also double check that the Slicer-build/Slicer --launcher-dump-environment looks like it has all the correct paths.</p>

---

## Post #4 by @gregsharp.geo (2017-05-21 20:55 UTC)

<blockquote>
<p>Do you have the error if you don’t disable BRAINS?</p>
</blockquote>
<p>BRAINS doesn’t build.</p>
<p><a href="http://na-mic.org/Mantis/view.php?id=4268" class="onebox" target="_blank" rel="noopener nofollow ugc">http://na-mic.org/Mantis/view.php?id=4268</a></p>

---

## Post #5 by @gregsharp.geo (2017-05-21 20:58 UTC)

<blockquote>
<p>Looks like a mix of python versions.  Maybe check that your<br>
environment doesn’t have and LD_PRELOAD.  Also double check that the<br>
Slicer-build/Slicer --launcher-dump-environment looks like it has all<br>
the correct paths.</p>
</blockquote>
<p>LD_PRELOAD is not set.</p>
<p>The environment looks fine to me.  However, I don’t really know what I<br>
am looking for.  Pasted below.</p>
<pre><code class="lang-auto">LD_LIBRARY_PATH=/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/.:/usr/lib/x86_64-linux-gnu:../lib/Slicer-4.7/qt-loadable-modules:/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/cli-modules/.:/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/qt-loadable-modules/.:/home/gsharp/build/slicer-4/Slicer-build/OpenSSL:/home/gsharp/build/slicer-4/Slicer-build/tcl-build/lib:/home/gsharp/build/slicer-4/Slicer-build/python-install/lib:/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/.:/home/gsharp/build/slicer-4/Slicer-build/teem-build/bin/.:/home/gsharp/build/slicer-4/Slicer-build/DCMTK-build/lib/.:/home/gsharp/build/slicer-4/Slicer-build/ITKv4-build/lib/.:/home/gsharp/build/slicer-4/Slicer-build/CTK-build/CTK-build/bin/.:/home/gsharp/build/slicer-4/Slicer-build/CTK-build/QtTesting-build/.:/home/gsharp/build/slicer-4/Slicer-build/CTK-build/PythonQt-build/.:/home/gsharp/build/slicer-4/Slicer-build/LibArchive-install/lib:/home/gsharp/build/slicer-4/Slicer-build/OpenIGTLink-build:/home/gsharp/build/slicer-4/Slicer-build/OpenIGTLink-build/bin/.:/home/gsharp/build/slicer-4/Slicer-build/JsonCpp-build/src/lib_json/.:/home/gsharp/build/slicer-4/Slicer-build/ParameterSerializer-build/lib/.:/home/gsharp/build/slicer-4/Slicer-build/SlicerExecutionModel-build/ModuleDescriptionParser/bin/.:/home/gsharp/build/slicer-4/Slicer-build/python-install/lib/python2.7/site-packages/numpy/core:/home/gsharp/build/slicer-4/Slicer-build/python-install/lib/python2.7/site-packages/numpy/lib
PATH=/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/.:/usr/lib/x86_64-linux-gnu/qt4/bin:/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/cli-modules/.:/home/gsharp/build/slicer-4/Slicer-build/tcl-build/bin:/home/gsharp/build/slicer-4/Slicer-build/python-install/bin:/home/gsharp/build/slicer-4/Slicer-build/teem-build/bin/.
PYTHONHOME=/home/gsharp/build/slicer-4/Slicer-build/python-install
PYTHONNOUSERSITE=1
PYTHONPATH=/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/.:/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin/Python:/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/qt-loadable-modules/.:/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/lib/Slicer-4.7/qt-loadable-modules/Python:/home/gsharp/build/slicer-4/Slicer-build/python-install/lib/python2.7/lib-tk:/home/gsharp/build/slicer-4/Slicer-build/python-install/lib/python2.7:/home/gsharp/build/slicer-4/Slicer-build/python-install/lib/python2.7/lib-dynload:/home/gsharp/build/slicer-4/Slicer-build/python-install/lib/python2.7/site-packages:/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/Wrapping/Python:/home/gsharp/build/slicer-4/Slicer-build/VTKv7-build/lib/.:/home/gsharp/build/slicer-4/Slicer-build/CTK-build/CTK-build/bin/Python:/home/gsharp/build/slicer-4/Slicer-build/CTK-build/CTK-build/bin/.
QT_PLUGIN_PATH=/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/bin:/home/gsharp/build/slicer-4/Slicer-build/CTK-build/CTK-build/bin:/usr/lib/x86_64-linux-gnu/qt4/plugins
SLICER_HOME=/home/gsharp/build/slicer-4/Slicer-build/Slicer-build
SSL_CERT_FILE=/home/gsharp/build/slicer-4/Slicer-build/Slicer-build/share/Slicer-4.7/Slicer.crt
TCLLIBPATH=/home/gsharp/build/slicer-4/Slicer-build/tcl-build/lib/itcl4.0.1
TCL_LIBRARY=/home/gsharp/build/slicer-4/Slicer-build/tcl-build/lib/tcl8.6
TK_LIBRARY=/home/gsharp/build/slicer-4/Slicer-build/tcl-build/lib/tk8.6
</code></pre>

---

## Post #6 by @pieper (2017-05-21 21:37 UTC)

<p>Interesting - in LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu is inserted before the slicer build directories.  That looks wrong to me since that directory has other python shared libraries that aren’t the ones slicer builds.</p>
<p>Maybe if you start a new terminal  (with Slicer --xterm) you can set the LD_LIBRARY_PATH without that entry (or move it to the end if needed to resolve other libs).  You can run Slicer-build/bin/SlicerApp-real and see if it works.</p>
<p>I can confirm that on my ubuntu I have the same /usr/lib/x86_64 entry in LD_LIBRARY_PATH, but I don’t get a crash but I probably have a different python version.</p>

---

## Post #7 by @gregsharp.geo (2017-05-21 23:09 UTC)

<blockquote>
<p>Interesting - in LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu is<br>
inserted before the slicer build directories.  That looks wrong to me<br>
since that directory has other python shared libraries that aren’t<br>
the ones slicer builds.</p>
<p>Maybe if you start a new terminal  (with Slicer --xterm) you can set<br>
the LD_LIBRARY_PATH without that entry (or move it to the end if<br>
needed to resolve other libs).  You can run<br>
Slicer-build/bin/SlicerApp-real and see if it works.</p>
<p>I can confirm that on my ubuntu I have the same /usr/lib/x86_64 entry<br>
in LD_LIBRARY_PATH, but I don’t get a crash but I probably have a<br>
different python version.</p>
</blockquote>
<p>Sadly, the result is “Segmentation fault”.</p>
<p>For the record:</p>
<pre><code class="lang-auto">$ which python
/usr/bin/python
$ python --version
Python 2.7.13
</code></pre>
<p>I will rebuild in debug mode, and get a stack trace.<br>
Any other ideas helpful.</p>
<p>Thanks!<br>
Greg</p>

---

## Post #8 by @jcfr (2017-05-23 14:47 UTC)

<p>This is a known limitation of our build system, see <a href="http://www.na-mic.org/Bug/view.php?id=3574">http://www.na-mic.org/Bug/view.php?id=3574</a></p>
<p>In a nutshell, if Qt is installer in a system location, configure with <code>-DSlicer_USE_SYSTEM_QT:BOOL=1</code></p>
<p>I will look at this after <a href="https://github.com/Slicer/Slicer/pull/727">https://github.com/Slicer/Slicer/pull/727</a> is integrated.</p>

---
