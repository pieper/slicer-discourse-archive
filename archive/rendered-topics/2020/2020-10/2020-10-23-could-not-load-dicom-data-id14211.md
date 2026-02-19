---
topic_id: 14211
title: "Could Not Load Dicom Data"
date: 2020-10-23
url: https://discourse.slicer.org/t/14211
---

# Could not load DICOM data

**Topic ID**: 14211
**Date**: 2020-10-23
**URL**: https://discourse.slicer.org/t/could-not-load-dicom-data/14211

---

## Post #1 by @ButuiHu (2020-10-23 07:18 UTC)

<p>I’m using 4.11.20200930 r29402 / 002be18 in ArchLinux. I could not load DICOM data now, but it used to work with 4.10.2. Here is the output log:</p>
<pre><code class="lang-auto">loadSourceAsModule - Failed to load file "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/sceneImport2428.py"  as module "sceneImport2428" !
Fail to instantiate module  "sceneImport2428"
The following modules failed to be instantiated:
   ThresholdThreadingTest
   sceneImport2428
   DICOMScalarVolumePlugin
   MultiVolumeImporterPlugin
   DICOMImageSequencePlugin
   DICOMVolumeSequencePlugin
   Editor
Traceback (most recent call last):
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
    from . import overrides
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py", line 7, in &lt;module&gt;
    from numpy.core._multiarray_umath import (
ImportError: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/sceneImport2428.py", line 8, in &lt;module&gt;
    import EditorLib
  File "/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/__init__.py", line 37, in &lt;module&gt;
    exec("from .{0} import {0}Options, {0}Tool, {0}Logic, {0}".format(effectName))
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/PaintEffect.py", line 10, in &lt;module&gt;
    import numpy
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 48, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.6 from ""
  * The NumPy version is: "1.19.1"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned
loadSourceAsModule - Failed to load file "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/ThresholdThreadingTest.py"  as module "ThresholdThreadingTest" !
Fail to instantiate module  "ThresholdThreadingTest"
Traceback (most recent call last):
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
    from . import overrides
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py", line 7, in &lt;module&gt;
    from numpy.core._multiarray_umath import (
ImportError: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/ThresholdThreadingTest.py", line 6, in &lt;module&gt;
    import EditorLib
  File "/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/__init__.py", line 37, in &lt;module&gt;
    exec("from .{0} import {0}Options, {0}Tool, {0}Logic, {0}".format(effectName))
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/PaintEffect.py", line 10, in &lt;module&gt;
    import numpy
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 48, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.6 from ""
  * The NumPy version is: "1.19.1"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned
loadSourceAsModule - Failed to load file "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py"  as module "MultiVolumeImporterPlugin" !
Fail to instantiate module  "MultiVolumeImporterPlugin"
Traceback (most recent call last):
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
    from . import overrides
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py", line 7, in &lt;module&gt;
    from numpy.core._multiarray_umath import (
ImportError: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 5, in &lt;module&gt;
    import vtk.util.numpy_support
  File "/opt/3dslicer/lib/Slicer-4.11/python3.6/site-packages/vtkmodules/util/numpy_support.py", line 31, in &lt;module&gt;
    import numpy
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 48, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.6 from ""
  * The NumPy version is: "1.19.1"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned
loadSourceAsModule - Failed to load file "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/Editor.py"  as module "Editor" !
Fail to instantiate module  "Editor"
Traceback (most recent call last):
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
    from . import overrides
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py", line 7, in &lt;module&gt;
    from numpy.core._multiarray_umath import (
ImportError: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/Editor.py", line 4, in &lt;module&gt;
    import EditorLib
  File "/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/__init__.py", line 37, in &lt;module&gt;
    exec("from .{0} import {0}Options, {0}Tool, {0}Logic, {0}".format(effectName))
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/PaintEffect.py", line 10, in &lt;module&gt;
    import numpy
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 48, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.6 from ""
  * The NumPy version is: "1.19.1"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned
loadSourceAsModule - Failed to load file "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMVolumeSequencePlugin.py"  as module "DICOMVolumeSequencePlugin" !
Fail to instantiate module  "DICOMVolumeSequencePlugin"
Traceback (most recent call last):
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
    from . import overrides
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py", line 7, in &lt;module&gt;
    from numpy.core._multiarray_umath import (
ImportError: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMVolumeSequencePlugin.py", line 5, in &lt;module&gt;
    import numpy
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 48, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.6 from ""
  * The NumPy version is: "1.19.1"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned
loadSourceAsModule - Failed to load file "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py"  as module "DICOMScalarVolumePlugin" !
Fail to instantiate module  "DICOMScalarVolumePlugin"
Traceback (most recent call last):
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
    from . import overrides
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py", line 7, in &lt;module&gt;
    from numpy.core._multiarray_umath import (
ImportError: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 1, in &lt;module&gt;
    import numpy
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 48, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.6 from ""
  * The NumPy version is: "1.19.1"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned
loadSourceAsModule - Failed to load file "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMImageSequencePlugin.py"  as module "DICOMImageSequencePlugin" !
Fail to instantiate module  "DICOMImageSequencePlugin"
Traceback (most recent call last):
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
    from . import overrides
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py", line 7, in &lt;module&gt;
    from numpy.core._multiarray_umath import (
ImportError: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMImageSequencePlugin.py", line 5, in &lt;module&gt;
    import numpy
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/opt/3dslicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 48, in &lt;module&gt;
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.6 from ""
  * The NumPy version is: "1.19.1"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libgfortran-2e0d59d6.so.5.0.0: ELF load command address/offset not properly aligned
Session start time .......: 2020-10-23 15:11:51
Slicer version ...........: 4.11.20200930 (revision 29402 / 002be18) linux-amd64 - installed release
Operating system .........: Linux / 5.4.72-1-lts / #1 SMP Sat, 17 Oct 2020 13:30:57 +0000 - 64-bit
Memory ...................: 15791 MB physical, 0 MB virtual
CPU ......................: GenuineIntel Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz, 8 cores, 8 logical processors
VTK configuration ........: OpenGL2 rendering, Sequential threading
Qt configuration .........: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)
Developer mode enabled ...: no
Prefer executable CLI ....: yes
Application path .........: /opt/3dslicer/bin
Additional module paths ..: (none)
</code></pre>
<p>It seems a lot of modules fail to init. BTW, where does slicer store its log file? I just copy these messages from the log message window.</p>

---

## Post #2 by @pieper (2020-10-23 12:28 UTC)

<p>it appears there’s a problem with your python setup that prevents slicer from finding its own libraries and packages.  Slicer’s launcher should be putting Slicer’s requirements at the front of the path variables, but perhaps there’s something in your config that breaks that (I don’t use ArchLinux so I’m not sure what it does).  Try running from a clean environment.</p>

---

## Post #3 by @ButuiHu (2020-10-24 03:14 UTC)

<p>I don’t build 3dslicer from the source in ArchLinux, I just download the binary package from and re-package it. ArchLinux’s build tool will run <code>strip</code> by default, I disable it, and it works now.</p>

---

## Post #4 by @pieper (2020-10-24 14:00 UTC)

<p>Thanks for reporting back.  I started a PR to add this info to the install docs.  Can you add a little more detail (specifically, what command is needed to disable <code>strip</code>?)</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5263" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5263" target="_blank" rel="noopener">Add ArchLinux installation information</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Slicer:archlinux-install</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-24" data-time="13:59:13" data-timezone="UTC">01:59PM - 24 Oct 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars0.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 5 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5263/files" target="_blank" rel="noopener">
          <span class="added">+5</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @ButuiHu (2020-10-24 16:14 UTC)

<p>If you like, you could simply install 3dslicer from <a href="https://github.com/archlinuxcn/repo" rel="noopener nofollow ugc">ArchLinux CN repo</a> by:</p>
<pre><code class="lang-auto">pacman -S 3dslicer-bin
# or
pacman -S 3dslicer-nightly-bin
</code></pre>
<p>after adding the ArchLinux CN repo.<br>
<strong>Note: this is an unofficial/third-party repo.</strong></p>
<p>The <code>PKGBUILD</code> file is available on <a href="https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=3dslicer-bin" rel="noopener nofollow ugc">AUR</a>. As you can see, it simply repacks the binary tarball, and add a user-friendly desktop entry. Also, by setting</p>
<pre><code class="lang-auto">options=(!strip !emptydirs)
</code></pre>
<p>the empty dirs would be removed, and <code>strip</code> is not run. That’s all.<br>
If you download the official slicer tarball, extract, and run it, there is no issue related with <code>strip</code>.</p>
<p>BTW, I’m trying to build slicer from the source for ArchLinux. maybe I could help update this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#archlinux" rel="noopener nofollow ugc">doc</a>.</p>

---

## Post #6 by @pieper (2020-10-25 15:23 UTC)

<p>Thanks <a class="mention" href="/u/butuihu">@ButuiHu</a> - that’s very helpful.  I haven’t used ArchLinux myself but I can see there’s a very active community so it’s good we can support it.  For now I just updated the documentation PR to point to this discussion thread.</p>

---
