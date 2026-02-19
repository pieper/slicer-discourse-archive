---
topic_id: 13873
title: "Numerous Errors On Startup With Todays Nightly On Mac"
date: 2020-10-05
url: https://discourse.slicer.org/t/13873
---

# Numerous errors on startup with today's nightly on mac

**Topic ID**: 13873
**Date**: 2020-10-05
**URL**: https://discourse.slicer.org/t/numerous-errors-on-startup-with-todays-nightly-on-mac/13873

---

## Post #1 by @fedorov (2020-10-05 21:54 UTC)

<p>Is the preview release expected to be non-functional today?</p>
<p>There is a long list of errors on startup, the initial part is below:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'getSlicerRCFileName' is not defined
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 13, in &lt;module&gt;
    from . import vtkCommonCore
ImportError: dlopen(/Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so, 1): Library not loaded: /Volumes/D/P/S-0-build/VTK-build/lib/libvtkWrappingPythonCore-9.0.1.dylib
  Referenced from: /Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so
  Reason: image not found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/AddManyMarkupsFiducialTest.py", line 5, in &lt;module&gt;
    import vtk, qt, ctk, slicer
  File "/Applications/Slicer.app/Contents/bin/Python/vtk.py", line 30, in &lt;module&gt;
    all_m = importlib.import_module('vtkmodules.all')
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 15, in &lt;module&gt;
    import _vtkmodules_static
ModuleNotFoundError: No module named '_vtkmodules_static'
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 13, in &lt;module&gt;
    from . import vtkCommonCore
ImportError: dlopen(/Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so, 1): Library not loaded: /Volumes/D/P/S-0-build/VTK-build/lib/libvtkWrappingPythonCore-9.0.1.dylib
  Referenced from: /Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so
  Reason: image not found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/AtlasTests.py", line 4, in &lt;module&gt;
    import vtk, qt, ctk, slicer
  File "/Applications/Slicer.app/Contents/bin/Python/vtk.py", line 30, in &lt;module&gt;
    all_m = importlib.import_module('vtkmodules.all')
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 15, in &lt;module&gt;
    import _vtkmodules_static
ModuleNotFoundError: No module named '_vtkmodules_static'
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 13, in &lt;module&gt;
    from . import vtkCommonCore
ImportError: dlopen(/Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so, 1): Library not loaded: /Volumes/D/P/S-0-build/VTK-build/lib/libvtkWrappingPythonCore-9.0.1.dylib
  Referenced from: /Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so
  Reason: image not found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/BRAINSFitRigidRegistrationCrashIssue4139.py", line 3, in &lt;module&gt;
    import vtk, qt, ctk, slicer
  File "/Applications/Slicer.app/Contents/bin/Python/vtk.py", line 30, in &lt;module&gt;
    all_m = importlib.import_module('vtkmodules.all')
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 15, in &lt;module&gt;
    import _vtkmodules_static
ModuleNotFoundError: No module named '_vtkmodules_static'
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 13, in &lt;module&gt;
    from . import vtkCommonCore
ImportError: dlopen(/Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so, 1): Library not loaded: /Volumes/D/P/S-0-build/VTK-build/lib/libvtkWrappingPythonCore-9.0.1.dylib
  Referenced from: /Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so
  Reason: image not found

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/Charting.py", line 8, in &lt;module&gt;
    import vtk, qt, ctk, slicer
  File "/Applications/Slicer.app/Contents/bin/Python/vtk.py", line 30, in &lt;module&gt;
    all_m = importlib.import_module('vtkmodules.all')
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 15, in &lt;module&gt;
    import _vtkmodules_static
ModuleNotFoundError: No module named '_vtkmodules_static'
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/__init__.py", line 13, in &lt;module&gt;
    from . import vtkCommonCore
ImportError: dlopen(/Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so, 1): Library not loaded: /Volumes/D/P/S-0-build/VTK-build/lib/libvtkWrappingPythonCore-9.0.1.dylib
  Referenced from: /Applications/Slicer.app/Contents/bin/Python/vtkmodules/vtkCommonCore.cpython-36m-darwin.so
  Reason: image not found
</code></pre>

---

## Post #2 by @jamesobutler (2020-10-06 00:27 UTC)

<p>Yes, the preview is still unstable due to the recent transition to VTK9. You can view some of the recent VTK related issues at <a href="https://github.com/Slicer/Slicer/issues" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues</a>. If you need something that works the new snapshot 4.11.20200930 stable release at <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> should work.</p>

---
